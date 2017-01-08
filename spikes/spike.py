import sys

from spikes.DATA import USAGE
from spikes.normalize import normalize
from spikes.print_spike import print_spike
from spikes.spike_data import spike_data


def spike(data, rows=1):
    try:
        data = list(map(int, data))

    except ValueError:
        sys.stderr.write(USAGE)
        sys.exit(65)

    normalized_data = normalize(data, rows=rows)
    spiked_data = spike_data(normalized_data, rows=rows)
    spiked_data.reverse()
    spikes = ""
    for index, row in enumerate(spiked_data):
        spikes += print_spike(row)
        if index + 1 < len(spiked_data):
            spikes += "\n"

    return spikes

