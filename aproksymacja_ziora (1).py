import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
mA=np.loadtxt("macierza.txt")
mB=np.loadtxt("macierzb.txt")

n=mA.shape[0]

xN=np.linspace(0,10,20)

M=np.zeros((2,2))
P=np.zeros (2)

M[0][0]=n
for i in range (n):
    M[0][1]=M[1][0]+mA[i]
    M[1][0]=M[1][0]+mA[i]
    M[1][1]=M[1][1]+mA[i]**2

print (M)


for i in range (n):
    P[0]=P[0]+mB[i]
    P[1]=P[1]+mA[i]*mB[i]

print (P)

K=np.linalg.solve(M,P)

print (K)

def f(x,a1,a0):
    return a1*x+a0

plt.plot(xN,f(xN,K[1],K[0]),'g-',label='Wykres aproksymacji liniowej')
plt.plot(mA,mB,'ro',label='Punkty')
plt.legend()
plt.title('Wykres aproksymacji liniowej', fontdict={'fontname': 'monospace', 'fontsize': 18})
plt.xlabel('Oś X')
plt.ylabel('Oś Y')

M1=np.zeros((3,3))
P1=np.zeros (3)

M1[0,0]=n
for i in range (n):
    M1[0,1]=M1[0,1]+mA[i]
    M1[0,2]=M1[0,2]+mA[i]**2
    M1[1,0]=M1[1,0]+mA[i]
    M1[1,1]=M1[1,1]+mA[i]**2
    M1[1,2]=M1[1,2]+mA[i]**3
    M1[2,0]=M1[2,0]+mA[i]**2
    M1[2,1]=M1[2,1]+mA[i]**3
    M1[2,2]=M1[2,2]+mA[i]**4

for i in range (n):
    P1[0]+=mB[i]
    P1[1]+=mA[i]*mB[i]
    P1[2]+=(mA[i]**2)*mB[i]

print (M1)
print (P1)

K1=np.linalg.solve(M1,P1)

print (K1)

def f1(a0,a1,a2,x):
    return a0+a1*x+a2*x**2
plt.plot(xN,f1(K1[0],K1[1],K1[2],xN),'b-',label='Wykres aproksymacji kwadratowej')
plt.legend()
plt.show()