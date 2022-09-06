# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:47:23 2022

@author: larag
"""

m=int(input("ingresa el modulo: "))
numa=int(input("ingrese cuantos números pseudoaletorios quiere: "))
n=[65,89,98,3,69] #esta secuencia va cambiando, dependiendo de lo que quiera el usuario

def Algoritmo_aditivo(n, m, numa):

    for i in range(0,numa):
        x1=n[i]
        x2=n[(len(n)-1)]
        x=(x1+x2)%m
        n.append(x)
        r=x/(m-1)
        print("x"+str((len(n))),"=","(","x"+str((len(n)-1)),"*","x"+str(i+1),") mod",m,"=","(",x2,"*",x1,") mod",m,"=",x)
        print("r"+str(i+1),"=",x,"/",(m-1),"=",r)    
        
Algoritmo_aditivo(n, m, numa)
    
    
    
    
        
    
    
    

