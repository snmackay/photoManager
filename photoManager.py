import os
import subprocess
import sys
from os import listdir
from os.path import isfile, join
from PIL import Image
import shutil


#_______________________________________________________________________________
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
#_______________________________________________________________________________

#_______________________________________________________________________________
#checks to see if exif data can be used
#def getFileDate(photo):
    #varr=Image.open(photo)._getexif()[36867]
    #if varr==None:
        #return photo
    #else:
        #return varr
    #return photo
#_______________________________________________________________________________

#_______________________________________________________________________________
#for files with exif data:
#renames the files that are being passed in.
#def renameFileExif(file,date):
    #print(date)
    #date2=date.split( )
    #date2="Year-"+date2[0]+" Time-"+date2[1]
    #date2=date2.replace(":" , "_")
    #os.rename(file,date2+".jpg")
    #return date2+".jpg"
#_______________________________________________________________________________

#_______________________________________________________________________________
#for files without exif data
#renames files that are being passed in
#cases handled: IMG_, yearmonthday_rando.jpg
def renameFileOOF(file):
    if("IMG_") in file:
        file2=file.split("_")
        yearNums=file2[1]
        year="Year-"+yearNums[0:4]+"_"+yearNums[4:6]+"_"+yearNums[6:8]
        year2=year+" Time-"+file2[2]
        os.rename(file,year2+".jpg")
        print("if1")
    else :
        file2=file.split("_")
        print(file2)
        if(file2[0].isnumeric()):
            yearNums=file2[0]
            year="Year-"+yearNums[0:4]+"_"+yearNums[4:6]+"_"+yearNums[6:8]
            if(file2[1].isnumeric()):
                year2=year+" Time-"+file2[1]
                year2=year2+file2[1]
                os.rename(file,year2+".jpg")

            else:
                year2=year+" Time-"+file2[1]
                year2=year2+file2[1]
                os.rename(file,year2+".jpg")


#_______________________________________________________________________________

#_______________________________________________________________________________
#restore the photos in a file struct
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
    shutil.move(current,newDir)
#_______________________________________________________________________________

#_______________________________________________________________________________
#main controller function, calls helpers in order
def main(directory):
    photoFiles=genFileList(directory)

    for file in photoFiles:
        print(file)
        #date=getFileDate(file)
        renameFileOOF(file)

    #regather file names from the directory before the files are relocated. ONLY
    #move files that are named correctly
    newFiles=genFileList(directory)
    for file in newFiles:
        if "Year" in file and "Month" in file:
            storePhoto(file)
        else:
            continue


#_______________________________________________________________________________
if "__name__==__main__":
    inputer= os.getcwd()
    main(inputer)
