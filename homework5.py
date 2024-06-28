immutable_var=(1,2,5,'a','b','d')
print(immutable_var)
#immutable_var [0]='c'
# изменить значение элемента нельзя, кортеж неизменяемый
mutable_list=([1,2,3],4,5,6)
print(mutable_list)
mutable_list[0][1]=7
print(mutable_list)
