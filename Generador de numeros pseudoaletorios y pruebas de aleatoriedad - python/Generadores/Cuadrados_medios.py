# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 09:24:28 2022

@author: larag
"""
import numpy as np

def middle(nump, nums):
    num_len_s=len(str(nums))
    num_len_p=len(str(nump))
    r1=int((num_len_s-num_len_p)/2)
    n=str(nums)
    num = n[r1:(r1+num_len_p)]
    return num

seed=int(input("ingresa la semilla: "))
numa=int(input("ingrese cuantos números pseudoaletorios quiere: "))

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
                print("seed: ",seed, ", cuadrado:", pow2, (", r"+str(i+1)+":"),("0."+m))
                lista.append(str("0."+m))
                seed=m  
        
    else:
        print("tiene que ingresar una seed con minimo 4 digitos")
    
Cuadrados_medios(seed, numa)