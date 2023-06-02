import numpy as np

mA=np.loadtxt('macierza.txt')
mB=np.loadtxt('macierzb.txt')

def mnozenie(A,B):
    mC=np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for j in range (B.shape[1]):
            suma=0
            # print("suma= ",suma,end=' ')
            for s in range(A.shape[1]):
                suma +=A[i][s]*B[s][j]
                # print(A[i][s],'*',B[s][j],end=' ')
            # print('=',suma)
            mC[i][j]=suma
    return mC

# W=np.dot(mA,mB)
# print (W)

# print (mnozenie(mA,mB))

def odejmowanie(A,B):
    mC=A-B
    return mC
# print (odejmowanie(W,mnozenie(mA,mB)))

def wyznacznik(B):
    A=np.zeros(B.shape)
    A[:,:]=B
    det=A[0][0]
    for s in range(A.shape[1]-1):
        for i in range(s+1,A.shape[1]):
            for j in range(s+1,A.shape[1]):
                A[i][j]-=((A[i][s])/(A[s][s]))*A[s][j]
        det*=A[s+1][s+1]
    return det

W=np.linalg.det(mB)
print (W)
print (wyznacznik(mB))

print(odejmowanie(wyznacznik(mB),W))