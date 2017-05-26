#!/usr/bin/env python


from multiprocessing import Pool, cpu_count
import numpy as np
import time
import math


def great_circle(args):
    lon1,lat1,lon2,lat2 = args
    radius = 3956
    x = math.pi/180.0
    a = (90.0-lat1)*(x)
    b = (90.0-lat2)*(x)
    theta = (lon2-lon1)*(x)
    c = math.acos((math.cos(a)*math.cos(b)) +
                  (math.sin(a)*math.sin(b)*math.cos(theta)))
    return radius*c

lon1,lat1,lon2,lat2 = 42,0.5,-13,-32
n = 1e06
mat = np.zeros((n,4),)
mat = mat + [lon1,lat1,lon2,lat2]

timeStart = time.time()
po = Pool(processes=cpu_count()-1)
_results = po.map_async(great_circle,(mat[i,:] for i in range(mat.shape[0])))
results =  _results.get()

print time.strftime('%H:%M:%S', time.gmtime(time.time()-timeStart))
print 'done'
