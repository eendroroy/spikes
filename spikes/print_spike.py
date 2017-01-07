# coding=utf-8
def print_spike(l):
    chars = [' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
    spike = ""
    for n in l:
        spike += chars[n]
    print spike
