# -*- coding: utf-8 -*- 
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| Code #6                       |#'
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
from math import erf

print 'Simulating...'
print ''

sigma = 0.2	# 20 %
r = 0.1 		# Juros de 10 %/ano
k = 100		# Strike

gamma = 2*r/(sigma**2)

for Tmt in [0.01, 0.5, 1.5]:	# T-t anos
	tau = 0.5*(sigma**2)*(Tmt)
	s2t = np.sqrt(2*tau)
	
	G = []
	S_space = range(10,200)
	for S in S_space:
		x = np.log(float(S)/k)
		d1 = x/s2t + 0.5*(gamma + 1)*s2t
		d2 = x/s2t + 0.5*(gamma - 1)*s2t
		Nd1 = 0.5*(1+erf(d1/np.sqrt(2)))
		Nd2 = 0.5*(1+erf(d2/np.sqrt(2)))
	
		G = np.append(G, S*Nd1 - k*np.exp(-Tmt*r)*Nd2)
	pl.plot(S_space,G)

pl.xlabel('Preço da Ação S(t)'.decode('utf-8'))
pl.ylabel('Preço da Opção G(S,$\\tau$)'.decode('utf-8'))
pl.legend(['T-t = 0.01','T-t = 0.5', 'T-t = 1.5'])
pl.savefig('BS.svg')
pl.show()




