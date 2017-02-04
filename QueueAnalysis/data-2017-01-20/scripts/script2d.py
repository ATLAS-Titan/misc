import math
infilepath = 'third-bin.csv'
outfilepath = 'data-313-812'
infile = open(infilepath)
maxWalltime = 720
minWalltime =60
walltimeInt = 60
numBin = maxWalltime/walltimeInt
print(numBin)
m1=  [0]*numBin
m2 = [0]*numBin
count = [0]*numBin
minNodes = 313
maxNodes = 813

for line in infile:
	tokens =line.split()
	nnodes = int(float(tokens[0]))
	walltime = int(tokens[1]) 
	if nnodes >= minNodes and nnodes < maxNodes:
		index = (walltime-minWalltime)/walltimeInt
		print(str(walltime) + " "+ str(index))
		queuetime = int(tokens[2])
		m1[index] += queuetime
		m2[index]+=math.pow(queuetime,2)
outfile = open(outfilepath,'w+')
Interval = minWalltime
for i in range(0,len(m1)):
	if count[i] >0:
		tempM1 =m1[i]/count[i] 
		tempM2 = math.sqrt(m2[i]- tempM1*tempM1)
		outfile.write(str(minWalltime)+" "+ tempM1 + " "+ tempM2)
		print(str(Interval)+" "+ tempM1 + " "+ tempM2)
	Interval+=minWalltime
