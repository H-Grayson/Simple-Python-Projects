import os
import time
import shutil
import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askdirectory



root = Tk()
root.title("Select folder to be cleared after 24 hours of inactivity")
root.geometry("350x350")


    #button targeting where files will be selected from
def sbutton():
    folderChecked = filedialog.askdirectory()
    sourceDirectory.insert(0,folderChecked)
        
    
    #button targeting where files last modified >= 24 hours ago will go
def fbutton():
    folderTarget = filedialog.askdirectory()
    destinationDirectory.insert(0,folderTarget)

def sortbutton():
    source = sourceDirectory.get()
    destination = destinationDirectory.get()
    source_files = os.listdir(source)
    # if files in folder are getmtime >= 24 hours move files from folderChecked to folderTarget
    for file in source_files:
        filepath = os.path.join(source, file)
        if os.path.getmtime(filepath) >= (time.time() - 60*60*24):
            shutil.move(source + '/' + file, destination)

label = Label(root, text="Choose folder to be checked daily.")
label.grid(row=0, column=0, padx=(20,10), pady=(30,0))

# button used to choose folder to scan for .txt files
browseB = ttk.Button(root, text="From", command=sbutton)
browseB.grid(row=1, column=0, padx=(20,10), pady=(30,0))
sourceDirectory = Entry(root, width=100)
sourceDirectory.grid(row=2, column=0, padx=(20,10), pady=(30,0))

# button used to select where the .txt files will go
selectB = ttk.Button(root, text="To", command=fbutton)
selectB.grid(row=3, column=0, padx=(20,10), pady=(30,0))
destinationDirectory = Entry(root, width=100)
destinationDirectory.grid(row=4, column=0, padx=(20,10), pady=(30,0))
                          
# button used to perform sort action
sortB = ttk.Button(root, text="Sort", command=sortbutton)
sortB.grid(row=5, column=0, padx=(20,10), pady=(30,0))

root.mainloop()
