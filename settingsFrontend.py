from tkinter import *

#tk initalizer
window=Tk()
window.wm_title("Settings")

#Zone Selector Section
l1 = Label(window, text="Selected Zone")
l1.grid(row=0,column=0)

b1=Button(window, text="North", width=12)
b1.grid(row=1,column=0, padx=5, pady=5)

b2=Button(window, text="South", width=12)
b2.grid(row=1,column=1, padx=5, pady=5)

b3=Button(window, text="east", width=12)
b3.grid(row=1,column=2, padx=5, pady=5)

b4=Button(window, text="West", width=12)
b4.grid(row=1,column=3, padx=5, pady=5)

#Details Section
l1 = Label(window, text="School Name")
l1.grid(row=2,column=0)

e1_val = StringVar()
e1=Entry(window, textvariable=e1_val, width=50)
e1.grid(row=2,column=1,columnspan=3, pady=5, padx=5)

l2 = Label(window, text="Address")
l2.grid(row=3,column=0)

e2_val = StringVar()
e2=Entry(window, textvariable=e2_val, width=50)
e2.grid(row=3,column=1,columnspan=3, pady=5, padx=5)

l3 = Label(window, text="Postal Code")
l3.grid(row=4,column=0)

e3_val = StringVar()
e3=Entry(window, textvariable=e3_val, width=50)
e3.grid(row=4,column=1,columnspan=3, pady=5, padx=5)

window.mainloop()
