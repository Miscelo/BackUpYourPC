#!/usr/bin/env python3

import os
from setuptools import getTime, createLog


user = "mic"
backupfile = "../data/backupfolders.txt"

def startmenue(backupfile, user):
    print("****** MENU *******")
    print("(i) Insert new Backup folder")
    print("(r) Remove Backup- Folders")
    print("(o) Show Backup- folders")
    print("(s) Send last backup- report.")
    print("(m) Show logs.")
    print("(c) General configuration")
    print("(b) Start BACKUP")
    print("(h) Help - First instructions")
    letter = input("Your choice: ")
    print(letter)
    if(letter == "i"):
        newFolder(backupfile, user)


def newFolder(backupfile, user):
    backuppath = input("Please write full path for your backup- folder or (Q)uit!")
    if backuppath is not "Q":
        with open(backupfile, "a") as f:
            f.write(backuppath)
    message = backuppath + "created and added to file " + backupfile +".:" + user
    createLog(message)

startmenue(backupfile, user)

"""
#Exist file with backup-path inside  /data/backupfolders.txt
if(os.path.exists(backupfile)):
    with open(backupfile, "r") as f:
        for line in f:
            print(line)

else:
    with open(backupfile, "a") as file:
        file.write("/home/"+user+"/Testfolder\n")

    
newfolder = input("Write path to backupfolder")




date = getTime()
print(date)
"""


# except PErmission error
# except Filenot found error