import dataAnalysis as da
import math
import os
nodeStart =313
nodeEnd = 3749
nodeInt = 500
walltimeStart =60
walltimeEnd = 720
walltimeInt = 60
infile = 'third-bin.csv'
outfile= 'third'
tresholdAvg = float('inf')
tresholdSD= 100
tresholdCount=-100
sX=50
sY=50
directory="splittedData" 
column = 3
scale = 3600
# Extract data from a file and group them in classes
output = open(outfile,"w+")
for filename in os.listdir(directory):
	tokens = filename.split('-')
	confInt = da.getAvgAndSD(directory+"/"+filename,column,scale)
	output.write("["+tokens[1]+"-"+tokens[2] + "] ")
	for num in confInt:
		output.write(str(num) +" ")
	output.write("\n")
output.close()

