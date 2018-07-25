# import libraries
from qutip import *
import numpy as np
import random as rd

# Defining Basis
q0 = basis(2, 0)  # |0> # already a Qobj
q1 = basis(2, 1)  # |1>

# Message-Qubit to be sent by Alice
a = 2
while 0 > a or a > 1:
    try:
        a = float(input('\nEnter alpha (0 - 1): '))  # enter alpha (coefficient)
    except ValueError: print("please use float 0 - 1")
MQ = ((a * q0) + ((1 - a) * q1)).unit() # / (np.sqrt((a ** 2 + (1 - a) ** 2)))  # message 
MQ_dm = ket2dm(MQ)

# Checking Unity
innerprod = MQ.dag() * MQ
if innerprod[0][0][0] == (1 + 0j):
    print("\nUnity confirmed of MQ:")
    print(MQ)
else: 
    print("\nNot a UNITY: Check MQ config")
    exit()

# Preparing Bell state (Entangled Here- and There-Qubit)
selection = 4
while 0 > selection or selection > 3:
    try:
        selection = int(input('\nSelect Bell-state to encrypt Message (0 - 3): '))
    except ValueError: print("please use integer 0 - 3")
    
if selection is 0:
    b = "00"  # bell state 00
elif selection is 1:
    b = "01"  # bell state 01
elif selection is 2:
    b = "10"  # bell state 10
elif selection is 3:
    b = "11"  # bell state 11
EP = bell_state(state=b)  # Entangled Pair
print("\nSelected Bell-state: " + b)
print(EP)

# Combine the states:
MQEP = tensor(MQ, EP)  # message + Alice's qubit (here)
MQEP_dm = ket2dm(MQEP)
print("\nTotal 3-Qubit Density Matrix: ")
print(MQEP_dm)
print("\nChecking the trace:", MQEP_dm.tr())

# Performing Q-Sequence:
CNOT = cnot(N=3, control=0, target=1)  # CNOT gate
H = snot(N=3, target=0)  # Hadamard "H" gate 
U = H * CNOT  # (8x8)
PSI01 = U * MQEP
print("\nAfter 1st Q-Sequence: ")
print(PSI01)  # 3 qubit system (8x1)
print("Checking the trace: ", ket2dm(PSI01).tr())
psi01 = PSI01.full()
print(Qobj(psi01[:2]).unit())

# measurement of all Alice's Qubit
CH01 = rd.randint(0, 1) # random 0 or 1
CH02 = rd.randint(0, 1)
