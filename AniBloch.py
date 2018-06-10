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
ax = Axes3D(fig, azim=-80, elev=20)
sphere = Bloch(axes=ax)
# b3d = Bloch3d()
anisphere = Bloch(axes=ax)
t_length = [37,100]

#POINTS
pnt = [1 / np.sqrt(3), 1 / np.sqrt(3), 1 / np.sqrt(3)]
vec = [0, 1, 0]
up = basis(2, 0)
#x, y z up states
x = (basis(2, 0) + (1 + 0j) * basis(2, 1)).unit() # |0> + |1>
y = (basis(2, 0) + (0 + 1j) * basis(2, 1)).unit() # |0> + j|1>
z = (basis(2, 0) + (0 + 0j) * basis(2, 1)).unit() # |0> + 0|1>
# dots
phi = 0.0 * pi
xp = [np.cos(phi) * sin(th) for th in np.linspace(0, 0.5 * pi, t_length[0])]
yp = [np.sin(phi)*sin(th) for th in np.linspace(0, 0.5 * pi, t_length[0])]
zp = [np.cos(th) for th in np.linspace(0, 0.5 * pi, t_length[0])]
pnts = [xp, yp, zp]

sphere.add_points(pnt)
sphere.add_points(pnts)
sphere.add_vectors(vec)
sphere.add_states(up)
sphere.add_states([x, y, z])

# anisphere.add_states([x, y, z])

def animate(j):
    anisphere.clear()
    # anisphere.add_points(np.array([xp[:j+1],yp[:j+1],zp[:j+1]]))
    anisphere.add_vectors(np.array([xp[j], yp[j], zp[j]]))
    anisphere.make_sphere()
    return anisphere

# animation starts
ani = animation.FuncAnimation(fig, animate, np.arange(t_length[0]),
                              interval=25, repeat=False, blit=False)
#Install FFMPEG using: brew install ffmpeg
# ani.save('Redfield.mp4', fps=15)

anisphere.show()
