from nominatim import Nominatim
import csv

Nom=Nominatim()

row = Nom.query("Singapore 419612")

if len(row) == 0:
    print ("Failure")
else :
    print(row[0].get("lat") + ", " + row[0].get("lon"))

#lat = Nom.query("Singapore GEYLANG METHODIST SECONDARY SCHOOL")[0].get("lat")
#lon = Nom.query("Singapore GEYLANG METHODIST SECONDARY SCHOOL")[0].get("lon")
#print(lat + ", " + lon)

#, 60 PASIR RIS DRIVE 1, 519524
