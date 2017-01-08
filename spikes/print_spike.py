# coding=utf-8
from spikes.CONFIGS import BARS


def print_spike(l):
    spike = ""
    for n in l:
        spike += BARS[n]
    print spike
