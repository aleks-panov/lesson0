def divide(first, second):
    first = float(first)
    second = float(second)
    if second == 0:
        return 'Ошибка'
    else:
        res = first / second
        return res
