from tkinter import *
import csv

#retrieve all of the schools by selection, and their long, lat.
#TODO: add in long and lat and get them and store them, ready to be used.
def north_schools():
    with open("data/north.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            reset()
            for row in file:
                lb1.insert(END,row[0])

def south_schools():
    with open("data/south.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            reset()
            for row in file:
                lb1.insert(END,row[0])

def west_schools():
    with open("data/west.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            reset()
            for row in file:
                lb1.insert(END,row[0])

def east_schools():
    with open("data/east.csv","r") as file:
            file = csv.reader(file, delimiter=',')
            reset()
            for row in file:
                lb1.insert(END,row[0])

def reset():
    lb1.delete(0, END)

#TODO: select list box and appear on the address, postal code and school name
def getid(event):
    global selected
    index=lb1.curselection()
    print(len(index))
    #selected = lb1.get(index[0])
    #selected1 = lb1.get(index[1])
    #print(selected)
    #print(selected1)



#TODO: Add command to check then write the long lat into the csv file
#TODO: Delete command to delete the specified school_label
#TODO: Edit Command to edit the details and check again before removing everything

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

#ListBox + Buttons
lb1 = Listbox(window, height=8,width=50, selectmode=MULTIPLE)
lb1.grid(row=5, column=0, rowspan=6, columnspan=3)
lb1.bind("<<ListboxSelect>>",getid)

add_button=Button(window, text="Add", width=12)
add_button.grid(row=5,column=3, padx=5, pady=5)

check_button=Button(window, text="Check", width=12)
check_button.grid(row=8,column=3, padx=5, pady=5)

edit_button=Button(window, text="Edit", width=12)
edit_button.grid(row=6,column=3, padx=5, pady=5)

delete_button=Button(window, text="Delete", width=12)
delete_button.grid(row=7,column=3, padx=5, pady=5)

window.mainloop()
