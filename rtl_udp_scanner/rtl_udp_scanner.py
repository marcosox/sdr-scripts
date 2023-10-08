#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Controls rtl_udp to scan a frequency range
import socket
import time
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace

OP_FREQ: bytes = b'\x00'  # Change frequency
OP_MODE: bytes = b'\x01'  # Change mode (?)
OP_SQUELCH: bytes = b'\x02'  # Set squelch level
OP_GAIN: bytes = b'\x03'  # Set gain (GAIN_AUTO = -100)
OP_AGC: bytes = b'\x08'  # Set AGC AGC_ON (1)/AGC_OFF (0)

GAIN_AUTO: int = -100

AGC_ON: int = 1
AGC_OFF: int = 0


def prepare_command(opcode: bytes, data: int) -> bytes:
    buffer: bytearray = bytearray(opcode)
    i = 0
    while i < 4:
        buffer.append(data & 0xff)
        data = data >> 8
        i = i + 1
    return buffer


def parse_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        description="Simple frequency scanner for rtl_udp",
        formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("start",
                        type=int,
                        help="Starting frequency in Hz")
    parser.add_argument("stop",
                        type=int,
                        help="End frequency in Hz")
    parser.add_argument("--interval",
                        type=float,
                        help="Frequency switching interval in seconds",
                        default=1.0)
    parser.add_argument("--step",
                        type=int,
                        help="Frequency step in Hz",
                        default=1000)
    parser.add_argument("-H",
                        "--host",
                        type=str,
                        help="rtl_udp host",
                        default="localhost")
    parser.add_argument("-P",
                        "--port",
                        type=int,
                        help="rtl_udp port",
                        default=6020)
    return parser.parse_args()


def main():
    args: Namespace = parse_args()

    host: str = args.host
    port: int = args.port
    interval: float = args.interval
    step: int = args.step
    start: int = args.start
    stop: int = args.stop

    s: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    for frequency in range(start, stop, step):
        buffer = prepare_command(opcode=OP_FREQ, data=frequency)
        print(" ".join([f"{x:02X}" for x in buffer]))
        s.send(buffer)
        time.sleep(interval)
    s.close()


if __name__ == '__main__':
    main()
