# -*- coding: utf-8 -*-
"""
Scientific programmers need long arrays of 
numbers. Vanilla python has a list. Looks 
like an array, but does much more.

Price: slow, and syntax is a bit tedious
"""


import math as ma
nx = 2**20
dx = 1.0/float(nx)
w = 16.0 * ma.pi
    
xa = [i * dx for i in range(0, nx, 1)]
sinxa = [ma.sin(w * xi) for xi in xa]

"""
sin(w*x) calculation takes about 1 second

R is 10 times faster
> system.time( sinx <- sin(16*pi*x) )
   user  system elapsed 
  0.092   0.000   0.092 
"""

"""
Fortunately, there is numpy. Don't even
think about scientific programming without
it
"""

import numpy as np
xb = np.arange(0.0,1.0,dx)
sinxb = np.sin(w*xb)

"""
Even better, the matplotlib plotting
packages are based around numpy
"""

import matplotlib.pyplot as plt
plt.plot(xb,sinxb)
plt.xlabel('x')
plt.ylabel(r'$\sin(\omega  x)$')

