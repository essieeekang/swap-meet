def my_max(collection, key=lambda item: item):
    if not collection:
        raise ValueError

    max_item = collection[0]
    max_value = key(max_item)

    for item in collection:
        if key(item) > max_value:
            max_item = item
            max_value = key(item)

    return max_item


def my_min(collection, key=lambda item: item):
    if not collection:
        raise ValueError

    min_item = collection[0]
    min_value = key(min_item)

    for item in collection:
        if key(item) < min_value:
            min_item = item
            min_value = key(item)

    return min_item
