import numpy as np
import matplotlib.pyplot as plt

#Parametros
U = 1  #[m/s]
a = 5  #[m]

#intervalos
x0 , xf = -15 , 15
y0 , yf = -15 , 15

#Creación de vectores
x = np.linspace(x0,xf,120)
y = np.linspace(y0,yf,120)

# x=rcost, y=rsent
# r=sqrt(x^2+y^2)
X,Y = np.meshgrid(x,y)
r = np.sqrt(X**2+Y**2)
t = np.arccos(X/r)

#Stream Line - Lineas de corriente
SL = np.zeros_like(X)

for j in range(X.shape[1]) :
    for i in range(X.shape[1]) :
        if r[i,j] > a :
            SL[i,j] = U*r[i,j]*(1-a**2/(r[i,j]**2))*np.sin(t[i,j])

#Lineas de corriente
#Serán los valores de X,Y para los cuales la Stream Line es constante
#O también se pueden
fig1 = plt.figure(figsize=(10,8))
fig1.subplots_adjust(hspace=0.3, wspace=0.3)
plt.subplot(221)
plt.contour(X, Y, SL,20,cmap='jet')
plt.colorbar()
plt.title('Lineas de corriente')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.axis([x0,xf,y0,yf])

Vx= U * (1 + a ** 2 / (r ** 4) * (Y**2-X**2))
Vy = -U * a ** 2 / (r ** (4)) * (X*Y)

for j in range(X.shape[1]) :
    for i in range(X.shape[1]) :
        if r[i,j] < a :
            Vx[i,j] = 0
            Vy[i,j] = 0

Campo_Velocidad = np.sqrt(Vx**2+Vy**2)


plt.subplot(223)
plt.contourf(X,Y,Campo_Velocidad,50, cmap='jet')
plt.colorbar()
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Campo de velocidad')
plt.axis([x0,xf,y0,yf])

plt.subplot(224)
plt.contourf(X,Y,Campo_Velocidad,50, cmap='jet')
plt.colorbar()
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Campo de velocidad y vectores')
plt.axis([x0,xf,y0,yf])

#Creación de vectores
x = np.linspace(x0,xf,30)
y = np.linspace(y0,yf,30)

# x=rcost, y=rsent
# r=sqrt(x^2+y^2)
X,Y = np.meshgrid(x,y)
r = np.sqrt(X**2+Y**2)
t = np.arccos(X/r)


#Campo de vectores
Vx= U * (1 + a ** 2 / (r ** 4) * (Y**2-X**2))
Vy = -U * a ** 2 / (r ** (4)) * (X*Y)

for j in range(X.shape[1]) :
    for i in range(X.shape[1]) :
        if r[i,j] < a :
            Vx[i,j] = 0
            Vy[i,j] = 0


ax = fig1.add_subplot(222)
ax.quiver(X,Y,Vx,Vy, angles='xy',scale_units='xy', scale=1)
plt.colorbar(cmap='hot')
ax.set_title('Campo de vectores')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
plt.axis([x0,xf,y0,yf])

ax = fig1.add_subplot(224)
ax.quiver(X,Y,Vx,Vy, angles='xy',scale_units='xy', scale=1)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
plt.axis([x0,xf,y0,yf])

plt.show()






