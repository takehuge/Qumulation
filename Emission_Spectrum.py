import numpy as np
from qutip import *
import pylab as plt

N = 4   #number of cavity fock state
wc = wa = 1.0 * 2 * np.pi   #cavity and atom resonant freq
g = 0.1 *2 * np.pi   #coupling strength between cavity and atom
kappa = 0.75   #cavity decay rate
gamma = 0.25   #atom decay rate

# Jaynes-Cumming Hamiltonian
a = tensor(destroy(N), qeye(2))
sm = tensor(qeye(N), destroy(2))   #sigma
H = wc * a.dag() * a + wa * sm.dag() * sm + g * (sm.dag() * a + sm * a.dag())

# collapse operators
n_th = 0.25
c_ops = [np.sqrt(kappa * (1 + n_th)) * a, np.sqrt(kappa * n_th) * a.dag(), np.sqrt(gamma) * sm]

# resulting spectrum
tlist = np.linspace(0, 100, 5000)
corr = correlation_ss(H, tlist, c_ops, sm.dag(), sm)
wlist1, spec1 = spectrum_correlation_fft(tlist, corr)

# calculate the power spectrum using spectrum, which internally uses essolve
# to solve for the dynamics (by default)
wlist2 = np.linspace(0.25, 1.75, 200) * 2 * np.pi
spec2 = spectrum(H, wlist2, c_ops, sm.dag(), sm)

# plot the spectra
fig, ax = plt.subplots(1, 1)
ax.plot(wlist1 / (2 * np.pi), spec1, 'b', lw=2, label='eseries method')
ax.plot(wlist2 / (2 * np.pi), spec2, 'r--', lw=2, label='me+fft method')
ax.legend()
ax.set_xlabel('Frequency')
ax.set_ylabel('Power spectrum')
ax.set_title('Vacuum Rabi splitting')
ax.set_xlim(wlist2[0]/(2*np.pi), wlist2[-1]/(2*np.pi))
plt.show()

