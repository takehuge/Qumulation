# To illustrate Ramsey operation by figuratively moving around bloch sphere
# with spherical coordinates

import matplotlib
matplotlib.use('tkAgg')

from qutip import *
from scipy import *
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Config Bloch Sphere
fig = plt.figure(figsize=(7, 7))
ax = Axes3D(fig, azim=-25, elev=12) #azim: camera-right's deg from y-axis, elev: camera-up's deg from horizontal
sphere = Bloch(axes=ax)
anisphere = Bloch(axes=ax)
anisphere.frame_color = 'blue'
anisphere.frame_width = 1.5
anisphere.sphere_alpha = 0.17
anisphere.sphere_color = 'yellow'
anisphere.vector_width = 4.8
anisphere.vector_color = 'red'
anisphere.point_marker = 'o'

turns = 10.8/8
delay = int(np.ceil(turns * 2*30))
t_length = [35,delay,35]

# Y-rotation for pi/2
xp = [sin(th) for th in np.linspace(0, 0.5 * pi, t_length[0])]
yp = np.zeros(t_length[0])
zp = [cos(th) for th in np.linspace(0, 0.5 * pi, t_length[0])]
pnts = [xp, yp, zp]

# Free precession for a duration of time called delay
xq = [cos(phi) for phi in np.linspace(0, t_length[1] * pi / 30, t_length[1])]
yq = [sin(phi) for phi in np.linspace(0, t_length[1] * pi / 30, t_length[1])]
zq = np.zeros(t_length[1])

# Y-rotation again for pi/2
xr = [cos(t_length[1] * pi / 30) * cos(-rot)
      for rot in np.linspace(0, 0.5 * pi, t_length[2])]
yr = sin(t_length[1] * pi / 30) * np.ones(t_length[2])
zr = [cos(t_length[1] * pi / 30) * sin(-rot)
      for rot in np.linspace(0, 0.5 * pi, t_length[2])]

X = np.concatenate((xp, xq, xr))
Y = np.concatenate((yp, yq, yr))
Z = np.concatenate((zp, zq, zr))

def animate(j):
    anisphere.clear()
    if j < t_length[0]:
        anisphere.add_points(
            np.array([X[:j + 1], Y[:j + 1], Z[:j + 1]]))
        anisphere.point_color = ['red']
    elif t_length[0] <= j < sum(t_length[0:2]):
        anisphere.add_points(
            np.array([X[0:t_length[0]], Y[:j + 1], Z[:j + 1]]))
        anisphere.add_points(
            np.array([X[t_length[0]:j + 1], Y[t_length[0]:j + 1], Z[t_length[0]:j + 1]]))
        anisphere.point_color = ['red', 'green']
    else: 
        anisphere.add_points(
            np.array([X[0:t_length[0]], Y[:j + 1], Z[:j + 1]]))
        anisphere.add_points(
            np.array([X[t_length[0]:sum(t_length[0:2])], Y[t_length[0]:sum(t_length[0:2])], Z[t_length[0]:sum(t_length[0:2])]]))
        anisphere.add_points(
            np.array([X[sum(t_length[0:2]):j + 1], Y[sum(t_length[0:2]):j + 1], Z[sum(t_length[0:2]):j + 1]]))
        anisphere.point_color = ['red', 'green', 'blue']
    anisphere.add_vectors(np.array([X[j], Y[j], Z[j]]))
    anisphere.make_sphere()
    return anisphere

# animation starts
ani = animation.FuncAnimation(fig, animate, np.arange(sum(t_length)),
                              interval=25, repeat=False, blit=False)
#Install FFMPEG using: brew install ffmpeg
ani.save('RamseyOpflop.mp4', fps=15)

anisphere.show()
