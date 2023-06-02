import numpy as np
import matplotlib.pyplot as plt


a=-6.704
b=2.244
m=[1,2,3,4,5,6,7,10,15,20,30,50]
E=np.zeros((4,len(m)))
print (m)
def f(x):
    wynik=41*x*x+20*x-88
    return wynik
def fp(x):
    return 82*x+20

def ribisekcja(a,b,m):
    y=np.zeros(m)
    x = np.zeros(m)
    for i in range(m):
        x[i]=(a+b)/2
        y[i]=x[i]
        if f(x[i])==0:
            return x[i]
        elif f(a) *f(x[i])<0:
            b=x[i]
        elif f(a) *f(x[i])>0:
            a=x[i]
    return x[m-1]
for i in range (len(m)):
    print ("Metoda Bisekcji: \n",ribisekcja(a,b,m[i]),"\n Po odjęciu: ",1.7291060826964222+ribisekcja(a,b,m[i]))
    E[0,i]=round((((ribisekcja(a,b,m[i]))-(-1.7291060826964222))/(-1.7291060826964222))*100,2)

def cieciw (a,b,m):
    x=np.zeros(m)
    x[0]=a-((f(a))/(f(b)-f(a)))*(b-a)
    for i in range (m-1):
        x[i+1]=x[i]-((f(x[i]))/(f(b)-f(x[i])))*(b-x[i])
    return x[m-1]
for i in range (len(m)):
    print ("\nMetoda cieciw: \n",cieciw(b,a,m[i]),"\nRóżnica wyników",1.7291060826964222+cieciw(b,a,m[i]))
    E[1,i]=round(((cieciw(b,a,m[i])-(-1.7291060826964222))/(-1.7291060826964222))*100,2)

def newton(a,b,m):
    x=np.zeros(m)
    x[0]=a
    for i in range (0,m-1):
        x[i+1]=x[i]-(f(x[i])/fp(x[i]))
    return x[m-1]
for i in range (len(m)):
    print ("\nMetoda Newtona: \n",newton(a,b,m[i]),"\nRóżnica wyników",1.7291060826964222+newton(a,b,m[i]))
    E[2,i]=round(((newton(a,b,m[i])-(-1.7291060826964222))/(-1.7291060826964222))*100,2)

def newton_rapsona(a,b,m):
    x=np.zeros(m)
    x[0]=a
    for i in range (0,m-1):
        x[i+1]=x[i]-(f(x[i])/fp(x[0]))
    return x[m-1]
for i in range (len(m)):
    print ("\nMetoda Newtona_Rapsona: \n",newton_rapsona(a,b,m[i]),"\nRóżnica wyników",1.7291060826964222+newton_rapsona(a,b,m[i]))
    E[3,i]=round(((newton_rapsona(a,b,m[i])-(-1.7291060826964222))/(-1.7291060826964222))*100,2)

print("m\t1\t2\t3\t\t4")
for i in range(len(m)):
    print(m[i],'  ',E[0,i],'%  ',E[1,i],'%  ',E[2,i],'%  ',E[3,i],"%\n")

# x=np.linspace(a,b,100)
# y2=np.zeros(10)
# plt.plot(x,f(x),label="Parabola")
# plt.plot(y,y2,'ro',label='Punkty')
# plt.plot(a,0,'ro')
# plt.plot(b,0,'ro')
# plt.title('Wykres bisekcij', fontdict={'fontname': 'monospace', 'fontsize': 18})
# plt.xlabel('Oś X')
# plt.ylabel('Oś Y')
# plt.legend()
# plt.show()