from typing import final
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

#options is array, optionchars is array of corresponding answer chars
#returns index of Chose option
def ask(question, optionlist, optionchars, defaultoption):
        #global questions_enabled
        #if questions_enabled:
        #        return defaultoption
        options = optionlist.copy()
        final = question + ' ('
        for i in range(0, len(options)):
                #highlight answer char in options
                charindex = options[i].find(optionchars[i])
                options[i] = options[i][:charindex] + '[' + optionchars[i] + ']' + options[i][charindex+1:]

                final += options[i] 
                if i < len(options)-1:
                        final += '/'

        final = final + '):       '
        while True:
                log(MSG.USER, final)
                inp = input().lower()
                if inp == 'default' or inp == 'def':
                        return defaultoption
                index = "".join(optionchars).lower().find(inp)
                if index >= 0:
                        return optionchars[index]
                print('answer does not correspond to any option, please try again')

#ask("how many bitches do you currently own?", ["I dont own any", "I own many", "a few"], ['d', 'm', 'f'], 'd')