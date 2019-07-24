#ifndef KERNEL_CUH
#define KERNEL_CUH

/*
* Obtien la coincidencia de T en I, la salida se pone en x,y que representa el punto inferior izquierdo
 */
void GetMatch(float* I, float* T, int Iw, int Ih, int Tw, int Th, int* x,
              int* y);

#endif
