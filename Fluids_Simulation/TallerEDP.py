import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import rc

rc('animation', html='jshtml')

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [],'k', lw=0.7)
plt.xlabel('x, in')
plt.ylabel('y, in')
plt.grid('minor')

def init():
  ax.set_xlim(0, 4)
  ax.set_ylim(-1, 1)
  return ln,

def animate(t):
  x = np.linspace(0, 4, 50)
  y = np.sin(np.pi*x)/np.pi**2 * (1-np.cos(np.pi*t)) #DEBE IGUALAR Y A SOLUCI´ON u(x,t) OBTENIDA
  ln.set_data(x, y)
  return ln,

anim = animation.FuncAnimation(fig, animate,init_func=init,frames=np.linspace(0, 60, 100))
writergif = animation.PillowWriter(fps=6)
anim.save('basic_animation.gif', writer=writergif)
plt.show()
