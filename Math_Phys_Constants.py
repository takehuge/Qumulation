# Defining Global Constants (SI Units)%
import math
import numpy as np
from scipy import constants
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)

# Basic Python Math: power
print('3 to the power of 5 equals ', math.pow(3, 5))
print('CHECKING 3 to the power of 5 equals ', 3**5, '\n')
# Basic Python Math: exponential
print('exponential function of 7: ', math.exp(7))
print('CHECKING exponential function of 7: ', math.e**7, '\n')

# Gravitational constant
G = 6.67408e-11 #m3 kg-1 s-2
print('Local G:', G)
G = constants.G
print('scipy G:', G, '\n')

# Avogrado number/constant
nAvogrado = 6.022e23 #mol^-1
print('Local N_A:', nAvogrado)
nAvogrado = constants.N_A
print('scipy N_A:', nAvogrado, '\n')

# Electric constants
eps0 = 8.854187817620e-12 #(F/m)
X = eps0
print('Local epsilon_0:', X)
X = constants.epsilon_0
print('scipy epsilon_0:', X, '\n')

# Planck constant
h = 6.6260755e-34 #in SI unit J.s
X = h
print('Local h:', X)
X = constants.h
print('scipy h:', X, '\n')

# Elementary Charge
e = 1.60217733e-19 #in SI unit C
X = e
print('Local e:', X)
X = constants.e
print('scipy e:', X, '\n')

# Electron Mass
me = 9.10938188e-31 #kg
X = me
print('Local m_e:', X)
X = constants.m_e
print('scipy m_e:', X, '\n')

# Boltzmann Constant
kB = 1.380650424e-23
X = kB
print('Local k:', X)
X = constants.k
print('scipy k:', X, '\n')

# Speed of light
c = 299792458 #m/s
X = c
print('Local c:', X)
X = constants.c
print('scipy c:', X, '\n')

# Magnetic constant
mu0 = 4 * math.pi * (1e-7) #in T.m/A or H/m or Wb(A.m)
X = mu0
print('Local mu_0:', X)
X = constants.mu_0
print('scipy mu_0:', X, '\n')

# Units
kilo = 1e3
mega = 1e6
giga = 1e9
tera = 1e12
atto = 1e-18
femto = 1e-15
pico = 1e-12
nano = 1e-9
micro = 1e-6
milli = 1e-3

Angstrom = constants.angstrom
print('1 Angstrom = ', Angstrom,'m\n')

# Bohr Magneton
muB = e*h/2/np.pi/2/me  # J/T
mu_B = constants.e*constants.h/2/math.pi/2/constants.m_e
X = muB
print('Local mu_B:', X)
X = constants.physical_constants['Bohr magneton']
print('scipy mu_B:', X[0])
print('CHECKING scipy mu_B:', mu_B, '\n')

# Conductance Quanta/Quantum
G0 = 2*e**2/h
G_0 = 2*constants.e**2/constants.h
X = G0
print('Local G0:', X)
X = constants.physical_constants['conductance quantum']
print('scipy G0:', X[0])
print('CHECKING scipy G0:', G_0, '\n')

# Magnetic Flux Quanta/Quantum  
Phi0 = h/2/e
Phi_0 = constants.h/2/constants.e
X = Phi0
print('Local Phi0:', X)
X = constants.physical_constants['mag. flux quantum']
print('scipy Phi0:', X[0])
print('CHECKING scipy Phi0:', Phi_0, '\n')  

# Planck Length
LPlanck = np.sqrt(G*h/2/math.pi/c/c/c)
PlanckLength = np.sqrt(constants.G*constants.hbar/(constants.c**3))
X = LPlanck
print('Local Planck length:', X)
X = constants.physical_constants['Planck length']
print('scipy Planck length:', X[0])
print('CHECKING scipy Planck length:', PlanckLength, '\n')

