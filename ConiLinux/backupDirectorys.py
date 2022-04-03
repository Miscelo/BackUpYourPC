#!/usr/bin/env python3

import sys
import os
from datetime import date, datetime
import shutil

def getTime():
    #backupdate returns "YYYY-MM-DD HH:MM:SS" - format
    backuptime = datetime.now()
    strtime = backuptime.strftime("%Y-%m-%d %H:%M:%S")
    return strtime


#list of all folders that will be backuped.
backupfolders = ['/home/[user]/Documents', '/home/[user]/pro']

#Make a control that all the given pathes exist on startup.
def checkPathExists():
    pass

# funktion return true, if there are more than 10% free on disk, false if not
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total *100
    return free > 10




