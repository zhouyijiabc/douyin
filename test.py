import sys
import  pyautogui as pya
from random import randint, choice
from time import sleep
import pyperclip
from pynput import keyboard
import threading

def get_msg(msg_txt):
    with open(msg_txt,'r',encoding='utf-8') as f:
        msgs = f.readlines()
        msg_list = [i.replace('\n','') for i in msgs]
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

def random_msg():
    l1 = ['已拍','拍了','买了','我拍了','刚拍了','刚买了','冲了','要了','下单了']
    l2 = ['1号','2号','3号','臭干子','八宝丝','4种辣条礼包']
    l3 = ['加急','快点发货','加加急','今天发货哦','快点发','日期新鲜吗？','想吃','加加急','上午发','快点哦','哈哈','嘻嘻','发快点','等着吃','啊啊','同学经常给我吃','学校有卖，比这贵','就爱吃飞旺','现在就发','马上发','香香辣辣的']
    l4 = ['小时候经常吃','上学吃过','小时候的味道','臭干子yyds','从小到大都吃','比卫龙好吃多了，不喜欢吃甜辣',
          '冲冲冲','姐妹们，不要犹豫，冲冲冲','这价格，良心商家','上学就吃这个','良心商家','中学就吃这个','下课就买这个',
          '小时候买都要5毛，划算','是小时候的味道吗','两天就炫完了，回购','这个巨好吃','有没有组合套餐','很实惠',
          '上学的时候吃过贼好吃','飞旺辣条我的童年','童年回忆','小时候一天买一根','中学的时候天天必吃',
          '贼喜欢吃飞旺','好久没吃过了，想要','是新鲜日期吗','就是这个味道','就是这个包装','小时候的辣条，配饭吃贼香',
          '上学跟同座一人一根']
    s1 = choice(l1) + ','+choice(l2) + ',' + choice(l3) + ',' + choice(l4)
    s2 = choice(l1) + ',' + choice(l3) + ',' + choice(l4)
    s3 = choice(l1)
    s4 = choice(l3)
    s5 = choice(l4)
    s6 = choice(l2) + ',' + choice(l3)
    s7 = choice(l3) + ',' + choice(l4)
    s8 = choice(l1) + ',' + choice(l4)
    res = choice([s1,s2,s3,s4,s5,s6,s7,s8])
    return res


def change_is_stop():
    global is_stop
    if is_stop is True:
        is_stop = False
        print ('已开启')
    else:
        is_stop = True
        print('已停止')

def cat():
    with keyboard.GlobalHotKeys({
            '<alt>+c': change_is_stop}) as h:
        h.join()

def send_msg(msg,postion_tuple):
    # randint(1,2)
    x,y = postion_tuple
    pya.click(x-80,y, duration=1)
    sleep(randint(1,3))
    pya.hotkey('ctrl','v')
    sleep(randint(1,2))
    pya.hotkey('enter')


def t():
    global is_stop
    is_stop = False
    sleep_time = 0
    msg_num = 0
    while True:
        xy_list = get_position('./send.png', 0.8)
        for x, y in xy_list:
            if is_stop is False:
                msg = random_msg()
                # msg = '好搞笑'
                pyperclip.copy(msg)
                pya.click(x-80, y, duration=1)
                sleep(randint(1, 2))
                pya.hotkey('ctrl', 'v')
                sleep(randint(1, 2))
                pya.hotkey('enter')
                sleep(randint(5, 10))
                msg_num +=1
                print(f'正在发送第 {msg_num} 条弹幕：  ', msg)
            else:
                sleep_time +=1
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

