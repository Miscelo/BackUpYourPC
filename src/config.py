""" Config.py .- file where the user will decide the folders that will be backuped with their subfolders.
    Finally, the result of this script will be a file with a list of folders to backup in it.
    Every line will be an entry like: /home/<username>/Documents   or    /etc/network/
"""
#!/usr/bin/env python3

import os
import csv
import logging

# This files will be create starting this script. Just backupfile will be created in a function when needed.
logfile = "../data/backup.log"
backupfile = "../data/backupfolders.csv"
path_id_file = "../data/path_id"
email_file = "../data/email"
destination_file = "../data/destination"

# *** ----- Logging Module , basicConfig ----- ***
logging.basicConfig(filename=logfile,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    filemode='a',
                    datefmt='%b %d %H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger()


menu = {"i": "insert new Backup-folders",
        "r": "remove Backup-folders",
        "s": "show Backup-folders",
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


# Function will check if the input from keyboad of the user is a key of the "menu"-Dictionary
def valid_item(userinput, menu):
    return userinput in menu.keys()

def get_item():
    print("----------------------------------------------------------------------------------")
    letter = input("\tYour choice: ")
    return letter

# Whis this functino, the user can choose with a key different functions.
def choose_item(menu):
    letter = "notvalid"
    while not valid_item(letter, menu):
        letter = get_item()
        if letter == "i":
            add_newFolder(backupfile)
        elif letter == "r":
            remove_folder(backupfile)
        elif letter == "s":
            show_folder(backupfile)
        elif letter == "d":
            config_destination(destination_file)
        elif letter == "e":
            print("set email")
        elif letter == "l":
            show_logfile(logfile)
        elif letter == "b":
            print("will call main.py and start a backup")
        elif letter == "h":
            print("Help, I need somebody.")
        elif letter == "q":
            print("----------------------------------------------------------------------------------")
            print("************************  Finish Program - See you soon  *************************")
        else:
            print("\t* Input Error!!! \""+letter+"\" is not a valid input! Try again please. *")
            print_menu(menu)
        return letter

# Every file has a starting Value.
# Later, before starting backup, we will use this values for checking the configuration.
def create_Configfiles(path_id_file, email_file, destination_file):
    try:
        with open(path_id_file, "x") as file:
            file.write("1")
    except FileExistsError:
        pass
    try:
        with open(email_file, "x") as file:
            file.write("mail@host.com")
    except FileExistsError:
        pass
    try:
        with open(destination_file, "x") as file:
            file.write("1,Not configured yet")
    except FileExistsError:
        pass


# return a unique value of a config file as a string
def read_configFile(configfile):
    with open(configfile) as file:
        value = file.read()
    return value


# increase the path ID number once in the file
def raise_pathID(path_id):
    path_int = (int(path_id))+1
    with open("../data/path_id", "w") as file:
        file.write(str(path_int))    

# Write an ID and userinput to
def add_newFolder(backupfile):
    path_id = read_configFile("../data/path_id")
    backuppath = input("\tPlease write full path for your backup- folder or (Q)uit! ")
    if not os.path.exists(backuppath):
        print("\n\tInfo: Path " + backuppath + " does not exist or check rights for reading!")
    if(backuppath != "Q"):
        path_dic = [{"id": path_id, "path": backuppath}]
        keys = ["id", "path"]
        try:
            with open(backupfile, "a") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys)
                if( path_id == "1" ):
                    writer.writeheader()
                writer.writerows(path_dic)
            csvfile.close()
            logger.info("Added path to \'" + backupfile + "\' with ID " + path_id + ": " + backuppath)
        except FileNotFoundError:
            print("File not Found Error: Database file "+backupfile)
            logger.error("File not Found Error: Database file "+backupfile)
    raise_pathID(path_id)

#read the csv file in memory as a list, then edit that list, and then write it back to the csv file without one line.
def remove_folder(backupfile):
    lines = list()
    id_delete = input("\tPlease enter the ID of the path to be deleted from list: ")
    try:
        with open(backupfile, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == id_delete:
                        lines.remove(row)
    except FileNotFoundError:
        print("File not Found Error: Database file " + backupfile)
        logger.error("File not Found Error: Database file " + backupfile)
    with open(backupfile, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    print("\tID " + id_delete + " deleted successfully!" )
    logger.info("Backuppath with ID " + id_delete + " deleted from " + backupfile)

def show_folder(backupfile):
    print("\tID: Backup-Folder")
    try:
        with open(backupfile) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("\t{}: {}".format(row["id"], row["path"]))
    except FileNotFoundError:
        print("File not Found Error: Database file " + backupfile)
        logger.error("File not Found Error: Database file " + backupfile)


def config_destination(destination_file):
    print("\tPath of destination or host for backup.")
    with open(destination_file) as file:
        reader = file.read()
    print("\t"+reader)
    change_destination = input("\tWould you like to set the destination folder for your backup? [Y/N] ")
    if change_destination == "Y":
        destination = input("\tPlease write path to your backup folder e.g. \'/home/username/backup\': ")
        with open(destination_file, 'w') as file:
            file.write(destination)
        logger.info("Destination for backup configured to " + destination)
    else:
        print_menu(menu)




def show_logfile(logfile):
    with open(logfile) as file:
        for line in file:
            print(line.rstrip("\n"))



create_Configfiles(path_id_file, email_file, destination_file)
print_menu(menu)
item = ' '
while not (item == "q"):
    item = choose_item(menu)



