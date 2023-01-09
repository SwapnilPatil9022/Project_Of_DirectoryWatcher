"""
            --------- Automation using python -----------
    Automation script which accept directory name from user and display all names and checksum of duplicate files from that directory.
"""

from sys import*
import os
import hashlib

def hashfile(path, blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs, fileList in  os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path) 
                print(path)
                print(file_hash)
                print(' ')

def printDuplicate(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values())) 

    if len(results) > 0:
        print("Duplicates Found : ")

        print("The following files are identical")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print("\t\t%s"% subresult)
    else:
        print("No duplicate file found")

def main():
    print("--------Search Duplicate file and checksum from that Directory using Automation script--------")

    print("Application name : " +argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse specific directory and display size of files")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName Absolutepath_of_Directory Extension")
        exit()

    try:
        arr = DisplayChecksum(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()


