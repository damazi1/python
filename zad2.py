import numpy as np
mE=np.loadtxt('macierze.txt')
# print(mE)

def odwrotna(E):
    A=np.zeros(E.shape)
    A[:,:]=E
    n=A.shape[0]
    B=np.zeros((n,2*n))
    C=np.eye(n,dtype=int)
    for i in range(n):
        for j in range(n):
            B[i][j]=A[i][j]
    for i in range(n):
        for j in range(n+1,2*n):
            B[i][j]=0
    for i in range(n):
        B[i][i+n]=1
    print(B)
    for s in range(n):
        c=B[s][s]
        B[s][s]=B[s][s]-1
        for j in range(s+1,n*2):
            d=B[s][j]/c
            for i in range(n):
                B[i][j]=B[i][j]-d*B[i][s]
    for i in range(n):
        for j in range(n,2*n):
            A[i-n][j-n]=B[i][j]
    return A
    
W=np.linalg.inv(mE)
print (np.around(np.dot(mE,odwrotna(mE)),10))