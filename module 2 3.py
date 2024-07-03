my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
a = len(my_list)
d = 0
while d <= a:
    b = my_list[d]
    d = d + 1
    if b > 0:
        print(b)
        continue
    if b < 0:
        break