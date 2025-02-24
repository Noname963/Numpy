import numpy as np

a = [1,2,3,4]
b = [1,2,3,4]

print(a)
print(a[0])
print(b[0])

a2 = np.array([[1,2,3],[4,5,6]])
ab = [[1,2,3],[4,5,6]]
print(ab)
print(a2)

try:
    ab[0][1]
except Exception as e:
    print(e)

print(ab[0][1])
print(a2[0,1])

print((a2[0,1]))
print(a2[0,1].item())

print(a2[0,1].real)
print(a2[0,1].imag)