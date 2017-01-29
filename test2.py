import csv

fileLoc = "data/east.csv"
schoolsToAdd = []

def writeSchool():
    print("-----")
    print(schoolsToAdd)
    with open(fileLoc, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        for school in schoolsToAdd:
            writer.writerow(school)

def deleteSchool(schoolName):
    schoolsToAdd[:] = [] #empty the schoolsToAdd just in case
    with open(fileLoc) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] != schoolName:
                schoolsToAdd.append([row[0],row[1],row[2],row[3],row[4],row[5]])
        writeSchool()

deleteSchool("CHANGKAT CHANGI SECONDARY SCHOOL")

import csv

fileLoc = "data/east.csv"
schoolsToAdd = []

def writeSchool():
    with open(fileLoc, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        for school in schoolsToAdd:
            writer.writerow(school)

def editSchool(school,zone,address,postal,lat,lon):
    schoolsToAdd[:] = [] #empty the schoolsToAdd just in case
    with open(fileLoc) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[4] != lat:
                schoolsToAdd.append([row[0],row[1],row[2],row[3],row[4],row[5]])
            else:
                schoolsToAdd.append([school,zone,address,postal,lat,lon])
        writeSchool()

editSchool("CHANGKAT CHANGI SECONDARY SCHOOLs","EAST 41","23 SIMEI ST 31","5298941","1.3404936","103.952981211205")
