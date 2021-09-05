from tkinter import *
# if import * does import all, why we need the following lines?
from tkinter import ttk # this are the tabs called notebooks 
from tkinter import messagebox

root = Tk()
root.title('converter')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry('500x500')


#create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady = 50)

#create two frames
curreny_frame = Frame(my_notebook, width = 480,  height = 480)
conversion_frame = Frame(my_notebook, width = 480, height = 480)

curreny_frame.pack(fill = 'both', expand = 1)
conversion_frame.pack(fill = 'both', expand = 1)


#add our tabs
my_notebook.add(curreny_frame, text = 'Currencies')
my_notebook.add(conversion_frame, text = 'convert')

####################
# currency code
####################










root.mainloop()

