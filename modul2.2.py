first=int(input('Введите первое число '))
second=int(input('Введите второе число '))
third=int(input('Введите третье число '))
third=int(third)
if first==second==third:
    print(3)
elif first==second or first==third:
    print(2)
elif second==first or second==third:
    print(2)
elif third==first or third==second:
    print(2)
else:
    print(0)







