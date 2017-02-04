import dataAnalysis as da
import math
import os
nodeStart =313
nodeEnd = 3749
nodeInt = 500
walltimeStart =60
walltimeEnd = 720
walltimeInt = 60
outfile= 'duration.csv'
tresholdAvg = float('inf')
tresholdSD= 100
tresholdCount=-100
sX=50
sY=50
directory="dataBIN" 
column = 3
scale = 3600
SS = 3600
# Extract data from a file and group them in classes
output = open(outfile,"w+")
first = 60
last=1440
step =60
numbin = (last-first)/step +1
print numbin 
hist = []
for i in range(0,numbin+1):
	hist.append([])
counter=0
for filename in os.listdir(directory):
	inputfile = open(directory+"/"+filename)
	for line in inputfile:
		tokens = line.split()
		index =(int(float(tokens[2])))/step
		print(tokens[2]+  " " + tokens[3] + " " + str(index))
		hist[index].append(tokens[3])
		
		counter+=1
for i in range(0,len(hist)):
	temp1,temp2,temp3,temp4,temp5 = da.getAvgAndSDFromList(hist[i],column,scale=SS)
	output.write(str(i*step) + " " + str(temp1) + " "+ str(temp2)+" "+str(temp3)+ " "+ str(temp4)+ " " + str(temp5)+"\n")	
output.close()

