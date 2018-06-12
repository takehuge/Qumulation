import matplotlib
matplotlib.use('tkAgg')

from qutip import *
from scipy import *
from numpy import *
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Config Bloch Sphere
fig = plt.figure(figsize=(7, 7))
# azim: camera-right's deg from y-axis, elev: camera-up's deg from horizontal
ax = Axes3D(fig, azim=-25, elev=12)
sphere = Bloch(axes=ax)
sphere.frame_color = 'blue'
sphere.frame_width = 1.5
sphere.sphere_alpha = 0.17
sphere.sphere_color = 'yellow'
sphere.vector_width = 4.8
sphere.vector_color = 'red'
sphere.point_marker = 'o'

t_length = 101
rotrange = linspace(0, 100, t_length)
x=[]
y=[]
z=[]

# Y-axis Rotation
for j in rotrange:
    x.append(expect(sigmax(), ry(j * pi / 100, 1, 0) * basis(2, 0)))
    y.append(expect(sigmay(), ry(j * pi / 100, 1, 0) * basis(2, 0)))
    z.append(expect(sigmaz(), ry(j * pi / 100, 1, 0) * basis(2, 0)))

R = sqrt(array(x)**2 + array(y)**2 + array(z)**2)
print(R)

def animate(j):
    sphere.clear()
    sphere.add_vectors([x[j], y[j], z[j]])
    sphere.make_sphere()
    return sphere

# animation starts
ani = animation.FuncAnimation(fig, animate, arange(t_length),
                              interval=25, repeat=False, blit=False)
#Install FFMPEG using: brew install ffmpeg
# ani.save('RamseyOpflop.mp4', fps=15)

sphere.show()
