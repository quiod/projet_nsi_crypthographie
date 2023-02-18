#fonction nombre premier et tests dessus

from time import *
from math import sqrt

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


                
                