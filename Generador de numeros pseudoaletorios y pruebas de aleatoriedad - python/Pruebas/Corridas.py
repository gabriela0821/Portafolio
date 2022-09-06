import math

def co_cont(lista):
    newl=[]
    cont=0
    for i in range(0,len(lista)+1):
        if(i==len(lista)):
            break
        if(i==0):
            newl.append(lista[i])
        else:
            if(lista[i]!=lista[i-1]):
                newl.append(lista[i])
    return len(newl)

def corridas(lista):
    corrida=[]
    n1=0
    n0=0
    for i in range(0, len(lista)):
        
        if(lista[i]<0.5):
            corrida.append(1)
            n1+=1
        else:
            corrida.append(0)
            n0+=1
            
    n=n0+n1
    c0=co_cont(corrida)
    #print("c0:",c0,"n0:",n0,"n1:",n1,"n:", n)
    
    u=((2*(n0)*(n1))/n)+(1/2)
    #print("u: ",u)
    alfa=((2*n0*n1)*(2*n0*n1-n))/((n**2)*(n-1))
    #print("alfa: ",alfa)
    z=(c0-u)/math.sqrt(alfa)
    #print("z: ",z)
        
    #z0.025=1.96
    zcond=1.96 
    
    if((zcond*-1)<=z or z>=zcond):
        print("Hipótesis Nula: La secuencia de números es independiente y por lo tanto la secuencia es aleatoria.")
    else:
        print("Hipótesis Alternativa: La secuencia de números No es Independiente y por lo tanto la secuencia No es aleatoria.")

lista=[0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 0.62, 0.36, 0.27,
       0.19, 0.72, 0.75, 0.09, 0.54, 0.2, 0.1, 0.36, 0.16, 0.28, 
       0.18, 0.1, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32, 0.82, 0.53, 
       0.31, 0.42, 0.73, 0.4, 0.83, 0.45, 0.13, 0.57, 0.63, 0.29]
corridas(lista)

