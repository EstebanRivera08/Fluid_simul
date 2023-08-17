
import matplotlib.pyplot as plt
import numpy as np

#Se leen los archivos .dat y se transfieren a un array

Pos = np.genfromtxt(r"C:\Users\Iconeus\Downloads\PythonWorkshops\data_pos.dat") #Datos de posición
Speed = np.genfromtxt(r"C:\Users\Iconeus\Downloads\PythonWorkshops\data_speed.dat") #Datos de rapidez
Vel = np.genfromtxt(r"C:\Users\Iconeus\Downloads\PythonWorkshops\data_vel.dat") #Datos de velocidad
Pv = np.genfromtxt(r"C:\Users\Iconeus\Downloads\PythonWorkshops\data_pv.dat") #Datos de presión y volumen

#Se extraen los componentes de las variables vectoriales, como:

#Posición
xP = Pos[:,0]
yP = Pos[:,1]
zP = Pos[:,2]

#Velocidad
Vx = Vel[:,0]
Vy = Vel[:,1]
Vz = Vel[:,2]

#Y se calculan las magnitudes de cada uno de los vectores
r = np.sqrt(xP**2 + yP**2 + zP**2)
V = np.sqrt(Vx**2 + Vy**2 + Vz**2)

#Para las magnitudes escalares como la magnitud de los vectores de posición
#Y los datos de la rapidez, se le calculan el promedio y desviación estandar

rprom = np.mean(r)
rstd = np.std(r)
Speedprom = np.mean(Speed)
Speedstd = np.std(Speed)

#Se imprimen en pantalla los resultados
print("La distancia promedio es: {:0.5}".format(rprom))
print("La desv. estándar de la distancia es: {:0.5}".format(rstd))
print("La rapidez promedio es: {:0.5}".format(Speedprom))

#Extraemos los datos de volumen y presión del gas
P = Pv[:,0]
V = Pv[:,1]

Pprom = np.mean(P)
Vprom = np.mean(V)
Work = np.trapz(V,P)
print("El valor promedio de la presión y volumen es {} y {} respectivamente".format(Pprom,Vprom))
print("El trabajo es integral(P(v)dv)$: {}".format(Work))


# Se empiezan a crear las diferentes figuras:

#Dispersión 3D de la posición
fig1 = plt.figure(figsize=(10, 7))
ax1 = plt.axes(projection="3d")

ax1.scatter3D(xP, yP, zP, color="green")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
plt.title("Position")


# Histograma de la magnitud de la posición
fig2 = plt.figure(figsize=(8, 5))
plt.hist(r, 50,
         histtype ='bar',edgecolor='black',
         facecolor = 'blue', alpha=0.5)
plt.xlabel('Magnitud de la posición, $\|r_i\|$')
plt.ylabel('Frecuencia')
plt.title("$\mu_r$ = {:.3} y  $\sigma_r$ = {:.3}".format(rprom,rstd))


#Campo de vectores de la velocidad de cada partícula
fig3 = plt.figure(figsize=(10, 7))
ax2 = plt.axes(projection="3d")

ax2.quiver(xP,yP,zP,Vx,Vy,Vz,color='blue',length=0.1)
ax2.scatter3D(xP, yP, zP, color="black")
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
plt.title("Vectores de velocidad")

#Histograma de la rapidez de las particulas
fig4 = plt.figure(figsize=(8, 5))
Kb = 1.380648e-23 # J/K
m = 1.2e-20 #kg
T = 500 # K
dv = 2 # m/s
Np = 100
v = np.linspace(0,3,500)

f = lambda v: 4*np.pi*Np*v**2*(m/(2*np.pi*Kb*T))**(3/2)*np.exp(-m*v**2/(2*Kb*T))*dv #Función de frecuencia de Maxwell-Botlzman
plt.hist(Speed,edgecolor='black',
         facecolor = 'green', alpha=0.5)
plt.plot(v,f(v),'r')
plt.xlabel('Rapidez, $\|v_i\|$')
plt.ylabel('Frecuencia')
plt.title("$\mu_v$ = {:.4} y  $\sigma_v$ = {:.3}".format(Speedprom,Speedstd))



# show plot
plt.show()
