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
anisphere = Bloch(axes=ax)
t_length = [12,24,80]

# Y-rotation for pi/2
phi = 0.0 * pi
xp = [np.cos(phi) * sin(th) for th in np.linspace(0, 0.5 * pi, t_length[0])]
yp = [np.sin(phi)*sin(th) for th in np.linspace(0, 0.5 * pi, t_length[0])]
zp = [np.cos(th) for th in np.linspace(0, 0.5 * pi, t_length[0])]
pnts = [xp, yp, zp]

th = 0.0*pi
xq = [cos(phi) for phi in np.linspace(0, 0.7*pi, t_length[1])]
yq = [sin(phi) for phi in np.linspace(0, 0.7*pi, t_length[1])]
zq = np.zeros(t_length[1])

xr = [cos(0.7 * pi)*cos(rot) for rot in np.linspace(0, 2*pi, t_length[2])]
yr = sin(0.7 * pi)*np.ones(t_length[2])
zr = [cos(0.7 * pi) * sin(rot) for rot in np.linspace(0, 2 * pi, t_length[2])]

X = np.concatenate((xp,xq, xr))
Y = np.concatenate((yp, yq, yr))
Z = np.concatenate((zp, zq, zr))

def animate(j):
    anisphere.clear()
    if j <= sum(t_length[0:2]):
        anisphere.add_vectors(np.array([X[j], Y[j], Z[j]]))
    else:
        anisphere.add_points(
            np.array([X[sum(t_length[0:2]):j + 1], Y[sum(t_length[0:2]):j + 1], Z[sum(t_length[0:2]):j + 1]]))
        anisphere.add_vectors(np.array([X[j], Y[j], Z[j]]))
    anisphere.make_sphere()
    return anisphere

# animation starts
ani = animation.FuncAnimation(fig, animate, np.arange(sum(t_length)),
                              interval=25, repeat=False, blit=False)
#Install FFMPEG using: brew install ffmpeg
# ani.save('RamseyOp.mp4', fps=15)

anisphere.show()
