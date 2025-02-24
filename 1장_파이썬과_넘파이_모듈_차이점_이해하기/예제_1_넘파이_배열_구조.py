import numpy as np
print(np.__version__)
print(np.ndarray)
print(np.ndarray.__name__)
print(type(np.ndarray.var))

for i in dir(np.ndarray):
    if not i.startswith("_"):
        if type(np.ndarray.__dict__[i]) != type(np.ndarray.var):
            print(i)




