import requests
import matplotlib.pyplot as plt
import pandas as pd



r = requests.get("https://api.github.com")
print(r.text)
print(r.encoding)



x = [1, 3, 5, 7, 9]
y = [3, 4, 5, 6, 7]

plt.plot(x, y, marker='1')

plt.title('график')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()



Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = pd.Series(Data)
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j']
b = pd.Series(Data, Index)
print(b)