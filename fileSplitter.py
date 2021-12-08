import os

filesToSplit = '' # directory containing csv files to split
fileList = os.listdir(fileToSplit) # list the files in the directory
splitNumber = 10000 # number of lines to split files by
filePart = 1 # an integer to append to the end of new file names. This will go up by one for each file.
splitFiles = '' # directory to store new broken up files


for file in fileList:
    csvfile = open(filesToSplit + file, 'r').readlines() # read the lines of one file in the directory
    for i in range(len(csvfile)):
        if i % splitNumber == 0: 
            # create a file named after the original with 'part'+the number file part for this split and
            # write a number of lines to it equal to the splitNumber (or less if there are not enough left)
            open(splitFiles + file + 'part' + str(filePart) + '.csv', 'w+').writelines[i+i+splitNumber]
            filePart += 1