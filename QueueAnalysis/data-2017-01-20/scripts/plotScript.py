import dataAnalysis as da
import math
nodeStart =313
nodeEnd = 3749
nodeInt = 500
walltimeStart =60
walltimeEnd = 720
walltimeInt = 60
infile = 'third-bin.csv'
outfile= 'outfilethird'
tresholdAvg = float('inf')
tresholdSD= 100
tresholdCount=-100
sX=50
sY=50
# Extract data from a file and group them in classes
data = da.groupByIntervals(nodeStart,nodeEnd,nodeInt,walltimeStart,walltimeEnd,walltimeInt,infile,outfile)
# Creates a xyz table for the first moment from data
tableM1 = da.createXYZTable(data,nodeStart,nodeInt,walltimeStart,walltimeInt,da.M1)
# Creates a xyz table for the second moment from data
tableM2 = da.createXYZTable(data,nodeStart,nodeInt,walltimeStart,walltimeInt,da.M2)
#Convert standard deviation from second moment
for i in range(0,len(tableM2['z'])):
	tableM2['z'][i] = math.sqrt(tableM2['z'][i]-math.pow(tableM1['z'][i],2))
# Creates a xyz table for the number of sample points from data
tablePoints = da.createXYZTable(data,nodeStart,nodeInt,walltimeStart,walltimeInt,da.COUNT)
#Plots the average queue time as a function of # nodes and walltime
da.plotXYZTable(tableM1,nodeStart,nodeEnd,nodeInt,walltimeStart,walltimeEnd,walltimeInt,tresholdAvg,sizeX=sX,sizeY=sY,zlabel='Avg queue time')
# plots the standard deviation of the queue time as function of the # nodes and walltime
da.plotXYZTable(tableM2,nodeStart,nodeEnd,nodeInt,walltimeStart,walltimeEnd,walltimeInt,tresholdSD,sizeX=sX,sizeY=sY,zlabel='S.D. queue time')
# Plots the number of sample points as function of the # nodes and walltime
da.plotXYZTable(tablePoints,nodeStart,nodeEnd,nodeInt,walltimeStart,walltimeEnd,walltimeInt,tresholdCount,sizeX=sX,sizeY=sY,zlabel='# sample points')
