
for DIR in /home/yuhneg/data/tartanair-v2-test-seg-300/Data_easy/*
    do 
    echo $DIR;
    echo $(basename $DIR);

    ./Examples/Monocular/mono_tartanair ./Vocabulary/ORBvoc.txt Examples/Monocular/TartanAir.yaml $DIR $DIR/mono_results.txt;
    cp $DIR/mono_results.txt mono_results/$(basename $DIR).txt
    done