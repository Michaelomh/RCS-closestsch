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
