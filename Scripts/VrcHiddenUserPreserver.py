#A script to change the show satus of all users to default
#Writen by Dyslex1k
import os
import getpass
import glob

#
whitelist = []
blacklist = []

username = getpass.getuser()
file_path = fr"C:\Users\{username}\AppData\LocalLow\VRChat\VRChat\LocalPlayerModerations"

def meetupShow(folder):
    #Finds the location of the vrc file
    with open(folder, "w") as file:
        writeString = ""
        for host in whitelist:
            writeString = writeString + host + "                        005\n"
    
        for user in blacklist:
            writeString = writeString + user

        file.write(writeString)
        print(writeString)

def preserveHide(folder):
    with open(folder, "r") as file:
        lines = file.readlines()
        for line in lines:
            if "             004\n" in line:
                blacklist.append(line)


# Construct the complete pattern with the folder path
pattern = os.path.join(file_path, "usr_*-show-hide-user.vrcset")

# Use glob to retrieve matching files in the specified folder
matching_files = glob.glob(pattern)

if matching_files:
    for file_path in matching_files:
        preserveHide(file_path)
        meetupShow(file_path)
else:
    print("No matching files found.")
