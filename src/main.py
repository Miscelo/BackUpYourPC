#!/usr/bin/env python3

import os
from setuptools import getTime

print("Show Path to backup:")


user = "mic"
backupfile = "../data/backupfolders.txt"

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