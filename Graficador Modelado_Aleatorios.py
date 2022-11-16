# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 00:24:07 2022

@authors: Camilo Gomez y Gabriela Lara
"""

import math
from math import log
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns  
import tkinter as tk
from tkinter import ttk
from tkinter import *

print("SELECCIONE PRIMERO SU GENERADOR DE PREFERENCIA, Y LUEGO SU MÉTODO DE VARIABLES ALEATORIAS")

#GENERADORES DE NUMEROS ALEATORIOS

def middle(nump, nums):
    num_len_s=len(str(nums))
    num_len_p=len(str(nump))
    r1=int((num_len_s-num_len_p)/2)
    n=str(nums)
    num = n[r1:(r1+num_len_p)]
    return num


def Cuadrados_medios(seed, numa):
    lista=[]
    if len(str(seed))>3:
        for i in range(0,numa):
            pow2=int(seed)**2
            m=middle(seed,pow2)
            if(int(seed)==0 or int(m)==0 or m==seed):
                print("no se pueden generar más números")
                break
            else:
                lista.append(float("0."+m))
                seed=m  
    else:
        print("tiene que ingresar una seed con minimo 4 digitos")
        
    return lista


def Productos_medios(seed, numa):
    
    lista=[]
    seed1=seed
    seed2=seed+1
    
    if len(str(seed1))>3 and len(str(seed2))>3:
        
        for i in range(0,numa):
            prod=int(seed1)*int(seed2)
            m=middle(seed1,prod)
            
            if(int(seed1)==0 or int(seed2)==0 or int(m)==0 or m==seed2):
                print("no se pueden generar más números")
                break
            else:
                lista.append(float("0."+m))
                seed1=seed2
                seed2=m
                
    else:
        print("tiene que ingresar una seed con minimo 4 digitos")
        
    return lista


def Generador_Visual_Basic(seed,n):
    a=1140671485 #constante
    m=pow(2,24) #constante
    c=12820163 
    xi=seed
    aux= []
    for i in range(0, n):
        xi1=(a*xi+c)%m
        ri=xi1/(m-1)
        aux.append(ri)
        xi=xi1
    return aux

def Generador_Fortran(seed, n):
    a=630360016 #constante
    m=pow(2,31) #constante
    xi=seed
    aux= []
    for i in range(0, n):
        
        xi1=(a*xi)%(m-1)
        xii=xi1/((m-1)-1)
        aux.append(xii)
        xi=xi1
    return aux

def Generador_Congruencial_multiplicativo(seed,k,g,n):
    lista=[]
    g1=int(g)
    k1=int(k)
    if (seed%2!=0):
        m=2**g1
        a=5+(8*k1)
    
        for i in range(1,n+1):
            x=(a*seed)%m
            r=x/(m-1)
            lista.append(r)
            seed=x
            
        return lista
    else:
        print("La semilla debe ser un número impar")
        return 0
        


#GENERADORES DE VARIABLES ALEATORIAS

media=10
desviacion=2
grados=3
tasa=4
alpha=5 #5, antes 2
beta=2 #2


#D. Box Muller
def distribucion_normal_bm(lista1, lista2):
    
    aux= []
    d=desviacion
    
    for i in range(0, len(lista1)):
        
        #con coseno
        zi1 = math.sqrt((-2 * np.log10(lista1[i])))*(math.cos(2*math.pi*lista2[i]))
        
        #con seno
        zi2 = math.sqrt((-2 * np.log10(lista2[i])))*(math.sin(2*math.pi*lista1[i]))
        
        aux.append(media+d*zi2)
    
    return aux


#D. Log. Normal
def Distribucion_Log_Normal(lista1, lista2):
    
    lista=distribucion_normal_bm(lista1, lista2)
    xi=[]
    for i in range(0, len(lista)):
        xi.append(math.exp(lista[i]))
        
    return xi


#D. Chi Cuadrado
def Distribucion_Chi_Cuadrado(lista1, lista2, grados,sem,can):
    xi=[]
    listar=[]
    r=0
    
    for j in range(0, grados):
        r1 = Generador_Visual_Basic(sem,can)
        r2 = Generador_Visual_Basic((sem+1),can)
        
        ri=distribucion_normal_bm(r1, r2)
        listar.append(ri)
        r=len(ri) 
    
    for k in range(0, r):
        x=0
        for i in range(0, grados):
            
            x+=pow(listar[i][k],2)
        
        xi.append(x)
        
        
    return xi


#Distribucion T
def Distribucion_T(lista1, lista2, grados):
    
    ti=[]
    listar=[]
    r=0
    
    for j in range(0, grados):
        ri=distribucion_normal_bm(lista1, lista2)
        listar.append(ri)
        r=len(ri)
        
        
    for i in range(0,r):
        x = 0
        for k in range(1,grados):
            x += (listar[k][i])
    
        ti.append(listar[0][i] / math.sqrt( x/grados-1 ))
        
    return ti


#Distribucion F
def Distribucion_F(lista1, lista2, lista3, lista4, grado1, grado2, sem, can):
    
    fi=[]
    
    x1=Distribucion_Chi_Cuadrado(lista1, lista2, grado1, sem, can)
    x2=Distribucion_Chi_Cuadrado(lista3, lista4, grado2, sem+5, can)
    for i in range(0, len(x1)):
        
        
        fi.append(x2[i]/x1[i])
        
    return fi


#Distribucion Exponencial
def Distribucion_Exponencial(lista1,lista2):
    
    ei=[]
    z1 = distribucion_normal_bm(lista1, lista2)
    
    for i in range(0, len(z1)):
        
        ei.append((-1/tasa)*(np.log10(z1[i])))
        
    return ei


#Distribucion Gamma
def Distribucion_Gamma(lista1, lista2):
    
    dgi=[]
    teta=4.5
    
    #1
    a=1/math.sqrt(2*alpha-1)
    b=alpha-np.log10(4)
    q=alpha+(1/alpha)
    d=1+np.log10(teta)
    
    #3
    vi=[]
    zi=[]
    wi=[]
    yi=[]
    
    for i in range(0, len(lista1)):
        vi.append(a*(np.log10(lista1[i]/(1-lista1[i]))))
        zi.append((lista1[i]**2)*lista2[i])
        
    for j in range(0, len(lista1)):
        yi.append(alpha*math.exp(vi[j]))
        
    for h in range(0, len(lista1)):
        wi.append(b+q*vi[h]-yi[h])
        
    #4
    for k in range(0, len(lista1)):
        
        if((wi[k]+d-beta*zi[k])>0):
            dgi.append(yi[k]*beta)
        #5
        else:
            if(wi[k]>= np.log10(zi[k])):
                dgi.append(yi[k]*beta)

    return dgi


#Distribucion Directa
def Directa(lista1, lista2):
    listaaux = []
    for i in range(0, len(lista2)):
        zi= (math.sqrt(-2 * math.log(lista2[i], 10))) * math.sin(2 * math.pi * lista1[i])
        listaaux.append(zi)
    listaaux2= []
    for j in range(0, len(listaaux)):
        xi= media + desviacion* listaaux[j]
        listaaux2.append(xi)

    return listaaux2


#Distribucion Inversa
def Inversa(aux):
    lista12=[]
    for i in range(0, len(aux)):
        parte1= -1/ np.mean(aux)
        parte2= np.log(1 - (aux[i]))
        total = parte1 * parte2
        lista12.append(total)
    return lista12


#Distribucion Inversa
def Convolucion(lista):
    media=2
    parte1= -1/media
    lista2a=[]
    for k in range(0, len(lista[0])):
        multiplicacion= 1
        for j in range(0, grados):
            auxmiltiplacacion= (1-lista[j][k]) * multiplicacion
            multiplicacion = auxmiltiplacacion


        parte2= parte1 * np.log(multiplicacion)

        lista2a.append(parte2)

    return lista2a


#Distribucion Inversa
def Aceptacion_y_Rechazo(secuencia1, secuencia2):
    # la funcion va a hacer 5x mas adelante multiplicare el x
    funcion1= 5

    # Limites
    a=-2
    b=2
    # altura de la grafica
    M=2
    # lista para almacenar a aux1
    listatotaldefuncion=[]
    listaaxuax1=[]
    for i in range(0, len(secuencia1)):


        aux1= a + (secuencia1[i])*(b-a)

        funcionparte2= funcion1 * aux1

        listatotaldefuncion.append(funcionparte2)
        listaaxuax1.append(aux1)
    listatotal1=[]
    for j in range(0, len(secuencia2)):

        if secuencia2[j] <= ((listatotaldefuncion[j])/M):

            listatotal1.append((listaaxuax1[j]))

    return listatotal1
    
##################

def confianza(op):
     
    global inputg1
    global inputg2
    
    global grado1
    global grado2
    
    #global k1
    #global g1
    

     
    inputg1.place_forget()
    inputg2.place_forget()
    grado1.place_forget()
    grado2.place_forget()
    k1.place_forget()
    g1.place_forget()
    entrada_2.place_forget()
    entrada_3.place_forget()
     
    
    alea = str(combo2.get())
    gen = str(combo1.get())
    
    if(gen == "Algoritmo_Congruencial_M" ):
        k1.place(x=340, y=120)
        g1.place(x=340, y=145)
        entrada_2.place(x=360, y=120)
        entrada_3.place(x=360, y=145)
    
    
    if(alea == "D. Chi-Cuadrado"):
         
        inputg1.place(x=30, y=170)
        grado1.place(x=140, y=170)
        
    
    if(alea == "Distribucion T"):
        
        inputg1.place(x=30, y=170)
        grado1.place(x=140, y=170)
    
    
    if(alea == "Distribucion F"):
        
        inputg1.place(x=30, y=170)
        grado1.place(x=140, y=170)
        
        inputg2.place(x=270, y=170)
        grado2.place(x=369, y=170)
        
        
    if(alea == "D. Log-Normal"):
        inputg1.grid_remove()
        inputg2.grid_remove()
        
        
    if(alea == "Convolucional"):
        
        inputg1.place(x=30, y=170)
        grado1.place(x=140, y=170)
    
        
    
        
#######################
def histograma(datos):
       plt.figure()
       plt.hist(datos,15, histtype='barstacked', density=True);
       sns.kdeplot(datos); 
       plt.show()    
       
       #cuenta, cajas, ignorar = plt.hist(datos, 15,histtype='barstacked', density=True)
       #plt.ylabel('frequencia')
       #plt.xlabel('valores')
       #plt.title('Histograma Gamma')
       #plt.show()




#############################

def graficar():
    
    r1 = []
    r2 = []
    xi = []
    
    alea = str(combo2.get())
    can = int(cantidad.get())
    sem = int(semilla.get())
    gen = str(combo1.get())
    valor = grafico_v.get()
    
    k = k_var.get()
    g = g_var.get()
    
     
    re = ''.join(reversed(str(semilla.get())))
    
    
    #D. NORMAL BOX MULLER
    if(alea == "D. Normal BoxMuller"):
        
        #VISUAL BASIC
        if(gen == "Visual Basic" or gen == "Productos medios"):
            r1 = Generador_Visual_Basic(sem,can)
            r2 = Generador_Visual_Basic((sem+1),can)

            xi = distribucion_normal_bm(r1,r2)
           
            if(valor == 1): 
                histograma(xi)
            
            
        #FORTRAN    
        if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
            r1 = Generador_Fortran(sem,can)
            r2 = Generador_Fortran((sem+1),can)

            xi = distribucion_normal_bm(r1,r2)
           
            if(valor == 1): 
                histograma(xi)
                
                
        #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
        if(gen == "Algoritmo_Congruencial_M"):
            if(int(g)<=1):
                print("g debe ser mayor o igual a 2")
            
            else:
                
                r1 = Generador_Congruencial_multiplicativo(sem,int(k),int(g),can)
                r2 = Generador_Congruencial_multiplicativo((sem+4),int(k)+1,int(g)+1,can)
            
                if(r1==0 or r2==0):
                    print("vuelva a ingresar una semilla")
                
                else:
                    xi = distribucion_normal_bm(r1,r2)
                   
                    if(valor == 1): 
                        histograma(xi)
  
   #------------------------------------------------------------   
  
    
    #D. LOG NORMAL
    if(alea == "D. Log-Normal"):
        
        
        #VISUAL BASIC
        if(gen == "Visual Basic" or gen == "Productos medios"):
            r1 = Generador_Visual_Basic(sem,can)
            #r2 = Generador_Visual_Basic((int(re)+1),can)
            r2 = Generador_Visual_Basic((sem+1),can)

            xi = Distribucion_Log_Normal(r1,r2)
           
            
            if(valor == 1): 
                histograma(xi)
            
            
        #FORTRAN     
        if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
            r1 = Generador_Fortran(sem,can)
            #r2 = Generador_Fortran((int(re)+1),can)
            r2 = Generador_Visual_Basic((sem+1),can)

            xi = Distribucion_Log_Normal(r1,r2)
           
            if(valor == 1): 
                histograma(xi)
        
        
        #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
        if(gen == "Algoritmo_Congruencial_M"):
            if(int(g)<=1):
                print("g debe ser mayor o igual a 2")
            
            else:
                
                r1 = Generador_Congruencial_multiplicativo(sem,int(k),int(g),can)
                r2 = Generador_Congruencial_multiplicativo((sem+4),int(k)+1,int(g)+1,can)
            
                if(r1==0 or r2==0):
                    print("vuelva a ingresar una semilla")
                
                else:
                    xi = Distribucion_Log_Normal(r1,r2)
                   
                    if(valor == 1): 
                        histograma(xi)
                
        
     
    #------------------------------------------------------------    
     
    
    #D. EXPONENCIAL
    if(alea == "Distribucion Exponencial"):

       
       #VISUAL BASIC
       if(gen == "Visual Basic" or gen == "Productos medios"):
           r1 = Generador_Visual_Basic(sem,can)
           #r2 = Generador_Visual_Basic((int(re)+1),can)
           r2 = Generador_Visual_Basic((sem+1),can)

           xi = Distribucion_Exponencial(r1,r2)
         
           
           if(valor == 1): 
               histograma(xi)
           
           
       #FORTRAN     
       if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
           r1 = Generador_Fortran(sem,can)
           #r2 = Generador_Fortran((int(re)+1),can)
           r2 = Generador_Visual_Basic((sem+1),can)

           xi = Distribucion_Exponencial(r1,r2)
          
           if(valor == 1): 
               histograma(xi)
               
               
       #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
       if(gen == "Algoritmo_Congruencial_M"):
           if(int(g)<=1):
               print("g debe ser mayor o igual a 2")
           
           else:
               
               r1 = Generador_Congruencial_multiplicativo(sem,int(k),int(g),can)
               r2 = Generador_Congruencial_multiplicativo((sem+4),int(k)+1,int(g)+1,can)
           
               if(r1==0 or r2==0):
                   print("vuelva a ingresar una semilla")
               
               else:
                   xi = Distribucion_Exponencial(r1,r2)
                  
                   if(valor == 1): 
                       histograma(xi)       

    #------------------------------------------------------------  
         
    #D. CHI CUADRADO
    if(alea == "D. Chi-Cuadrado"):
        
        g_1 = int(grados_1.get())
         
        #VISUAL BASIC
        if(gen == "Visual Basic" or gen == "Productos medios"): 
            r1 = Generador_Visual_Basic(sem,can)
            #r2 = Generador_Visual_Basic((int(re)+1),can)
            r2 = Generador_Visual_Basic((sem+1),can)
               
            xi = Distribucion_Chi_Cuadrado(r1,r2,g_1,sem,can)
            
            if(valor == 1):
                histograma(xi)
        
        
        #FORTRAN 
        if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
            r1 = Generador_Fortran(sem,can)
            #r2 = Generador_Fortran((int(re)+1),can)
            r2 = Generador_Fortran((sem+1),can)

            xi = Distribucion_Chi_Cuadrado(r1,r2,g_1,sem,can)
           
            if(valor == 1): 
                histograma(xi)
                
                
        #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
        if(gen == "Algoritmo_Congruencial_M"):
            if(int(g)<=1):
                print("g debe ser mayor o igual a 2")
            
            else:
                
                r1 = Generador_Congruencial_multiplicativo(sem,int(k),int(g),can)
                r2 = Generador_Congruencial_multiplicativo((sem+4),int(k)+1,int(g)+1,can)
            
                if(r1==0 or r2==0):
                    print("vuelva a ingresar una semilla")
                
                else:
                    xi = Distribucion_Chi_Cuadrado(r1,r2,g_1,sem,can)
                   
                    if(valor == 1): 
                        histograma(xi)   
                
    #------------------------------------------------------------      
        
    #D. T
    if(alea == "Distribucion T"):
        
        g_1 = int(grados_1.get())
            
            #VISUAL BASIC
        if(gen == "Visual Basic" or gen == "Productos medios"):
           r1 = Generador_Visual_Basic(sem,can)
           #r2 = Generador_Visual_Basic((int(re)+1),can)
           r2 = Generador_Fortran((sem+1),can)
               
           xi = Distribucion_T(r1,r2,g_1)
             
               
           if(valor == 1): 
               histograma(xi)
            
            
        #FORTRAN
        if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
            r1 = Generador_Fortran(sem,can)
            #r2 = Generador_Fortran((int(re)+1),can)
            r2 = Generador_Fortran((sem+1),can)
            xi = Distribucion_T(r1,r2,g_1)
                
               
            if(valor == 1): 
                histograma(xi)
                
                
        #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
        if(gen == "Algoritmo_Congruencial_M"):
            if(int(g)<=1):
                print("g debe ser mayor o igual a 2")
            
            else:
                
                r1 = Generador_Congruencial_multiplicativo(sem,int(k),int(g),can)
                r2 = Generador_Congruencial_multiplicativo((sem+4),int(k)+1,int(g)+1,can)
            
                if(r1==0 or r2==0):
                    print("vuelva a ingresar una semilla")
                
                else:
                    xi = Distribucion_T(r1,r2,g_1)
                   
                    if(valor == 1): 
                        histograma(xi) 
            
    #--------------------------------------------------------------
    
    #D. F
    if(alea == "Distribucion F"):
        
        g_1 = int(grados_1.get())
        g_2 = int(grados_2.get())
        
        
        #VISUAL BASIC
        if(gen == "Visual Basic" or gen == "Productos medios"):
           r1 = Generador_Visual_Basic(sem,can)
           r2 = Generador_Visual_Basic((sem*sem),can)
           
           r3 = Generador_Fortran(sem,can)
           r4 = Generador_Fortran((sem+10),can)
           
           xi = Distribucion_F(r1,r2,r3,r4,g_1,g_2, sem, can)
           
           if(valor == 1): 
               histograma(xi)
           
         
        #FORTRAN
        if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
            
            r1 = Generador_Visual_Basic(sem,can)
            r2 = Generador_Visual_Basic((sem*sem),can)
            
            r3 = Generador_Fortran(sem,can)
            r4 = Generador_Fortran((sem+1),can)
            
            xi = Distribucion_F(r1,r2,r3,r4,g_1,g_2, sem, can)
        
            
            if(valor == 1): 
                histograma(xi)
                
        
        #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
        if(gen == "Algoritmo_Congruencial_M"):
            
            
            if(int(g)<=1):
                print("g debe ser mayor o igual a 2")
            
            else:
                
                
                r1 = Generador_Congruencial_multiplicativo(sem,k,g,can)
                r2 = Generador_Congruencial_multiplicativo((sem+4),int(k)+1,int(g)+1,can)
                
                r3 = Generador_Congruencial_multiplicativo(sem,k,g,can)
                r4 = Generador_Congruencial_multiplicativo((sem+2),int(k)+1,int(g)+1,can)
            
                if(r1==0 or r2==0):
                    print("vuelva a ingresar una semilla")
                
                else:
                    xi = Distribucion_F(r1,r2,r3,r4,g_1,g_2, sem, can)
                   
                    if(valor == 1): 
                        histograma(xi)  
        
            
    #----------------------------------------------------------------
    
    
    #D. GAMMA
    if(alea == "Distribucion Gamma"):
         
        #VISUAL BASIC
        if(gen == "Visual Basic" or gen == "Productos medios"):
            
            r1 = Generador_Visual_Basic(sem,can)
            r2 = Generador_Visual_Basic((sem+1),can)
            xi = Distribucion_Gamma(r1,r2)
            
            if(valor == 1): 
                histograma(xi)
            
        
        #FORTRAN
        if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
            
            r1 = Generador_Fortran(sem,can)
            r2 = Generador_Fortran((sem+1),can)
            xi = Distribucion_Gamma(r1,r2)
         
            if(valor == 1): 
                histograma(xi)
        
        
        #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
        if(gen == "Algoritmo_Congruencial_M"):
            if(int(g) <= 2):
                print("g debe ser mayor o igual a 3")
            
            else:
                
                r1 = Generador_Congruencial_multiplicativo(sem,k,g,can)
                r2 = Generador_Congruencial_multiplicativo((sem+4),int(k)+1,int(g)+1,can)
            
                if(r1==0 or r2==0):
                    print("vuelva a ingresar una semilla")
                
                else:
                    xi = Distribucion_Gamma(r1,r2)
                   
                    if(valor == 1): 
                        histograma(xi)   
                    
                    
    #----------------------------------------------------------------                


    #TRANSFORMADA DIRECTA
    if(alea == "Transformada Directa"):
        
        
        #VISUAL BASIC
        if(gen == "Visual Basic" or gen == "Productos medios"):
            r1 = Generador_Visual_Basic(sem,can)
            r2 = Generador_Visual_Basic((sem+1),can)

            xi = Directa(r1, r2)
           
            if(valor == 1): 
                histograma(xi)
            
            
        #FORTRAN    
        if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
            r1 = Generador_Fortran(sem,can)
            #r2 = Generador_Fortran((int(re)+1),can)
            r2 = Generador_Fortran((sem+1),can)

            xi = Directa(r1, r2)
           
            if(valor == 1): 
                histograma(xi)
                
                
        #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
        if(gen == "Algoritmo_Congruencial_M"):
            if(int(g)<=1):
                print("g debe ser mayor o igual a 2")
            
            else:
                
                
                r1 = Generador_Congruencial_multiplicativo(sem,k,g,can)
                r2 = Generador_Congruencial_multiplicativo((sem+4),int(k)+1,int(g)+1,can)
                
            
                if(r1==0 or r2==0):
                    print("vuelva a ingresar una semilla")
                
                else:
                    xi = Directa(r1,r2)
                   
                    if(valor == 1): 
                        histograma(xi) 
                    
                    
    #----------------------------------------------------------------                


    #TRANSFORMADA INVERSA
    if(alea == "Transformada Inversa"):
       
       
       #VISUAL BASIC
       if(gen == "Visual Basic" or gen == "Productos medios"):
           r1 = Generador_Visual_Basic(sem,can)

           xi = Inversa(r1)
          
           if(valor == 1): 
               histograma(xi)
           
           
       #FORTRAN    
       if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
           r1 = Generador_Fortran(sem,can)

           xi = Inversa(r1)
          
           if(valor == 1): 
               histograma(xi)
               
               
       #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
       if(gen == "Algoritmo_Congruencial_M"):
           if(int(g) <= 2):
               print("g debe ser mayor a 3")
           
           else:
               
               r1 = Generador_Congruencial_multiplicativo(sem,k,g,can)
               
               if(r1==0):
                   print("vuelva a ingresar una semilla")
               
               else:
                   xi = Inversa(r1)
                  
                   if(valor == 1): 
                       histograma(xi)
   
    
    #----------------------------------------------------------------                


    #CONVOLUCION
    if(alea == "Convolucional"):
      
      g_1 = int(grados_1.get())
      
      
      #VISUAL BASIC
      if(gen == "Visual Basic" or gen == "Productos medios"):
          r1=[]
          for i in range(0, g_1):
              semilla2 = sem * sem
              generador = Generador_Visual_Basic(semilla2,can)
              r1.append(generador)

          xi = Convolucion(r1)
         
          if(valor == 1): 
              histograma(xi)
          
          
      #FORTRAN    
      if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
          r1=[]
          for i in range(0, g_1):
              semilla2 = sem * sem
              generador = Generador_Fortran(semilla2,can)
              r1.append(generador)

          xi = Convolucion(r1)
         
          if(valor == 1): 
              histograma(xi)
              
              
      #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
      if(gen == "Algoritmo_Congruencial_M"):
          if(int(g)<=2 or g_1<=2):
              print("g y el grado deben ser mayor o igual a 3")
          
          else:
              r1=[]
              for i in range(0, g_1):
                  semilla2 = sem * sem
                  generador = Generador_Congruencial_multiplicativo(semilla2,k,g,can)
                  r1.append(generador)
              
              if(r1==0):
                  print("vuelva a ingresar una semilla")
              
              else:
                  xi = Convolucion(r1)
                 
                  if(valor == 1): 
                      histograma(xi)
                  
    #----------------------------------------------------------------                


    #TRANSFORMADA ACEPTACION Y RECHAZO
    if(alea == "Aceptación y Rechazo"):
      
      
      #VISUAL BASIC
      if(gen == "Visual Basic" or gen == "Productos medios"):
          
          r1 = Generador_Fortran(sem,can)
          r2 = Generador_Fortran((sem+1),can)
          xi = Aceptacion_y_Rechazo(r1,r2)
         
          if(valor == 1): 
              histograma(xi)
          
          
      #FORTRAN    
      if(gen == "Generador_Fortran" or gen == "Cuadrados medios"):
          
          r1 = Generador_Fortran(sem,can)
          r2 = Generador_Fortran((sem+1),can)
          xi = Aceptacion_y_Rechazo(r1,r2)
         
          if(valor == 1): 
              histograma(xi)
              
              
      #ALGORITMO CONGRUENCIAL MULTIPLICATIVO   
      if(gen == "Algoritmo_Congruencial_M"):
          
          if(int(g)<=3):
              print("g debe ser mayor o igual a 4")
          
          else:
              
              r1 = Generador_Congruencial_multiplicativo(sem,k,g,can)
              r2 = Generador_Congruencial_multiplicativo((sem+4),int(k)+1,int(g)+1,can)
              
              if(r1==0):
                  print("vuelva a ingresar una semilla")
              
              else:
                  xi = Aceptacion_y_Rechazo(r1,r2)
                 
                  if(valor == 1): 
                      histograma(xi)
                  
   #------------------------------------------------------------   


root = tk.Tk()
root.geometry('525x280')
root.title('Aplicacion')

titulo = ttk.Label(root, text="Generador de variables aleatorias")
titulo.place(x=150, y=10)

labelcombo1 = ttk.Label(root, text="Seleccione la Generador Aleatorio")
labelcombo1.place(x=250, y=40)

combo1 = ttk.Combobox(root,width=25, state="readonly",
                       values = ["Visual Basic",
                                    "Generador_Fortran",
                                    "Productos medios",
                                    "Cuadrados medios",
                                    "Algoritmo_Congruencial_M"])
combo1.place(x=250, y=60) 

label_combo2 = ttk.Label(root, text="Seleccione la variable aleatoria")
label_combo2.place(x=30, y=40)

aleatoria = tk.StringVar() 
combo2 = ttk.Combobox(root,width=20, textvariable=aleatoria,
                     values = ["D. Normal BoxMuller",
                                    "D. Log-Normal",
                                    "D. Chi-Cuadrado",
                                    "Distribucion T",
                                    "Distribucion F",
                                    "Distribucion Exponencial",
                                    "Distribucion Gamma",
                                    "Transformada Directa",
                                    "Transformada Inversa",
                                    "Convolucional",
                                    "Aceptación y Rechazo"
                                    ],state="readonly")
combo2.place(x=30, y=60) 
inputg1 = ttk.Label(root, text="Grados Libertad 1:")
inputg2 =ttk.Label(root, text="Grados Libertad 2:")

global grados_1
global grados_2

grados_1 = tk.StringVar()
grados_2 = tk.StringVar()


grado1 = ttk.Entry(root,textvariable=grados_1)
grado2 = ttk.Entry(root,textvariable=grados_2)
 

#CANTIDAD A GENERAR
cantidad = tk.StringVar()
v = ttk.Label(root, text="Cantidad a Generar:")
v.place(x=30, y=120)

inputcant = ttk.Entry(root,textvariable=cantidad)
inputcant.place(x=140, y=120)


#SEMILLA INICIAL
semilla = tk.StringVar()
v = ttk.Label(root, text="Semilla inicial:")
v.place(x=30, y=145)

entrada_1 = ttk.Entry(root,textvariable=semilla)
entrada_1.place(x=140, y=145)


#K
k_var = tk.StringVar()
k1 = ttk.Label(root, text="K:")

entrada_2 = ttk.Entry(root,textvariable=k_var)

#G
g_var = tk.StringVar()
g1 = ttk.Label(root, text="G:")

entrada_3 = ttk.Entry(root,textvariable=g_var)


#METODO GRAFICOS
grafico_v = tk.IntVar() 

labels = ttk.Label(root, text="Seleccione Gráfico:")
labels.place(x=30, y=200)

histo = tk.Radiobutton(root, text="Histograma", variable = grafico_v, value=1)
histo.place(x=30, y=220)
 



#BOTON DE GRAFICA
boton = tk.Button(root,text = 'Graficar', command = graficar)
boton.place(x=390, y=220) 


combo2.bind("<<ComboboxSelected>>",confianza)


root.mainloop()

######################################



