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
def getFileDate(photo):
    #varr=Image.open(photo)._getexif()[36867]
    #if varr==None:
        #return photo
    #else:
        #return varr
    return photo
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
def renameFileOOF(file):
    if("IMG_") in file:
        file2=file.split("_")
        yearNums=file2[1]
        year="Year-"+yearNums[0][1][2][3]+"_"+yearNums[4][5]+"_"+yearNums[6][7]
        year2=year+" Time-"+file2[2]
        return year2
    else :
        file2=file.split("_")
        print(file2)
        if(file2[0].isnumeric()):
            yearNums=file2[0]
            print(yearNums)
            print(len(yearNums))
            year="Year-"+yearNums[0][1][2][3]+"_"+yearNums[4][5]+"_"+yearNums[6][7]
            if(file2[1].isnumeric()):
                year2=year+" Time-"+file2[1]
                year2=year2+file2[1]
                return year2
            else:
                return year2
        else:
            year="Other-"+file
            return year

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
        date=getFileDate(file)
        if(date!=file):
            #exif works, will call exif block
            newfile=renameFileExif(file,str(date))
        else:
            #
            newfile=renameFileOOF(file)

        storePhoto(newfile)
#_______________________________________________________________________________
if "__name__==__main__":
    inputer= os.getcwd()
    main(inputer)
