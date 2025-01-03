import os.path
import math
import numpy as np
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
gridArr = np.array([])
#location vars
myLat = 30.517990
myLon = -97.734530
distFrom = np.array([])
R = 6378 # this is in km

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

#long/latitude struct
@dataclass
class lat_lon:
    latArr: np.array([])
    lonArr: np.array([])
    
latlon = lat_lon(np.array([]), np.array([]))

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
#takes just grid loc
def grid2Coord(gridVar):
    return mh.to_location(gridVar)

#parse grids into an array
def parseGrid(gridVar):
    #loop + datatype var
    i = 0
    #array
    locArr = np.array([])
    temp = []
    while i < len(gridVar):
        if gridVar[i].isspace():
            if temp:
                locArr = np.append(locArr, "".join(temp))
                temp = []
        else:
            temp.append(gridVar[i])
        i += 1
    if temp:
        locArr = np.append(locArr, "".join(temp))
    return locArr
    
#conv input to array elements
def lat_lon_move(gridArr):
    a = 0
    lonLat = [None] * len(gridArr)
    while a < len(gridArr):
        lonLat[a] = gridArr[a]
        a = a + 1
    return lonLat

#converts grids to lat/lon array
def lat_lon_conv(lat_lon_output):
    counter = 0
    b = len(lat_lon_output) * 2
    c = 0
    result = []
    #get lat + lon
    #this is broken
    while c < len(lat_lon_output):
        tempVar = mh.to_location(lat_lon_output[c])
        result.append(tempVar)
        c += 1
    return result
        
#sorts lat and lon into their own arrays
def lat_lon_sort(conv_output):
    latitude = []
    longitude = []
    
    for pair in conv_output:
        lat, lon = pair
        latitude.append(lat)
        longitude.append(lon)
    print(latitude)
    print(longitude)
    latlon.latArr = latitude
    latlon.lonArr = longitude
    return latlon

#calculate distance
#cleaned up by bot lol
def distCalc():
    # Define the radius of Earth in kilometers
    R = 6371  # Earth radius in kilometers
    disArr = np.array([])
    # Reference point (your coordinates)
    myLat = 30.517990
    myLon = -97.734530

    # Convert myLat and myLon from degrees to radians
    myLat = myLat * (math.pi / 180)
    myLon = myLon * (math.pi / 180)

    # Convert all latitudes and longitudes from degrees to radians
    latlon.latArr = [lat * (math.pi / 180) for lat in latlon.latArr]
    latlon.lonArr = [lon * (math.pi / 180) for lon in latlon.lonArr]

    # Calculate distance for each coordinate in latlon
    for i in range(len(latlon.latArr)):
        # Calculate the differences in latitudes and longitudes
        chanLat = latlon.latArr[i] - myLat
        chanLon = latlon.lonArr[i] - myLon

        # Haversine formula
        a = math.sin(chanLat / 2) ** 2 + math.cos(myLat) * math.cos(latlon.latArr[i]) * math.sin(chanLon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Calculate distance
        d = R * c
        disArr = np.append(disArr, d)
        print(f"Distance to point {i}: {d} km")
    return disArr
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
# print(parsedInfo.grid)
gridArr = parseGrid(parsedInfo.grid)
# print(gridArr)

#structure for conversion + push to vars
#fix this shit
# a = 0
# lonLat = [None] * len(gridArr)
# while a < len(gridArr):
#     lonLat[a] = gridArr[a]
#     a = a + 1
# print(a)

latlon.latArr = np.append(latlon.latArr ,"hi")
latlon.latArr = np.append(latlon.latArr ,"sigmna")
latlon.latArr = np.append(latlon.latArr ,"dasf")
# print(latlon.latArr[0])
# print(latlon.latArr[1])
# print(latlon.latArr[2])
hi = lat_lon_move(gridArr)

# print(gridArr)
# print(hi[2])
yeah = lat_lon_conv(hi)
print(lat_lon_conv(hi))
# print(lat_lon_sort(hi))
# print(latlon.latArr)
ugh = lat_lon_sort(yeah)
print(ugh)
jug = distCalc()
print(jug[3])
    
