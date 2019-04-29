from tkinter import *
from tkinter import filedialog
import tkFileDialog
from PIL import Image, ImageTk
import platform
from tkinter import ttk

import cv2
import numpy as np
nombre_img="" 
img_tk=None
img_cv=None

plataform=platform.system()
raiz=Tk()
raiz.title("Image Viewer")
raiz.resizable(0,0)
raiz.geometry("500x500+300+300")
if plataform=="Windows":
	raiz.iconbitmap("mail.ico")
#miFrame=Frame()
#miFrame.pack()

Keys={}



def getFile():
   raiz.filename=filedialog.askopenfilename(initialdir = "/",title = "Seleccione archivos csv",filetypes = (("Archivos csv","*.csv"),("Todos los Archivos","*.*")))
   Keys["gmailaddress"]=cuadroCorreo.get()
   Keys["gmailpassword"]=cuadroPasword.get()
   Keys["ruta"]=raiz.filename
   Keys["rutaFiles"]=getRuta(Keys["ruta"])


def Execute(): 
	sentMail(Keys)

def cargar_img():
	global nombre_img
	nombre_img=tkFileDialog.askopenfilename(initialdir = "/home/Documents",title = "Select file",filetypes = (("bmp files","*.bmp"),("all files","*.*")))
	global img_tk
	global img_cv
	img_tk = ImageTk.PhotoImage(Image.open (nombre_img).resize((200, 200)))
	img_cv=cv2.imread(nombre_img)
	img_cv = cv2.resize(img_cv, (200, 200))
	img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGBA)
	label = Label (image = img_tk)
	label.place(x=60, y=150)
	mainloop()

#Button(self,text="Cargar Imagen",command=self.cargar_img).place(x=100,y=100)
botonBuscar=Button(raiz,text="Cargar Imagen",command = cargar_img)
botonBuscar.grid(row=2,column=1)


raiz.mainloop()
