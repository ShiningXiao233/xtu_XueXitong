tiku='./xi'
alist=$(ls $tiku/*)
i=1
pth='HTMLtoTXT.py'
for a in $alist
do
    # echo $a ./tiku/TT$i.html
    if [ "$i" -le 9 ]
    then
         python $pth $a $tiku/TT0$i.txt
    else
         python $pth $a $tiku/TT$i.txt
    fi
    i=$(expr $i + 1)    
    
done