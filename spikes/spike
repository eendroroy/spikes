import sys
import getopt

from spikes.normalize import normalize
from spikes.print_spike import print_spike
from spikes.spike_data import spike_data

USAGE = """
Usage: spike [-l <number_of_lines>] list_of_numbers]
"""


def spike(args=sys.argv):

    try:
        opts, args = getopt.getopt(args[1:], "l:")
        rows = 1
        for opt, arg in opts:
            if opt == '-l':
                rows = int(arg)
            else:
                sys.stderr.write(USAGE)
                return 128
    except getopt.GetoptError:
        sys.stderr.write(USAGE)
        return 2
    except ValueError:
        sys.stderr.write(USAGE)
        return 64

    try:
        data = map(int, args)
    except ValueError:
        sys.stderr.write(USAGE)
        return 65

    spiked_data = spike_data(normalize(data, rows=rows), rows=rows)
    for r in xrange(rows - 1, -1, -1):
        print_spike(spiked_data[r])

    return 0


def main():
    try:
        sys.exit(spike(sys.argv))
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()
