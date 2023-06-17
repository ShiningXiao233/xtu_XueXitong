alist=$(ls ./mao/*)
i=1

for a in $alist
do
    # echo $a ./tiku/TT$i.html
    if [ $i -le 9 ]
    then
        wkhtmltopdf --encoding utf-8 $a ./mao/TT0$i.pdf
    else
        wkhtmltopdf --encoding utf-8 $a ./mao/TT$i.pdf
    fi
    i=$(expr $i + 1)    
    
done