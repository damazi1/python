import numpy as np

M=np.loadtxt('macierza.txt')
d=np.loadtxt('wyniki.txt')
n=M.shape[0]

def gauss(A,b):
    C=np.zeros((n,n+1))
    C[:,0:n]=A
    C[:,n]=b
    x=np.zeros(n)
    for s in range(0, n-1):
        for i in range(s+1, n):
            # L = A[i,s] / A[s,s]
            for j in range(s+1, n+1):
                C[i,j] = C[i,j] - (C[i,s] / C[s,s]) * C[s,j]
    x[n-1] = C[n-1,n]/C[n-1,n-1]
    for i in range(n-2,-1,-1):
        suma = 0.0
        for s in range(i+1, n):
            suma = suma + C[i,s] * x[s]
        x[i] = (C[i,n] - suma) / C[i,i]
    return x

print('G:',gauss(M,d))
print('S:',np.linalg.solve(M,d))


