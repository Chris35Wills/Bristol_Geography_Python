# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:34:22 2015

@author: steph
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
import scipy.sparse.linalg as sla
import scipy.linalg as la
import time


def poissonOp(L,nx,ny,dx):
    """ 
    Set non-zero entries of L so that
    Lu = r is Poisson's equation discretized
    on a cell-centered nx * ny uniform mesh
    
    needs L[i,j], so works with numpy matrix
    and sparse dok matrix    
    
    """
    def idof(ix,iy):
        return ix + nx*iy
    
    for ix in xrange(0,nx):
        for iy in xrange(0,ny):
            p = idof(ix,iy)
            e = idof(ix+1,iy)
            w = idof(ix-1,iy)
            n = idof(ix,iy+1)
            s = idof(ix,iy-1)
   
            L[p,p] = dx**2 * 1.0
            
            if (ix > 0):
                L[p,w] = -1.0
                L[p,p] = L[p,p] + 1.0
                
            if (ix < nx-1):
                L[p,e] = -1.0
                L[p,p] = L[p,p] + 1.0
                    
            if (iy > 0):
                L[p,s] = -1.0
                L[p,p] = L[p,p] + 1.0       
            
            if (iy < ny-1):
                L[p,n] = -1.0
                L[p,p] = L[p,p] + 1.0
    
    return L    

def poissonSolve(nx, sparse, plotMat, plotSoln):
    ny = nx
    N = nx*ny 
    dx = 1.0/float(nx)
    x = np.arange(0.5*dx,1.0,dx)
    #y = np.arange(0.5*dx,1.0,dx)
    xf = np.arange(0.0,1.0+0.5*dx,dx)
    yf = np.arange(0.0,1.0+0.5*dx,dx)
    r = np.zeros(N) 
    r[0:nx] = np.sin(4.0*np.pi*x)
    r[ (N-nx):N] = np.cos(4.0*np.pi*x)

    time_assembly = 0.0
    time_solve = 0.0

    if (sparse):
        # Assemble        
        time_assembly = time.time()
        # dok is a nice format for building         
        Ldok = sp.dok_matrix((N,N))
        Ldok = poissonOp(Ldok,nx,ny,dx)
        #but csr is the format that solvers want        
        Ls = sp.csr_matrix(Ldok)        
        time_assembly = time.time() - time_assembly 
        if (plotMat):
            plt.figure()
            plt.imshow(Ldok.todense(),cmap='RdYlBu_r')
        # Solve
        time_solve = time.time()
        u = sla.spsolve(Ls,r).reshape((nx, ny))
        time_solve = time.time() - time_solve
    else:
        # Assemble
        time_assembly = time.time()
        Ld = np.zeros(N*N).reshape((N,N))
        Ld = poissonOp(Ld,nx,ny,dx)
        time_assembly = time.time() - time_assembly
        if (plotMat):
            plt.figure()
            plt.imshow(Ld,cmap='RdYlBu_r')
        # Solve
        time_solve = time.time()
        u = la.solve(Ld,r).reshape((nx, ny))
        time_solve = time.time() - time_solve
    
    if (plotSoln):
        plt.figure()
        plt.pcolormesh(xf,yf,u)

    return time_assembly, time_solve


#ta,ts = poissonSolve(16,True,True,True)

#ta,ts = poissonSolve(256,True,False,True)

n = np.array([16,32,64,128,256,512])
tas = np.zeros(len(n))
tss = np.zeros(len(n))

for i in xrange(0,len(n)):
    tas[i],tss[i] = poissonSolve(n[i],True,False,False)

tad = np.zeros(4)
tsd = np.zeros(4)
for i in xrange(0,4):
    tad[i],tsd[i] = poissonSolve(n[i],False,False,False)
    
#%%  
plt.figure()
plt.loglog(n,tss,'bo-',label='UMFPACK')
plt.plot(n[0:4],tsd[0:4],'ro-',label='LAPACK')  
plt.xlabel('degrees of freedom')
plt.ylabel('solve time')
plt.legend()