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
print("primer vector: ")
print(v)

for j in range(len(A)):
    w[0, j] = np.sum(A[:, j] ** 3) ** 0.333333
print(w)


for k in range(len(A)):
    vt[k, 0] = v[0, k]
print(vt)
s = 1 / np.dot(w, vt) * np.dot(vt, w)
print(s)