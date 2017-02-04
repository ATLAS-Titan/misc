!rm 'AvgTimeAll.gif'
set xtics (1,2,3,4,5)
set terminal gif font "arial,8"
set out 'AvgTimeAll.gif' 
set key top right
set xlabel 'Bin' 
set ylabel 'Average time (minutes)'
set y2label 'Ratio between Execution time and Walltime'
set title "Execution time vs Wall-time as function of the bin" 
set xrange[0:6] 
set yrange[0:*]
set ytics 0,50,300
set y2range[0:1.1]
set y2tics
plot 'avgRT.csv' u ($1-0.3):2:4:5:(0.15) axes x1y1 title 'Wall-time(WT)' with boxerrorbars lw 3,\
'avgET.csv' u ($1):2:4:5:(0.15) axes x1y1 title 'Execution time,(ET)' with boxerrorbars lw 3,\
'avgRatioETWT.csv' u ($1+0.3):2:4:5:(0.15) axes x1y2 title 'ET/WT' with boxerrorbars lw 3;



### Average requested time and average execution time as function of the bin

!rm 'AvgTime.gif'

set xtics (1,2,3,4,5)
set terminal gif 
set out 'AvgTime.gif'
set key font "8"
set key top left
set xlabel 'Bin' 
set ylabel 'Average time (minutes)'
set title "Execution time and Wall-time as function" 
set xrange[0:6] 
set yrange[0:*]
plot 'avgRT.csv' u ($1-0.2):2:4:5:(0.4) title 'Requested time' with boxerrorbars lw 3,\
'avgET.csv' u ($1+0.2):2:4:5:(0.4) title 'Exectuion time' with boxerrorbars lw 3;

reset

#Average waiting time per bin
reset
!rm 'AvgQT.gif'
set out 'AvgQT.gif' 
set xtics (1, 2,3,4,5)
#exec = 45
set terminal gif
set grid
set key font "8"
set key top right
set xlabel 'Bin' 
set ylabel 'Average queue time (hours)' 
set xrange[0:6]
set yrange[0:*]
plot 'avgQT.csv' u ($1):2:4:5:(0.5) notitle with boxerrorbars lw 3;

# Average waiting time as function of the wall-time
reset 

!rm 'AvgQTfWT.gif'

set terminal gif font "arial,8"
set out 'AvgQTfWT.gif' 
set key top right
set xlabel 'Wall-time (interval of 60 minutes)' 
set ylabel 'Average time (hours)'
set title "Queue time as function of the wall-time" 
set xrange[-25:1500] 
set xtics 60 rotate
f(x) = x < 1 ? 10+x : 10+log(x)
set yrange[f(0.1):f(165)]
set ytics ("0.1" f(0.1),"0.5" f(0.5),"1" f(1) ,"20" f(20),"40" f(40), "60" f(60), "80" f(80), "100" f(100), "120" f(120), "160" f(160))
set grid
plot 'duration.csv' u ($1):(f($2)):(f($4)):(f($5)):(30)  notitle with boxerrorbars lw 3;

reset
# Number of jobs as function of the wall-time
!rm 'AvgNumJobfWT.gif'

set terminal gif font "arial,8"
set out 'AvgNumJobfWT.gif' 
set key top right
set xlabel 'Wall-time (interval of 60 minutes)' 
set ylabel '# jobs'
set title "Number of jobs as function of the wall-time" 
set xrange[-25:1500] 
set xtics 60 rotate
f(x) = log(x)
set yrange[f(1):f(10000)]
set ytics ("10" f(10),"25" f(25),"50" f(50) ,"100" f(100),"200" f(200), "400" f(400), "1000" f(1000), "2000" f(2000), "4000" f(4000), "8000" f(8000),"10000" 10000)
set grid
plot 'duration.csv' u ($1):(f($6)):(30)  notitle with boxes fill solid border lw 3;





# Average ration between exeuction time and requested time
reset

!rm 'AvgRatio.gif'
set out 'AvgRatio.gif'
set xtics (1, 2,3,4,5)
set terminal gif
set key font "8"
set key top right
set grid
set title "Ratio between Execution time and walltime as function of the bin"
set xlabel 'Bin' 
set ylabel 'Ratio between Execution time and Walltime' 
set xrange[0:6] 
plot 'avgRatioETWT.csv' u ($1):2:4:5:(0.5) notitle with boxerrorbars lw 3;


#Percentage jobs
reset

!rm 'PercJobs.gif'
set out 'PercJobs.gif'
set title "Cumulative distribution of the submitted jobs as function of the number of nodes"
#exec = 45
set terminal gif font "arial,8"
set key font "4"
set key top right
set xlabel '# nodes' 
set ylabel '% jobs on batch queue' 
set yrange[0:1.01]
set grid
numnodes=18688
set xrange[log(1):log(numnodes)] 
set xtics ("1" log(1),"10" log(10), "50" log(20), "100" log(100), "250" log(250), "500" log(500), "1000" log(1000),"2500" log(2500),"5000" log(5000),"8000" log(8000),"12000" log(12000),"18688" log(numnodes)) rotate
set yrange[0:*]
plot 'numnodes' u (log($1)):($2/$4) title '' smooth cumulative with l lw 3;

#Number of jobs as function of the number of jobs
reset

!rm 'NumJobs.gif'
set out 'NumJobs.gif'
set title "Frequency of the submitted jobs as function of the number of nodes"
#exec = 45
set terminal gif
set key font "4"
set key top right
set xlabel '# nodes' 
set ylabel 'number jobs' 
#set yrange[0:1.01]
set grid
f1 = 100
f2 = 10
b1 =100
b2 = 1000
f(x) = x < b1 ? x*f1 : x < b2 ? b1*f1+((x-b1)*f2) : b1*f1+b2*f2+((x-f2)) 
numnodes=18688
set xrange[1:numnodes] 
set yrange[log(1):log(6750)]
#set xtics 0,250,8000
set ytics ("25" log(25),"50" log(50), "100" log(100), "200" log(200), "500" log(500), "1000" log(1000), "2000" log(2000),"4000" log(4000),"6000" 6000)
#set xrange[0:8000]

plot 'numnodes' u 1:(log($2)):(0.2) title '' with boxes fill solid border lw 3;

#Average duration of jobs as function of the number of jobs
reset

!rm 'AvgDurationJobs.gif'
set out 'AvgDurationJobs.gif'
#exec = 45
set terminal gif
set key font "4"
set key top right
set xlabel '# nodes' 
set ylabel 'Average wall-time (minutes)' 
#set yrange[0:1.01]
set grid
f1 = 100
f2 = 10
b1 =100
b2 = 1000
f(x) = x < b1 ? x*f1 : x < b2 ? b1*f1+((x-b1)*f2) : b1*f1+b2*f2+((x-f2)) 
numnodes=18688
set xrange[1:numnodes] 
set title "Average wall time (minutes) as function of the number of nodes"
#set yrange[log(1):log(6750)]
#set xtics 0,250,8000
#set xtics ("1" log(1),"10" log(10), "50" log(20), "100" log(100), "250" log(250), "500" log(500), "1000" log(1000),"2500" log(2500),"5000" log(5000),"8000" log(8000),"12000" log(12000),"18688" log(numnodes)) rotate
#set ytics ("50" log(50),"100" log(100), "500" log(500), "1000" log(1000), "2500" log(2500), "5000" log(5000), "6500" log(6550))
#set xrange[0:8000]
plot 'numnodes2' u (f($1)):(($3)/($2)):(0.2) title '' with boxes lw 3;


#Duration jobs 
reset
!rm 'DurationJobs.gif'
set out 'DurationJobs.gif'
#exec = 45
set terminal gif
set key font "8"
set key top right
set xlabel '# nodes' 
set grid
set ylabel 'hours'
set title "total wall-time vs execution time as function of the number nodes "
f(x)= log(x) 
set xrange[log(1):log(18000)]
set xtics ("1" log(1),"10" log(10), "50" log(20), "100" log(100), "250" log(250), "500" log(500), "1000" log(1000),"2500" log(2500),"5000" log(5000),"8000" log(8000),"12000" log(12000),"18000" log(18000)) rotate
set yrange[0:*]
plot 'numnodes2' u (log($1)):($3/(60)) title 'Requested wall-time' smooth cumulative with l lw 3,\
'numnodes' u (log($1)):($3/(60)) title 'Execution time' smooth cumulative with l lw 3;




reset


#exec = 45

set terminal gif
!rm 'NumJobsBin.gif'
set out 'NumJobsBin.gif'
set title "Distribution of submitted jobs as function of the bins"
set grid
set xtics (1,2,3,4,5)
set key font "8"
set key top right
set xlabel 'Bin' 
set ylabel '# Submitted Jobs' 
set yrange[0:15000]
set xrange[0:6]
set y2label 'Percentage of submitted jobs'
set y2range[0:1]
set y2tics
set ytics nomirror
numjobs=14395
plot 'avg.csv' u 1:2:(0.5) axes x1y1 notitle with boxes fill solid border lt 1,\
'avg.csv' u 1:($2/numjobs) axes x1y2 notitle smooth cumulative with lp lt 2 lw 4;


