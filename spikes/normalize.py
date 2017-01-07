# coding=utf-8
def normalize(data, rows=1):
    """

    :type rows: int
    :type data: list
    """
    upper_limit = rows * 8
    normalized_list = list()

    max_item = max(data)
    min_item = min(data)
    diff = float(max_item) - float(min_item)

    for item in data:
        norm = int(round((((float(item) - float(min_item)) / diff) * upper_limit), 0))
        adjusted_norm = norm if norm > 0 else 1
        normalized_list.append(int(item) if item == 0 else adjusted_norm)

    return normalized_list
