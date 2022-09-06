# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:47:23 2022

@author: larag
"""

x0=int(input("ingresa x0: "))
k=int(input("ingresa k: ")) #entero
g=int(input("ingresa g: ")) #entero
c=int(input("ingresa c: ")) #primo
numa=int(input("ingrese cuantos números pseudoaletorios quiere: "))

def Algoritmo_lineal(x0,k,g,c,numa):
    
    m=2**g 
    a=1+(4*k)
    print("x0 =",x0)

    for i in range(1,numa+1):
        x=(a*x0+c)%m
        r=x/(m-1)
        print("x"+str(i),"=","(",a,"*",x0," +",c,") mod",m,"=",x)
        print("r"+str(i),"=",x,"/",c,"=",r)
        x0=x
        
        
Algoritmo_lineal(x0,k,g,c,numa)

