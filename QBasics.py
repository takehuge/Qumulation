from qutip import *
from numpy import *

# print(qutip.about())

# import qutip.testing as qt
# qt.run()

q0 = basis(2,0)
q1 = basis(2,1)
q10 = tensor(q1, q0)
dm10 = ket2dm(q10)
print("q10: ")
print(q10)

CNOT = cnot(N=2, control=0, target=1)  # control and target qubit position
print("\nApplying CNOT to q10: ")
PSI = CNOT * q10
DM = ket2dm(PSI)
DMM = CNOT * dm10
print(PSI)
print(DM)
print(DMM)

# Hgate = snot(N=1)  # N: dimension
# print("\nApplying H to q0: ")
# print((Hgate*q0).full())