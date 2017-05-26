/*
nvcc -o foo.out
*/

#include <stdio.h>
#include <stdlib.h>

// global declarations
typedef struct {
  int width;
  int height;
  float* elements;
} Matrix;

// functions
int print_mat_by_row(const Matrix M){
  int i,j;
  int n,d;
  
  n = M.height;
  d = M.width;
  
  printf("\nprinting matrix rows -- size: %d, rank: %d\n",n,d);
  for (i=0; i<n; i++)
    {
      printf("row(%d)[",i);
      for (j=0; j<d; j++)
  	{
	  printf(" %g ",M.elements[i * M.width + j]);
	}
      printf("]\n");
    }
  printf("\n");
  return 0;
}

__global__ void matrix_multiply_kernel(Matrix A, const Matrix B, const Matrix C, int aHeight, int aWidth, int bHeight, int bWidth){
  int x,j,k;
  float p;
  x = blockIdx.x;
  
  if (x < aHeight){    
    for(j=0; j< bWidth; j++){       // the num of cols in B
      p=0;                          // reset product to 0
      for(k=0; k < aWidth; k++){    // the num of cols in  A awa num rows in B
	p+=A.elements[x * aWidth + k] * B.elements[k * bWidth + j];
      }
      C.elements[x * bWidth + j] = p;
    }
  }
}

int main (void)
{
  // allocate host variables
  Matrix A,B,C;
  A.height = 4;
  A.width = 2;
  A.elements = (float*) malloc(A.width * A.height * sizeof(float));

  B.height = 2;
  B.width = 3;
  B.elements = (float*) malloc(B.width * B.height * sizeof(float));

  C.height = A.height;
  C.width = B.width;
  C.elements = (float*) malloc(C.width * C.height * sizeof(float));

  // allocate device variables
  Matrix dev_A, dev_B, dev_C;
  cudaMalloc((void**) &dev_A.elements, A.height * A.width * sizeof(float));
  cudaMalloc((void**) &dev_B.elements, B.height * B.width * sizeof(float));
  cudaMalloc((void**) &dev_C.elements, C.height * C.width * sizeof(float));

  // populate host matrices -- in general M.elements[row * M.width + col] = value; 
  A.elements[0 * A.width + 0] = 1;
  A.elements[0 * A.width + 1] = 2;
  A.elements[1 * A.width + 0] = 3;
  A.elements[1 * A.width + 1] = 4;
  A.elements[2 * A.width + 0] = 5;
  A.elements[2 * A.width + 1] = 6;
  A.elements[3 * A.width + 0] = 7;
  A.elements[3 * A.width + 1] = 8;

  B.elements[0 * B.width + 0] = 1;
  B.elements[0 * B.width + 1] = 2;
  B.elements[0 * B.width + 2] = 3;
  B.elements[1 * B.width + 0] = 4;
  B.elements[1 * B.width + 1] = 5;
  B.elements[1 * B.width + 2] = 6;

  // print out the matrices
  print_mat_by_row(A);
  print_mat_by_row(B);
   
  // copy to device
  cudaMemcpy(dev_A.elements, A.elements, A.height * A.width * sizeof(float),cudaMemcpyHostToDevice);
  cudaMemcpy(dev_B.elements, B.elements, B.height * B.width * sizeof(float),cudaMemcpyHostToDevice);
  cudaMemcpy(dev_C.elements, C.elements, C.height * C.width * sizeof(float),cudaMemcpyHostToDevice);

  // invoke the kernel
  matrix_multiply_kernel<<<A.height,1>>>(dev_A,dev_B,dev_C, A.height, A.width, B.height, B.width);

  // Read C from device memory
  cudaMemcpy(C.elements, dev_C.elements, C.height * C.width * sizeof(float),cudaMemcpyDeviceToHost);
  print_mat_by_row(C);
    
  // free up memory
  cudaFree(dev_A.elements);
  cudaFree(dev_B.elements);
  cudaFree(dev_C.elements);

  free(A.elements);
  free(B.elements);
  free(C.elements);
  
  return 0;
}
