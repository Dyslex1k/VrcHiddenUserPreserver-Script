#A script to change the show satus of all users to default

import os
import getpass
import glob

meetup_hosts = ["usr_24bc8044-6ec2-4a3d-bdc4-cd6cf858c72f", "usr_cc00ac2c-e64e-4111-be5b-c852a44ff2f1", "usr_aa7c5388-6124-487a-a620-bd8d5f8beedc", "usr_4da3cfac-907f-4ea1-bfe5-f59a866f7ef0", "usr_923acdda-9202-4f4d-91c0-d0d7269c96a5"]
blacklist = []

username = getpass.getuser()
file_path = fr"C:\Users\{username}\AppData\LocalLow\VRChat\VRChat\LocalPlayerModerations"

def meetupShow(folder):
    #Finds the location of the vrc file
    with open(folder, "w") as file:
        writeString = ""
        for host in meetup_hosts:
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
        print(file_path)
        preserveHide(file_path)
        meetupShow(file_path)
else:
    print("No matching files found.")
