set datafile separator ","

!rm 'ET.eps'
set term pos eps color enhanced "Helvetica" 8
set out 'ET.eps' 
set key top right
set xlabel 'Pilot Size (nodes)' 
set ylabel 'Average time (minutes)'
set y2label 'Ratio between Execution time and Walltime'
set title "Execution time vs Total Pilot duration"  
set grid
f(x,y) = "exp1" eq x ? y : 1/0
g(x,y) = "exp2" eq x ? y : 1/0
h(x,y) = "exp3" eq x ? y : 1/0
k(x,y) = "exp4" eq x ? y : 1/0

plot '../data/units2.csv' u 1:(f(strcol(8),$2)) title '1000' with p,\
'../data/units2.csv' u 1:(g(strcol(8),$2)) title '2000' with p,\
'../data/units2.csv' u 1:(h(strcol(8),$2)) title '250' with p,\
'../data/units2.csv' u 1:(k(strcol(8),$2)) title '500' with p;

reset 
set datafile separator ","

!rm 'ET.gif'
set terminal gif font "arial,8"
set out 'ET.gif' 
set key top right
set xlabel 'Pilot Size (nodes)' 
set ylabel 'Average time (minutes)'
set y2label 'Ratio between Execution time and Walltime'
set title "Execution time vs Total Pilot duration"  
set grid
f(x,y) = "exp1" eq x ? y : 1/0
g(x,y) = "exp2" eq x ? y : 1/0
h(x,y) = "exp3" eq x ? y : 1/0
k(x,y) = "exp4" eq x ? y : 1/0

plot '../data/units2.csv' u 1:(f(strcol(8),$2)) title '1000' with p,\
'../data/units2.csv' u 1:(g(strcol(8),$2)) title '2000' with p,\
'../data/units2.csv' u 1:(h(strcol(8),$2)) title '250' with p,\
'../data/units2.csv' u 1:(k(strcol(8),$2)) title '500' with p;

reset



!rm 'ExecutionTime.eps'
set term pos eps color enhanced "Helvetica" 8
set out 'ExecutionTime.eps' 
set key top right
set xlabel 'Pilot Size (nodes)' 
set ylabel 'Average time (minutes)'
set y2label 'Ratio between Execution time and Walltime'
set title "Execution time vs Total Pilot duration"  
set yrange[0:100]
set xrange[0:2100]
set xtics (250,500,1000,2000)	
set grid
plot 'UnitFiles.csv' u ($6-60):7:9:10:(40)  title 'Launching' with boxerrorbars lw 3,\
'UnitFiles.csv' u ($1):2:4:5:(40) title 'Effective Duration' with boxerrorbars lw 3,\
'PilotTimes.csv' u ($6+60):7:9:10:(40)  title 'Pilot Duration' with boxerrorbars lw 3;

!rm 'ExecutionTime.gif'
set terminal gif font "arial,8"
set out 'ExecutionTime.gif' 
set key top right
set xlabel 'Pilot Size (nodes)' 
set ylabel 'Average time (minutes)'
set y2label 'Ratio between Execution time and Walltime'
set title "Execution time vs Total Pilot duration"  
set yrange[0:100]
set xrange[0:2100]
set xtics (250,500,1000,2000)	
set grid
plot 'UnitFiles.csv' u ($6-60):7:9:10:(40)  title 'Launching' with boxerrorbars lw 3,\
'UnitFiles.csv' u ($1):2:4:5:(40) title 'Effective Duration' with boxerrorbars lw 3,\
'PilotTimes.csv' u ($6+60):7:9:10:(40)  title 'Pilot Duration' with boxerrorbars lw 3;



reset

#Average waiting time per bin
reset
!rm 'AvgQT.gif'
set out 'AvgQT.gif' 
set terminal gif
set grid
set key font "8"
set key top right
set xlabel 'Pilot size (nodes)' 
set ylabel 'Average queue time (minutes)' 
set yrange[0:600]
set xrange[0:2100]
set grid
set xtics (250,500,1000,2000)
plot 'PilotTimes.csv' u ($1):2:4:5:(50) notitle with boxerrorbars lw 3;

