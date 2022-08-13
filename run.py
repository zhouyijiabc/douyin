import pyautogui as pya
import pyperclip
from time import sleep
import random
# x, y = pya.size()
def get_msg(msg_txt):
    with open(msg_txt,'r',encoding='utf-8') as f:
        msgs = f.readlines()
        msg_list = [i.replace('\n','') for i in msgs]
        # print(msg_list)
        return msg_list
    
msg_list = get_msg('./msg.txt')  
msg_list[len(msg_list)-1]
for num in range(20):
    aa = pya.locateAllOnScreen('./send.png',confidence=0.9)
    xy_list = [pya.center(i) for i in aa]
    # xy_list = [(2,4), (3,5), (4,6), (5,7), (6,8)]
    xy_index = 0
    for msg in msg_list:
        sl1 = random.randint(1,3)
        sl2 = random.randint(10,20)
        pyperclip.copy(msg)
        
        x, y = xy_list[xy_index]
        if xy_index < len(xy_list) - 1:
            xy_index += 1
        else:
            xy_index = 0
        x, y  = xy_list[xy_index ]
        pya.click(x-80, y, duration=1)
        sleep(sl1)
        pya.hotkey('ctrl','v')
        sleep(sl1)
        pya.click(x, y, duration=1)
        print(x,y, msg)
        sleep(sl2)
