#ajout de fonction lancement+fonction creation de d 
from math import *
from random import *

for d in range(520):
    if (3*d)%520==1:
        print(d)

    
def nombre_premier(n):
    l = [2]
    v = False
    for i in range(n):
        for j in range(2,int(sqrt(i)+1)):
            v = True
            if i%j == 0:
                v = False
                break
        if v == True:
            l.append(i)
    return l
                
def creation_n():
    l=nombre_premier(10**3)
    p=(l[randint(0,len(l)-1)])
    q=(l[randint(0,len(l)-1)])
    n=p*q
    return n,p,q

def phi(p,q):
    return (p-1)*(q-1)

def creation_e():
    a = creation_n()
    p = phi(a[1],a[2])
    for i in range(2,p):
        if p%i != 0:
            return i
def creation_d(p,e):
    for d in range(p):
        if (e*d)%p==1:
            return d

    

##########################directive######################################


n=creation_n()
p=phi(n[1],n[2])
e=creation_e()
d=creation_d(p,e)



        














    