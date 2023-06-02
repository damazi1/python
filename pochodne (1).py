import numpy as np
import matplotlib.pyplot as plt

m=11
n=21
x=np.linspace(0,2,n)
y=np.linspace(0,1,m)
x,y=np.meshgrid(x,y)
z=np.zeros((m,n))
zx=np.zeros(n)
zxA=np.zeros((m,n))
zxB=np.zeros((m,n))

def f(x,y):
    return 2*x**2
def fx(x,y):
    return 4*x
def fyy(x,y):
    return 4

def wypz(z,x,y,zxA):
    for i in range (m):
        for j in range(n):
            z[i][j]=(f(x[i][j],y[i][j]))
            zxA[i][j]=fx(x[i][j],y[i][j])
            zxB[i][j]=fyy(x[i][j],y[i][j])

pz=z[3]
px=x[3]
def poch(zx,pz,px):
    for i in range (n):
        if(i==0):
            zx[i]=(pz[i+1]-pz[i])/(px[i+1]-px[i])
        elif(i==n-1):
            zx[i]=(pz[i]-pz[i-1])/(px[i]-px[i-1])
        else:
            zx[i]=(pz[i+1]-pz[i-1])/(px[i+1]-px[i-1])

wypz(z,x,y,zxA)
poch(zx,pz,px)

pzA=zxA[3]
Rpx=zx-pzA

zx1=np.zeros(n)
def poch2(zx1,zx,pz,px):
    for i in range (n):
        if(i==0):
            zx1[i]=(zx[i+1]-zx[i])/(px[i+1]-px[i])
        elif(i==n-1):
            zx1[i]=(zx[i]-zx[i-1])/(px[i]-px[i-1])
        else:
            zx1[i]=(pz[i-1]-2*pz[i]+pz[i+1])/((px[i]-px[i-1])*(px[i+1]-px[i]))

poch2(zx1,zx,pz,px)

pzB=zxB[3]
RRpx=zx1-pzB

print(Rpx,"\n",zx)

print(RRpx,"\n",zx1)

plt.plot(px,zx,'b',label="pochodna funkcji")
plt.plot(px,pzA,'--r',label="pochodna sprawdzenie ")
plt.plot(px,Rpx,'orange',label='roznica')
plt.legend()
plt.xlabel("oś x")
plt.ylabel("oś y")
plt.show()

plt.plot(px,zx1,'r',label="2 Pochodna funckji")
plt.plot(px,pzB,'--b',label="2 pochodna sprawdzenie")
plt.plot(px,RRpx,'orange',label='roznica')
plt.legend()
plt.xlabel("oś x")
plt.ylabel("oś y")
plt.show()