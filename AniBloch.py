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

sphere = Bloch(axes=ax)
# sphere.add_points(pnt)
sphere.add_points(pnts)
sphere.add_vectors(vec)
# sphere.add_states(up)
# sphere.add_states([x, y, z])
sphere.save(dirc='temp')

# anisphere = Bloch3d()
anisphere = Bloch(axes=ax)
# anisphere.add_states([x, y, z])
def animate(j):
    anisphere.clear()
    # anisphere.add_points([xp[j], yp[j], zp[j]])
    anisphere.add_vectors([xp[j], yp[j], zp[j]])
    # anisphere.save(dirc='temp') #saving images to temp directory in current working directory
    anisphere.make_sphere()
    return anisphere

def init():
    anisphere.vector_color = ['r']
    return ax

# animation starts
ani = animation.FuncAnimation(fig, animate, np.arange(t_length[0]),
                              init_func=init, interval=25, repeat=False, blit=False)
#Install FFMPEG using: brew install ffmpeg
ani.save('Redfield.mp4', fps=15)

# anisphere.show()
