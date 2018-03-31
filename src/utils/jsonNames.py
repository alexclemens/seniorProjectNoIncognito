# -*- coding: utf-8 -*-

import pathlib

# define the path
currentDirectory = pathlib.Path('/Users/alexclemens/Downloads/PPB-2017')

# define the pattern
currentPattern = "*.jpg"


pics = {"data": []};
path = "/Users/alexclemens/Documents/cs190/seniorProject/CLMtracker/clmtrackr-gh-pages_no_git/src/utils/output.js"
file = open(path,"w")

i=0
for currentFile in currentDirectory.glob(currentPattern): 
	#curr = currentFile.replace("PosixPath(", "").replace(")","")
	pics["data"].append({"pic"+str(i):str(currentFile)})
    #print(currentFile)
	i+=1



file.write(str(pics))
file.close()