import math
import scipy.stats
from scipy.stats import chi2

def varianza(lista):
    alfa=0.025
    suma= 0
    lisl = len(lista)
    promedio = 0

    for i in lista:
        sumapseudo=(suma+i)
    for j in lista:
        promedio+=((j-(sum(lista)/len(lista)))**2)
        
    vf=promedio/lisl
    n=len(lista)-1

    li=(scipy.stats.chi2.ppf(alfa, n)) / (12*(n))
    ls=(scipy.stats.chi2.ppf(1-alfa, n)) / (12*(n))
    
    if (li<=vf<=ls):
        print("Es una Secuencia de Números Pseudoaleatorios")
        print("limite inferior:", li, " , varianza:", vf," , limite superior:", ls)
    else:
        print("limite inferior:", li, " , varianza:", vf," , limite superior:", ls)


lista=[0.6353,0.9887,0.8121,0.2923,0.7376]
varianza(lista)
