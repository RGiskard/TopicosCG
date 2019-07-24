# Proyecto 

Transformada de Haar Paralelo y secuencial
## Requirements

* CUDA
* c++
* QT

## Running

```bash
nvcc Imagen.h main.cu -o program -lm -lpthread -lX11

```

## Screenshots

### Ejecución interfaz gráfica

![alt text](https://raw.githubusercontent.com/RGiskard/TopicosCG/master/Final/Data/haarseq1.png)

## Tabla Comparativa tiempos
| Resolucion  | CPU  | GPU |
| :------------ |:---------------:| -----:|
| 512x512      | 75.431 | 	1.62 |
| 512x512     | 77.001       |  1.53 |
| 1000x1000 | 298.195        |    4.72 |
|1000x500|	132.822|	2.59|
|1000x180|	54.952|	1.14|
|1001x1001|	262.093|	4.68|
|1001x1001|	282.516|	4.65|
|1024x1024|	343.029|	4.93|
|1024x1024|	340.84|	5.00|
|1200x800|	258.979|	4.66|
|1200x800|	262.766|	4.49|
|1200x800|	256.271|	4.44|
|1200x800|	260.928|	4.48|
|1200x800|	255.702|	4.45|
|7168x7168|	17026.9|	207.05|







