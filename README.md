# sdr-scripts

Scripts related to rtl_sdr tools

- `rtl_udp_scanner/`: Used to remotely control [rtl_udp](https://github.com/sysrun/rtl-sdr)
  to scan a frequency range with a defined step and interval
- `record_and_stream/`: Shell script to records from rtl_fm and encode to wav file,
  all while streaming audio via udp
- `nginx/`: Simple webpage to preview and stream all audio files in a folder, use with `nginx_config.txt`
- `plot_rtl_power`: Shell script to scan a range of frequencies with [rtl_power](http://kmkeen.com/rtl-power/) and
    save a PNG heatmap image of its output. You will need configure the path to
    [`heatmap.py`](https://github.com/keenerd/rtl-sdr-misc), which must be downloaded separately