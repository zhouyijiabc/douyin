from pickletools import read_bytes1
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

def get_msg_list(msg_txt):
    with open(msg_txt,'r',encoding='utf-8') as f:
        msg_list = f.readlines()
    msg_list = [i.replace('\n','') for i in msg_list]
    return msg_list

def random_msg():
    global change_msg
    global res0
    global res1
    global res2
    global res3
    
    l1 = get_msg_list('m1.txt')
    l2 = get_msg_list('m2.txt')
    l3 = get_msg_list('m3.txt')
    l4 = get_msg_list('m4.txt')
    l5 = get_msg_list('m5.txt')
    s1 = choice(l1) + ','+choice(l2) + ',' + choice(l3) + ',' + choice(l4)
    s2 = choice(l1) + ',' + choice(l3) + ',' + choice(l4)
    s3 = choice(l1)
    s4 = choice(l3)
    s5 = choice(l4)
    s6 = choice(l2) + ',' + choice(l3)
    s7 = choice(l3) + ',' + choice(l4)
    s8 = choice(l1) + ',' + choice(l4)
    s9 = choice(l5)
    res0 = choice([s1,s2,s3,s4,s5,s6,s7,s8,s9])
    res1 = choice(s9) # 搞笑话术
    res2 = s5 #询单聊天
    res3 = choice(l1) + ','+choice(l2) + ',' + choice(l3) # 排单话术
    
    change_msg = res0
    return change_msg


def change_is_stop():
    global is_stop
    if is_stop is True:
        is_stop = False
        print ('已开启')
    else:
        is_stop = True
        print('已停止')

def change_msg_list():
    global change_msg
    global res0
    global res1
    global res2
    global res3

    if change_msg is res0:
        print('已切换成搞笑话术')
        change_msg = res1
    elif change_msg is res1:
        print('已切换成询单话术')
        change_msg = res2
    elif change_msg is res2:
        print('已切换成拍单话术')
        change_msg = res3
    else:
        change_msg = res0
        print('已切换成混搭话术')
        

def change_interval_time():
    global interval_time
    if interval_time == (1, 5):
        interval_time = (5, 10)
        print('已调整发送间隔时间为： 5-10 秒')
    if interval_time == (5, 10):
        interval_time = (10, 15)
        print('已调整发送间隔时间为： 10-15 秒')
    elif interval_time == (10,15):
        interval_time= (15, 20)
        print('已调整发送间隔时间为： 15-20 秒')
    elif interval_time == (15, 20):
        interval_time = (20, 25)
        print('已调整发送间隔时间为： 20-25 秒')
    elif interval_time == (20, 25):
        interval_time = (25, 30)
        print('已调整发送间隔时间为： 25-30 秒')
    elif interval_time == (25, 30):
        interval_time = (30, 50)
        print('已调整发送间隔时间为： 30-50 秒')
    else:
        interval_time = (1,5)
        print('已调整发送间隔时间为： 1-5 秒')

def cat():
    with keyboard.GlobalHotKeys({
            '<alt>+c': change_is_stop,
            '<alt>+m': change_msg_list,
            '<alt>+t': change_interval_time}) as h:
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
    global interval_time
    interval_time = (1, 5)
    sleep_time = 0
    msg_num = 0
    while True:
        try:
            xy_list = get_position('./send.png', 0.8)
        except Exception as e:
            print('请确保图片正确，或者要找的图片在屏幕上')
            print(e)
            pass

        for x, y in xy_list:
            if is_stop is False:
                msg = random_msg()
                # msg = '好搞笑'
                pyperclip.copy(msg)
                pya.click(x-80, y)
                # sleep(randint(1, 2))
                pya.hotkey('ctrl', 'v')
                sleep(1)
                pya.hotkey('enter')
                print(interval_time)
                sleep(randint(interval_time[0], interval_time[1]))
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
        
