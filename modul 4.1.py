from fake_math import divide as fake_divide
from true_math import divide as true_divide

res1 = fake_divide(69, 3)
res2 = fake_divide(3, 0)
res3 = true_divide(49, 7)
res4 = true_divide(15, 0)
print(res1)
print(res2)
print(res3)
print(res4)
