import os
import subprocess
import sys
from os import listdir
from os.path import isfile, join

#generates list of photos within directory
def genFileList(directory):
    listOfFiles=os.listdir(directory)
    photoFiles=list()

    #Iterate over all files in directory and grab just photos
    for file in listOfFiles:
        fullPath=os.path.join(directory,entry)
        if fullPath.endswith(".jpg") or fullPath.endswith(".png"):
            photoFiles=photoFiles+file

    return photoFiles

def renameFiles(photoFiles):


#main controller function, calls helpers in order
def main(directory):
    photoFiles=genFileList(directory)
    renameFiles(photoFiles)
    fixedFiles=genFileList(directory)


if "__name__==__main__":
    inputer= str(sys.argv[1])
    main(inputer)
