from colorama import Fore, Back, Style
from enum import Enum

AllChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']


loadwheelnum = 0
LoadWheelChars = ['◐', '◓', '◑', '◒']

class MSG(Enum):
    LOG = 1
    WARNING = 2
    ERROR = 3
    USER = 4

def loadwheel():
        if loadwheelnum+1 < len(LoadWheelChars):
                loadwheelnum+=1
        else:
                loadwheelnum=0
        return LoadWheelChars[loadwheelnum]

def log(type, str):
        if type == MSG.LOG:
                print(Fore.GREEN + "[LOG] " + Style.RESET_ALL + str)
        elif type == MSG.WARNING:
                print(Fore.YELLOW + "[WARNING] " + Style.RESET_ALL + str)
        elif type == MSG.ERROR:
                print(Fore.RED + "[ERROR] " + Style.RESET_ALL + str)
        elif type == MSG.USER:
                print(Fore.CYAN + str + Style.RESET_ALL, end = "")