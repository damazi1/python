import numpy as np
import matplotlib.pyplot as plt
h=0.3
n=5


def poch(x,y):
    return 1.1*x+0.8*y
def uzup1(h,n):
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    x[0]=-0.1
    y[0]=0.3
    for i in range(0,n+1,1):
        x[i] = x[0]+i*h
    for i in range(0,n,1):
        y[i+1] = y[i]+h*poch(x[i],y[i]) 
    return x,y

x1,y1=uzup1(h,n)

def uzup2(h,n):
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    x[0]=-0.1
    y[0]=0.3
    for i in range (1,n+1):
        x[i]=x[0]+i*h
    for i in range (0,n):
        x1= 0.5*(x[i]+x[i+1])
        y1= y[i]+0.5*h*poch(x[i],y[i])
        m=poch(x1,y1)
        y[i+1]=y[i]+h*m
    return x,y

x2,y2=uzup2(h,n)

def uzup3(h,n):
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    x[0]=-0.1
    y[0]=0.3
    for i in range (1,n+1):
        x[i]=x[0]+i*h
    for i in range(0,n):
        m1=poch(x[i],y[i])
        m2=poch(x[i]+0.5*h,y[i]+0.5*h*m1)
        m3=poch(x[i]+h,y[i]-h*m1+2*h*m2)
        y[i+1]=y[i]+(h*(m1+4*m2+m3))/6
    return x,y

x3,y3=uzup3(h,n)

plt.plot(x1,y1,'blue',label="Prosta metoda eulera")
plt.plot(x2,y2,'red',label="Ulepszona metoda eulera")
plt.plot(x3,y3,'black',label="metoda rungego kutty")
plt.xlabel("oś x")
plt.ylabel("oś y")
plt.legend()
plt.show()