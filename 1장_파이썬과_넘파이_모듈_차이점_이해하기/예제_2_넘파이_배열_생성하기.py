from traceback import print_tb

import numpy as np

a = [1,2,3,4]
b = np.array(a)
print(a)
print(type(b))

t = (1,2,3,4)
c = np.array(t)
print(type(c))

print(b.data)
print(b.data.obj)
print(type(b.data.obj))

d = c
print(d.base is c.base)

d[0] = 100
print(d)
print(c)

e = np.array(c)
e[0] = 99
print(e)
print(c)

f = np.array(1,dtype=np.float64)
print(f)
print(e.dtype)

a2 = np.array([[1,2,3],[4,5,6]])
print(a2.shape)
print(a2.ndim)
print(a2.dtype)
print(a2.itemsize)
print(a2.strides)
print(a2.flatten)
print(a2.ravel)