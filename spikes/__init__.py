#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import sys

from spikes.spike import Spike, spike


def read_args():
    usage = Spike.usage()
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'l:')
        rows = 1
        for opt, arg in opts:
            if opt == '-l':
                rows = int(arg)
            else:
                sys.stderr.write(usage)
                sys.exit(128)
    except getopt.GetoptError:
        sys.stderr.write(usage)
        sys.exit(2)
    except ValueError:
        sys.stderr.write(usage)
        sys.exit(64)

    return args, rows


def main():
    args, rows = read_args()
    try:
        if args.__len__() < 1:
            args = sys.stdin.read().strip().replace('\n', ' ').split(' ')
        if args.__len__() < 1:
            sys.stderr.write(Spike.usage())
            return 1
        args = list(filter(None, args))
        print(spike(args, rows))
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(1)


