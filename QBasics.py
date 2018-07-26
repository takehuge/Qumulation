from qutip import *
from numpy import *

# print(qutip.about())

# import qutip.testing as qt
# qt.run()

q0 = basis(2,0)
q1 = basis(2,1)
qs = (q0 + q1).unit()
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

Hgate = snot(N=1)  # N: dimension
print("\nApplying H to q0: ")
print((Hgate*q0).full())

q01s = tensor(q0, q1, qs)
dm_q01s = ket2dm(q01s)
print("\nSeparable Qubit state: ")
dm01 = dm_q01s
print(dm01.full())
print("Equivalent to: ")
dm02 = tensor(q01s.ptrace(0), q01s.ptrace(1), q01s.ptrace(2))
print(dm02.full())
print("And: ")
dm03 = tensor(dm_q01s.ptrace(0), dm_q01s.ptrace(1), dm_q01s.ptrace(2))
print(dm02.full())
print("All zeros?")
print((dm01 - dm02))

print("\nHow about Entangled state: ")
Bell = bell_state(state="01")
qstate = tensor(q0, Bell)
dmstate = ket2dm(qstate)
dm01 = dmstate
print(dm01.full())
print("If forced to separate:")
dm02 = tensor(qstate.ptrace(0), qstate.ptrace(1), qstate.ptrace(2))
print(dm02.full())
dm03 = tensor(dmstate.ptrace(0), dmstate.ptrace(1), dmstate.ptrace(2))
print(dm03.full())
print("NOT SAME ANYMORE!")

dm01=[]
print("\nHow about BELL state: ")
Bell = bell_state(state="01").unit()
print("Bell state 01:")
print(Bell.full())
dmstate = ket2dm(Bell)
dm01 = dmstate
print("Bell dm:")
print(dm01.full())
print("Checking pure state: ")
print((dm01 ** 2).tr()) # pure state if 1, mixed if < 1
print("If forced to separate:")
dm02 = tensor(qstate.ptrace(0), qstate.ptrace(1))
print(dm02.full())
dm03 = tensor(dmstate.ptrace(0), dmstate.ptrace(1))
print(dm03.full())
print("NOT SAME ANYMORE!")

