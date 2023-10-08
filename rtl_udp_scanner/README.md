# rtl_udp_scanner.py

Used to remotely control [rtl_udp](https://github.com/sysrun/rtl-sdr)
to scan a frequency range with a defined step and interval

## Usage

```
python3 rtl_udp_scanner.py [-h] [--interval INTERVAL] [--step STEP] [-H HOST] [-P PORT] <start> <stop>
```

- `INTERVAL` sets the interval between hops in seconds. Default is 1s
- `STEP` sets the frequency step in hz. Default is 1Khz
- `start` and `stop` frequencies are in hz