""" Config.py .- file where the user will decide the folders that will be backuped with their subfolders.
    Finally, the result of this script will be a file with a list of folders to backup in it.
    Every line will be an entry like: /home/<username>/Documents   or    /etc/network/
"""
#!/usr/bin/env python3

import os
import logging

# *** ----- Logging Module , basicConfig ----- ***
logfile = "../data/backup.log"

logging.basicConfig(filename=logfile,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    filemode='a',
                    datefmt='%b %d %H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger()
# END ---------------------------------------- ***



backupfile = "../data/backupfolders.txt"
menu = {"i": "insert new Backup-folders",
        "r": "remove Backup-folders",
        "s": "show Back-folders",
        "d": "destination-folders configuration",
        "e": "email configuration for reports",
        "l": "logfile (show)",
        "b": "BACKUP (start backup)",
        "h": "help",
        "q": "quit"}


def print_menu(menu):
    print("\n*************************       BACKUP YOUR PC         ***************************")
    for menu_key, menu_text in menu.items():
        print("\t({}) {}".format(menu_key, menu_text))


def valid_item(userinput, menu):
    return userinput in menu.keys()

def get_item():
    print("----------------------------------------------------------------------------------")
    letter = input("\tYour choice: ")
    return letter


def choose_item(menu):
    letter = "notvalid"
    while not valid_item(letter, menu):
        letter = get_item()
        if (letter == "i"):
            add_newFolder(backupfile)
        elif (letter == "r"):
            remove_foder(backupfile)
        elif (letter == "s"):
            print("show backupfolders")
        elif (letter == "d"):
            print("show destinatino folders")
        elif (letter == "e"):
            print("set email")
        elif (letter == "l"):
            print("show all logs")
        elif (letter == "b"):
            print("will call main.py and start a backup")
        elif (letter == "h"):
            print("Help, I need somebody.")
        elif (letter == "q"):
            print("----------------------------------------------------------------------------------")
            print("*** Finish Program \"BackUp Your PC\" ***")
        else:
            print("Input Error: Not a valid input! Try again please.")
        return letter



def add_newFolder(backupfile):
    backuppath = input("Please write full path for your backup- folder or (Q)uit! ")
    if(backuppath != "Q"):
        try:
            with open(backupfile, "a") as f:
                f.write(str(backuppath)+"\n")
            logger.info(backuppath + " created and added to file :=" + backupfile)
        except FileNotFoundError:
            print("File not Found Error: Database file "+backupfile)
            logger.error("File not Found Error: Database file "+backupfile)


def remove_foder(backupfile):
    print("remove"+backupfile)



print_menu(menu)
item = ' '
while not (item == "q"):
    item = choose_item(menu)



