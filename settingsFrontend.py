from tkinter import *
import csv
from nominatim import Nominatim

nom = Nominatim()

schoolsToAdd = []

#retrieve all of the schools by selection, and their long, lat.
def north_schools():
    global SELECTEDZONE
    SELECTEDZONE = "north"
    with open("data/north.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            resetListBox()
            for row in file:
                lb1.insert(END,row[0])

def south_schools():
    global SELECTEDZONE
    SELECTEDZONE = "south"
    with open("data/south.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            resetListBox()
            for row in file:
                lb1.insert(END,row[0])

def west_schools():
    global SELECTEDZONE
    SELECTEDZONE = "west"
    with open("data/west.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            resetListBox()
            for row in file:
                lb1.insert(END,row[0])

def east_schools():
    global SELECTEDZONE
    SELECTEDZONE = "east"
    with open("data/east.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            resetListBox()
            for row in file:
                lb1.insert(END,row[0])

#reset list box to be empty.
def resetListBox():
    lb1.delete(0, END)

#reset list box to the correct school
def repopulateSchools():
    if (SELECTEDZONE == "north"):
        north_schools()
    elif (SELECTEDZONE == "south"):
        south_schools()
    elif (SELECTEDZONE == "west"):
        west_schools()
    elif (SELECTEDZONE == "east"):
        east_schools()

def resetListBox2():
    lb1.after(500, repopulateSchools)

#get the school name of the current selection
def getid(event):
    global selected
    selected = lb1.get(lb1.curselection()[0])
    print(selected)
    getSchoolInfo(selected)

#get all info based on school name and populate the entry boxes
def getSchoolInfo (schoolName):
    #print(SELECTEDZONE)
    dataloc = "data/" + SELECTEDZONE + ".csv"
    #print(dataloc)
    with open(dataloc,"r") as file:
            file = csv.reader(file, delimiter=',')
            for row in file:
                if(row[0] == schoolName) :
                    #reset value
                    lat_entry.config(state=NORMAL)
                    lon_entry.config(state=NORMAL)
                    school_entry.delete(0,END)
                    address_entry.delete(0,END)
                    postal_entry.delete(0,END)
                    lat_entry.delete(0,END)
                    lon_entry.delete(0,END)

                    #insert new value
                    school_entry.insert(END,row[0])
                    address_entry.insert(END,row[2])
                    postal_entry.insert(END,row[3])
                    lat_entry.insert(END,row[4])
                    lon_entry.insert(END,row[5])
                    lat_entry.config(state=DISABLED)
                    lon_entry.config(state=DISABLED)

#command to rewrite the full schools in the schoolsToAdd list
def writeSchool():
    with open("data/" + SELECTEDZONE + ".csv", 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        for school in schoolsToAdd:
            writer.writerow(school)
        #reset the lines
        school_entry.delete(0,END)
        address_entry.delete(0,END)
        postal_entry.delete(0,END)
        lat_entry.config(state=NORMAL)
        lon_entry.config(state=NORMAL)
        lon_entry.delete(0,END)
        lat_entry.delete(0,END)

#command to edit the new school information. Does not check the long and lat and use the previous long and lat
def editSchool(school,zone,address,postal,lat,lon):
    schoolsToAdd[:] = [] #empty the schoolsToAdd just in case
    with open("data/" + SELECTEDZONE + ".csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[4] != lat:
                schoolsToAdd.append([row[0],row[1],row[2],row[3],row[4],row[5]])
            else:
                schoolsToAdd.append([school,zone,address,postal,lat,lon])
        writeSchool()

#command to delete an entry in the row
def deleteSchool(schoolName):
    schoolsToAdd[:] = [] #empty the schoolsToAdd just in case
    with open("data/" + SELECTEDZONE + ".csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] != schoolName:
                schoolsToAdd.append([row[0],row[1],row[2],row[3],row[4],row[5]])
        writeSchool()

#checks if the lat and lon param is found within Singapore
def validSingaporeCoord(lat, lon):
    if (1.2 < lat < 1.5) and (103 < lon < 104):
        return True
    else:
        return False

#checks if the param is found within Singapore, used validSingaporeCoord method
def checkMap(query):
    nomObj = nom.query(query)
    if len(nomObj) > 0 and validSingaporeCoord(float(nomObj[0].get("lat")), float(nomObj[0].get("lon"))) :
        return True
    else :
        return False

#checks if all params is found in singapore, used checkMap method
def validCoord(school, address, postal):
    if checkMap(school):
        nomObj = nom.query(school)
        lat = nomObj[0].get("lat")
        lon = nomObj[0].get("lon")
        return[lat,lon]
    elif checkMap(address):
        nomObj = nom.query(address)
        lat = nomObj[0].get("lat")
        lon = nomObj[0].get("lon")
        return[lat,lon]
    elif checkMap(postal):
        nomObj = nom.query(postal)
        lat = nomObj[0].get("lat")
        lon = nomObj[0].get("lon")
        return[lat,lon]
    else:
        return["0","0"]

#main Commands
def addCommand():
    school = school_val.get()
    address = address_val.get()
    postal = postal_val.get()
    print(school + ", " + address + ", " + postal)

    #Checks the long and lat & Change the text in add
    lat = validCoord(school, address, postal)[0]
    lon = validCoord(school, address, postal)[1]

    if lat == "0" or lon == "0":
        #If false, notify using red boxes on the entry field
        school_entry.config(fg='red')
        address_entry.config(fg='red')
        postal_entry.config(fg='red')
    else :
        #If true, add into csv, everything + long and lat, zone don't care
        print(lat + ", " + lon)
        #write into text entry
        lat_entry.config(state=NORMAL)
        lon_entry.config(state=NORMAL)
        lat_entry.delete(0,END)
        lon_entry.delete(0,END)
        lat_entry.insert(END,lat)
        lon_entry.insert(END,lon)
        lat_entry.config(state=DISABLED)
        lon_entry.config(state=DISABLED)

        #write into csv
        with open("data/" + SELECTEDZONE + ".csv", 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
            writer.writerow([school, SELECTEDZONE.upper() + " MANUAL", address , postal, lat, lon])

        #after finish writing, resetListBox
        resetListBox2()

def editCommand():
    school = school_val.get()
    address = address_val.get()
    postal = postal_val.get()
    lat = lat_val.get()
    lon = lon_val.get()
    editSchool(school,"zone",address,postal,lat,lon)
    resetListBox2()

def deleteCommand():
    school = school_val.get()
    deleteSchool(school)
    resetListBox2()

#tk initalizer
window=Tk()
window.wm_title("Settings")

#Zone Selector Section
l1 = Label(window, text="Selected Zone")
l1.grid(row=0,column=0)

north_button=Button(window, text="North", width=12, command=north_schools)
north_button.grid(row=1,column=0, padx=5, pady=5)

south_button=Button(window, text="South", width=12, command=south_schools)
south_button.grid(row=1,column=1, padx=5, pady=5)

east_button=Button(window, text="East", width=12, command=east_schools)
east_button.grid(row=1,column=2, padx=5, pady=5)

west_button=Button(window, text="West", width=12, command=west_schools)
west_button.grid(row=1,column=3, padx=5, pady=5)

#Details Section
school_label = Label(window, text="School Name")
school_label.grid(row=2,column=0, sticky= "E")

address_label = Label(window, text="Address")
address_label.grid(row=3,column=0, sticky= "E")

postal_label = Label(window, text="Postal Code")
postal_label.grid(row=4,column=0, sticky= "E")

school_val = StringVar()
school_entry=Entry(window, textvariable=school_val, width=50)
school_entry.grid(row=2,column=1,columnspan=3, pady=5, padx=5)

address_val = StringVar()
address_entry=Entry(window, textvariable=address_val, width=50)
address_entry.grid(row=3,column=1,columnspan=3, pady=5, padx=5)

postal_val = StringVar()
postal_entry=Entry(window, textvariable=postal_val, width=50)
postal_entry.grid(row=4,column=1,columnspan=3, pady=5, padx=5)

#long lat Entry Box
lat_label = Label(window, text="Latitude")
lat_label.grid(row=5,column=0, sticky= "E")

lat_val = StringVar()
lat_entry=Entry(window, textvariable=lat_val, width=10)
lat_entry.grid(row=5,column=1, pady=5, padx=5)

lon_label = Label(window, text="Longitude", width=15)
lon_label.grid(row=5,column=2, sticky= "E")

lon_val = StringVar()
lon_entry=Entry(window, textvariable=lon_val, width=16)
lon_entry.grid(row=5,column=3, pady=5, padx=5)

#ListBox + Buttons
lb1 = Listbox(window, height=8,width=50)
lb1.grid(row=6, column=0, rowspan=6, columnspan=3)
lb1.bind("<<ListboxSelect>>",getid)

add_button=Button(window, text="Add", width=12, command=addCommand)
add_button.grid(row=6,column=3, padx=5, pady=5)

edit_button=Button(window, text="Edit", width=12, command=editCommand)
edit_button.grid(row=7,column=3, padx=5, pady=5)

delete_button=Button(window, text="Delete", width=12, command=deleteCommand)
delete_button.grid(row=8,column=3, padx=5, pady=5)

check_button=Button(window, text="Close", width=12, command=window.destroy)
check_button.grid(row=9,column=3, padx=5, pady=5)

window.mainloop()
