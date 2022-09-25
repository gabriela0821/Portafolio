# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:00:31 2022

@author: larag
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
 

def light_on(canvas,objeto):
    canvas.itemconfig(objeto, fill='green') 
    
def light_off(canvas,objeto):
    canvas.itemconfig(objeto, fill='gray') 
    
def cambio_texto(x):
    root = tk.Tk()
    root.geometry('500x210')
    root.title('Información')
    lab = ttk.Label(root, text=x).pack()
    root.mainloop()

def simulacion():
    master = tk.Tk()
    master.geometry('700x500')
    master.title('Simulación')
    
    
    canvas = Canvas(master,width=1000, height=600, bg='white')
    canvas.pack(expand=YES, fill=BOTH)
    
     
    #EDAD DE LA PALMA

    edad1 = canvas.create_oval(50, 50, 80, 80, fill='gray')
    canvas.create_text(70, 90, text='SEMILLAS GERMINADAS')
    
    edad2 = canvas.create_oval(50, 110, 80, 140, fill='gray')
    canvas.create_text(70, 150, text='PALMA ADULTA')
    
    
    #SINTOMAS PRIMERA FILA
    
    S1 = canvas.create_oval(220, 50, 250, 80, fill='gray')
    canvas.create_text(240, 90, text='Manchas color crema')
    
    S2 = canvas.create_oval(220, 110, 250, 140, fill='gray')
    canvas.create_text(240, 150, text='Radicula color marrón')
    
    S3 = canvas.create_oval(220, 170, 250, 200, fill='gray')
    canvas.create_text(240, 210, text='Semilla con parches blancos')
    
    S4 = canvas.create_oval(220, 230, 250, 260, fill='gray')
    canvas.create_text(240, 270, text='Necrosis')
    
    S5 = canvas.create_oval(220, 290, 250, 320, fill='gray')
    canvas.create_text(240, 330, text='Amarillamiento de la hoja')
    
    S6 = canvas.create_oval(220, 350, 250, 380, fill='gray') 
    canvas.create_text(240, 390, text='Perdida de brillo de los frutos')

    #SINTOMAS SEGUNDA FILA

    S7 = canvas.create_oval(350, 60, 380, 90, fill='gray')
    canvas.create_text(370, 100, text='Moho color verde-azul')    
    
    S8 = canvas.create_oval(350, 120, 380, 150, fill='gray')
    s8 = "Al colocar las semillas infectadas en cámara se pueden evidenciar abanicos de color gris claro"
    button = ttk.Button(canvas,text = 'S.I.', command=lambda: cambio_texto(s8))
    button.place(x=330, y=152)
    
    S9 = canvas.create_oval(350, 180, 380, 210, fill='gray')
    s9 = "Hinchazón anormal de la semilla"
    button = ttk.Button(canvas,text = 'H.A.', command=lambda: cambio_texto(s9))
    button.place(x=330, y=212)
    
    S10 = canvas.create_oval(350, 240, 380, 270, fill='gray')
    s10 = "Presencia de un 'mordisco' en las hojas jovenes"
    button = ttk.Button(canvas,text = 'P.M.', command=lambda: cambio_texto(s10))
    button.place(x=330, y=272)
    
    S11 = canvas.create_oval(350, 300, 380, 330, fill='gray')
    s11 = "Clamidosporas en el corazón de la palma"
    button = ttk.Button(canvas,text = 'C.C.', command=lambda: cambio_texto(s11))
    button.place(x=330, y=332)
    
    S12 = canvas.create_oval(350, 360, 380, 390, fill='gray')
    s12 = "Flagelados aislados en raices"
    button = ttk.Button(canvas,text = 'F.A.', command=lambda: cambio_texto(s12))
    button.place(x=330, y=392)
    
    
    #6 ENFERMEDADES
    
    F1 = canvas.create_oval(450, 50, 480, 80, fill='gray')
    f1 = "ENFERMEDAD DE GERMEN MARRON\n\nTratamiento:\nEl germen marrón se previene manteniendo el contenido de humedad de la\nsemilla por debajo del 19%, durante el período de calentamiento. Se\nrecomienda el tratamiento de la semilla con una mezcla\nfungicida-bactericida (Thiram más Estreptomicina)."
    button = ttk.Button(canvas,text = 'Enfermedad 1', command=lambda: cambio_texto(f1))
    button.place(x=450, y=82)
    
    F2 = canvas.create_oval(450, 120, 480, 150, fill='gray')
    f2 = "ENFERMEDAD DE FITOTOXICIDAD\n\nTratamiento:\nDejar de utilizar lo pesticidas actuales, ya que pueden\nser a base de BHC-gama, cobre o mercurio."
    button = ttk.Button(canvas,text = 'Enfermedad 2', command=lambda: cambio_texto(f2))
    button.place(x=450, y=152)
    
    F3 = canvas.create_oval(450, 190, 480, 220, fill='gray')
    f3 = "ENFERMEDAD DE PUDRICION DE LA SEMILLA\n\nTratamiento:\nSe recomienda el tratamiento de la semilla con una mezcla\nfungicida-bactericida (Thiram más Estreptomicina), El patógeno\nse desarrolla especialmente sobre los restos de pulpa que quedan\nsobre las semillas, cuando éstas no se limpian adecuadamente. por\nello se recomienda el tratamiento de la semilla con sustancias\nprotectoras, además del lavado a fondo."
    button = ttk.Button(canvas,text = 'Enfermedad 3', command=lambda: cambio_texto(f3))
    button.place(x=450, y=222)
    
    F4 = canvas.create_oval(450, 260, 480, 290, fill='gray')
    f4 = "ENFERMEDAD DEL COGOLLO\n\nTratamiento:\n-El patógeno puede ser aislado utilizando\nla técnica de trampeo descrita por Drenth\ny Sendall.\n-Mejora en los drenajes y el mejor balance\nde nutrientes en la palma remoción del tejido\nenfermo y la protección del tejido\nexpuesto con insecticidas, fungicidas y bactericidas.\n-Programa de aspersión para proteger las plantas vecinas,\nla eliminación de los estados avanzados de la enfermedad y\nla renovación temprana de lotes afectados."
    button = ttk.Button(canvas,text = 'Enfermedad 4', command=lambda: cambio_texto(f4))
    button.place(x=450, y=292)
    
    F5 = canvas.create_oval(450, 330, 480, 360, fill='gray')
    f5 = "ENFERMEDAD DE MARCHITEZ LETAL\n\nTratamiento:\nPara esta enfermedad se debe hacer una detección temprana\n de los síntomas y la erradicación de las palmas enfermas."
    button = ttk.Button(canvas,text = 'Enfermedad 5', command=lambda: cambio_texto(f5))
    button.place(x=450, y=362)
    
    F6 = canvas.create_oval(450, 400, 480, 430, fill='gray')
    f6 = "ENFERMEDAD DE MARCHITEZ SORPRESIVA\n\nTratamiento:\nSe debe hacer una identificación temprana de las palmas\nenfermas y se procede a su rápida erradicación,complementada\ncon el manejo adecuado de las gramíneas presentes en los lotes\nafectados y la aplicación de insecticidas en el área, para reducir\nla población de los insectos que pueden estar involucrados en su\ndiseminación."
    button = ttk.Button(canvas,text = 'Enfermedad 6', command=lambda: cambio_texto(f6))
    button.place(x=450, y=432)
    
    
   #////////////////////////////////////////////////////////////
    
    
    #6 ENFERMEDADES:
    
    #GERMEN MARRON
    
    master.after(1000, lambda led=edad1: light_on(canvas,led)) 
    master.after(17000, lambda led=edad1: light_off(canvas,led))
    
    master.after(1000, lambda led=S1: light_on(canvas,led)) 
    master.after(17000, lambda led=S1: light_off(canvas,led))
    
    master.after(1000, lambda led=S2: light_on(canvas,led)) 
    master.after(17000, lambda led=S2: light_off(canvas,led))
    
    master.after(4000, lambda led=S7: light_on(canvas,led)) 
    master.after(17000, lambda led=S7: light_off(canvas,led))
    
    master.after(4000, lambda led=F1: light_on(canvas,led)) 
    master.after(17000, lambda led=F1: light_off(canvas,led))
 
    #////////////////////////////////////////////////////////////
    #FITOTOXICIDAD
    
    master.after(18000, lambda led=edad1: light_on(canvas,led)) 
    master.after(30000, lambda led=edad1: light_off(canvas,led))
    
    master.after(20000, lambda led=S9: light_on(canvas,led)) 
    master.after(30000, lambda led=S9: light_off(canvas,led))
    
    master.after(20000, lambda led=F2: light_on(canvas,led)) 
    master.after(30000, lambda led=F2: light_off(canvas,led))
    
    
    #////////////////////////////////////////////////////////////
    #PUDRICION DE LA SEMILLA
    
    master.after(31000, lambda led=edad1: light_on(canvas,led)) 
    master.after(37000, lambda led=edad1: light_off(canvas,led))
    
    master.after(31000, lambda led=S3: light_on(canvas,led)) 
    master.after(37000, lambda led=S3: light_off(canvas,led))
    
    master.after(31000, lambda led=S8: light_on(canvas,led)) 
    master.after(37000, lambda led=S8: light_off(canvas,led))
    
    master.after(33000, lambda led=F3: light_on(canvas,led)) 
    master.after(37000, lambda led=F3: light_off(canvas,led))
    
    
    #////////////////////////////////////////////////////////////
    #PUDRICION DEL COGOLLO
     
    master.after(39000, lambda led=edad2: light_on(canvas,led)) 
    master.after(46000, lambda led=edad2: light_off(canvas,led))
    
    master.after(39000, lambda led=S4: light_on(canvas,led)) 
    master.after(46000, lambda led=S4: light_off(canvas,led))
    
    master.after(40000, lambda led=S5: light_on(canvas,led)) 
    master.after(46000, lambda led=S5: light_off(canvas,led))
    
    master.after(40000, lambda led=S10: light_on(canvas,led)) 
    master.after(46000, lambda led=S10: light_off(canvas,led))
    
    master.after(43000, lambda led=S11: light_on(canvas,led)) 
    master.after(46000, lambda led=S11: light_off(canvas,led))
    
    master.after(43000, lambda led=F4: light_on(canvas,led)) 
    master.after(46000, lambda led=F4: light_off(canvas,led))
    
    
    #////////////////////////////////////////////////////////////
    #MARCHITEZ LETAL
    
    master.after(48000, lambda led=edad2: light_on(canvas,led)) 
    master.after(55000, lambda led=edad2: light_off(canvas,led))
    
    master.after(48000, lambda led=S4: light_on(canvas,led)) 
    master.after(55000, lambda led=S4: light_off(canvas,led))
    
    master.after(49000, lambda led=S10: light_on(canvas,led)) 
    master.after(55000, lambda led=S10: light_off(canvas,led))
    
    master.after(50000, lambda led=F5: light_on(canvas,led)) 
    master.after(55000, lambda led=F5: light_off(canvas,led))
    
    
    #////////////////////////////////////////////////////////////
    #MARCHITEZ SORPRESIVA
    
    master.after(57000, lambda led=edad2: light_on(canvas,led)) 
    master.after(62000, lambda led=edad2: light_off(canvas,led))
    
    master.after(57000, lambda led=S4: light_on(canvas,led)) 
    master.after(62000, lambda led=S4: light_off(canvas,led))
    
    master.after(58000, lambda led=S5: light_on(canvas,led)) 
    master.after(62000, lambda led=S5: light_off(canvas,led))
    
    master.after(58000, lambda led=S10: light_on(canvas,led)) 
    master.after(62000, lambda led=S10: light_off(canvas,led))
    
    master.after(59000, lambda led=S12: light_on(canvas,led)) 
    master.after(62000, lambda led=S12: light_off(canvas,led))
    
    master.after(60000, lambda led=F6: light_on(canvas,led)) 
    master.after(62000, lambda led=F6: light_off(canvas,led))



    master.mainloop()
    


root = tk.Tk()
root.geometry('200x150')
root.title('Simulación SE')
button_atipico = tk.Button(root,text = 'Comenzar la Simulación', command=simulacion)
button_atipico.place(x=30, y=60) 

root.mainloop()

    