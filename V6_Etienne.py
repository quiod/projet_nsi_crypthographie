#creation finaaaal de d avec l'optimisation des activité
from math import *
from random import *
  
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
    l=nombre_premier(10**4)
    p=(l[randint(0,len(l)-1)])
    q=(l[randint(0,len(l)-1)])
    n=p*q
    return n,p,q

def phi(p,q):
    return (p-1)*(q-1)
        
def creation_d(p,e):
    for d in range(p):
        if (e*d)%p==1:
            return d

def pgcd(a,b):
    if a == 0:
        return b
    else:
        return pgcd(b%a,a)
    
def creation_e(f):
    e = randint(2,f)
    if pgcd(e,f) == 1:
        return e
    return creation_e(f)


##########################directive######################################


n=creation_n()
f=phi(n[1],n[2])
e=creation_e(f)
d=creation_d(f,e)



        














    