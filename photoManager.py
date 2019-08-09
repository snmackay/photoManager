import os
import subprocess
import sys
from os import listdir
from os.path import isfile, join
from PIL import Image

#generates list of photos within directory
def genFileList(directory):
    listOfFiles=os.listdir(directory)
    photoFiles=list()

    #Iterate over all files in directory and grab just photos
    for file in listOfFiles:
        fullPath=os.path.join(directory,file)
        if fullPath.endswith(".jpg") or fullPath.endswith(".png"):
            photoFiles=photoFiles+[file]

    return photoFiles

#gets file date taken using EXIF
def getFileDate(photo):
    return Image.open(photo)._getexif()[36867]

#renames the files that are being passed in.
def renameFile(file,date):
    print(date)
    date2=date.split( )
    date2="Day-"+date2[0]+" Time-"+date2[1]
    date2=date2.replace(":" , "_")
    os.rename(file,date2+".jpg")


#main controller function, calls helpers in order
def main(directory):
    photoFiles=genFileList(directory)

    for file in photoFiles:
        date=getFileDate(file)
        print(date)
        renameFile(file,str(date))

    #renameFiles(photoFiles)
    #fixedFiles=genFileList(directory)


if "__name__==__main__":
    inputer= os.path.dirname(os.path.realpath(__file__))
    main(inputer)
