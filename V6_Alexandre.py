''''recherche d'une amélioration quant à la vitesse 
de la creation_d'''
from time import *
from math import sqrt
from random import randint


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

def creation_n(l):
    p=(l[randint(0,len(l)-1)])
    q=(l[randint(0,len(l)-1)])
    n=p*q
    return n,p,q

def phi(p,q):
    return (p-1)*(q-1)

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

def creation_d(e,f):
    for i in range(f):
        if (i*e)%f == 1:
            return i
            
#########################DIRECTIVES###########################
l = nombre_premier(10**5)
t = creation_n(l)
f = phi(t[1],t[2])
e = creation_e(f)
s = time()
d = creation_d(e,f)
print(time()-s)






    
    

                
                