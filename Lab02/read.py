from tkinter import *
from tkinter import filedialog
import tkFileDialog
from PIL import Image, ImageTk
import platform
from tkinter import ttk
from tkinter import messagebox
import cv2
import numpy as np
nombre_img="" 
img_tk=None
img_cv=None

plataform=platform.system()
raiz=Tk()
raiz.title("Image Viewer")
raiz.resizable(0,0)
raiz.geometry("600x600+300+300")
if plataform=="Windows":
	raiz.iconbitmap("mail.ico")
#miFrame=Frame()
#miFrame.pack()

from funciones import *

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

def sumar():
	var=int(cuadroSuma.get())
	#if img_cv==None:	
	#	messagebox.showinfo(message="No se ha cargado una imagen", title="Error")	
	temp1=img_cv
	temp1=img_sum(temp1,var)
	ims = Image.fromarray(temp1)
	imgs = ImageTk.PhotoImage(image=ims) 	
	label_imgsum=Label(image=imgs)
	label_imgsum.place(x=300,y=150)
	suma.mainloop()
	

#Cajas
cuadroSuma=Entry(raiz)
cuadroSuma.grid(row=2,column=3,padx=0,pady=0)


#Button(self,text="Cargar Imagen",command=self.cargar_img).place(x=100,y=100)
botonBuscar=Button(raiz,text="Cargar Imagen",command = cargar_img)
botonSumar=Button(raiz,text="Sumar",command = sumar)
botonBuscar.grid(row=2,column=1)
botonSumar.grid(row=2,column=2)


raiz.mainloop()
