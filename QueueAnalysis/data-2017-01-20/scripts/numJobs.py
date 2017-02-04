import dataAnalysis as da
import math
import os
nodeStart =313
nodeEnd = 3749
nodeInt = 500
walltimeStart =60
walltimeEnd = 720
walltimeInt = 60
outfile= 'numnodes2'
tresholdAvg = float('inf')
tresholdSD= 100
tresholdCount=-100
sX=50
sY=50
directory="dataBIN" 
column = 3
scale = 3600
# Extract data from a file and group them in classes
output = open(outfile,"w+")
nnodes=18688
hist =[0]*(nnodes+1)
hist2 =[0]*(nnodes+1)
counter=0
for filename in os.listdir(directory):
	inputfile = open(directory+"/"+filename)
	for line in inputfile:
		tokens = line.split()
		hist[int(float((tokens[1])))]+=1	
		hist2[int(float(tokens[1]))]+=float(tokens[2])
		counter+=1
for i in range(1,len(hist)):
	output.write(str(i) +" "+ str(hist[i])+" "+str(hist2[i])+ " " +str(counter)+"\n")
output.close()

