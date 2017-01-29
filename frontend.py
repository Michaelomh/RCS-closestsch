#imports
from tkinter import *
from autocomplete import *
from backend import *
from geopy.distance import vincenty

#TODO: Once you got a list of schools and the selecting school, you go and find the closest school.

#There is a need to if empty then do nothing.
def getSchoolList(event):
    global activeSchoolList
    global selected
    activeSchoolList = []
    activeList=lb1.curselection()
    for i in activeList:
        activeSchoolList.append(lb1.get(i))
    print(activeSchoolList)

#get all info based on school name and populate the entry boxes
def retrieveSchoolCoords(schoolName) :
    toReturn = []
    dataloc = "data/" + SELECTEDZONE + ".csv"
    #print(dataloc)
    with open(dataloc,"r") as file:
        file = csv.reader(file, delimiter=',')
        for row in file:
            if(row[0] == schoolName) :
                toReturn = (row[4], row[5])
                break
    return toReturn

def closestSchoolLocator():
    #TODO 1. Get the selected school - DONE
    #TODO 2. Get the list of selected schools - DONE
    #TODO 3. Get the distance from the selected school to all the schools. - DONE
    #TODO 4. Return the minimum distance, the school and put to result page
    selectedSchool = e1.get()
    print("Selected School = ",e1.get())
    #get long, lat of the school, don't bother searching?
    selectedCoords = retrieveSchoolCoords(selectedSchool)
    shortestDist = 99999
    bestSchool = "No Result Found"
    for schools in activeSchoolList:
        diffDist = vincenty(selectedCoords, retrieveSchoolCoords(schools))
        if shortestDist > float(str(diffDist)[0:7]):
            shortestDist = float(str(diffDist)[0:7])
            bestSchool = schools
            #print(schools, float(str(diffDist)[0:7]))
            #print("ShortestDist is now = ", shortestDist)
        #else:
            #print(schools, "failed@", float(str(diffDist)[0:7]))
    #print("final result =", bestSchool, "(",shortestDist, "km)")
    result_textbox.delete(0, END)
    result_textbox.insert(END,bestSchool)

#retrieve all of the schools by selection, and their long, lat.
def north_schools():
    listbox_text.set("North Zone Schools")
    global SELECTEDZONE
    SELECTEDZONE = "north"
    with open("data/north.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            resetListBox()
            for row in file:
                lb1.insert(END,row[0])

def south_schools():
    listbox_text.set("South Zone Schools")
    global SELECTEDZONE
    SELECTEDZONE = "south"
    with open("data/south.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            resetListBox()
            for row in file:
                lb1.insert(END,row[0])

def west_schools():
    listbox_text.set("West Zone Schools")
    global SELECTEDZONE
    SELECTEDZONE = "west"
    with open("data/west.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            resetListBox()
            for row in file:
                lb1.insert(END,row[0])

def east_schools():
    listbox_text.set("East Zone Schools")
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

#tk initalizer
window=Tk()
window.wm_title("Closest School Finder")

#selecting school to search for
l1 = Label(window, text="Selected School")
l1.grid(row=0,column=0)

e1 = AutocompleteEntry(schoolList, window, width=50)
e1.grid(row=0,column=1,columnspan=3, pady=5, padx=5)

#Buttons to change the value in the list box.
b1=Button(window, text="North", width=12, command=north_schools)
b1.grid(row=1,column=0, padx=5, pady=5)

b2=Button(window, text="South", width=12, command=south_schools)
b2.grid(row=1,column=1, padx=5, pady=5)

b3=Button(window, text="East", width=12, command=east_schools)
b3.grid(row=1,column=2, padx=5, pady=5)

b4=Button(window, text="West", width=12, command=west_schools)
b4.grid(row=1,column=3, padx=5, pady=5)

listbox_text = StringVar()
listbox_text.set("Please select a zone")

#list box + Scroll bar goes here
listbox_label = Label(window,textvariable=listbox_text)
listbox_label.grid(row=2,column=0, columnspan=2, sticky= "W",padx=5)

lb1 = Listbox(window, height=8,width=68, selectmode=MULTIPLE)
lb1.grid(row=3, column=0, rowspan=6, columnspan=4)
lb1.bind("<<ListboxSelect>>",getSchoolList)

#Result Rows
result_label = Label(window, text="Result")
result_label.grid(row=9,column=0)

result_textVal = StringVar()
result_textbox=Entry(window, textvariable=result_textVal, width=30)
result_textbox.grid(row=9,column=1, columnspan=2)

result_button=Button(window, text="Search", width=12, command=closestSchoolLocator)
result_button.grid(row=9,column=3, pady=5, padx=5)

window.mainloop()
