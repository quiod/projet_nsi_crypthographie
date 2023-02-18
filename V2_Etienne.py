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
    l=nombre_premier(10**5)
    p=(l[randint(0,len(l)-1)])
    q=(l[randint(0,len(l)-1)])
    n=p*q
    return n,p,q
        
    