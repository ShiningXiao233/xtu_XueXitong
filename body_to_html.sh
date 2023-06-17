for i in $(ls ./all/*)
do
    mv $i $i.html
    echo $i.html ok!
done