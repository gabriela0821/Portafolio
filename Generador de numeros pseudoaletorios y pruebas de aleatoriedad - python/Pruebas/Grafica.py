import math
from scipy import stats
from scipy.stats import chi2
import matplotlib.pyplot as plt
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

def prueba_grafica(lista):
    fig=plt.figure()
    aux=fig.add_subplot(111)
    res=stats.probplot(lista, dist=stats.uniform, sparams=(6,), plot=aux)
    plt.show()
    
    
lista=[0.733,0.339,0.123,0.953,0.405]
prueba_grafica(lista)

