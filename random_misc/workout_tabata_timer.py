# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# tabata timer is 20s work/10s rest, usually repeated 8x (4min) per movement
# and often done through 4 exercises (with no extra rest, that's 16min total)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# TODO make prettier prints
# TODO make start countdown 1 2 3
# TODO make it beep!
# TODO make a GUI!
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import time
from colorama import Fore, Back, Style

# kinda the cheating way to do it here, NOTE better to figure out modulus or better math so it could scale infinitely:
work_list = [0, 30, 60, 90, 120, 150, 180, 210, 240, ...]
rest_list = [20, 50, 70, 110, 140, 170, 200, 230, 260, ...]

def work_action():
    print(Fore.RESET + Back.RESET + Style.RESET_ALL, end="")
    print(Back.RED + Fore.BLACK + 'WORK! NO PAIN NO GAIN! IT\'S ONLY 20 SECONDS: DO IT!')
    return

def rest_action():
    print(Fore.RESET + Back.RESET + Style.RESET_ALL, end="")
    print(Fore.GREEN + Back.BLUE + Style.BRIGHT + '~~~~~~ TAKE A BREAK! ~~~~~~')
    return

def tabata_timer(max_time):

    print('Start!')

    for x in range(max_time):
        print(x)
        time.sleep(.1) # 1s normally, 0.1 or faster for testing...
        
        if x in work_list:
            work_action()
        if x in rest_list:
            rest_action()
            
    print(Fore.RESET + Back.RESET + Style.RESET_ALL)

# print(ord('õ'))
# print(chr(245))
tabata_timer(31)