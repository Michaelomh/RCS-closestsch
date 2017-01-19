from tkinter import *

root = Tk()

frame = Frame(root, bd=2, relief=SUNKEN)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, bd=0, yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

frame.pack()

mainloop()
