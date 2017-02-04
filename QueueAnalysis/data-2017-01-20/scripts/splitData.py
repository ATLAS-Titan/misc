import dataAnalysis as da
import math
import os
nodeStart =313
nodeEnd = 3749
nodeInt = 500
walltimeStart =0
walltimeEnd = 720
walltimeInt = 120
infile = 'dataBIN/third-bin.csv'
outfile= 'outfilethird'
# Extract data from a file and group them in classes
directory = "splittedData"
os.mkdir(directory)
data = da.splitInIntervals(nodeStart,nodeEnd,nodeInt,walltimeStart,walltimeEnd,walltimeInt,infile,directory+"/"+outfile)
				
