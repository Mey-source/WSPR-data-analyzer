import os.path
from dataclasses import dataclass

#initial vars
#file realted vars
file = None
fileData = None
fileName = None
#data type vars
whitespace = None
dateTime = None
date = None
time = None

#func for taking in txt file data
def takeInData():
    file = open(fileName, "r")
    fileData = file.read()
    return fileData
    
#finds whitespace amt
def numWhiteSpace():
    i = 1
    whitespace = 0
    while i < len(fileData):
        if fileData[i:i + 1].isspace():
            whitespace = whitespace + 1
        else:
            pass
        i = i + 1
    return whitespace

#Date and Time
#ARGS MUST BE 6 AND 4 CHARS
def findDateTime(date, time):
    #conv time UTC -> CST
    t1 = int(time[:2]) + 18
    if t1 > 24:
        t1 = t1 - 24
    else:
        t1 = t1
    t2 = (time[2:])
    #concat time
    t = str(t1) + ":" + (t2)
    
    #conv date
    d1 = date[:2]
    d2 = date[2:4]
    d3 = date[4:]
    #concat date
    d = d2 + "-" + d3 + "-" + d1
    return d + " " + t

def findTime(time):
    #conv time UTC -> CST
    t1 = int(time[:2]) + 18
    if t1 > 24:
        t1 = t1 - 24
    else:
        t1 = t1
    t2 = (time[2:])
    #concat time
    t = str(t1) + ":" + (t2)
    return t
    
#----[main]----#

#check if valid file
while fileName == None:
    fileName = input("file to parse: ")
    #get length to cut out of fileName
    foo = len(fileName) - 4
    #if valid
    if fileName[foo:] == ".txt":
        if os.path.isfile(fileName) == True:
            #processing
            fileData = takeInData()
            whitespace = numWhiteSpace()
            #printing outputs
            print("whitespace = " + str(whitespace))
    #if invalid
        else:
            fileName = None
            print("retry2")
    else:
        fileName = None
        print("retry1")



    