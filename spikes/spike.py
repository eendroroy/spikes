#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if sys.version_info[0] == 3:
    uchr = chr
elif sys.version_info[0] == 2:
    uchr = unichr


class Spike(object):

    __BAR_INDEX = 8
    __BARS = [
        ' ',
        uchr(9601),
        uchr(9602),
        uchr(9603),
        uchr(9604),
        uchr(9605),
        uchr(9606),
        uchr(9607),
        uchr(9608),
    ]
    __USAGE = 'Usage: spike [-l <number_of_lines>] list_of_numbers]'

    @staticmethod
    def usage():
        return Spike.__USAGE

    @staticmethod
    def __normalize(data, rows=1):
        upper_limit = rows * Spike.__BAR_INDEX
        normalized_list = list()

        max_item = float(max(data))

        if max_item == float(0):
            Spike.__normalize_zero_list(normalized_list, data, upper_limit)
        else:
            Spike.__normalize_positive_list(normalized_list, data, max_item, upper_limit)

        return normalized_list

    @staticmethod
    def __normalize_zero_list(n_list, data, upper_limit):
        for item in data:
            n_list.append((int(item) if item < upper_limit else upper_limit))

    @staticmethod
    def __normalize_positive_list(n_list, data, max_item, upper_limit):
        for item in data:
            norm = int(round(float(item) / max_item * upper_limit, 0))
            adjusted_norm = (norm if norm > 0 else 1)
            n_list.append((int(item) if item == float(0) else adjusted_norm))

    @staticmethod
    def __spike_column(spiked, column, rows):
        full_rows = int(column / Spike.__BAR_INDEX)
        fraction_val = column - full_rows * Spike.__BAR_INDEX

        for full_row in range(0, full_rows):
            spiked[full_row].append(Spike.__BAR_INDEX)
        if full_rows < rows:
            spiked[full_rows].append(fraction_val)
        for rest_row in range(full_rows + 1, rows):
            spiked[rest_row].append(0)

    @staticmethod
    def __spike_data(data, rows):
        spiked = list()
        for _ in range(0, rows):
            spiked.append(list())

        for column in data:
            Spike.__spike_column(spiked, column, rows)

        return spiked

    @staticmethod
    def __print_spike(row):
        _spike = ''
        for bar in row:
            _spike += Spike.__BARS[bar]
        return _spike

    @staticmethod
    def make_spike(spiked_data):
        spikes = ''
        for index, row in enumerate(spiked_data):
            spikes += Spike.__print_spike(row)
            if index + 1 < len(spiked_data):
                spikes += '\n'

        return spikes

    @staticmethod
    def get_spike(data, rows=1):
        try:
            data = list(map(float, data))
        except ValueError:
            sys.stderr.write(Spike.__USAGE)
            sys.exit(65)

        spiked_data = Spike.__spike_data(Spike.__normalize(data, rows), rows)
        spiked_data.reverse()

        return Spike.make_spike(spiked_data)


def spike(data, rows=1):
    spikes = Spike.get_spike(data, rows)
    return spikes
