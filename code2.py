# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| Code #2                       |#'
print '| -------                       |#'
print '|                               |#'
print '| By.: Prof. Carlo R. da Cunha  |#'
print '|                               |#'
print '|                     Mar/2018  |#'
print '\'-------------------------------\'#'
print '  ################################'
print ''
print 'Importing Libraries:'

import numpy as np
import matplotlib.pyplot as pl

print 'Simulating...'
print ''

#############################################
## LE ARQUIVO                               #
#############################################
# 0:Mes, 1:Dia, 2:Ano, 3:Abertura, 4:Maxima, 
# 5:Minima, 6:Fechamento, 7:Volume, 8:MarketCap
fpt = open('btc.dat','r')
p = np.array([])

for line in fpt:
	row = line.split()
	p = np.append(p, float(row[6]))
p = np.flip(p,0)		# Reverte a ordem

#############################################
## CALCULA RETURNOS                         #
#############################################
r = np.array([])
for n in range(0,len(p)-1):
	r = np.append(r,np.log(p[n+1])-np.log(p[n]))

#############################################
# PSD                                       #
#############################################
# Janela de Hann
h = np.hanning(len(r))								
rw = [ir*ih for ir,ih in zip(r,h)]

# FFT
F = np.fft.fft(rw)									

# PSD
S = [(f*np.conj(f)).real for f in F]			
S = S[0:len(S)/2]

# Autocorrelacao
A = np.fft.ifft(S).real								

#############################################
# PLOT                                      #
#############################################
pl.subplot(221)
pl.semilogy(p)
pl.subplot(223)	
pl.plot(r)
pl.subplot(222)
pl.plot(S)
pl.subplot(224)
pl.plot(A)

#pl.savefig('fft.svg')
pl.show()	
			
