import matplotlib
matplotlib.use('tkAgg')

from qutip import *
from scipy import linspace, pi
from numpy import array, mean, sqrt, arange

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm

# Config Bloch Sphere
# azim: camera-right's deg from y-axis, elev: camera-up's deg from horizontal
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection='3d')

# ax.set_aspect("equal") # NOT implemented in the latest Matplotlib

sphere = Bloch(axes=ax, view=[-25,12]) # view=[azim,elev]
# sphere.frame_color = 'blue'
# sphere.frame_width = 1.5
# sphere.sphere_alpha = 0.17
# sphere.sphere_color = 'yellow'

# ax1 = fig.add_subplot(1, 2, 2, projection='3d')
# ax1.set_aspect("equal")
# sphere01 = Bloch(axes=ax1, view=[-25, 12])  # view=[azim,elev]
# sphere01.vector_width = 4.8
# sphere01.vector_color = 'red'
# sphere01.point_marker = 'o'

t_length = 101
rotrange = linspace(0, 100, t_length)
rotrange2 = linspace(0, 100/2, int((t_length+1)/2))
x, y, z =[], [], []
x1, y1, z1 =[], [], []
x2, y2, z2 =[], [], []
xh, yh, zh =[], [], []
xhh, yhh, zhh =[], [], []
xH, yH, zH =[], [], []
xHH, yHH, zHH =[], [], []

# Y-axis Rotation
Inistate = basis(2, 0) #snot(1)*basis(2, 0)
for j in rotrange:
    x.append(expect(sigmax(), ry(j * pi / 100, 1, 0) * Inistate))
    y.append(expect(sigmay(), ry(j * pi / 100, 1, 0) * Inistate))
    z.append(expect(sigmaz(), ry(j * pi / 100, 1, 0) * Inistate))

# X-axis Rotation
Inistate = basis(2, 0) #snot(1)*basis(2, 0)
for j in rotrange:
    x1.append(expect(sigmax(), rx(j * pi / 100, 1, 0) * Inistate))
    y1.append(expect(sigmay(), rx(j * pi / 100, 1, 0) * Inistate))
    z1.append(expect(sigmaz(), rx(j * pi / 100, 1, 0) * Inistate))

# Z-axis Rotation
Inistate = basis(2, 0) #snot(1)*basis(2, 0)
for j in rotrange:
    x2.append(expect(sigmax(), rz(j * pi / 100, 1, 0)
                     * ry(pi / 2, 1) * Inistate))
    y2.append(expect(sigmay(), rz(j * pi / 100, 1, 0)
                     * ry(pi / 2, 1) * Inistate))
    z2.append(expect(sigmaz(), rz(j * pi / 100, 1, 0)
                     * ry(pi / 2, 1) * Inistate))

# H Rotation
Inistate = basis(2, 0) #snot(1)*basis(2, 0)
for j in rotrange:
    xh.append(expect(sigmax(), rx(j * -pi / 100, 1, 0) * Inistate))
    yh.append(expect(sigmay(), rx(j * -pi / 100, 1, 0) * Inistate))
    zh.append(expect(sigmaz(), rx(j * -pi / 100, 1, 0) * Inistate))
for j in rotrange2:
    xh.append(expect(sigmax(), ry(j * -pi / 100, 1, 0) * rx(-pi, 1) * Inistate))
    yh.append(expect(sigmay(), ry(j * -pi / 100, 1, 0) * rx(-pi, 1) * Inistate))
    zh.append(expect(sigmaz(), ry(j * -pi / 100, 1, 0) * rx(-pi, 1) * Inistate))

# 2nd H Rotation (back)
Inistate = ry(-pi / 2, 1) * rx(-pi, 1) * basis(2, 0)
for j in rotrange:
    xhh.append(expect(sigmax(), rx(j * -pi / 100, 1, 0) * Inistate))
    yhh.append(expect(sigmay(), rx(j * -pi / 100, 1, 0) * Inistate))
    zhh.append(expect(sigmaz(), rx(j * -pi / 100, 1, 0) * Inistate))
for j in rotrange2:
    xhh.append(expect(sigmax(), ry(j * -pi / 100, 1, 0) * rx(pi, 1) * Inistate))
    yhh.append(expect(sigmay(), ry(j * -pi / 100, 1, 0) * rx(pi, 1) * Inistate))
    zhh.append(expect(sigmaz(), ry(j * -pi / 100, 1, 0) * rx(pi, 1) * Inistate))

# H-axis Rotation
Inistate = basis(2, 0) #snot(1)*basis(2, 0)
for j in rotrange:
    xH.append(expect(sigmax(), ((rx(j * -pi / 100, 1, 0) +
                                 rz(j * -pi / 100, 1, 0)) * Inistate).unit()))
    yH.append(expect(sigmay(), ((rx(j * -pi / 100, 1, 0) +
                                 rz(j * -pi / 100, 1, 0)) * Inistate).unit()))
    zH.append(expect(sigmaz(), ((rx(j * -pi / 100, 1, 0) +
                                 rz(j * -pi / 100, 1, 0)) * Inistate).unit()))

# 2nd H-axis Rotation (back)
Inistate = ry(-pi / 2, 1) * rx(-pi, 1) * basis(2, 0)
for j in rotrange:
    xHH.append(expect(sigmax(), ((rx(j * -pi / 100, 1, 0) +
                                 rz(j * -pi / 100, 1, 0)) * Inistate).unit()))
    yHH.append(expect(sigmay(), ((rx(j * -pi / 100, 1, 0) +
                                 rz(j * -pi / 100, 1, 0)) * Inistate).unit()))
    zHH.append(expect(sigmaz(), ((rx(j * -pi / 100, 1, 0) +
                                 rz(j * -pi / 100, 1, 0)) * Inistate).unit()))

R = sqrt(array(x)**2 + array(y)**2 + array(z)**2)
print(R)
R1 = sqrt(array(x1)**2 + array(y1)**2 + array(z1)**2)
print(R1)

def animate(j):
    # Hadamard
    # sphere.clear()
    # sphere.add_points([xh[:j+1], yh[:j+1], zh[:j+1]])
    # sphere.add_vectors([xh[j], yh[j], zh[j]])
    # sphere.make_sphere()
    # 2nd Hadamard
    sphere.clear()
    sphere.add_points([xH[:j+1], yH[:j+1], zH[:j+1]])
    sphere.add_vectors([xH[j], yH[j], zH[j]])
    sphere.make_sphere()
    return sphere

def init():
    sphere.vector_width = 12
    sphere.vector_color = 'red'
    sphere.point_marker = 'o'
    sphere.font_size = 53
    return ax

# animation starts
framerange = arange(len(rotrange)) # for H-axis gate
# framerange = arange(len(rotrange) + len(rotrange2)) # for X, Y, Z gate
# framerange = arange(t_length) + int((t_length + 1)/2) # for Hback gate
ani = animation.FuncAnimation(fig, animate, framerange,
                              init_func=init, interval=25, repeat=False, blit=False)
#Install FFMPEG using: brew install ffmpeg
ani.save('QubitsH.mp4', fps=15)

# visually plotting out:
X, Y, Z = xhh, yhh, zhh
max_range = array([max(X)-min(X), max(Y)-min(Y), max(Z)-min(Z)]).max() / 2.0

mid_x = (max(X)+min(X)) * 0.5
mid_y = (max(Y)+min(Y)) * 0.5
mid_z = (max(Z)+min(Z)) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.show()
