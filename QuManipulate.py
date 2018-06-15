import matplotlib
matplotlib.use('tkAgg')

from qutip import *
from scipy import *
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Config Bloch Sphere
# azim: camera-right's deg from y-axis, elev: camera-up's deg from horizontal
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.set_aspect("equal")
sphere = Bloch(axes=ax, view=[-25,12]) # view=[azim,elev]
# sphere.frame_color = 'blue'
# sphere.frame_width = 1.5
# sphere.sphere_alpha = 0.17
# sphere.sphere_color = 'yellow'
sphere.vector_width = 4.8
sphere.vector_color = 'red'
sphere.point_marker = 'o'

# ax1 = fig.add_subplot(1, 2, 2, projection='3d')
# ax1.set_aspect("equal")
# sphere01 = Bloch(axes=ax1, view=[-25, 12])  # view=[azim,elev]
# sphere01.vector_width = 4.8
# sphere01.vector_color = 'red'
# sphere01.point_marker = 'o'

Inistate = snot(1)*basis(2,0)
t_length = 101
rotrange = linspace(0, 100, t_length)
rotrange2 = linspace(0, 100/2, int((t_length+1)/2))
x=[]
y=[] 
z=[]
x1=[]
y1=[]
z1=[]
x2 = []
y2 = []
z2 = []
xh = []
yh = []
zh = []
xH = []
yH = []
zH = []

# Y-axis Rotation
for j in rotrange:
    x.append(expect(sigmax(), ry(j * pi / 100, 1, 0) * Inistate))
    y.append(expect(sigmay(), ry(j * pi / 100, 1, 0) * Inistate))
    z.append(expect(sigmaz(), ry(j * pi / 100, 1, 0) * Inistate))

# X-axis Rotation
for j in rotrange:
    x1.append(expect(sigmax(), rx(j * pi / 100, 1, 0) * Inistate))
    y1.append(expect(sigmay(), rx(j * pi / 100, 1, 0) * Inistate))
    z1.append(expect(sigmaz(), rx(j * pi / 100, 1, 0) * Inistate))

# Z-axis Rotation
for j in rotrange:
    x2.append(expect(sigmax(), rz(j * pi / 100, 1, 0)
                     * ry(pi / 2, 1) * Inistate))
    y2.append(expect(sigmay(), rz(j * pi / 100, 1, 0)
                     * ry(pi / 2, 1) * Inistate))
    z2.append(expect(sigmaz(), rz(j * pi / 100, 1, 0)
                     * ry(pi / 2, 1) * Inistate))

# H Rotation
for j in rotrange:
    xh.append(expect(sigmax(), rx(j * -pi / 100, 1, 0) * Inistate))
    yh.append(expect(sigmay(), rx(j * -pi / 100, 1, 0) * Inistate))
    zh.append(expect(sigmaz(), rx(j * -pi / 100, 1, 0) * Inistate))
for j in rotrange2:
    xh.append(expect(sigmax(), ry(j * -pi / 100, 1, 0) * rx(pi, 1) * Inistate))
    yh.append(expect(sigmay(), ry(j * -pi / 100, 1, 0) * rx(pi, 1) * Inistate))
    zh.append(expect(sigmaz(), ry(j * -pi / 100, 1, 0) * rx(pi, 1) * Inistate))

# H-axis Rotation
for j in rotrange:
    xH.append(expect(sigmax(), ((rx(j * -pi / 100, 1, 0) +
                                 rz(j * -pi / 100, 1, 0)) * Inistate).unit()))
    yH.append(expect(sigmay(), ((rx(j * -pi / 100, 1, 0) +
                                 rz(j * -pi / 100, 1, 0)) * Inistate).unit()))
    zH.append(expect(sigmaz(), ((rx(j * -pi / 100, 1, 0) +
                                 rz(j * -pi / 100, 1, 0)) * Inistate).unit()))

R = sqrt(array(x)**2 + array(y)**2 + array(z)**2)
print(R)
R1 = sqrt(array(x1)**2 + array(y1)**2 + array(z1)**2)
print(R1)

def animate(j):
    sphere.clear()
    sphere.add_points([xh[:j+1], yh[:j+1], zh[:j+1]])
    sphere.add_vectors([xh[j], yh[j], zh[j]])
    sphere.make_sphere()
    # sphere01.clear()
    # sphere01.add_vectors([x1[j], y1[j], z1[j]])
    # sphere01.make_sphere()
    return sphere#, sphere01


# animation starts
ani = animation.FuncAnimation(fig, animate, arange(t_length) + int((t_length +1)/2),
                              interval=25, repeat=False, blit=False)
#Install FFMPEG using: brew install ffmpeg
ani.save('QubitsHback.mp4', fps=15)

plt.show()
