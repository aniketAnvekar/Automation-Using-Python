
'''Reading a file'''
f = open('C:\\Users\\anike\\Desktop\\Automate with Python\\Ex_Files_Python_Automation\Exercise Files\\inputFile.txt','r')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)

f.close()



'''Writing into a file'''
f = open('C:\\Users\\anike\\Desktop\\Automate with Python\\Ex_Files_Python_Automation\Exercise Files\\inputFile.txt','r')
passFile = open('C:\\Users\\anike\\Desktop\\Automate with Python\passFile.txt','w')

for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)

f.close()
passFile.close()


import os
from pathlib import Path


'''Organizing file system'''
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','jpeg','.png'],
    "PYTHON": ['.py','.ipynb']
    }

def pickDirectory(value):
    for category,suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'


def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = (filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
        
organizeDirectory()
