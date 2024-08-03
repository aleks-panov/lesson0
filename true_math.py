def divide(first, second):
    from math import inf
    first = float(first)
    second = float(second)
    if second == 0:
        return inf
    else:
        res = first / second
        return res
