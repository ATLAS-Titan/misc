import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats as st
M1 = 'm1'
M2 = 'm2'
COUNT = 'samplePoints'
MIN = 'min'
MAX = 'max' 

def splitInIntervals(nodeStart,nodeEnd,nodeBinSize,walltimeStart,wallTimeEnd,walltimeBinSize,infilePath,outfilePath):
	'''
	Read a file and group data in bins according node size and walltime. <data>Start indicates the starting point, <data>End the last point, <data>BinSize the width of the bin. infilePath indicates the path of the input file. outfilePath indicates where the output will be written
	Empty bin are not written in the file
	The method returns a list of lists of dictionary
'''
	inputfile = open(infilePath,'r')
	#Initialized data collection variable
	data = list()
	for i in range(nodeStart,nodeEnd+1,nodeBinSize):
		item = []	
		for j in range(walltimeStart,wallTimeEnd+1,walltimeBinSize):
			item2 = []
			item.append(item2)
		data.append(item)
	
	for line in inputfile:
		tokens = line.split()
		nnodes = int(float(tokens[1]))
		walltime = int(tokens[2])
		row = (nnodes-nodeStart)/nodeBinSize
		if row >= len(data):
			row -=1
	
		column = (walltime-walltimeStart)/walltimeBinSize
		if column >= len(data[row]):
			column-=1
		#print(str(row) +  " "+ str(column) + " "+ str(nnodes) +  " "+ str(walltime))
		data[row][column].append(tokens)
		
	nnodeBin = nodeStart
	walltimeBin = walltimeStart
	for row in data:
		walltimeBin = walltimeStart
		for col in row:
			# Write on the file only if the bin is not empty
			
			if len(col) !=0:
				outfile = open(outfilePath+"-"+str(nnodeBin)+"-"+str(walltimeBin),'w+')
				for record in col:
					for item in record:
						outfile.write(item + " ")
					outfile.write("\n")	
				outfile.close()
			walltimeBin+=walltimeBinSize
		nnodeBin+=nodeBinSize
			

	return data




def groupByIntervals(nodeStart,nodeEnd,nodeBinSize,walltimeStart,wallTimeEnd,walltimeBinSize,infilePath,outfilePath=None):
	'''
	TO DO : CHANGE THE NAME --- Initially was meant for something different
	Read a file and group data in bins according node size and walltime. <data>Start indicates the starting point, <data>End the last point, <data>BinSize the width of the bin. infilePath indicates the path of the input file. outfilePath indicates where the output will be written
	Empty bin are not written in the file
	The method returns a list of lists of dictionary
'''
	inputfile = open(infilePath,'r')
	#Initialized data collection variable
	data = list()
	for i in range(nodeStart,nodeEnd+1,nodeBinSize):
		item = []	
		for j in range(walltimeStart,wallTimeEnd+1,walltimeBinSize):
			temp = {}
			temp[M1]=0
			temp[M2]=0
			temp[COUNT]=0
			temp[MIN]=float('inf')
			temp[MAX]=float('-inf')
			item.append(temp)
		data.append(item)
	
	for line in inputfile:
		token = line.split()
		nnodes = int(float(token[0]))
		walltime = int(token[1])
		waittime = float(token[2])/3600
		row = (nnodes-nodeStart)/nodeBinSize
		if row >= len(data):
			row -=1
	
		column = (walltime-walltimeStart)/walltimeBinSize
		if column >= len(data[row]):
			column-=1
		#print(str(row) +  " "+ str(column) + " "+ str(nnodes) +  " "+ str(walltime))
		data[row][column][M1]+=waittime
		data[row][column][M2]+=waittime*waittime
		data[row][column][COUNT]+=1
		if data[row][column][MIN] > waittime:
			data[row][column][MIN] = waittime	 	
		if data[row][column][MAX] < waittime:
			data[row][column][MAX] = waittime
	if outfilePath != None:
		outfile = open(outfilePath,'w+')	
		nnodeBin = nodeStart
		walltimeBin = walltimeStart
		for row in data:
			walltimeBin = walltimeStart
			for col in row:
				# Write on the file only if the bin is not empty
				if col[COUNT] !=0:
					outfile.write(str(nnodeBin) + " " +str(walltimeBin)+ " "+ str(col[M1]/float(col[COUNT]))+ " " + str(col[M2]/float(col[COUNT])) + " " +str(col[COUNT])+ " " +str(col[MIN]) +" "+ str(col[MAX])+"\n")
					col[M1]=col[M1]/float(col[COUNT])
					col[M2]=col[M2]/float(col[COUNT])

				walltimeBin+=walltimeBinSize
				nnodeBin+=nodeBinSize
		outfile.close()
	return data


def createXYZTable(data,xStart,xInt,yStart,yInt,zlabel):
	'''
	The methods takes a list of lists of dictionary as created in the method "groupByIntervals" and returns a table with three column x, y and z and as many rows as the bins are.
	'''
	newdata = {'x':list(),'y':list(),'z':list()}
	currentX =xStart
	for row in data:
		currentY = yStart
		for column in row:
			newdata['x'].append(currentX)
			newdata['y'].append(currentY)
			newdata['z'].append(column[zlabel]) 
			currentY+=yInt
		currentX+=xInt
	return newdata

def plotXYZTable(table,xMin,xMax,xInt,yMin,yMax,yInt,treshold=float('Inf'),sizeX=10,sizeY=10,col='b',xlabel='# nodes',ylabel='walltime',zlabel=''):
	'''
	Plots an xyz table as defined in the method "createXYZTable" and plot it in a 3d historgram
	'''
	from mpl_toolkits.mplot3d import Axes3D
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	xCounter  = xMin
	xtic = []
	while(xCounter <= xMax):
		xtic.append(xCounter)
		xCounter+=xInt
	yCounter = yMin
	ytic = []
	while(yCounter <= yMax):
		ytic.append(yCounter)
		yCounter+=yInt	
	for i  in range(0,len(table['z'])):
        	if table['z'][i] > treshold:
                	table['z'][i] =0
	dx = np.zeros_like(table['x'])+sizeX
	dy = np.zeros_like(table['y'])+sizeY
	plt.xticks(xtic)
	plt.yticks(ytic)
	
	ax.bar3d(table['x'],table['y'], np.zeros_like(table['x']),dx,dx, table['z'], color=col)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.set_zlabel(zlabel)
	plt.show()

def getAvgAndSD(inputPath,column,scale=1,perc=0.05):
	inputfile = open(inputPath)
	M1 = 0.0
	M2 = 0.0
	count = 0
	for line in inputfile:
		tokens = line.split()
		temp = float(tokens[column])/scale
		M1 += temp
		M2 += temp*temp
	 	count+=1
	if count > 1:
		avg = M1/count
		sd = math.sqrt(M2/count - avg*avg)/math.sqrt(count)
		hmin,hmax = st.t.interval(1-perc, count-1, loc=avg,scale=sd)
		return (avg,sd,hmin,hmax,count)
	else:
		return (-1,0,0,0,0)
###TO DO: Unify the two functions.
def getAvgAndSDFromList(listValues,scale=1,perc=0.05):
	M1 = 0.0
	M2 = 0.0
	count = 0
	for item in listValues:
		temp = float(item)/scale
		M1 += temp
		M2 += temp*temp
	 	count+=1
	if count > 1:
		avg = M1/count
		sd = math.sqrt(M2/count - avg*avg)/math.sqrt(count)
		hmin,hmax = st.t.interval(1-perc, count-1, loc=avg,scale=sd)
		return (avg,sd,hmin,hmax,count)
	else:
		return (-1,0,0,0,0)
			
