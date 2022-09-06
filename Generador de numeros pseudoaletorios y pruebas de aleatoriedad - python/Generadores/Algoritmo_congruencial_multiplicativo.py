# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:47:23 2022

@author: larag
"""

x0=int(input("ingresa x0: "))
k=int(input("ingresa k: ")) 
g=int(input("ingresa g: ")) 
numa=int(input("ingrese cuantos números pseudoaletorios quiere: "))

def Algoritmo_congruencial_multip(x0, k, g, numa):

    if (x0%2!=0):
        m=2**g
        a=5+(8*k)
        print("x0 =",x0)    
    
        for i in range(1,numa+1):
            x=(a*x0)%m
            r=x/(m-1)
            print("x"+str(i),"=","(",a,"*",x0,") mod",m,"=",x)
            print("r"+str(i),"=",x,"/",(m-1),"=",r) 
            x0=x
    else:
        print("x0 debe ser un número impar")
        
Algoritmo_congruencial_multip(x0, k, g, numa)
    
    
    
    
        
    
    
    

