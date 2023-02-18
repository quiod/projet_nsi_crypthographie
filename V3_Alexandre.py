#fonction de la creation de e, reflexions sur les variables à conserver
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

def creation_n():
    l=nombre_premier(10**5)
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
        

    
    

                
                