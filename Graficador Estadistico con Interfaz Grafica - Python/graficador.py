# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 21:26:42 2022

@author: larag
"""
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox as MessageBox
import pandas as pd
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from scipy import stats
from pandas import DataFrame
import turtle
import numpy as np

archivo='abalone.csv'

 

datos=pd.read_csv(archivo)
columnas=[0,1, 2,
3,
4,
5,
6,
7,
8]
datos.columns=columnas

 
aux = ['Sexo','Longitud',
'Diametro',
'Altura',
'Peso Entero',
'Peso Casacara',
'Peso Viseral',
'Peso Caparazon',
'# de Anillos' ]
"""
plot.hist(datos['length'])
plot.subplots()
plot.boxplot(datos['length'])
fig=plot.figure()
ax=fig.add_subplot(111)
res=stats.probplot(datos['length'],dist=stats.norm,plot=ax)
"""

class App:    
    

    def __init__(self, root):
        
        def Histograma(df,col):
            
            window = Tk()
            window.geometry("600x600")
            namew="Histograma - "+aux[col]
            window.wm_title(namew)
            
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.hist(df[col])
            
            canvas = FigureCanvasTkAgg(fig, window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            
            ax.set_xlabel("Valor de los datos")
            ax.set_ylabel("Cantidad de datos")
            
            toolbar = NavigationToolbar2Tk(canvas, window)
            
            toolbar.update()
            window.mainloop()
            

        def Normalización(df, col):
            
            window = Tk()
            window.geometry("600x600")
            namew="Normalización - "+aux[col]
            window.wm_title(namew)
            
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            stats.probplot(df[col],dist=stats.norm,plot=ax)
            
            canvas = FigureCanvasTkAgg(fig, window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            
            ax.set_xlabel("Valor de los datos")
            ax.set_ylabel("Cantidad de datos")
            
            toolbar = NavigationToolbar2Tk(canvas, window)
            
            toolbar.update()
            window.mainloop()
        
        
        def Boxplot(df, col):
            window = Tk()
            window.geometry("600x600")
            namew="Boxplot - "+aux[col]
            window.wm_title(namew)
            
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.boxplot(df[col])
            
            canvas = FigureCanvasTkAgg(fig, window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            
            ax.set_xlabel("Valor de los datos")
            ax.set_ylabel("Cantidad de datos")
            
            toolbar = NavigationToolbar2Tk(canvas, window)
            
            toolbar.update()
            window.mainloop()


        def Dispersion(df,col1,col2):
            
            window = Tk()
            window.geometry("600x600")
            namew="Dispersion - "+aux[col1]+" y "+aux[col2]
            window.wm_title(namew)
            
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.scatter((df[col1]), (df[col2]))
            
            canvas = FigureCanvasTkAgg(fig, window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            
            ax.set_xlabel("Valor de los datos")
            ax.set_ylabel("Cantidad de datos")
            
            toolbar = NavigationToolbar2Tk(canvas, window)
            
            toolbar.update()
            window.mainloop()

        def eliminar(df, index):
            index = sorted(set(index))
            df = df.drop(index)
            return df
        
        def IdentificarAtipicos(df, ft, valorAlfa):
            q1 = df[ft].quantile(0.25)
            q3 = df[ft].quantile(0.75)
            iqr = q3 - q1
        
            bigote_inferior = q1 - valorAlfa * iqr
            bigote_superior = q3 + valorAlfa * iqr
        
            ls = df.index[(df[ft]<bigote_inferior) | (df[ft] > bigote_superior)]
            return ls

        def determinar(n,j):
            pos=[]
            cont=0
            for i in range(0,len(j)):
                if(j[i]==1):
                    cont+=1
                    pos.append(i+1)
        
            if(cont!=n):
                MessageBox.showwarning(title="¡ADVERTENCIA!", message="No se puede graficar con el numero de variables seleccionadas")
                return "false"
      
            if(cont==1 and n==1):
                return pos[0]
      
            if(cont==2 and n==2):
                return pos
            
        
        def boton():
               opcion=radio.get()
               entradas1=[long1.get()
                          ,diame1.get()
                          ,altura1.get()
                          ,pesoe1.get()
                          ,pesocasc1.get()
                          ,pesovise1.get()
                          ,pesocapar1.get()
                          ,nanillos1.get()]
               if(opcion==0):
                   ve=determinar(1,entradas1)
                   if(ve!="false"):
                       Histograma(datos, ve)
                   
               if(opcion==1):
                   ve=determinar(1,entradas1)
                   if(ve!="false"):
                       Normalización(datos, ve)
                   
               if(opcion==2):
                   ve=determinar(1,entradas1)
                   if(ve!="false"):
                       Boxplot(datos, ve)
                       
               if(opcion==3):
                   ve=determinar(2,entradas1)
                   if(ve!="false"):
                       Dispersion(datos, ve[0],ve[1])
                       
        def sinatipicos():
               
               alfa=alpha.get()
               opcion=radio.get()
               entradas1=[long1.get()
                          ,diame1.get()
                          ,altura1.get()
                          ,pesoe1.get()
                          ,pesocasc1.get()
                          ,pesovise1.get()
                          ,pesocapar1.get()
                          ,nanillos1.get()]
               
               
               if(opcion==0):
                   ve=determinar(1,entradas1)
                   index=IdentificarAtipicos(datos, ve, alfa)
                   data2=eliminar(datos, index)
                   if(ve!="false"):
                       Histograma(data2, ve)
                   
               if(opcion==1):
                   ve=determinar(1,entradas1)
                   index=IdentificarAtipicos(datos, ve, alfa)
                   data2=eliminar(datos, index)
                   if(ve!="false"):
                       Normalización(data2, ve)
                   
               if(opcion==2):
                   ve=determinar(1,entradas1)
                   index=IdentificarAtipicos(datos, ve, alfa)
                   data2=eliminar(datos, index)
                   if(ve!="false"):
                       Boxplot(data2, ve)
                       
               if(opcion==3):
                   ve=determinar(2,entradas1)
                   index0=IdentificarAtipicos(datos, ve[0], alfa)
                   index1=IdentificarAtipicos(datos, ve[1], alfa)
                   data2=eliminar(datos, index1)
                   data3=eliminar(datos, index0)
                   if(ve!="false"):
                       Dispersion(data3, ve[0],ve[1])
                       
        
        #variable para radiobutton opciones generales
        radio = IntVar()
        
        #variable opciones - primera parte
        long1 = IntVar()
        pesoe1 = IntVar()
        pesocapar1 = IntVar()
        diame1 = IntVar()
        pesocasc1 = IntVar()
        nanillos1 = IntVar()
        altura1 = IntVar()
        pesovise1 = IntVar()
        
        #variable alpha - eliminar atipicos
        alpha = DoubleVar()
        
        #setting title
        root.title("GRAFICADOR")
        #setting window size
        width=674
        height=680
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_448=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        GLabel_448["font"] = ft
        GLabel_448["fg"] = "#333333"
        GLabel_448["justify"] = "center"
        GLabel_448["text"] = "Grafica con atípicos"
        GLabel_448.place(x=0,y=30,width=164,height=34)

        GLabel_853=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        GLabel_853["font"] = ft
        GLabel_853["fg"] = "#333333"
        GLabel_853["justify"] = "center"
        GLabel_853["text"] = "Grafica sin atípicos"
        GLabel_853.place(x=10,y=300,width=145,height=32)


        #1 PARTE (FUNCIONANDO)
        
        check_Histograma=tk.Radiobutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_Histograma["font"] = ft
        check_Histograma["fg"] = "#333333"
        check_Histograma["justify"] = "center"
        check_Histograma["text"] = "Histograma"
        check_Histograma["value"]=0
        check_Histograma["variable"]=radio
        check_Histograma.place(x=22,y=80,width=90,height=25)
        

        check_Normalizacion=tk.Radiobutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_Normalizacion["font"] = ft
        check_Normalizacion["fg"] = "#333333"
        check_Normalizacion["justify"] = "center"
        check_Normalizacion["text"] = "Normalización"
        check_Normalizacion["value"]=1
        check_Normalizacion["variable"]=radio
        check_Normalizacion.place(x=25,y=110,width=99,height=25)
        
        
        check_Boxplot=tk.Radiobutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_Boxplot["font"] = ft
        check_Boxplot["fg"] = "#333333"
        check_Boxplot["justify"] = "center"
        check_Boxplot["text"] = "Boxplot"
        check_Boxplot["value"]=2
        check_Boxplot["variable"]=radio
        check_Boxplot.place(x=140,y=80,width=90,height=25)
        

        check_Dispercion=tk.Radiobutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_Dispercion["font"] = ft
        check_Dispercion["fg"] = "#333333"
        check_Dispercion["justify"] = "center"
        check_Dispercion["text"] = "Dispercion"
        check_Dispercion["value"]=3
        check_Dispercion["variable"]=radio
        check_Dispercion.place(x=148,y=110,width=90,height=25)
        
        
        
        
        #2 PARTE (EN PROCESO)
        

        GLabel_444=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_444["font"] = ft
        GLabel_444["fg"] = "#333333"
        GLabel_444["justify"] = "center"
        GLabel_444["text"] = "Variables de entrada"
        GLabel_444.place(x=20,y=150,width=119,height=33)

        check_Longitud_1=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_Longitud_1["font"] = ft
        check_Longitud_1["fg"] = "#333333"
        check_Longitud_1["justify"] = "center"
        check_Longitud_1["text"] = "Longitud"
        check_Longitud_1["variable"]=long1
        check_Longitud_1.place(x=20,y=190,width=75,height=25)
        check_Longitud_1["offvalue"] = "0"
        check_Longitud_1["onvalue"] = "1"

        check_pesoentero_1=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesoentero_1["font"] = ft
        check_pesoentero_1["fg"] = "#333333"
        check_pesoentero_1["justify"] = "center"
        check_pesoentero_1["text"] = "peso entero"
        check_pesoentero_1["variable"]=pesoe1
        check_pesoentero_1.place(x=20,y=220,width=95,height=30)
        check_pesoentero_1["offvalue"] = "0"
        check_pesoentero_1["onvalue"] = "1"

        check_pesocaparazon_1=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesocaparazon_1["font"] = ft
        check_pesocaparazon_1["fg"] = "#333333"
        check_pesocaparazon_1["justify"] = "center"
        check_pesocaparazon_1["text"] = "peso caparazon"
        check_pesocaparazon_1["variable"]=pesocapar1
        check_pesocaparazon_1.place(x=23,y=250,width=110,height=30)
        check_pesocaparazon_1["offvalue"] = "0"
        check_pesocaparazon_1["onvalue"] = "1"

        check_diametro_1=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_diametro_1["font"] = ft
        check_diametro_1["fg"] = "#333333"
        check_diametro_1["justify"] = "center"
        check_diametro_1["text"] = "Diametro"
        check_diametro_1["variable"]=diame1
        check_diametro_1.place(x=150,y=190,width=75,height=25)
        check_diametro_1["offvalue"] = "0"
        check_diametro_1["onvalue"] = "1"

        check_pesocascara_1=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesocascara_1["font"] = ft
        check_pesocascara_1["fg"] = "#333333"
        check_pesocascara_1["justify"] = "center"
        check_pesocascara_1["text"] = "peso cascara"
        check_pesocascara_1["variable"]=pesocasc1
        check_pesocascara_1.place(x=150,y=220,width=96,height=30)
        check_pesocascara_1["offvalue"] = "0"
        check_pesocascara_1["onvalue"] = "1"

        check_ndeanillos_1=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_ndeanillos_1["font"] = ft
        check_ndeanillos_1["fg"] = "#333333"
        check_ndeanillos_1["justify"] = "center"
        check_ndeanillos_1["text"] = "# de anillos"
        check_ndeanillos_1["variable"]=nanillos1
        check_ndeanillos_1.place(x=150,y=250,width=94,height=30)
        check_ndeanillos_1["offvalue"] = "0"
        check_ndeanillos_1["onvalue"] = "1"

        check_altura_1=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_altura_1["font"] = ft
        check_altura_1["fg"] = "#333333"
        check_altura_1["justify"] = "center"
        check_altura_1["text"] = "Altura"
        check_altura_1["variable"]=altura1
        check_altura_1.place(x=250,y=190,width=75,height=25)
        check_altura_1["offvalue"] = "0"
        check_altura_1["onvalue"] = "1"

        check_pesoviseras_1=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesoviseras_1["font"] = ft
        check_pesoviseras_1["fg"] = "#333333"
        check_pesoviseras_1["justify"] = "center"
        check_pesoviseras_1["text"] = "peso víseras"
        check_pesoviseras_1["variable"]=pesovise1
        check_pesoviseras_1.place(x=260,y=220,width=92,height=30)
        check_pesoviseras_1["offvalue"] = "0"
        check_pesoviseras_1["onvalue"] = "1"
        
        
        #TERCERA PARTE (SIN EMPEZAR)

        input_alpha=tk.Entry(root)
        input_alpha["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        input_alpha["font"] = ft
        input_alpha["fg"] = "#333333"
        input_alpha["justify"] = "center"
        input_alpha["text"] = ""
        input_alpha["textvariable"]=alpha
        input_alpha.place(x=440,y=300,width=160,height=30)

        GLabel_219=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_219["font"] = ft
        GLabel_219["fg"] = "#333333"
        GLabel_219["justify"] = "center"
        GLabel_219["text"] = "Valor del factor de alfa para los atipicos"
        GLabel_219["relief"] = "flat"
        GLabel_219.place(x=180,y=295,width=228,height=40)

        button_graficar_originales=tk.Button(root)
        button_graficar_originales["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=9)
        button_graficar_originales["font"] = ft
        button_graficar_originales["fg"] = "#000000"
        button_graficar_originales["justify"] = "center"
        button_graficar_originales["text"] = "Graficar los datos originales"
        button_graficar_originales.place(x=440,y=190,width=160,height=38)
        button_graficar_originales["command"] = boton

        button_eliminar_atipicos=tk.Button(root)
        button_eliminar_atipicos["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=10)
        button_eliminar_atipicos["font"] = ft
        button_eliminar_atipicos["fg"] = "#000000"
        button_eliminar_atipicos["justify"] = "center"
        button_eliminar_atipicos["text"] = "Eliminar Atípicos"
        button_eliminar_atipicos.place(x=440,y=240,width=160,height=30)
        button_eliminar_atipicos["command"] = sinatipicos

        check_Longitud_2=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_Longitud_2["font"] = ft
        check_Longitud_2["fg"] = "#333333"
        check_Longitud_2["justify"] = "center"
        check_Longitud_2["text"] = "Longitud"
        check_Longitud_2.place(x=140,y=400,width=70,height=25)
        check_Longitud_2["offvalue"] = "0"
        check_Longitud_2["onvalue"] = "1"
        #check_Longitud_2["command"] = self.check_Longitud_2_command

        check_diametro_2=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_diametro_2["font"] = ft
        check_diametro_2["fg"] = "#333333"
        check_diametro_2["justify"] = "center"
        check_diametro_2["text"] = "Diametro"
        check_diametro_2.place(x=140,y=430,width=72,height=25)
        check_diametro_2["offvalue"] = "0"
        check_diametro_2["onvalue"] = "1"
        #check_diametro_2["command"] = self.check_diametro_2_command

        check_altura_2=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_altura_2["font"] = ft
        check_altura_2["fg"] = "#333333"
        check_altura_2["justify"] = "center"
        check_altura_2["text"] = "Altura"
        check_altura_2.place(x=130,y=460,width=79,height=30)
        check_altura_2["offvalue"] = "0"
        check_altura_2["onvalue"] = "1"
        #check_altura_2["command"] = self.check_altura_2_command

        check_pesoentero_2=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesoentero_2["font"] = ft
        check_pesoentero_2["fg"] = "#333333"
        check_pesoentero_2["justify"] = "center"
        check_pesoentero_2["text"] = "peso entero"
        check_pesoentero_2.place(x=140,y=490,width=92,height=32)
        check_pesoentero_2["offvalue"] = "0"
        check_pesoentero_2["onvalue"] = "1"
        #check_pesoentero_2["command"] = self.check_pesoentero_2_command

        check_pesocascara_2=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesocascara_2["font"] = ft
        check_pesocascara_2["fg"] = "#333333"
        check_pesocascara_2["justify"] = "center"
        check_pesocascara_2["text"] = "peso cascara"
        check_pesocascara_2.place(x=140,y=520,width=96,height=30)
        check_pesocascara_2["offvalue"] = "0"
        check_pesocascara_2["onvalue"] = "1"
        #check_pesocascara_2["command"] = self.check_pesocascara_2_command

        check_pesoviseras_2=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesoviseras_2["font"] = ft
        check_pesoviseras_2["fg"] = "#333333"
        check_pesoviseras_2["justify"] = "center"
        check_pesoviseras_2["text"] = "peso viseras"
        check_pesoviseras_2.place(x=140,y=550,width=92,height=30)
        check_pesoviseras_2["offvalue"] = "0"
        check_pesoviseras_2["onvalue"] = "1"
        #check_pesoviseras_2["command"] = self.check_pesoviseras_2_command

        check_pesoviseras_2=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesoviseras_2["font"] = ft
        check_pesoviseras_2["fg"] = "#333333"
        check_pesoviseras_2["justify"] = "center"
        check_pesoviseras_2["text"] = "peso caparazon"
        check_pesoviseras_2.place(x=140,y=580,width=112,height=33)
        check_pesoviseras_2["offvalue"] = "0"
        check_pesoviseras_2["onvalue"] = "1"
        #check_pesoviseras_2["command"] = self.check_pesoviseras_2_command

        check_ndeanillos_2=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_ndeanillos_2["font"] = ft
        check_ndeanillos_2["fg"] = "#333333"
        check_ndeanillos_2["justify"] = "center"
        check_ndeanillos_2["text"] = "# de anillos"
        check_ndeanillos_2.place(x=140,y=610,width=88,height=30)
        check_ndeanillos_2["offvalue"] = "0"
        check_ndeanillos_2["onvalue"] = "1"
        #check_ndeanillos_2["command"] = self.check_ndeanillos_2

        GLabel_407=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_407["font"] = ft
        GLabel_407["fg"] = "#333333"
        GLabel_407["justify"] = "center"
        GLabel_407["text"] = "ENTRADAS"
        GLabel_407.place(x=140,y=370,width=70,height=25)

        GLabel_239=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_239["font"] = ft
        GLabel_239["fg"] = "#333333"
        GLabel_239["justify"] = "center"
        GLabel_239["text"] = "SALIDA"
        GLabel_239.place(x=280,y=370,width=70,height=25)

        button_obtener_regresion=tk.Button(root)
        button_obtener_regresion["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=10)
        button_obtener_regresion["font"] = ft
        button_obtener_regresion["fg"] = "#000000"
        button_obtener_regresion["justify"] = "center"
        button_obtener_regresion["text"] = "Obtener Regresión"
        button_obtener_regresion.place(x=440,y=370,width=160,height=30)
        #button_obtener_regresion["command"] = self.button_obtener_regresion_command

        check_longitud_3=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_longitud_3["font"] = ft
        check_longitud_3["fg"] = "#333333"
        check_longitud_3["justify"] = "center"
        check_longitud_3["text"] = "Longitud"
        check_longitud_3.place(x=280,y=400,width=74,height=30)
        check_longitud_3["offvalue"] = "0"
        check_longitud_3["onvalue"] = "1"
        #check_longitud_3["command"] = self.check_longitud_3_command

        check_diametro_3=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_diametro_3["font"] = ft
        check_diametro_3["fg"] = "#333333"
        check_diametro_3["justify"] = "center"
        check_diametro_3["text"] = "Diametro"
        check_diametro_3.place(x=280,y=430,width=79,height=30)
        check_diametro_3["offvalue"] = "0"
        check_diametro_3["onvalue"] = "1"
        #check_diametro_3["command"] = self.check_diametro_3_command

        check_altura_3=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_altura_3["font"] = ft
        check_altura_3["fg"] = "#333333"
        check_altura_3["justify"] = "center"
        check_altura_3["text"] = "Altura"
        check_altura_3.place(x=270,y=460,width=79,height=30)
        check_altura_3["offvalue"] = "0"
        check_altura_3["onvalue"] = "1"
        #check_altura_3["command"] = self.check_altura_3_command

        check_pesoentero_3=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesoentero_3["font"] = ft
        check_pesoentero_3["fg"] = "#333333"
        check_pesoentero_3["justify"] = "center"
        check_pesoentero_3["text"] = "peso entero"
        check_pesoentero_3.place(x=280,y=490,width=92,height=25)
        check_pesoentero_3["offvalue"] = "0"
        check_pesoentero_3["onvalue"] = "1"
        #check_pesoentero_3["command"] = self.check_pesoentero_3_command

        check_pesocascara_3=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesocascara_3["font"] = ft
        check_pesocascara_3["fg"] = "#333333"
        check_pesocascara_3["justify"] = "center"
        check_pesocascara_3["text"] = "peso cascara"
        check_pesocascara_3.place(x=280,y=520,width=96,height=25)
        check_pesocascara_3["offvalue"] = "0"
        check_pesocascara_3["onvalue"] = "1"
        #check_pesocascara_3["command"] = self.check_pesocascara_3_command

        check_pesoviseras_3=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesoviseras_3["font"] = ft
        check_pesoviseras_3["fg"] = "#333333"
        check_pesoviseras_3["justify"] = "center"
        check_pesoviseras_3["text"] = "peso viseras"
        check_pesoviseras_3.place(x=280,y=550,width=92,height=25)
        check_pesoviseras_3["offvalue"] = "0"
        check_pesoviseras_3["onvalue"] = "1"
        #check_pesoviseras_3["command"] = self.check_pesoviseras_3_command

        check_pesocaparazon_3=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_pesocaparazon_3["font"] = ft
        check_pesocaparazon_3["fg"] = "#333333"
        check_pesocaparazon_3["justify"] = "center"
        check_pesocaparazon_3["text"] = "peso caparazon"
        check_pesocaparazon_3.place(x=280,y=580,width=112,height=25)
        check_pesocaparazon_3["offvalue"] = "0"
        check_pesocaparazon_3["onvalue"] = "1"
        #check_pesocaparazon_3["command"] = self.check_pesocaparazon_3_command

        check_ndeanillos_3=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        check_ndeanillos_3["font"] = ft
        check_ndeanillos_3["fg"] = "#333333"
        check_ndeanillos_3["justify"] = "center"
        check_ndeanillos_3["text"] = "# de anillos"
        check_ndeanillos_3.place(x=280,y=610,width=88,height=30)
        check_ndeanillos_3["offvalue"] = "0"
        check_ndeanillos_3["onvalue"] = "1"
        #check_ndeanillos_3["command"] = self.check_ndeanillos_3_command

        GLabel_132=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_132["font"] = ft
        GLabel_132["fg"] = "#333333"
        GLabel_132["justify"] = "center"
        GLabel_132["text"] = "REGRESION"
        GLabel_132.place(x=20,y=370,width=75,height=25)

   

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
