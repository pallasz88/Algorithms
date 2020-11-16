def fibonacci(param):
    if param < 0 or param > 34:
        raise ValueError

    if type(param) is not int:
        raise TypeError

    if param == 0:
        return 0
    elif param == 1 or param == 2:
        return 1

    return fibonacci(param - 1) + fibonacci(param - 2)


def dynamic_fibonacci(param, lookup):
    if param < 0 or param > 99:
        raise ValueError

    if type(param) is not int or type(lookup) is not list:
        raise TypeError

    if param == 0 or param == 1:
        lookup[param] = param

    if lookup[param] is None:
        lookup[param] = dynamic_fibonacci(param - 1, lookup) + dynamic_fibonacci(param - 2, lookup)

    return lookup[param]
