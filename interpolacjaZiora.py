import numpy as np

A = np.loadtxt('A.txt')
B = np.loadtxt('B.txt')





def itr_prosta (A,B):
    n = A.shape[0]
    D = np.zeros((n,n))
    R = np.zeros((n,n))
    X = np.zeros((11,n))
    for i in range (n):
        D[i][i]=1/A[i][i]

    for i in range (n):
        for j in range (n):
            if i != j:
                R[i][j]=A[i][j]

    M = np.dot(-D,R)
    P = np.dot(D,B)


    m=X.shape[0]-1
    for i in range (n-1):
        for k in range (m):
            X[k+1]=np.dot(M,X[k])+P

    print (X)

    ra=np.linalg.solve(A,B)-X[-1]

    print("Różnica wyników: \n",ra)
    return X[-1]

itr_prosta(A,B)

# def itr_gauss(A,B):
#     n = A.shape[0]
#     D = np.zeros((n,n))
#     R = np.zeros((n,n))
#     X = np.zeros((11,n))

#     for i in range (n):
#         D[i][i]=1/A[i][i]

#     for i in range (n):
#         for j in range (n):
#             if i != j:
#                 R[i][j]=A[i][j]

#     W = np.dot(-D,R)
#     Z = np.dot(D,B)
#     m = X.shape[0]-1

#     for k in range (m):
#         for j in range(1,n):
#             s=0
#             s+=W[0][j]*X[k][j]
#             X[k+1][0]=s+Z[0]
#     for k in range (m):
#         for i in range (n):
#             for j in range (n):
#                 for l in range (n-1):
#                     X[k+1][i]=W[i][j]*X[k+1][j]+W[i][l+1]*X[k][j]+Z[i]

#     print (X)

# itr_gauss(A,B)