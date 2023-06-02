import numpy as np

# M=np.loadtxt('macierza.txt')
# d=np.loadtxt('wyniki.txt')
# n=M.shape[0]

# def gauss(A,b):
#     C=np.zeros((n,n+1))
#     C[:,0:n]=A
#     C[:,n]=b
#     x=np.zeros(n)
#     for s in range(0, n-1):
#         for i in range(s+1, n):
#             # L = A[i,s] / A[s,s]
#             for j in range(s+1, n+1):
#                 C[i,j] = C[i,j] - (C[i,s] / C[s,s]) * C[s,j]
#     x[n-1] = C[n-1,n]/C[n-1,n-1]
#     for i in range(n-2,-1,-1):
#         suma = 0.0
#         for s in range(i+1, n):
#             suma = suma + C[i,s] * x[s]
#         x[i] = (C[i,n] - suma) / C[i,i]
#     return x

# print('G:',gauss(M,d))
# print('S:',np.linalg.solve(M,d))

B=np.loadtxt('macierzb.txt')
c=np.loadtxt('wynikib.txt')

def thomas(M,d):
    m=M.shape[0]
    a=np.zeros(m)
    b=np.zeros(m)
    c=np.zeros(m)
    x=np.zeros(m)
    gam=np.zeros(m)
    bet=np.zeros(m)
    for i in range(m):
        b[i]=M[i,i]
        if i>0:
            a[i]=M[i][i-1]
        if i<m-1:
            c[i]=M[i][i+1]
    bet[0]=(-c[0]/b[0])
    gam[0]=d[0]/b[0]

    for i in range(1,m):
        bet[i]=(-c[i]/(a[i]*bet[i-1]+b[i]))
        gam[i]=(d[i]-a[i]*gam[i-1])/(a[i]*bet[i-1]+b[i])

    x[m-1]=gam[m-1]
    for i in range(m-2,-1,-1):
        x[i]=bet[i]*x[i+1]+gam[i]
    
    return x

print('G:',thomas(B,c))
print('S:',np.linalg.solve(B,c))