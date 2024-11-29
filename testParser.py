import os.path
import maidenhead as mh
from dataclasses import dataclass

#initial vars/structs

#file realted vars
file = None
fileData = None
fileName = None
#data type vars
whitespace = None
dateTime = None
#location vars
myLat = 30.517990
myLon = -97.734530

#datatype struct
@dataclass
class parseData:
    date: str
    UTC: str
    SNR: str
    DT: str
    freq: str
    call: str
    grid: str
    dBm: str
    misc: str

parsedInfo = parseData(str, str, str, str, str, str, str, str, str)

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

#UTC to CST
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

#parse data into catagories
def parseFile(fileData1):
    i = 0
    datatype = 1
# 	datatypes:
# 	date = 1
# 	UTC (time) = 2
# 	SNR = 3
# 	DT = 4
# 	Freq = 5
# 	Call = 6
# 	Grid = 7
# 	dBm = 8
#	other crap = 9-17

    #storage
    date1 = ""
    UTC1 = ""
    SNR1 = ""
    DT1 = ""
    Freq1 = ""
    Call1 = ""
    Grid1 = ""
    dBm1 = ""
    misc1 = ""
    #temps
    date = ""
    UTC = ""
    SNR = ""
    DT = ""
    Freq = ""
    Call = ""
    Grid = ""
    dBm = ""
    misc = ""
    while i < len(fileData1):
        if not fileData1[i:i + 1].isspace():
            match datatype:
                case 1:
                    date = date + fileData1[i:i + 1]
                    
                case 2:
                    UTC = UTC + fileData1[i:i + 1]
                    
                case 3:
                    SNR = SNR + fileData1[i:i + 1]
                    
                case 4:
                    DT = DT + fileData1[i:i + 1]
                    
                case 5:
                    Freq = Freq + fileData1[i:i + 1]
                    
                case 6:
                    Call = Call + fileData1[i:i + 1]
                    
                case 7:
                    Grid = Grid + fileData1[i:i + 1]
                    
                case 8:
                    dBm = dBm + fileData1[i:i + 1]
                    
                case 9:
                    misc = misc + fileData1[i:i + 1]
                    
                case 10:
                    misc = misc + fileData1[i:i + 1]
                    
                case 11:
                    misc = misc + fileData1[i:i + 1]
                    
                case 12:
                    misc = misc + fileData1[i:i + 1]
                    
                case 13:
                    misc = misc + fileData1[i:i + 1]
                    
                case 14:
                    misc = misc + fileData1[i:i + 1]
                    
                case 15:
                    misc = misc + fileData1[i:i + 1]
                    
                case 16:
                    misc = misc + fileData1[i:i + 1]
                    
                case 17:
                    misc = misc + fileData1[i:i + 1]
                    
        elif i + 1 < len(fileData1) and not fileData1[i:i + 2].isspace():
                match datatype:
                    case 1:
                        date1 = date1 + date
                        date = " "
                        
                    case 2:
                        UTC1 = UTC1 + UTC
                        UTC = " "
                        
                    case 3:
                        SNR1 = SNR1 + SNR
                        SNR = " "
                        
                    case 4:
                        DT1 = DT1 + DT
                        DT = " "
                        
                    case 5:
                        Freq1 = Freq1 + Freq
                        Freq = " "
                        
                    case 6:
                        Call1 = Call1 + Call
                        Call = " "
                        
                    case 7:
                        Grid1 = Grid1 + Grid
                        Grid = " "
                        
                    case 8:
                        dBm1 = dBm1 + dBm
                        dBm = " "
                        
                    case 9:
                        misc1 = misc1 + misc
                        misc = " "
                        
                    case 10:
                        misc1 = misc1 + misc
                        misc = " "
                        
                    case 11:
                        misc1 = misc1 + misc
                        misc = " "
                        
                    case 12:
                        misc1 = misc1 + misc
                        misc = " "
                        
                    case 13:
                        misc1 = misc1 + misc
                        misc = " "
                        
                    case 14:
                        misc1 = misc1 + misc
                        misc = " "
                        
                    case 15:
                        misc1 = misc1 + misc
                        misc = " "
                        
                    case 16:
                        misc1 = misc1 + misc
                        misc = " "
                        
                    case 17:
                        misc1 = misc1 + misc
                        misc = " "
                        
                datatype = datatype + 1  
        if datatype > 17:
            datatype = 1
        i += 1 
    parsedInfo.date = date1
    parsedInfo.UTC = UTC1
    parsedInfo.SNR = SNR1
    parsedInfo.DT = DT1
    parsedInfo.freq = Freq1
    parsedInfo.call = Call1
    parsedInfo.grid = Grid1
    parsedInfo.dBm = dBm1
    parsedInfo.misc = misc1       
    
#converts grid to Longitude and Latitude
def grid2Coord(gridVar):
    pass
    
#----[main]----#

#check if valid file
# while fileName == None:
#     fileName = input("file to parse: ")
#     #get length to cut out of fileName
#     foo = len(fileName) - 4
#     #if valid
#     if fileName[foo:] == ".txt":
#         if os.path.isfile(fileName) == True:
#             #processing
#             fileData1 = takeInData()
#             whitespace = numWhiteSpace()
#             #printing outputs
#             print("whitespace = " + str(whitespace))
#     #if invalid
#         else:
#             fileName = None
#             print("retry2")
#     else:
#         fileName = None
#         print("retry1")

fileName = "wsprP.txt"
fileData = takeInData()
parseFile(fileData)
print(parsedInfo.grid)






    
