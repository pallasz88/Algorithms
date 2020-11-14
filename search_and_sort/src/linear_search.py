def linear_search(array, param):

    for i, e in enumerate(array):
        if e == param:
            return i

    return -1
