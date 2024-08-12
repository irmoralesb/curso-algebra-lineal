# Polynomios
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Especificar el backend
import matplotlib.pyplot as plt

r = np.poly1d([1,2,3])
print(r)

s = np.poly1d([1,2,3,4,5])
print(s)


print("Are equal {0}".format(r == s))

print("r is grade {0}".format(r.order))
print("s is grade {0}".format(s.order))

addition = s + r
print("Addition {0}".format(addition))

product = s * r
print("Product {0}".format(product))


division = s/r
print("Division {0}".format(division))
rest = np.poly1d([4,5])

#original =  division * r  +  rest
original = np.poly1d(1,0,0) * r + 3

print("original: ")
print(original)
print("r and original are equal {0}".format(original == r))


print("Evaluate to value")
print(r(5))

print("roots")
print(r.r)

x = np.arange(-2, 3,.5)
y = r(x)

plt.plot(x,y)
plt.show()