import numpy as np

x=np.loadtxt('macierza.txt')
y=np.loadtxt('macierzb.txt')

n=x.shape[0]
h=x[1]-x[0]
m=np.zeros((n+2,n+2))
for i in range(1,n+1):
    m[i][i]=4
    m[i][i+1]=1
    m[i][i-1]=1
m[0][0]=-(3/h)
m[0][2]=3/h
m[n+1][n+1]=(3/h)
m[n+1][n-1]=-(3/h)
print ("zmienna M: ",np.round(m,3))

b=np.zeros(n+2)
b[n+1]=-1
for i in range(n):
    b[i+1]=y[i]
b[0]=1

print ("Zmienna b: ",b)

k=np.linalg.solve(m,b)

print (k)

k1=np.loadtxt('macierzk.txt')
n1=k.shape[0]
wynik=np.zeros(n1)

for i in range(n1):
    wynik[i]=k[i]-k1[i]

print(wynik)