#ifndef UTILS_CUH
#define UTILS_CUH

typedef struct SumTable_s {
  float* l1SumTable;
  float* l2SumTable;
  float* lxSumTable;
  float* lySumTable;
} SumTable;

/*
* Obtenga la información de los hilos máximos admitidos por bloque y el número
de SP por SM
 */
void GetDeviceInfo(int* maxThreadsPerBlock, int* workingThreadsPerBlock);

/*
 * Función auxiliar para asignar memoria en el dispositivo, informar un error si OOM
 */
void AllocateCudaMem(float** pointer, int size);

#endif
