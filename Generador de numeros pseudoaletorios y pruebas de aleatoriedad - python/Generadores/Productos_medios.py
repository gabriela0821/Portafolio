# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:09:56 2022

@author: larag
"""

def middle(nump, nums):
    num_len_s=len(str(nums))
    num_len_p=len(str(nump))
    r1=int((num_len_s-num_len_p)/2)
    n=str(nums)
    num = n[r1:(r1+num_len_p)]
    return num

seed1=int(input("ingresa la primera semilla: "))
seed2=int(input("ingresa la segunda semilla: "))
numa=int(input("ingrese cuantos números pseudoaletorios quiere: "))

def Productos_medios(seed1, seed2, numa):
    
    if len(str(seed1))>3 and len(str(seed2))>3:
        
        for i in range(0,numa):
            prod=int(seed1)*int(seed2)
            m=middle(seed1,prod)
            
            if(int(seed1)==0 or int(seed2)==0 or int(m)==0 or m==seed2):
                print("no se pueden generar más números")
                break
            else:
                print("seed1: ",seed1,", seed2: ",seed2, ", cuadrado:", prod, (", r"+str(i+1)+":"),("0."+m))
                seed1=seed2
                seed2=m
                
    else:
        print("tiene que ingresar una seed con minimo 4 digitos")
        
Productos_medios(seed1, seed2, numa)