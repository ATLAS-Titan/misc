import numpy
import dataAnalysis as da
hashMap={'exp1':1000, 'exp2':2000,'exp3':250,'exp4':500}
sessionFile ="sessions.csv"
pilotFile= "pilots.csv"
CUFile="units.csv"
path ="../data/"

QTFile = "PilotTimes2.csv"
UnitFile ="UnitFiles.csv"

PSIZE_PF_I=6
PRUN_PF_I=2
QT_PF_I=1

EFFTIME_CU_I=1
LASTTIME_I = 6

def ComputeExecutionTime(inputPath,outputPath):

	infile = open(inputPath)
	infile.readline() # Consunme first line
	outfile= open("./"+outputPath,"w+")
	EffTime = {}
	Overhead = {}
	TotDur = {}
	for key in hashMap.keys():
		EffTime[key] =[]
		Overhead[key] = []
		TotDur[key] = []
	for line in infile:
		tokens = line.split(',')
		EffTime[tokens[LASTTIME_I+1]]+=[tokens[QT_PF_I]]	
		sum = 0
		for i in range(2,LASTTIME_I):
			sum+=float(tokens[i])
		Overhead[tokens[LASTTIME_I+1]] +=[sum]
		TotDur[tokens[LASTTIME_I+1]] +=[float(sum)+float(tokens[QT_PF_I])]
	for k in EffTime.keys():
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(EffTime[k],60,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + " " )
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(Overhead[k],60,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + " " )
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(TotDur[k],60,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + "\n")	
	outfile.close()
	infile.close()




def ComputePilotTimes(inputPath,outputPath):

	infile = open(inputPath)
	infile.readline() # Consunme first line
	outfile= open("./"+outputPath,"w+")
	queueTime = {}
	duration = {}
	for key in hashMap.keys():
		queueTime[key] =[]
		duration[key] =[]
	for line in infile:
		tokens = line.split(',')
		queueTime[tokens[PSIZE_PF_I]]+=[tokens[QT_PF_I]]	
		duration[tokens[PSIZE_PF_I]]+=[tokens[PRUN_PF_I]]
	for k in queueTime.keys():
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(queueTime[k],60,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + " ")
		(avg,sd,hmin,hmax,count) = da.getAvgAndSDFromList(duration[k],60,perc=0.05)
		outfile.write(str(hashMap[k])  + " " + str(avg) + " " + str(sd) + " " + str(hmin)  + " " + str(hmax) + "\n")
	
	outfile.close()
	infile.close()
def main():
	ComputePilotTimes(path+pilotFile,QTFile)
	ComputeExecutionTime(path+CUFile,UnitFile)
if __name__=="__main__":
	main()
