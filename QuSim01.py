from qutip import *
import numpy as np

print("I'm ABC")
r = np.random.rand(2,1)
print(Qobj(r))

vac = basis(5,0)
print(vac)

a = create(5)
print(a.dag() * vac)
