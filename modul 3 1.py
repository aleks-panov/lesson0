calls = 0


def count_calls():
    global calls
    if calls >= 0:
        calls = calls + 1
    return calls


def string_info(s):
    count_calls()
    a = str(s)
    string_info = len(a), a.upper(), a.lower()
    return string_info


def is_contains(string, list_to_search):
    count_calls()
    a = string.lower()
    string = str(a)
    a1 = map(str.lower, list_to_search)
    list_to_search1 = list(a1)
    for i in range(0, len(list_to_search1)):
        if string == list_to_search1[i]:
            b = True
        elif string != list_to_search1:
            b = False
    return b


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
