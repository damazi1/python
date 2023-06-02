import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

a=-5.321
b=1.934
n=1
X=sp.symbols('x')

def f(x):
    return 12*x**3+5*x**2-9*x+12
def calkPa(a,b,n,cd):
    cp=0
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    h=(b-a)/n
    for i in range(n+1):
        x[i]=a+i*h
        y[i]=f(x[i])
    for i in range (n):
        cp+=h*y[i]
    if(((cp-cd)/cd)*100)<=0.1:
            print("Całka Pa dla n: ",n)
            return cp
    n+=100
    return calkPa(a,b,n,cd)

def calkTr(a,b,n,cd):
    cp=0
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    h=(b-a)/n
    for i in range(n+1):
        x[i]=a+i*h
        y[i]=f(x[i])
    for i in range (n):
        cp+=h*((y[i]+y[i+1])/2)
    if(((cp-cd)/cd)*100)<=0.1:
            print("Całka tr dla n: ",n)
            return cp
    n+=1
    return calkTr(a,b,n,cd)

def calkSa(a,b,n,cd):
    cp=0
    xs=0
    ys=0
    
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    h=(b-a)/n
    for i in range(n+1):
        x[i]=a+i*h
        y[i]=f(x[i])
    for i in range (n):
        xs=(x[i]+x[i+1])/2
        ys=(f(xs))
        cp+=h*((y[i]+y[i+1]+4*ys)/6)
    if(((cp-cd)/cd)*100)<=0.1:
        print("Całka Sa dla n: ",n)
        return cp
    n+=10
    return calkSa(a,b,n,cd)


cd = sp.integrate(f(X),(X,a,b))
cp=calkPa(a,b,n,cd)
ct=calkTr(a,b,n,cd)
cs=calkSa(a,b,n,cd)
E1=((ct-cd)/cd)*100

print (cd)
print(cp,"  ",ct,"  ",cs)

x=np.linspace(a,b,200)
plt.plot(f(x),'-b')
plt.xlabel("Oś X")
plt.ylabel("Oś Y")
plt.title("Wykres funkcji")
plt.show()
