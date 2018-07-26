# import libraries
from qutip import *
import numpy as np
import random as rd

# Defining Basis
q0 = basis(2, 0)  # |0> # already a Qobj
q1 = basis(2, 1)  # |1>

# Basis Library
Q = dict()
Q['0'], Q['1'] = q0, q1

# Message-Qubit to be sent by Alice
a = 2
while 0 > a or a > 1:
    try:
        a = float(input('\nEnter alpha (0 - 1): '))  # enter alpha (coefficient)
    except ValueError: print("please use float 0 - 1")
#Message Qubit:
MQ = ((a * q0) + ((1 - a) * q1)).unit() # / (np.sqrt((a ** 2 + (1 - a) ** 2)))  # message 
MQ_dm = ket2dm(MQ)
print("Checking Unity: ", MQ_dm.tr())

# Preparing Bell state (Entangled Here- and There-Qubit)
selection = 4
while 0 > selection or selection > 3:
    try:
        selection = int(input('\nSelect Bell-state to encrypt Message (0 - 3): '))
    except ValueError: print("please use integer 0 - 3")
    
if selection is 0:
    bell = "00"  # bell state 00
elif selection is 1:
    bell = "01"  # bell state 01
elif selection is 2:
    bell = "10"  # bell state 10
elif selection is 3:
    bell = "11"  # bell state 11

#Generating Bell-states (reverse of our circuit):
EP = cnot(2, 0, 1) * snot(2, 0) * \
    tensor(Q[bell[0]], Q[bell[1]])  # Entangled Pair
print("\nSelected Bell-state: " + bell)
print(EP.full())

# Combine the states:
MQEP = tensor(MQ, EP)  # message + Alice's qubit (here)
MQEP_dm = ket2dm(MQEP)
print("\nTotal 3-Qubit Density Matrix: ")
print(MQEP.full())
print("\nChecking the trace:", MQEP_dm.tr())

# Performing 1st Q-Sequence:
CNOT = cnot(N=3, control=0, target=1)  # CNOT gate
H = snot(N=3, target=0)  # Hadamard "H" gate 
U = H * CNOT  # (8x8)
PSI = U * MQEP
print("\nAfter 1st Q-Sequence: ")
print(PSI.full())  # 3 qubit system (8x1)
PSI_dm = ket2dm(PSI)
print("\nChecking the trace: ", PSI_dm.tr())
# print("we hope to get back this:")
# print("ket:\n ", Qobj(PSI[:2]).unit().full()) # check if it's the same as original
# print("DM:\n ", ket2dm(Qobj(PSI[:2]).unit()).full())

# Measurement of all Alice's Qubit
CH01 = str(rd.randint(0, 1))  # rd.randint(0, 1) # random 0 or 1
CH02 = str(rd.randint(0, 1))  # rd.randint(0, 1)
KEY = CH01 + CH02 # Encryption KEY sent by Alice to Bob thru classical channel
print("\nMeasurement of All Alice Qubit yield the KEY: '{'%s,%s'}'" %(CH01,CH02))

# Constructing Collapse Operator based on the KEY (using simple 2-Q basis) 
# config depends on the circuit
C_OP = tensor(ket2dm(Q[CH01]), ket2dm(Q[CH02]), qeye(2))
C_PSI = C_OP * PSI
BOB_PSI = C_PSI.ptrace(2) #tracing out Bob's Qubit #0 & 1 is Alice, 2 is Bob's
BOB_PSI = BOB_PSI.unit()
print("\nTHUS, Encrypted Bob's Message:\n", BOB_PSI.full())
print("\nAND, the decrytion scheme should be:")

# Constructing Encryption Library by comparing bell (Encryption Method) and KEY:
if bell == KEY: # 1: action 0 / 2: no action since flipping twice = no flip
    Z, X = 0, 0
    print("Doing nothing")
elif bell[0] != KEY[0] and bell[1] != KEY[1]:
    Z, X = 1, 1
    print("Apply X then Z")
elif bell[0] != KEY[0]:
    Z, X = 1, 0
    print("Apply Z only")
elif bell[1] != KEY[1]:
    Z, X = 0, 1
    print("Apply X only")

#Constructing General Correction gate (2nd Q-Sequence):
#Using the beauty of Pauli Matrix: sigma**2 = I
Correction = (sigmaz() ** Z) * (sigmax() ** X)
#Teleported Qubit (Final step: Decryption):
TQ_dm = Correction * BOB_PSI * Correction.dag()

#COMPARE
print("\nTeleporting......")
print("Teleported Qubit sent to Bob:\n", TQ_dm)
print("Which is INTACT compared to the original Message sent by Alice:\n", MQ_dm)
print("\nChecking trace:", TQ_dm.tr())
print("\nChecking purity:", (TQ_dm**2).tr())
precision = 1e-15
print("\nSUCCESS: ", abs(sum(sum(TQ_dm.full() - MQ_dm.full()))) < precision, "down to %s\n" % (precision))


