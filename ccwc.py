#!/usr/bin/env /home/codespace/.python/current/bin/python3
'''
Word count cmd  - ccwc

ccwc -l <fileName> : returns total lines
ccwc -c <fileNAme> : number of bytes in filec       
ccwc -w <fileNAme> : total words in file
ccwc -m <fileNAme> : total multibytes in file
ccwc <fileName> : equivalent to the -c, -l and -w options
https://medium.com/@pranithmahanti/build-your-own-custom-commands-in-linux-using-python-81abc88f13e8
https://codingchallenges.fyi/challenges/challenge-wc
'''

import sys
import os

def validateOptionValue(option):
    pass

def checkIfFileExists(fileName):
    pass


def readTotalLinesCount(fileName):
    f = open(fileName, "r")
    totalLines = f.readlines()
    f.close()
    return len(totalLines)

def readTotalBytes(fileName):
    file_size = os.path.getsize(fileName)
    return file_size

def readTotalWords(fileName):
    f = open(fileName, "r")
    totalLines = f.readlines()
    totalsWords = 0
    for line in totalLines:
        totalWordsInLine =line.split()
        totalsWords += len(totalWordsInLine)
    f.close()
    return totalsWords

def readTotalChars(fileName):
    f = open(fileName, "r")
    totalLines = f.readlines()
    totalsChars = 0
    for line in totalLines:
        totalWordsInLine =line.split()
        for word in totalWordsInLine:
            totalsChars += len(word)
    f.close()
    return totalsChars

option = sys.argv[1]

if len(sys.argv) == 3 :
    fileName=sys.argv[2]
#"/workspaces/LearnPython/CC/CC_LiveApplications/CustomLinuxCmd/TextFile.txt"

if option == "-l":
    print(readTotalLinesCount(fileName))
elif option == "-w":
    print(readTotalWords(fileName))
elif option == "-c":
    print(readTotalChars(fileName))
elif option == "-m":    
    print(readTotalBytes(fileName))
elif os.path.exists(os.path.dirname(option)):
    fileName = option
    print(readTotalLinesCount(fileName))
    print(readTotalWords(fileName))
    print(readTotalChars(fileName))
    print(readTotalBytes(fileName))
else:
    print("Please enter -l, -w, -c, -m options along with filename")


