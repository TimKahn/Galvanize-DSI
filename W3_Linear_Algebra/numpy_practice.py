import numpy as np

#First exercise
'''
a = np.arange(1,101).reshape(10,10)
print(a.shape)
print(a.mean(axis=1))
print(a.mean(axis=0))
print(a[4,:])
print(np.log(a))
print(np.cumsum(a, axis=1))
print(np.power(a, 2))
l = np.linspace(11,23)
print(l)
print(l.shape)
'''

#Second exercise
'''
labels = np.array(["A2M", "FOS", "BRCA2","CPOX"])
r1 = np.array([0.12,0.08,0.06,0.02])
r2 = np.array([0.01,0.07,0.11,0.09])
r3 = np.array([0.03,0.04,0.04,0.02])
r4 = np.array([0.05,0.09,0.11,0.14])

genes = np.vstack([r1, r2, r3, r4])
print(genes.mean(axis=1))
print(genes.mean(axis=0))
print(genes.max())
sortgenes =
'''
