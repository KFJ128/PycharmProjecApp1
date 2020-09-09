import numpy as np
def crearmatrizalealtoria(nunmerofilas, numerocolumnas):
    return np.random.randint(1, 11, (nunmerofilas, numerocolumnas))

A = crearmatrizalealtoria(6, 6)
print(A)
v = np.zeros((1, 6))
w = np.zeros((1, 6))
vt = np.zeros((6, 1))
for i in range(len(A)):
    v[0, i] = np.sum(A[i, :] ** 2) ** 0.5
print(v)

for i in range(len(A)):
    w[0, i] = np.sum(A[:, i] ** 3) ** 0.333333
print(w)


for i in range(len(A)):
    vt[i, 0] = v[0, i]
print(vt)
s = (vt * w)
print(s)