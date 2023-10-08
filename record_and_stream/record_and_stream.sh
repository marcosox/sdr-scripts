#!/bin/bash

# Receives, streams udp raw samples and exports to wav at the end
# Change the values below as necessary

FREQUENCY=88000000
SQUELCH=0
WAV_PATH=/path/to/folder
DURATION=12.0h
MODULATION=fm
STREAMING_HOST=127.0.0.1
STREAMING_PORT=7355
CORRECTION_PPM=0
RTLSDR_GAIN=38.6

TIMESTAMP=$(date +%Y%m%d-%H%M)
RAW_FILE=${FREQUENCY}_${TIMESTAMP}.raw
OUT_FILE=${WAV_PATH}/${TIMESTAMP}_${FREQUENCY}.wav

echo "Recording for ${DURATION}..."
timeout ${DURATION} rtl_fm -g ${RTLSDR_GAIN} -p ${CORRECTION_PPM} -f ${FREQUENCY} -l ${SQUELCH} -M ${MODULATION} | tee "${RAW_FILE}" | timeout ${DURATION} nc -u ${STREAMING_HOST} ${STREAMING_PORT}
# compand is used to compress the output audio in order to limit harmful peaks
sox -traw -r24k -es -b16 -c1 -V1 "${RAW_FILE}" -twav "${OUT_FILE}" compand 0.2,0.5 -80,-10,-10,-10,0,-20 0 -90 0.2 && rm "${RAW_FILE}"
