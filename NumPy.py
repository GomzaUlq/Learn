import numpy
import numpy as np

# x = np.arange(15)
# print(x)
# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# x = np.concatenate((a, b))
# print(x)
# b = x.reshape(2, 2)
# print(b)


a = np.arange(36)
b = a.reshape(6, 6)
print(b)
divisible_by_2 = a[a % 2 == 0]
print(divisible_by_2)
c = a[3:25]
print(c)