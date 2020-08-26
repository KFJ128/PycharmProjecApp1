import numpy as np
a = np.random.randint(10, size=(5, 5))
b = np.random.randint(10, size=(5, 5))
c = np.empty((5, 5))

for i in range(len(a)):
    for j in range(len(a[i])):
        c[i, j] = a[i, j] + b[i, j]
print(a)
print(b)
print(a+b)
print(c)
