# Laboratorio 5 template Matching

Template Matching ejemplo de ejecución
## Requirements

* CUDA
* c++

## Running

```bash
nvcc -O3 -g -o template-matching bmp_util.c kernel.cu main.cu utils.cu --compiler-options -Wall,-Wextra,-Wno-unused-result

./template-matching archivoEntrada.bmp archivoTemplate.bmp archivoSalida.bmp
```

## Screenshots

### template 1 Ojo

![alt text](https://github.com/RGiskard/TopicosCG/blob/master/Lab05/ojito.bmp)

![alt text](https://raw.githubusercontent.com/RGiskard/TopicosCG/master/Lab05/sharpeiOjo.bmp)

### template 2 Arruga

![alt text](https://github.com/RGiskard/TopicosCG/blob/master/Lab05/ruga.bmp)

![alt text](https://raw.githubusercontent.com/RGiskard/TopicosCG/master/Lab05/sharpeiRuga.bmp)






