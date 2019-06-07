from tkinter import *
from tkinter import filedialog
import tkFileDialog
from PIL import Image, ImageTk
import platform
from tkinter import ttk
from tkinter import messagebox
import cv2
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

nombre_img="" 
img_tk=None
img_cv=None

plataform=platform.system()
raiz=Tk()
raiz.title("Image Viewer")
raiz.resizable(0,0)
raiz.geometry("800x600+300+300")
if plataform=="Windows":
	raiz.iconbitmap("mail.ico")
#miFrame=Frame()
#miFrame.pack()

#from funciones import *

Keys={}


####Kernels

# 3x3 Identity transformation matrix
I = np.eye(3)

# create the scaling transformation matrix
T_s = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])

# create the rotation transformation matrix
T_r = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])

# create the rotation transformation matrix
T_k = np.array([[1, 0, 0], [-0, -1, 0], [0, 0, 1]])

#MAtrix espejo
T_m= np.array([[-1, 0, 0], [-1, 0, 0], [0, 0, 1]])

T_sk= np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
# create combined tranformation matrix
T = T_s @ T_r


#angle 45
Tangle=np.array([[0, 1.5, 0], [-1, 0, 0], [0, 0, 1]])


def rotate():
	img = plt.imread('lena.jpeg')
	# 2x scaling requires a tranformation image array 2x the original image
	img_transformed = np.empty((510, 510, 3), dtype=np.uint8)
	for i, row in enumerate(img):
	    for j, col in enumerate(row):
	        pixel_data = img[i, j,:]
	        input_coords = np.array([i, j,1])
	        i_out, j_out, _ = T_sk @ input_coords
	        img_transformed[i_out, j_out] = pixel_data

	plt.figure(figsize=(5, 5))
	plt.imshow(img_transformed)


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
	sumar.mainloop()

def multiplicar():
	global img_cv
	s=int(cuadroMulti.get())
	img_cv=img_multi(img_cv,s)
	ims = Image.fromarray(img_cv)
	imgs = ImageTk.PhotoImage(image=ims)
	label_imgmul=Label(image=imgs)
	label_imgmul.place(x=300,y=150)
	multiplicar.mainloop()

def gris():
	global img_cv
	img_cv=img_gris(img_cv)
	ims = Image.fromarray(img_cv)
	imgs = ImageTk.PhotoImage(image=ims)
	label_gris=Label(image=imgs)
	label_gris.place(x=300,y=150)
	gris.mainloop()
	

#Cajas
cuadroSuma=Entry(raiz)
cuadroSuma.grid(row=2,column=3,padx=0,pady=0)

cuadroMulti=Entry(raiz)
cuadroMulti.grid(row=2,column=5,padx=0,pady=0)


#Button(self,text="Cargar Imagen",command=self.cargar_img).place(x=100,y=100)
botonBuscar=Button(raiz,text="Cargar Imagen",command = rotate)
botonSumar=Button(raiz,text="Sumar",command = sumar)
botonMulti=Button(raiz,text="Multiplicar",command = multiplicar)
botonGris=Button(raiz,text="Gris",command = gris)
botonBuscar.grid(row=2,column=1)
botonSumar.grid(row=2,column=2)
botonMulti.grid(row=2,column=4)
botonGris.grid(row=2,column=6)

raiz.mainloop()
