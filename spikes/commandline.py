#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import re
import sys

from spikes.spike import Spike
from spikes.spike import spike


class Cli(object):

    __splitter = '[, ]+'

    @staticmethod
    def __sys_exit(message, status):
        sys.stderr.write(message)
        sys.exit(status)

    @staticmethod
    def __parse_arguments(opts, args, arguments, usage):
        rows = None
        for arg in args:
            arguments += re.split(Cli.__splitter, arg)
        for opt, arg in opts:
            if opt == '-l':
                rows = int(arg)
            else:
                Cli.__sys_exit(usage, 128)
        return arguments, rows

    @staticmethod
    def __read_argv():
        usage = Spike.usage()
        arguments = []
        rows = None
        try:
            argv = sys.argv[1:]
            opts, args = getopt.getopt(argv, 'l:')
            arguments, rows = Cli.__parse_arguments(opts, args, arguments, usage)
        except getopt.GetoptError:
            Cli.__sys_exit(usage, 2)
        except ValueError:
            Cli.__sys_exit(usage, 2)

        return arguments, rows

    @staticmethod
    def __read_std_in():
        usage = Spike.usage()
        arguments = []
        try:
            std_in = re.split(Cli.__splitter, sys.stdin.read().strip().replace('\n', ' '))
            opts, args = getopt.getopt(std_in, 'l:')
            arguments, rows = Cli.__parse_arguments(opts, args, arguments, usage)
        except getopt.GetoptError:
            sys.stderr.write(usage)
            sys.exit(2)
        except ValueError:
            sys.stderr.write(usage)
            sys.exit(64)

        return args, rows

    @staticmethod
    def __read():
        args, rows = Cli.__read_argv()
        if len(args) < 1:
            args_t, rows_t = Cli.__read_std_in()
            rows = rows or rows_t
            args += args_t
        if len(args) < 1:
            Cli.__sys_exit(Spike.usage(), 1)
        args = list(filter(None, args))
        rows = rows or 1

        return args, rows

    @staticmethod
    def run():
        try:
            args, rows = Cli.__read()
            print(spike(args, rows))
            sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(1)
