import csv

#retrieve all of the north schools, and their long, lat.
#TODO: add in long and lat and get them
def north_schools():
    with open("data/north.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            for row in file:
                lb1.insert(END,row[0])

#retrieve all of the south schools, and their long, lat.
#TODO: add in long and lat and get them
def south_schools():
    with open("data/south.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            for row in file:
                lb1.insert(END,row[0])

#retrieve all of the west schools, and their long, lat.
#TODO: add in long and lat and get them
def west_schools():
    with open("data/west.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            for row in file:
                lb1.insert(END,row[0])

#retrieve all of the east schools, and their long, lat.
#TODO: add in long and lat and get them
def east_schools():
    with open("data/east.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            for row in file:
                lb1.insert(END,row[0])
