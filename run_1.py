import time
import pyautogui as pya
from random import randint, choice
from time import sleep
import pyperclip
from pynput import keyboard
import threading


def get_msg(msg_txt):
    with open(msg_txt, 'r', encoding='utf-8') as f:
        msgs = f.readlines()
        msg_list = [i.replace('\n', '') for i in msgs]
        # print(msg_list)
        return msg_list


def get_position(pic_path, confidence=1):
    """
    pic_path: 图片路径
    confidence: 模糊查找 0-1
    返回 x, y 坐标列表
    """
    aa = pya.locateAllOnScreen(pic_path, confidence=confidence)
    xy_list = [pya.center(i) for i in aa]
    return xy_list


def get_msg_list(msg_txt):
    with open(msg_txt, 'r', encoding='utf-8') as f:
        msg_list = f.readlines()
    msg_list = [i.replace('\n', '') for i in msg_list]
    return msg_list


def random_msg(num):
    l1 = ['已拍','拍了','买了','我拍了','刚拍了','刚买了','冲了','要了','下单了']
    l2 = ['1号','2号','3号','臭干子','八宝丝','4种辣条礼包']
    l3 = ['加急','快点发货','加加急','今天发货哦','快点发','日期新鲜吗？','想吃','加加急','上午发','快点哦',
          '哈哈','嘻嘻','发快点','等着吃','啊啊','同学经常给我吃','学校有卖，比这贵','就爱吃飞旺','现在就发','马上发','香香辣辣的',]
    l4 = ['两天就炫完了，回购','这个巨好吃','有没有组合套餐','很实惠','上学的时候吃过贼好吃','飞旺辣条我的童年','童年回忆',
          '小时候一天买一根','中学的时候天天必吃','贼喜欢吃飞旺','好久没吃过了，想要','是新鲜日期吗','就是这个味道','就是这个包装','小时候的辣条，配饭吃贼香','上学跟同座一人一根',]
    l5 = ['辣条公的母的','在厕所里能吃吗？','饭前吃还是饭后吃','买辣条送男朋友不','一包有几斤','没牙老太太可以吃不',
          '是过期的不，不是过期的我不买','吃了能长生不老吗？','要吃几个疗程？','买这个影响我单手开法拉利吗？','吃了能长个不？',]

    s1 = choice(l1) + ',' + choice(l2) + ',' + choice(l3) + ',' + choice(l4)
    s2 = choice(l1) + ',' + choice(l3) + ',' + choice(l4)
    s3 = choice(l1)
    s4 = choice(l3)
    s5 = choice(l4)
    s6 = choice(l2) + ',' + choice(l3)
    s7 = choice(l3) + ',' + choice(l4)
    s8 = choice(l1) + ',' + choice(l4)
    s9 = choice(l5)
    res0 = choice([s1, s2, s3, s4, s5, s6, s7, s8, s9])
    res1 = s9  # 搞笑话术
    res2 = s5  # 询单聊天
    res3 = choice(l1) + ',' + choice(l2) + ',' + choice(l3)  # 排单话术
    if num == 0:
        return res0
    elif num == 1:
        return res1
    elif num == 2:
        return res2
    else:
        return res3


def change_is_stop():
    global is_stop
    if is_stop is True:
        is_stop = False
        print('已开启')
    else:
        is_stop = True
        print('已停止')


def change_msg_list():
    global num
    if num == 0:
        print('已切换成搞笑话术')
        num = 1
    elif num == 1:
        print('已切换成询单话术')
        num = 2
    elif num == 2:
        print('已切换成拍单话术')
        num = 3
    else:
        num = 0
        print('已切换成混搭话术')


def change_interval_time():
    global interval_time
    if interval_time == (0, 3):
        interval_time = (3, 8)
        print('已调整发送间隔时间为： 5-10 秒')
    if interval_time == (3, 8):
        interval_time = (8, 13)
        print('已调整发送间隔时间为： 10-15 秒')
    elif interval_time == (8, 13):
        interval_time = (13, 18)
        print('已调整发送间隔时间为： 15-20 秒')
    elif interval_time == (13, 18):
        interval_time = (18, 23)
        print('已调整发送间隔时间为： 20-25 秒')
    elif interval_time == (18, 23):
        interval_time = (23, 28)
        print('已调整发送间隔时间为： 25-30 秒')
    elif interval_time == (23, 28):
        interval_time = (28, 50)
        print('已调整发送间隔时间为： 30-50 秒')
    else:
        interval_time = (0, 3)
        print('已调整发送间隔时间为： 1-5 秒')


def cat():
    with keyboard.GlobalHotKeys({
        '<alt>+c': change_is_stop,
        '<alt>+m': change_msg_list,
        '<alt>+t': change_interval_time}) as h:
        h.join()


def send_msg(msg, postion_tuple):
    # randint(1,2)
    x, y = postion_tuple
    pya.click(x - 80, y, duration=1)
    sleep(randint(1, 3))
    pya.hotkey('ctrl', 'v')
    sleep(randint(1, 2))
    pya.hotkey('enter')


def t():
    global is_stop
    is_stop = False
    global interval_time
    interval_time = (0, 3)
    sleep_time = 0
    msg_num = 0
    global num
    num = 0
    while True:
        try:
            xy_list = get_position('./send.png', 0.8)
        except Exception as e:
            print('请确保图片正确，或者要找的图片在屏幕上')
            print(e)
            pass

        for x, y in xy_list:
            # print(f'开始时间{time.localtime()[4]}:{time.localtime()[5]}')
            if is_stop is False:
                msg = random_msg(num)
                pyperclip.copy(msg)
                pya.click(x - 80, y)
                pya.hotkey('ctrl', 'v')
                sleep(1)
                pya.hotkey('enter')
                sl = randint(interval_time[0], interval_time[1])
                print(sl)
                sleep(sl)
                msg_num += 1
                print(f'正在发送第 {msg_num} 条弹幕：  ', msg)
                # print(f'结束时间{time.localtime()[4]}:{time.localtime()[5]}')
            else:
                sleep_time += 1
                print(f'已暂停 {sleep_time} 秒')
                sleep(1)


if __name__ == '__main__':
    is_stop = False
    t1 = threading.Thread(target=cat)
    t2 = threading.Thread(target=t)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

