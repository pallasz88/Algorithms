def linear_search(array, param):
    if not array:
        return -1

    for i, e in enumerate(array):
        if e == param:
            return i

    return -1
