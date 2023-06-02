import numpy as np
import math
import matplotlib.pyplot as plt
mZ=np.loadtxt('macierzz.txt')

n=mZ.shape[0]
lp=2*n+1

def fun(x):
    return 1.3*x*x+1.59*x-1.57


x=np.zeros(lp)
y=np.zeros(lp)
for i in range(lp):
    x[i]=(2*i*np.pi)/lp
    y[i]=fun(x[i])


def interpol(lp,x):
    mM=np.zeros((lp,lp))
    for i in range(lp):
        mM[i][0]=1/math.sqrt(2)
        mM[i][1]=math.sin(x[i])
        mM[i][2]=math.cos(x[i])
        mM[i][3]=math.sin(2*x[i])
        mM[i][4]=math.cos(2*x[i])
        mM[i][5]=math.sin(3*x[i])
        mM[i][6]=math.cos(3*x[i])
    return mM
# print (interpol(lp,x))

a =np.linalg.solve(interpol(lp,x),y)
plt.plot(a,"-b",label="interpolacja")
plt.ylabel('oś Y')
plt.xlabel('oś X')
plt.show()
plt.legend(loc="upper left")
print (a)