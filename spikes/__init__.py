#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt
import re
import sys

from spikes.spike import Spike, spike


class CLI(object):
    __splitter = "[, ]+"

    @staticmethod
    def __sys_exit(message, status):
        sys.stderr.write(message)
        sys.exit(status)

    @staticmethod
    def __read_argv():
        usage = Spike.usage()
        arguments = []
        rows = None
        try:
            argv = sys.argv[1:]
            opts, args = getopt.getopt(argv, 'l:')
            for arg in args:
                arguments += re.split(CLI.__splitter, arg)
            for opt, arg in opts:
                if opt == '-l':
                    rows = int(arg)
                else:
                    CLI.__sys_exit(usage, 128)
        except getopt.GetoptError:
            CLI.__sys_exit(usage, 2)
        except ValueError:
            CLI.__sys_exit(usage, 2)

        return arguments, rows

    @staticmethod
    def __read_std_in():
        usage = Spike.usage()
        try:
            std_in = re.split(CLI.__splitter, sys.stdin.read().strip().replace('\n', ' '))
            opts, args = getopt.getopt(std_in, 'l:')
            rows = None
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

    @staticmethod
    def run():
        try:
            args, rows = CLI.__read_argv()
            if len(args) < 1:
                args_t, rows_t = CLI.__read_std_in()
                rows = rows or rows_t
                args += args_t
            if len(args) < 1:
                CLI.__sys_exit(Spike.usage(), 1)
            args = list(filter(None, args))
            rows = rows or 1
            print(spike(args, rows))
            sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(1)


def main():
    CLI.run()

