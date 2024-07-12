def print_params(a=1, b='Строка', c=2):
    print(a, b, c)


print_params()
values_list = [3, 'string', (6, 7, 8)]
values_dict = {'a': 123456, 'b': 829.374, 'c': [8, 9, 10]}
values_list_2 = [54.32, 'Строка']
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
