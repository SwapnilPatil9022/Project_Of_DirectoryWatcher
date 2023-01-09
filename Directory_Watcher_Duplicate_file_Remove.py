"""
            --------- Automation using python -----------
    Automation script which accept directory name from user and remove duplicate files from that directory.
"""

#=================================================
# Required Python Packages
#=================================================
import os
import hashlib
from sys import*
import time

#=================================================
# Function name : DeleteFiles
# Description : This function is work Duplicate file remove
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def DeleteFiles(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    icnt = 0

    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0
    else:
        print("No Duplicate file found.")

#=================================================
# Function name : hashfile
# Description : This hashfile function read the data and search checksum in directory.
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def hashfile(path, blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

#=================================================
# Function name : FindDuplicate
# Description : FindDuplicate function is find the duplicate files from directory
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        #---Travel the directory,subdirectory and files----
        for dirName, subdirs, fileList in  os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path) 
            
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid path")

#=================================================
# Function name : PrintResult
# Description : PrintResult function is find the duplicates files
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def PrintResult(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values())) 

    if len(results) > 0:
        print("Duplicates Found : ")
        print("The following files are Duplicate....")

        for result in results:
            for subresult in result:
                print("\t\t%s"% subresult)
    else:
        print("No duplicate file found")

#=================================================
# Function name : main
# Description : Main function from where execution starts
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def main():
    print("--------Travel directory and remove Duplicate files using Automation script--------")

    print("Application name : " +argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse specific directory and remove Duplicate files")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName Absolutepath_of_Directory Extension")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = FindDuplicate(argv[1])
        PrintResult(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print("Took %s secound to evaluate."% (endTime - startTime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

#=================================================
# Application starter
#=================================================
if __name__ == "__main__":
    main()
