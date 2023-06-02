import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

mX=np.loadtxt('macierzx.txt')
mY=np.loadtxt('macierzy.txt')

def lan(x,y):
    n=x.shape[0]
    d=np.zeros(n)
    d[0]=y[0]/((x[0]-x[1])*(x[0]-x[2]))
    d[1]=y[1]/((x[1]-x[0])*(x[1]-x[2]))
    d[2]=y[2]/((x[2]-x[0])*(x[2]-x[1]))

    a=d[0]+d[1]+d[2]
    b=d[0]*(-x[1]-x[2])+d[1]*(-x[0]-x[2])+d[2]*(-x[0]-x[1])
    c=d[0]*(-x[1]*(-x[2]))+d[1]*(-x[0]*(-x[2]))+d[2]*(-x[0]*(-x[1]))

    return(a,b,c)

print(lan(mX,mY))

# plt.figure()
# u = plt.plot(mX,mY,'ro') 
# t = np.linspace(0, 1, len(mX))
# # pxLagrange = scipy.interpolate.lagrange(t, mX) 
# # pyLagrange = scipy.interpolate.lagrange(t, mY) 
# n = 100
# ts = np.linspace(t[0],t[-1],n)
# xLagrange = pxLagrange(ts) 
# yLagrange = pyLagrange(ts) 
# plt.plot(xLagrange, yLagrange,'b-',label = "Wielomian")
# plt.legend()
# plt.show()
