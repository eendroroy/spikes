# coding=utf-8
from spikes.DATA import BARS


def print_spike(row):
    spike = ""
    for bar in row:
        spike += BARS[bar]
    return spike
