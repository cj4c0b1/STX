# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| Code #8                       |#'
print '| -------                       |#'
print '|                               |#'
print '| By.: Prof. Carlo R. da Cunha  |#'
print '|                               |#'
print '|                     Jun/2017  |#'
print '\'-------------------------------\'#'
print '  ################################'
print ''
print 'Importing Libraries:'

import numpy as np
import matplotlib.pyplot as pl

print 'Simulating...'
print ''

c = 0								# Constante para AR
p = 1								# Ordem do processo AR
q = 2								# Ordem do processo MA
									
# Condicoes iniciais
x = [0 for n in range(p)]								# AR
y = [0 for n in range(q)]								# MA
e = [np.random.normal(0,1) for n in range(q)]	# MA-Choque
z = [0 for n in range(p)]								# ARMA

# Parametros
phi = np.random.random_sample((p,))
theta = np.random.random_sample((q,))

# Tempo
for t in range(p,1000):		
	xt = c + np.dot(x[-p:],phi) + np.random.normal(0,1)
	x = np.append(x, xt)
	
	et = np.random.normal(0,1)	
	yt = c + et + np.dot(e[-q:],theta)
	y = np.append(y, yt)
	e = np.append(e, et) 
	
	zt = c + np.dot(z[-p:],phi) + np.random.normal(0,1) + np.dot(e[-q:],theta)
	z = np.append(z, zt) 
	
# Plot
pl.plot(z)
pl.show()