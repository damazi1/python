import numpy as np
import matplotlib.pyplot as plt


a=-3.704
b=-0.244
m=10
y=np.zeros(m)

def f(x):
    wynik=41*x*x+20*x-88
    return wynik

def ribisekcja(a,b,m,y):
    x = np.zeros(m)
    for i in range(m):
        x[i]=(a+b)/2
        y[i]=x[i]
        if f(x[i])==0:
            return x[i]
        elif f(a) *f(x[i])<0:
            b=x[i]
        elif f(a) *f(x[i])>0:
            a=x[i]
    return x[m-1]

print ("Metoda Bisekcji: \n",ribisekcja(a,b,m,y),"\n Po odjęciu: ",ribisekcja(a,b,m,y)+1.7291060826964222)

def cieciw (a,b,m):
    x=np.zeros(m)
    x[0]=a-((f(a))/(f(b)-f(a)))*(b-a)
    for i in range (m-1):
        x[i+1]=x[i]-((f(x[i]))/(f(b)-f(x[i])))*(b-x[i])
    return x[m-1]

print ("\nMetoda cieciw: \n",cieciw(b,a,m),"\nRóżnica wyników",1.7291060826964222+cieciw(b,a,m))

x=np.linspace(a,b,100)
y2=np.zeros(10)
plt.plot(x,f(x),label="Parabola")
plt.plot(y,y2,'ro',label='Punkty')
plt.plot(a,0,'ro')
plt.plot(b,0,'ro')
plt.title('Wykres bisekcij', fontdict={'fontname': 'monospace', 'fontsize': 18})
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.legend()
plt.show()