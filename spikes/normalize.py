# coding=utf-8
from spikes.DATA import BAR_INDEX


def normalize(data, rows=1):
    upper_limit = rows * BAR_INDEX
    normalized_list = list()

    max_item = max(data)
    min_item = 0
    diff = float(max_item) - float(min_item)

    if diff == 0:
        for item in data:
            normalized_list.append(item if item < upper_limit else upper_limit)
    else:
        for item in data:
            norm = int(round((((float(item) - float(min_item)) / diff) * upper_limit), 0))
            adjusted_norm = norm if norm > 0 else 1
            normalized_list.append(int(item) if item == 0 else adjusted_norm)

    return normalized_list
