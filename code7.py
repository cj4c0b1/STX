# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| Code #7                       |#'
print '| -------                       |#'
print '|                               |#'
print '| By.: Prof. Carlo R. da Cunha  |#'
print '|                               |#'
print '|                     Mai/2018  |#'
print '\'-------------------------------\'#'
print '  ################################'
print ''
print 'Importing Libraries:'

import numpy as np
import matplotlib.pyplot as pl

print 'Simulating...'
print ''

delta_t = 0.1
mu = 0.2
sigma = 1
theta = 3

X1 = np.array([0])
X2 = np.array([0])
X3 = np.array([1])
X4 = np.array([0])
X5 = np.array([0])

# Milstein Method
def Milstein(X, r):
	a = r[0]
	b = r[1]
	c = r[2]
	delta_W = np.random.normal(loc = mu, scale = np.sqrt(delta_t))
	y = X[-1] + a*delta_t + b*delta_W + 0.5*c*b*(delta_W*delta_W - delta_t)
	return np.append(X, y)

# Martingale
def Martingale(X):
	return np.append(X, np.random.normal(loc = X[-1], scale = np.sqrt(delta_t)))

# dX = u.dt + s.dW
def Brown(X):
	return [mu, sigma, 0]

# dX = u.X.dt + s.X.dW		
def Geom(X):
	a = mu*X[-1]
	b = sigma*X[-1]
	c = sigma
	return [a, b, c]

# dX = theta.(u-X)dt + s.dW
def OU(X):
	a = theta*(mu-X[-1])
	b = sigma
	return [a, b, 0]

# dX = theta.(u-X)dt + s.sqrt(X).dW	
def CIR(X):
	a = theta*(mu-X[-1])
	b = sigma*np.sqrt(X[-1])
	c = sigma/2
	return [a, b, c]

#=====================================#
# LOOP PRINCIPAL                      #
#=====================================#
for it in range(350):
	r2 = Brown(X2)				
	r3 = Geom(X3)				
	r4 = OU(X4)					
	r5 = CIR(X5)					
	
	X1 = Martingale(X1)
	X2 = Milstein(X2, r2)
	X3 = Milstein(X3, r3)
	X4 = Milstein(X4, r4)
	X5 = Milstein(X5, r5)

pl.plot(X5)
pl.xlabel('Tempo')
pl.ylabel('X(t)')
pl.title('dX = theta.(u-X)dt + s.sqrt(X).dW')
pl.savefig('SP4.svg')
pl.show()
			
