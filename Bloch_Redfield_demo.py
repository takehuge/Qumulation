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

delta = 0.2 * 2*np.pi
eps0 = 1 * 2*np.pi  # dephasing rate
gamma = 0.5  # decoherence rate
# H = Qobj()
H = - delta/2.0 * sigmax() - eps0/2.0 * sigmaz()

t_length = 1000
t_list = np.linspace(0, 15, t_length)
psi0 = rand_ket(2)
print(t_list[1])
e_ops = [sigmax(), sigmay(), sigmaz()]


def ohmic_spectrum(w):
    if w == 0:
        return gamma
    else:
        return gamma/2 * (w/(2*np.pi)) * (w > 0)

R, ekets = bloch_redfield_tensor(H, [sigmax()], [ohmic_spectrum])
np.real(R.full())
expt_list = bloch_redfield_solve(R, ekets, psi0, t_list, e_ops)
sx = expt_list[0]
sy = expt_list[1]
sz = expt_list[2]

print([sx[0], sy[0], sz[0]])

# output = brmesolve(H.data, psi0, t_list, [sigmax()], e_ops, [ohmic_spectrum])
# result = output.expect  # np.transpose(output.expect)
# for i in np.arange(t_length):
#     print([result[i][0], result[i][1], result[i][2]])

# sx = result[0]
# sy = result[1]
# sz = result[2]
# k = 0
# print(len(result))


def animate(j):
    sphere.clear()
    print('\n' * 37)
    print(np.array([sx[j], sy[j], sz[j]]))
    sphere.add_vectors(np.array([delta, 0, eps0]) / np.sqrt(delta ** 2 + eps0 ** 2))
    sphere.add_points(np.array([sx[:j + 1], sy[:j + 1], sz[:j + 1]]))
    sphere.add_vectors(np.array([sx[j].real, sy[j].real, sz[j].real]))
    sphere.make_sphere()
    return sphere


# def init():
#     sphere.vector_color = ['b']
#     return ax


ani = animation.FuncAnimation(fig, animate, np.arange(t_length),
                              interval = 25, repeat=False, blit=False)

sphere.show()

