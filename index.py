from Tkinter import *
from tkFileDialog import *

import os.path

filename = None

def newFile():
    global filename
    filename = "untitled"

    text.delete(0.0, END)

def saveFile():
    global filename

    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title='Error: ', message='there was an error while saving the file')

def openFile():
    f = askopenfile(mode='r')
    t = f.read
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("Editor")
root.minsize(width=240, height=144)

text = Text(root)

text.pack(expand=True, fill='both')

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_command(label="Save File", command=saveFile)
filemenu.add_command(label="Sve File As", command=saveAs)

filemenu.add_separator()

filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()