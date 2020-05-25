import matplotlib.pyplot as plt

fig = plt.figure()  # figsize=(4, 4)
ax = fig.add_subplot(111, projection='3d')

# Y é a lateral
# X é a frente
# Z é a altrura
# ax.bar3d(xpos, ypos, zpos, tam_fronte, tam_lateral, altura_barra, zsort='average')
ax.bar3d(1, 1, 1, 1, 2, 2, zsort='average')
ax.bar3d(3, 1, 1, 1, 2, 4, zsort='average')
ax.bar3d(5, 1, 1, 1, 2, 3, zsort='average')

# ax.set_zlim(-10, 10)
# ax.set_xlim(-10, 10)
ax.set_ylim(0, 10)

# ax = fig.add_axes(MyAxes3D(ax, 'l'))
# ax = fig.add_axes(MyAxes3D(ax, 'lr'))

# Coloca os ticks do z no canto direito
ax.zaxis._axinfo['juggled'] = (1, 2, 0)
# ax.xaxis._axinfo['juggled'] = (2,0,1)

# Remove os ticks do y na lateral esquerda
ax.yaxis.set_ticks([])

# Rotate the figure
ax.view_init(10, -95)
# for angle in range(0, 360):
#     ax.view_init(30, angle)
#     plt.draw()
#     plt.pause(.001)

plt.show()
