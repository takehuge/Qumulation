import matplotlib
matplotlib.use('tkAgg')

from qutip import *
from scipy import *
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7, 7))
ax = Axes3D(fig, azim=-40, elev=30)
sphere = Bloch(axes=ax)

t_length = 100
t_list = np.linspace(0, 350, t_length)
print(t_list[1:10])

# initial state
a = 1
psi0 = (a * basis(2, 0) + (1 - a) * basis(2, 1)) / (np.sqrt(a**2 + (1 - a)**2))
# psi0 = rand_ket(2) #random initial state
# psi0 = Qobj([[1 / np.sqrt(2)], [1 / np.sqrt(2)]]) #define initial ket with qobj

# exchange rates
w = 1 * 2 * np.pi  # qubit precession rate (qubit angular frequency)
delta = 2 * 2 * np.pi  # coupling rate
theta = 0.05 * np.pi      # qubit angle from sigma_z axis (toward sigma_x axis)
gamma1 = 0.05       # qubit relaxation rate
gamma2 = 0.0007  # qubit dephasing / decoherence rate (T2)

# Hamiltonian
H = - delta/2.0 * sigmax() - w/2.0 * sigmaz()

# Operators for which the expectations are computed upon
e_ops = [sigmax(), sigmay(), sigmaz()]

# Bloch-Redfield master equation
# def ohmic_spectrum(wn): # wn here is noise spectrum range, not qubit freq
#     if wn == 0: # dephasing inducing noise
#         return gamma2
#     else: # relaxation inducing noise
#         return gamma2 / 2 * (wn / (2 * np.pi)) * (wn > 0)

# R, ekets = bloch_redfield_tensor(H, [sigmax()], [ohmic_spectrum])
# np.real(R.full())
# expt_list = bloch_redfield_solve(R, ekets, psi0, t_list, e_ops)

# Lindblad Master Equation Solver
def qubit_integrate(w, theta, gamma1, gamma2, psi0, tlist):
    # operators and the hamiltonian
    sx = sigmax()
    sy = sigmay()
    sz = sigmaz()
    sm = sigmam() # Sigma minus
    # H = w * (np.cos(theta) * sz + np.sin(theta) * sx)
    # collapse operators
    c_op_list = []
    n_th = 0.5  # temperature
    rate = gamma1 * (n_th + 1)
    if rate > 0.0:
        c_op_list.append(np.sqrt(rate) * sm)
    rate = gamma1 * n_th
    if rate > 0.0:
        c_op_list.append(np.sqrt(rate) * sm.dag())
    rate = gamma2
    if rate > 0.0:
        c_op_list.append(np.sqrt(rate) * sz)

    # evolve and calculate expectation values
    output = mesolve(H, psi0, tlist, c_op_list, e_ops)
    return output

result = qubit_integrate(w, theta, gamma1, gamma2, psi0, t_list)
expt_list = result.expect

# Displaying results
sx = expt_list[0]
sy = expt_list[1]
sz = expt_list[2]
print([sx[0], sy[0], sz[0]])

def animate(j):
    sphere.clear()
    print('\n' * 37)
    print(np.array([j, sx[j], sy[j], sz[j]]))
    # sphere.add_vectors([np.sin(theta), 0, np.cos(theta)])
    sphere.add_vectors(np.array([delta, 0, w]) / np.sqrt(delta ** 2 + w ** 2)) #Quantization axis
    sphere.add_points(np.array([sx[:j + 1], sy[:j + 1], sz[:j + 1]]))
    sphere.add_vectors(np.array([sx[j].real, sy[j].real, sz[j].real]))
    sphere.make_sphere()
    return sphere

def init():
    sphere.vector_color = ['b']
    return ax

ani = animation.FuncAnimation(fig, animate, np.arange(t_length),
                              init_func=init, interval=25, repeat=False, blit=False)
#Install FFMPEG using: brew install ffmpeg
ani.save('Redfield01.mp4', fps=15)

sphere.show()

