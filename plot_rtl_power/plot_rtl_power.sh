#! /bin/bash

if [ "$#" -ne 3 ]; then
    echo "usage: $0 <start:end:binsize> <interval> <duration>"
fi

TIMESTAMP=$(date +%Y%m%d-%H%M)
OUTFOLDER=/path/to/folder
FILENAME=${TIMESTAMP}_$(echo -n $1 | sed 's/:/-/g')_$2s_$3
OUTPATH=${OUTFOLDER}/${FILENAME}
CORRECTION_PPM=0
RTL_SDR_GAIN=38.6
Y_TICKS=5m

rtl_power -f $1 -p${CORRECTION_PPM} -g${RTL_SDR_GAIN} -i $2  -e $3 ${OUTPATH}.csv
# configure the correct path to the heatmap.py script here
# you can get the script from https://github.com/keenerd/rtl-sdr-misc
/path/to/heatmap.py --ytick ${Y_TICKS} ${OUTPATH}.csv ${OUTPATH}.png
