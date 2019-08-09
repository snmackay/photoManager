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
        if fullPath.endswith(".jpg") or fullPath.endswith(".JPG"):
            photoFiles=photoFiles+[file]

    return photoFiles

#checks to see if exif data can be used
def getFileDate(photo):
    varr=Image.open(photo)._getexif()[36867]
    if varr

#-------------------------------------------------------------------------------
#for files with exif data:
#-------------------------------------------------------------------------------
#renames the files that are being passed in.
def renameFile(file,date):
    #print(date)
    date2=date.split( )
    date2="Year-"+date2[0]+" Time-"+date2[1]
    date2=date2.replace(":" , "_")
    os.rename(file,date2+".jpg")
    return date2+".jpg"

def storePhoto(newfile):

    #setup stuff
    newfile2=newfile.split("_")
    currentPath=os.getcwd()
    year=str(newfile2[0])
    month=str(newfile2[1])
    #create month directory dictionary
    months={}
    months['01']="January"
    months['02']="February"
    months['03']="March"
    months['04']="April"
    months['05']="May"
    months['06']="June"
    months['07']="July"
    months['08']="August"
    months['09']="September"
    months['10']="October"
    months['11']="November"
    months['12']="December"

    #create year directory
    newPath=os.path.join(currentPath,year,months[month])
    try:
        os.makedirs(newPath)
    except OSError:
        print("whoops, directory failed to make")
    else:
        print("whoo, make year directory")

    #move the file
    current=os.path.join(currentPath,newfile)
    newDir=os.path.join(newPath,newfile)
    os.rename(current,newDir)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


#main controller function, calls helpers in order
def main(directory):
    photoFiles=genFileList(directory)

    for file in photoFiles:
        date=getFileDate(file)
        #print(file)
        newfile=renameFile(file,str(date))

        storePhoto(newfile)

    #renameFiles(photoFiles)
    #fixedFiles=genFileList(directory)


if "__name__==__main__":
    inputer= os.getcwd()
    main(inputer)
