import cv2
import numpy as np
 
def img_sum(img,inc):
	alto,ancho,bpp = np.shape(img)
	for px in range(0,alto):
		for py in range(0,ancho):
			r=img[px][py][0]
			g=img[px][py][1]
			b=img[px][py][2]
			if (r + inc) > 255:
				img[px][py][0]=255
			else:
				img[px][py][0]=r+inc
			if (g + inc) > 255:
				img[px][py][1]=255
			else:
				img[px][py][1]=g+inc
			if (b + inc) > 255:
				img[px][py][2]=255
			else:
				img[px][py][2]=b+inc
	return img

def img_multi(img,inc):
	alto,ancho,bpp = np.shape(img)
	for px in range(0,alto):
		for py in range(0,ancho):
			r=img[px][py][0]
			g=img[px][py][1]
			b=img[px][py][2]
			img[px][py][0]=r*inc
			img[px][py][1]=g*inc
			img[px][py][2]=b*inc
	return img
def img_gris(img):
	alto,ancho,bpp = np.shape(img)
	for px in range(0,alto):
		for py in range(0,ancho):
			r=img[px][py][0]
			g=img[px][py][1]
			b=img[px][py][2]
			gris=0.2989 * r + 0.5870 * g + 0.1140 * b
			img[px][py][0]=img[px][py][1]=img[px][py][2]=gris
	return img
