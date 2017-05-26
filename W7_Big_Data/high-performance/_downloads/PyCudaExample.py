#!/usr/bin/env python

## import and initialize
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

## transfer data to the device
import numpy as np
a = np.random.randn(4,4)

## most cuda devices only support single precision so
a = a.astype(np.float32)

## allocate memory on the device
a_gpu = cuda.mem_alloc(a.nbytes)

## transfer data to the gpu
cuda.memcpy_htod(a_gpu, a)

## create a kernel
mod = SourceModule("""
  __global__ void doublify(float *a)
  {
    int idx = threadIdx.x + threadIdx.y*4;
    a[idx] *= 2;
  }
  """)

## get the reference to the function
func = mod.get_function("doublify")

## call the function
func(a_gpu, block=(4,4,1))

## get the data back from the gpu and print it
a_doubled = np.empty_like(a)
cuda.memcpy_dtoh(a_doubled, a_gpu)
print a_doubled
print a



