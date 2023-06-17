tiku='./mao/TXT'
outf=$tiku/mg.txt
alist=$(ls $tiku/*)
pth='mgf.py'
for a in $alist
do
    python $pth $a $outf
    echo $a ok!
done