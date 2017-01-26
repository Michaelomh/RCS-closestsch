from nominatim import Nominatim
import csv

nom = Nominatim()
fileLoc = ["data/east.csv", "data/north.csv", "data/south.csv", "data/west.csv"]

#give 2 params and return if that location is in singapore or not.
#lat max and min = 1.470 & 1.2289
#lon max and min = 103.5855 & 104.031
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
                print([row[0], lat, lon , 1])
            elif checkMap(row[2]):
                lat = nomObj[0].get("lat")
                lon = nomObj[0].get("lon")
                print([row[0], lat, lon , 2])
            elif checkMap(row[3]):
                lat = nomObj[0].get("lat")
                lon = nomObj[0].get("lon")
                print([row[0], lat, lon, 3])
            else :
                print([row[0], "SERIOUS ERROR"])

for files in fileLoc:
    openFile(files)
