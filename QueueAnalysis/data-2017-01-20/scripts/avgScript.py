import dataAnalysis as da
import sys
outPath = sys.argv[2]
output = open(outPath,'w+')
column = int(sys.argv[1])
directory='dataBIN'
SS=int(sys.argv[3])
temp1,temp2,temp3,temp4,temp5 = da.getAvgAndSD(directory+'/fifth-bin.csv',column,scale=SS)
output.write('5' + " " + str(temp1) + " "+ str(temp2)+" "+str(temp3)+ " "+ str(temp4)+ " " + str(temp5)+"\n")
temp1,temp2,temp3,temp4,temp5 = da.getAvgAndSD(directory+'/fourth-bin.csv',column,scale=SS)
output.write('4' + " " + str(temp1) + " "+ str(temp2)+ " "+ str(temp3) + " "+ str(temp4)+" "+ str(temp5) + "\n")
temp1,temp2,temp3,temp4,temp5  =da.getAvgAndSD(directory+'/third-bin.csv',column,scale=SS)
output.write('3' + " " + str(temp1) + " "+ str(temp2)+ " "+ str(temp3) + " " + str(temp4)+ " " + str(temp5)+"\n")
temp1, temp2,temp3,temp4,temp5  = da.getAvgAndSD(directory+'/second-bin.csv',column,scale=SS)
output.write('2' + " " + str(temp1) + " "+ str(temp2)+" "+ str(temp3) + " " + str(temp4)+ " "+ str(temp5)+"\n")
temp1, temp2,temp3,temp4,temp5  = da.getAvgAndSD(directory+'/first-bin.csv',column,scale=SS)
output.write('1' + " " + str(temp1) + " "+ str(temp2)+" "+ str(temp3) + " " + str(temp4)+ " "+ str(temp5)+"\n")
