#!/usr/bin/env python

import time,math
from multiprocessing import Pool, cpu_count
import numpy as np
from mylib import great_circle

lon1,lat1,lon2,lat2 = 42,0.5,-13,-32
n = 1000000
mat = np.random.randint(-360,360,n*4).reshape(n,4)
mat[np.where(mat==0)] = 1
timeStart = time.time()
po = Pool(processes=cpu_count()-1)
_results = po.map_async(great_circle,(mat[i,:] for i in range(mat.shape[0])))
results =  _results.get()

print(time.strftime('%H:%M:%S', time.gmtime(time.time()-timeStart)))
print('done')
