#!/bin/python

from enum import Enum
import sys
from Logger import *
from ReqManager import *
 
def doSQL(flags):
        getHTTP(flags[1])

#def doXSS(flags):


#def doVersions(flags):


#def doAll(flags):





print(open("Startup.txt", "r").read())
while True:
        log(MSG.USER, "Obel: ")
        flags = input().split()
        print(flags)

        for i in range(0, len(flags)):
                flag = flags[i]

                if flag == "sql":
                        doSQL(flags)
                #elif flag == "xss":
                        #doXSS(flags)
                #elif flag == "versions":
                        #doVersions(flags)
                #elif flag == "all":
                        #doAll(flags)