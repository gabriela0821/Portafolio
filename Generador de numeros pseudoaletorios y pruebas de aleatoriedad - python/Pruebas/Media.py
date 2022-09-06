import statistics
from scipy.stats import norm
import math


def media(lista):

    media=statistics.mean(lista)
    alfa=norm.ppf(1-(0.05/2))
    
    li=(1/2)-(alfa)*(1 / (math.sqrt( 12* (len(lista))) ))
    ls=(1/2)+(alfa)*(1 / (math.sqrt( 12* (len(lista))) ))
    
    if (li<=media<=ls):
        print("Es una Secuencia de Números Pseudoaleatorios")
        print("limite inferior:", li, " , media:", media," , limite superior:", ls)
    else:
        print("No es una Secuencia de Números Pseudoaleatorios")
        print("limite inferior:", li, " , media:", media," , limite superior:", ls)
        
        
lista=[0.6353,0.9887,0.8121,0.2923,0.7376]
media(lista)
