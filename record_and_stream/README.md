# record_and_stream.sh

Shell script to records from rtl_fm and encode to wav file, all while streaming audio via udp

## Usage

Configure the script with the env vars at the start of the file:

- FREQUENCY=88000000
- SQUELCH=30
- WAV_PATH=/path/to/folder
- DURATION=12.0h
- MODULATION=fm
- STREAMING_HOST=127.0.0.12
- STREAMING_PORT=7355
- CORRECTION_PPM=0
- RTLSDR_GAIN=38.6

The script runs forever until stopped with Ctrl-C. To automate its stop time (e.g. for a cron job) you can use the
`timeout` command:

`timeout 1.0h record_and_stream.sh`

The script sends raw wav samples via udp to the configured host and port. To listen to them you can use `sox`:

windows:

`ncat -u -l -p 7355 | sox -traw -r24k -es -b16 -c1 -V1 - -twaveaudio -d`

Unix:

`ncat -u -l -p 7355 | play -t raw -r 24k -es -b 16 -c 1 -V1 - | aplay -r 24k -f S16_LE -t raw -c 1`