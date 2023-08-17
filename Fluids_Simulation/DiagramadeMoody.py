import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative as df


#Regimén laminar
Re_laminar = np.linspace(600,3000,10)
f_laminar = 64/Re_laminar

#Regimén Turbulento
Re_turb = np.logspace(3.55,8,200)[np.newaxis]

def Ec_Colebrook_White(f,Re,e_D) :
    return 1/np.sqrt(f)+2*np.log10(e_D/3.71 + 2.51/(Re*np.sqrt(f)))
x = [1,1,1,1]
e_D =np.array([[1e-7,1e-6,1e-5,5e-5,1e-4,2e-4,4e-4,6e-4,1e-3,2e-3,4e-3,6e-3,1e-2,2e-2,3e-2,5e-2]])
f_turb = np.zeros((Re_turb.shape[1],e_D.shape[1]))

def nw(f,x0) :

    k = 0
    Tol = 1e-10
    IterMax = 1000

    if df(f,x0)==0 :
        print('La función no es diferenciable en el punto ingresado. \n')
    else :
        criteria =10

        while criteria>=Tol and k<IterMax :
            if np.abs(df(f,x0,dx=0.000001)) < 1e-5 :
                print("La derivada en el punto es cercana a cero, se detiene.")
                break
            else :
                k = k + 1
                x1 = x0 - f(x0)/df(f,x0,dx=1e-10)
                x = x0
                x0 = x1

                criteria = np.abs(f(x0))


    return x0

for j in range(e_D.shape[1]) :
    for i in range(Re_turb.shape[1]) :
        a = Re_turb[0,i]
        b = e_D[0,j]
        f = 0.001
        f_turb[i,j] = nw(lambda f: Ec_Colebrook_White(f,a,b),0.01)


plt.figure(figsize=(12,7))
plt.loglog(Re_laminar,f_laminar,'k',linewidth=0.7)
for j in range(e_D.shape[1]) :
    plt.loglog(Re_turb[0,:],f_turb[:,j],'k',linewidth=0.7)
    plt.text(1e8,f_turb[-1,j],"$\\varepsilon$/D = {}".format(e_D[0,j]))

plt.text(8e2,3e-2,"f = 64/Re")
plt.axis('tight')
plt.xlabel("Número de Reynolds (Re=$\\rho$VD/$\\mu$)")
plt.ylabel("Factor de fricción de Fanning, f")
plt.title("Diagrama de Moody")
plt.axis([600, 1e8, 0.006, 0.1])
plt.grid(True,which='both', color='gray', linestyle='-', linewidth=1, alpha=0.4)
plt.show()

