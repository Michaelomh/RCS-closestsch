from nominatim import Nominatim
import csv

schoolList = []
coordList = []
#Nom=Nominatim()

with open("data/east.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[0] + ", " + row[2] + ", " + row[3])
        nom = Nominatim()
        nomObj = []

        if len(nom.query(row[2])) > 0:
            #exist in school name
            nomObj = nom.query(row[2])
        elif len(nom.query(row[3])) > 0:
            #exists in address
            nomObj = nom.query("Singapore " + row[3])
        elif len(nom.query(row[0])) > 0:
            #exist in postal code
            nomObj = nom.query(row[0])

        if len(nomObj) > 0:
            #print if exist
            lat = float(nomObj[0].get("lat"))
            lon = float(nomObj[0].get("lon"))
            print(lat, lon)
            if not(0 < lat < 2) and  not(102 < lon < 104):
                print("Error At: " + row[0] + ", " + row[2] + ", " + row[3])
        else :
            #print error if does not exist
            print("Error")

        #check where works
        #retrieve long lat
        #print long lat

        '''
        if len(school) == 0
            print(row[0] + " - school fail")
        elif len(address) == 0:
            print(row[2] + " - school fail")
        '''
#print(schoolList)
'''
for rows in schoolList:
    print(rows)
    address = Nom.query(rows)
    print(address[0].get("lat") + ", " + address[0].get("lon"))


dir retrieveLonLat (listofSchools):



print(coordList)

lat = Nom.query("GONGSHANG PRIMARY SCHOOL")[0].get("lat")
lon = Nom.query("GONGSHANG PRIMARY SCHOOL")[0].get("lon")
print(lat + ", " + lon)
'''
