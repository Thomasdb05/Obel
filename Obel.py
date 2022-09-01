#!/bin/python

from enum import Enum
import sys
from logger import *
from initializer import *
 
#def doSQL(flags):

#def doXSS(flags):


#def doVersions(flags):


#def doAll(flags):




print(open("DATA/logging/Startup.txt", "r").read())
initiliaze()
while True:
        log(MSG.USER, "Obel: ")
        flags = input().split()
        print(flags)

        for i in range(0, len(flags)):
                flag = flags[i]

                #if flag == "sql":
                        #doSQL(flags)
                #elif flag == "xss":
                        #doXSS(flags)
                #elif flag == "versions":
                        #doVersions(flags)
                #elif flag == "all":
                        #doAll(flags)