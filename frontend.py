#imports
from tkinter import *
from autocomplete import *
from backend import *

#There is a need to if empty then do nothing.
def getid(event):
    global selected
    index=lb1.curselection()
    print(len(index))
    selected = lb1.get(index[0])
    #selected1 = lb1.get(index[1])
    print(selected)
    #print(selected1)

#tk initalizer
window=Tk()
window.wm_title("Closest School Finder")

#selecting school to search for
l1 = Label(window, text="Selected School")
l1.grid(row=0,column=0)

e1_val = StringVar()
print(schoolList)
e1 = AutocompleteEntry(schoolList, window, width=50)
e1.grid(row=0,column=1,columnspan=3, pady=5, padx=5)

#Buttons to change the value in the list box.
#TODO: Integrate the north, south, east and west command
b1=Button(window, text="North", width=12, command=north_schools)
b1.grid(row=1,column=0, padx=5, pady=5)

b2=Button(window, text="South", width=12, command=south_schools)
b2.grid(row=1,column=1, padx=5, pady=5)

b3=Button(window, text="east", width=12, command=east_schools)
b3.grid(row=1,column=2, padx=5, pady=5)

b4=Button(window, text="West", width=12, command=west_schools)
b4.grid(row=1,column=3, padx=5, pady=5)

#list box + Scroll bar goes here
listbox_label = Label(window, text="North Zone Schools")
listbox_label.grid(row=2,column=0, columnspan=2, sticky= "W",padx=5)

lb1 = Listbox(window, height=8,width=68, selectmode=MULTIPLE)
lb1.grid(row=3, column=0, rowspan=6, columnspan=4)
#lb1.bind("<<ListboxSelect>>",getid)

#for row in backend.view():
#    c1.insert(END,row)
'''
sb1 = Scrollbar(window)
sb1.grid(row=2,column=4,rowspan=6)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)
'''
#Result Rows
result_label = Label(window, text="Result")
result_label.grid(row=9,column=0, sticky= "E")

result_textVal = StringVar()
result_textbox=Entry(window, textvariable=result_textVal, width=30)
result_textbox.grid(row=9,column=1, columnspan=2)

result_button=Button(window, text="Search", width=12)
result_button.grid(row=9,column=3, pady=5, padx=5)

window.mainloop()
