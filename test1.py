from nominatim import Nominatim
import csv

nom = Nominatim()

#fileLoc = ["data/east.csv", "data/north.csv", "data/south.csv", "data/west.csv"]
fileLoc = ["data/east.csv"]

def validCoord(lat, lon):
    if (1.2 < lat < 1.5) and (103 < lon < 104):
        return True
    else:
        return False

def checkMap(query):
    #check school and long lat if either one is wrong check address, if either one is wrong, check postal code
    nomObj = nom.query(query)
    if len(nomObj) > 0 and validCoord(float(nomObj[0].get("lat")), float(nomObj[0].get("lon"))) :
        return True
    else :
        return False

def openFile(fileName):
    with open(fileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            #print(row[0] + ", " + row[2] + ", " + row[3])
            #if not row 0, then row 2, then row 3, if not error
            if checkMap(row[0]):
                nomObj = nom.query(row[0])
                lat = nomObj[0].get("lat")
                lon = nomObj[0].get("lon")
                latList.append(lat)
                lonList.append(lon)
                schoolList.append(row[0])
                zoneList.append(row[1])
                addressList.append(row[2])
                postList.append(row[3])
                print([row[0], lat, lon , 1])
            elif checkMap(row[2]):
                nomObj = nom.query(row[2])
                lat = nomObj[0].get("lat")
                lon = nomObj[0].get("lon")
                latList.append(lat)
                lonList.append(lon)
                schoolList.append(row[0])
                zoneList.append(row[1])
                addressList.append(row[2])
                postList.append(row[3])
                print([row[0], lat, lon , 2])
            elif checkMap(row[3]):
                nomObj = nom.query(row[3])
                lat = nomObj[0].get("lat")
                lon = nomObj[0].get("lon")
                latList.append(lat)
                lonList.append(lon)
                schoolList.append(row[0])
                zoneList.append(row[1])
                addressList.append(row[2])
                postList.append(row[3])
                print([row[0], lat, lon, 3])
            else:
                print([row[0], "SERIOUS ERROR"])

def writeFiles(fileName, schoolList, zoneList, addressList, postList, latList, lonList):
    with open(fileName, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        index = 0
        while index < len(schoolList):
            writer.writerow([schoolList[index], zoneList[index], addressList[index], postList[index], latList[index], lonList[index]])
            index+= 1

for files in fileLoc:
    latList = []
    lonList = []
    schoolList = []
    zoneList = []
    addressList = []
    postList = []
    openFile(files)
    writeFiles(files,schoolList, zoneList, addressList, postList, latList, lonList)
