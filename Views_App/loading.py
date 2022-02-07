#! /usr/bin/env python3
    
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
import time
from tkinter import font

FINISH = False

def Loading ():
    global porcentaje, Bar_progress, texto, root

    root = Tk ()
    root.title ("Loadding")
    root.resizable (False, False)
    root.configure (bg="blue")

    ph=PhotoImage (file="App/media/img/Loading_img.png")
    Label (root, image=ph, width=890, height=660).grid (row=0, column=0, rowspan=2, sticky=W+E)

    frame = Frame (root, background="#003333")
    frame.place (x=55, y=540)

    Label (frame, text="Cargando los datos.........................", font=("Cambria 12 bold"), foreground="red", bg="#003333").grid (row=0, column=0, padx=15, sticky=W)
    
    porcentaje = StringVar ()
    Label (frame, textvariable=porcentaje, font=("Cambria 12 bold"), foreground="red", background="#003333").grid (row=0, column=1, sticky=W)

    Bar_progress = ttk.Progressbar (frame, orient="horizontal", mode="determinate", length=750)
    Bar_progress.grid (row=1, column=0, columnspan=3, sticky=W+E, ipady=6, padx=15, pady=5)
            

    start ()
    root.mainloop ()

def start ():
    GB = 50
    deowload = 0
    speed = 1
    while deowload < GB:
        time.sleep (.2)
        Bar_progress['value']+=(speed/GB)*100
        deowload += speed
        porcentaje.set (str (int((deowload/GB)*100))+"%")
        root.update_idletasks ()
    
    FINISH = True
    if FINISH:
        root.destroy ()

