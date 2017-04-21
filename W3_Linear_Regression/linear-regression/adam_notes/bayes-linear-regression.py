#!/usr/bin/env python
"""
linear regression example

http://pymc-devs.github.io/pymc3/notebooks/getting_started.html

"""

from __future__ import division
import os,sys,pickle
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pymc3 as pm
from pymc3.backends import Text

from mylib import *

import logging
_logger = logging.getLogger("theano.gof.compilelock")
_logger.setLevel(logging.ERROR)

if not os.path.isdir("traces"):
    os.mkdir("traces")

seed = 42
n = 20
b0_true = -0.3
b1_true = 0.5
x,y = get_simple_regression_samples(n,b0=b0_true,b1=b1_true,seed=seed)
niter = 2000
run_trace = False


niter = 2000
with pm.Model():

    ## Priors for unknown model parameters
    b0 = pm.Normal('b0', mu=0, sd=10)
    betas = pm.Normal('betas', mu=0, sd=10, shape=x.shape[1])
    sigma = pm.HalfNormal('sigma', sd=1)

    ## Expected value of outcome
    mu = b0 + betas[0]*x[:,0]

    ## Likelihood (sampling distribution) of observations
    y_obs = pm.Normal('y_obs', mu=mu, sd=sigma, observed=y)

    ## inference
    start = pm.find_MAP()
    step = pm.NUTS() # Hamiltonian MCMC with No U-Turn Sampler

    db = Text('traces')
    trace = pm.sample(niter, step, start,random_seed=123, progressbar=True, trace=db)
    
## create a fit from the traces
b0_hat =  trace['b0'][-500:].mean()
b1_hat = trace['betas'][:,0][-500:].mean()
y_pred_pymc = b0_hat + (b1_hat*x[:,0])

## make a least squares fit    
coefs_lstsq = fit_linear_lstsq(x,y)
y_pred_lstsq = coefs_lstsq[0] + (coefs_lstsq[1]*x[:,0])

## plot the fits
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.plot(x[:,0],y,'ko')
ax.plot(x[:,0],y_pred_pymc,color='red',linewidth=5.0,label='pymc',alpha=0.5)
ax.plot(x[:,0],y_pred_lstsq,color='black',label='least squares')

## add a credible interval (1sd)
upper = y_pred_pymc + y_pred_pymc.std() * 0.5
lower = y_pred_pymc - y_pred_pymc.std() * 0.5
ax.plot(x[:,0],upper,color='black',label='upper')
ax.plot(x[:,0],lower,color='black',label='lower')

ax.legend()
plt.show()

## print summary
print("\n-----------------------")
print("truth: b0=%s,b1=%s"%(b0_true,b1_true))
print("pymc fit: b0=%s,b1=%s"%(round(b0_hat,3),round(b1_hat,3)))
print("lstsq fit: b0=%s,b1=%s"%(round(coefs_lstsq[0],3),round(coefs_lstsq[1],3)))
