# sdr-scripts

Scripts related to rtl_sdr tools

- `frequency_scan.py`: Used to remotely control [rtl_udp](https://github.com/sysrun/rtl-sdr)
  to scan a frequency range with a defined step and interval
- `record_and_convert.sh`: Shell script which records and encodes to wav file,
  while streaming audio via udp
- `nginx/audio_players.html`: Webpage to preview and stream all audio files in a folder, use with `nginx_config.txt`