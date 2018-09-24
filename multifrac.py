# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| Multifractal                  |#'
print '| ------------                  |#'
print '|                               |#'
print '| By.: Prof. Carlo R. da Cunha  |#'
print '|                               |#'
print '|                     Ago/2018  |#'
print '\'-------------------------------\'#'
print '  ################################'
print ''
print 'Importing Libraries:'

import numpy as np
import matplotlib.pyplot as pl

print 'Simulating...'
print ''

def condiciona(x):
	N = int(np.ceil(np.log2(len(x))))
	
	for n in range(len(x),2**N):
		x = np.append(x, 0)
		
	return x

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
## CALCULA RETORNOS                         #
#############################################
ret = np.array([])
for n in range(0,len(p)-1):
	ret = np.append(ret,np.log(p[n+1])-np.log(p[n]))

# Transorma para um processo ilimitado
r = np.cumsum(ret)-np.mean(ret)

q = np.linspace(-15,15,100)
h = []

for qi in q:
	fluc = []
	x = []
	for s in range(100):
		# Divide em janelas
		Ns = s+1
		b = np.array_split(r, Ns)
	
		# Remove tendencia e encontra flutuacao
		f = 0
		for w in range(Ns):
			c = np.polyfit(np.arange(len(b[w])),b[w],1)
			p = np.poly1d(c)
			y = [p(n) for n in np.arange(len(b[w]))]
			if qi != 0:
				z = np.sum([((yi-bi)**2)**(qi/2) for yi,bi in zip(y,b[w])])/len(y)
			else:
				z = np.sum([np.log((yi-bi)**2) for yi,bi in zip(y,b[w])])/(2*len(y))
			f = f + z/Ns
		
		if qi != 0:
			fluc = np.append(fluc, f**(1.0/qi))
		else:
			fluc = np.append(fluc, np.exp(f))
		x = np.append(x, len(r)/Ns)
	
	xl = [np.log(xi) for xi in x]
	yl = [np.log(fi) for fi in fluc]
	
	a = np.cov(xl,yl)[0][1]/np.var(xl)
	b = np.mean(yl)-a*np.mean(xl)
	yf = [a*xi+b for xi in xl]
	
	h = np.append(h, a)


a = [h[n]+q[n]*(h[n+1]-h[n])/0.1 for n in range(len(q)-1)]
f = [q[n]*(a[n]-h[n])+1 for n in range(len(a))] 

pl.plot(a,f,'o')
pl.show()


