# sdr-scripts

Scripts related to rtl_sdr tools

- `frequency_scan.py`: Used to remotely control [rtl_udp](https://github.com/sysrun/rtl-sdr)
  to scan a frequency range with a defined step and interval
- `record_and_stream.sh`: Shell script to records from rtl_fm and encode to wav file,
  all while streaming audio via udp
- `nginx/`: Simple webpage to preview and stream all audio files in a folder, use with `nginx_config.txt`