''''élaboration de l'algorithme étendu de Euclide pour améliorer la vitesse de calcul de la clé de décryptage'''
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


def euclide(a,b):
    l1 = [a,1,0]
    l2 = [b,0,1]
    while l1[0] != pgcd(a,b):
        l1[1] = (l1[1]-(l1[0]//l2[0])*l2[1])
        l1[2] = (l1[2]-(l1[0]//l2[0])*l2[2])
        l1[0] = l1[0]%l2[0]
        l1,l2 = l2,l1
    return l1[1]

def creation_d(u,f):
    return u%f
    
    
            
#########################DIRECTIVES###########################
l = nombre_premier(10**5)
t = creation_n(l)
f = phi(t[1],t[2])
e = creation_e(f)
u = euclide(e,f)
d = creation_d(u,f)
