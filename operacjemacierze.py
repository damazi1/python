import numpy as np

mA= np.loadtxt('macierza.txt')
mB=np.loadtxt('macierzb.txt')

# print ('\n Macierz a', mA)
# print (mA.shape)
# print (mA.size)
# print ('liczba wierszy',mA.shape[0])
# print ('liczba kolumn', mA.shape[1])

# if (mA.shape==mB.shape):
#     if (mA.size==mB.size):
#         mC=mA+mB
# print ('Suma A+B =', mC)


def max(t):
    maxi=mA[0,0]
    for i in range (mA.shape[0]):
        for j in range (mA.shape[1]):      
            if maxi<mA[i,j]:
                maxi=mA[i,j]
    return maxi
print (max(mA))


def srednia(t):
    srd=0
    for i in range (mA.shape[0]):
        for j in range (mA.shape[1]):
            srd=srd+mA[i,j]
    return (srd/mA.size)
print (srednia(mA))

def mediana(t):
    med=0
    mA1D=np.reshape(mA,mA.size)
    mA1D.sort()
    print(mA1D)
    if mA.size%2==0:
        med=mA1D[mA.size/2]
    else:
        med=mA1D[int(mA.size/2)]+mA1D[int(mA.size/2)+1]
    return med
print (mediana(mA))    