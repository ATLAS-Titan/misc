!rm 'weak.gif'

set xtics ("128/128" 1,"256/256" 2,"512/512" 3, "1024/1024" 4, "2048/2048" 5)
set terminal gif 
set out 'weak.gif'
set key font "8"
set key top left
set grid
set xlabel '#CUs/#Cores' 
set ylabel 'Time (seconds)'
set title "Weak scalability gromacs simulations" 
set xrange[0:*] 
set yrange[0:*]
plot 'weak.csv' u ($1):2:(0.5) notitle with boxes fill solid border lw 3;

!rm 'strong.gif'

set xtics ("512/128" 1,"512/256" 2,"512/512" 3)
set terminal gif 
set out 'strong.gif'
set key font "8"
set key top left
set grid
set xlabel '#CUs/#Cores' 
set ylabel 'Time (seconds)'
set title "Strong scalability gromacs simulations" 
set xrange[0:*] 
set yrange[0:*]
plot 'strong.csv' u ($1):2:(0.5) notitle with boxes fill solid border lw 3;
