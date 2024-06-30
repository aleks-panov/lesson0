my_dict={'Alex' : 1979, 'Max' : 1982, 'Denis' : 1984, 'Sergey' : 1988}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Ilya'))
my_dict.update({'Kirill' : 999230, 'Yulia' : 22283944})
a=my_dict.pop('Denis')
print(a)
print(my_dict)
my_set={1,2,2,'Max',33,33,'Alex'}
my_set.add(8)
my_set.add(5)
print(my_set)
my_set.discard('Max')
print(my_set)