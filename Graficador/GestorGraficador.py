import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, 10, 100)
v = np.linspace(-2 * np.pi, 2 * np.pi, 100)

funcion_x = "10*np.outer(np.sqrt(u), np.cos(v))"
funcion_y = "5*np.outer(np.sqrt(u), np.sin(v))"
funcion_z = "np.outer(np.ones(np.size(u)), u)"
r=2
def parametroX(funcion_x):
    x = eval(funcion_x)
    return x

def parametroY(funcion_y):
    y = eval(funcion_y)
    return y

def parametroZ(funcion_z):
    z = eval(funcion_z)
    return z

x= parametroX(funcion_x)
y= parametroY(funcion_y)
z= parametroZ(funcion_z)

ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b')
plt.show()