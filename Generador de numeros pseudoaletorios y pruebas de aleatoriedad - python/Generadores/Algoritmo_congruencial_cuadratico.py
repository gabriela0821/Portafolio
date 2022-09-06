# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:47:23 2022

@author: larag
"""

x0=int(input("ingresa x0: "))
m=int(input("ingresa el modulo: "))
a=int(input("ingresa a: ")) 
b=int(input("ingresa b: ")) 
c=int(input("ingresa c: "))
numa=int(input("ingrese cuantos números pseudoaletorios quiere: "))

def Algoritmo_congruencial_cuadr(x0,m,a,b,c,numa):

    if(a%2==0 and c%2!=0):
        for i in range(1,numa+1):
            x=(a*(x0**2)+b*(x0)+c)%m
            print("x"+str(i),"=","(",a,"*",str(x0)+"^2 +",b,"*",x0,"+",c,") mod",m,"=",x)
            x0=x
    else:
        print("la variable a no es par o la variable c no es impar")
        
        
Algoritmo_congruencial_cuadr(x0,m,a,b,c,numa)