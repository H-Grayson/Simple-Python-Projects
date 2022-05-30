import os
import time
import shutil
import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askdirectory
import pathlib
from pathlib import Path


root = Tk()
root.title("Select folder to be cleared after 24 hours of inactivity")
root.geometry("350x350")


def sbutton():
    global folderChecked
    folderChecked = filedialog.askdirectory(parent=root, initialdir="/", title="Select Dir")
    print(folderChecked)
        
    
    #button targeting where files last modified >= 24 hours ago will go
def fbutton():
    global folderTarget
    folderTarget = filedialog.askdirectory(parent=root, title='Choose a file')
    print("Sending to " + folderTarget)

def sortbutton():
    # if folder ends with .txt and getmtime >= 24 hours move files from folderChecked to folderTarget
    for file in folderChecked:
        if folderChecked.endswith(".txt") and os.path.getmtime(filename) >= (time.time() - 60*60*24):
            shutil.move(os.path.join(folderChecked, filename), folderTarget)
        
    else: print("No files needing moved")

def testButton():
    print(folderChecked)

def testButton1():
    print(folderTarget)
 
label = Label(root, text="Choose folder to be checked daily.")
label.pack(pady=10)

# button used to choose folder to scan for .txt files
browseB = ttk.Button(root, text="From", command=sbutton).pack(pady=20)

# button used to select where the .txt files will go
selectB = ttk.Button(root, text="To", command=fbutton).pack(pady=30)

# button used to perform sort action
sortB = ttk.Button(root, text="Sort", command = sortbutton).pack(pady=30)

testb1 = ttk.Button(text="sending", command=testButton).pack()
testb2 = ttk.Button(text="recieving", command=testButton1).pack()
