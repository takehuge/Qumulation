from qutip import Qobj, sigmax, sigmay, sigmaz, tensor, qeye
from numpy import complex64, exp, number, pi, array, matmul, around, kron
from scipy.linalg import expm, sinm, cosm

cU11 = Qobj([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]]) # cZ

print("X:\n %s" %sigmax())
print("Y:\n %s" %sigmay())
print("Z:\n %s" %sigmaz())

XxX = tensor(sigmax(), sigmax())
print("X cross X:\n %s" %XxX)

# print("I: %s" %qeye(2))
XxI = tensor(sigmax(), qeye(2))
IxX = tensor(qeye(2), sigmax())
XX = XxI * IxX
R_xx_90 = expm(1j*(pi/2)/2*array(XX))
print("R_xx_90:\n %s" %R_xx_90)

YxI = tensor(sigmay(), qeye(2))
IxY = tensor(qeye(2), sigmay())
YY = YxI * IxY
R_yy_90 = expm(1j*(pi/2)/2*array(YY))
print("R_yy_90:\n %s" %R_yy_90)

ZxI = tensor(sigmaz(), qeye(2))
IxZ = tensor(qeye(2), sigmaz())
ZZ = ZxI * IxZ
R_zz_90 = expm(1j*(pi/2)/2*array(ZZ))
print("R_zz_90:\n %s" %R_zz_90)
R_zz__90 = exp(1j*pi/4) * expm(1j* pi/4 * array(ZZ))
print("R_zz__90 (UZZ):\n %s" %around(R_zz__90, 0))
RZ_90__RZ90 = tensor( Qobj(expm(1j*(-pi/2)/2*array(sigmaz()))), Qobj(expm(1j*(-pi/2)/2*array(sigmaz()))) )
print("RZ-90 for Q1 and RZ90 for Q2: %s" %RZ_90__RZ90)
print("CZ:\n%s" %around( array(RZ_90__RZ90) @ R_zz__90, 0 ))

iSWAP_xxyy = around(R_xx_90 @ R_yy_90, 0)
print("iSWAP_xxyy:\n %s" %iSWAP_xxyy)
iSWAP_yyxx = around(matmul(R_yy_90, R_xx_90, dtype=complex64), 0)
print("iSWAP_yyxx:\n %s" %iSWAP_yyxx)

iSWAP = expm(1j*(pi/2)/2*(array(XX) + array(YY)))
print("iSWAP:\n %s" %iSWAP)

print("iSWAP_xxyy==iSWAP: %s" %(iSWAP_xxyy==iSWAP).all())
print("iSWAP_yyxx==iSWAP: %s" %(iSWAP_yyxx==iSWAP).all())

R_x_90 = expm(1j*(pi/2)/2*array(sigmax()))
print("R_x_90: %s" %R_x_90)

R_x_180 = expm(1j*(pi)/2*array(sigmax()))
print("R_x_180: %s" %R_x_180)