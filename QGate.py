from qutip import *
from numpy import *

cU = Qobj([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]])
cxcx = tensor(sigmax(), sigmax())
print(cxcx)
cxI = tensor(sigmax(), qeye(2))
X = tensor(sigmax(), qeye(2)) * tensor(sigmax(), sigmax())
print(X)