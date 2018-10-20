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

print 'Lendo Arquivo...'

# Media Movel
def mmovel(x,theta,s):
	N = len(x)
	ki = -int(np.floor(theta*(s-1)))
	ka = int(np.ceil((1-theta)*(s-1)))
	y = []
	for t in range(N):
		ac = 0
		nu = 0
		for k in range(ki,ka):
			if t-k >= 0 and t-k < N:
				ac = ac + x[t-k]
				nu = nu + 1
		y = np.append(y, ac/nu)
		
	return y

# Segmentacao da lista	
def split(x,s):
	N = len(x)
	n = 0
	ts = 0
	t = []
	y = []
	while(n < N):
		t.append(x[n])
		n = n + 1
		ts = ts + 1
		if ts >= s:
			ts = 0
			y.append(t)
			t = []
	return y

# Media quadratica
def rms(xv):
	z = []
	for x in xv:
		s = len(x)
		ac = 0
		for xi in x:
			ac = ac + xi**2
		z.append(np.sqrt(ac/s))
	return z
	
# Medida canonica
def medida(fv,qe):
	den = 0
	for f in fv:
		den = den + f**qe
	z = []
	for f in fv:
		z.append((f**qe)/den)
	return z
	
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

print 'Simulando...'
print ''

#############################################
## CALCULA RETORNOS                         #
#############################################
f = np.array([])
for n in range(0,len(p)-1):
	f = np.append(f,np.log(p[n+1])-np.log(p[n]))
N = len(f)

# Expoentes
Nq = 40
q_space = np.linspace(-10,10,Nq)

# Soma acumulada
F = np.cumsum(f)-np.mean(f)

na = [[] for n in range(Nq)]
nf = [[] for n in range(Nq)]
da = [[] for n in range(Nq)]

for s in range(4,40):
	# Tendencia
	Y = mmovel(F,0.5,s)
	# Residuo
	X = [Fi-Yi for Fi,Yi in zip(F,Y)]
	# Divide
	Xv = split(X,s)
	# RMS
	Fv = rms(Xv)
	
	nq = 0
	for q in q_space:
		# Medida canonica
		mu = medida(Fv,q)
		# Alfa
		na[nq].append(np.sum([mui*np.log(Fvi) for mui,Fvi in zip(mu,Fv)]))
		da[nq].append(np.log(s))
		# f(a)
		nf[nq].append(np.sum([mui*np.log(mui) for mui in mu]))
		nq = nq + 1

# Alfa e f(alfa)
alfa = []
fa = []
for n in range(Nq):
	C = np.polyfit(da[n],na[n],1)[0]
	alfa.append(C)
	C = np.polyfit(da[n],nf[n],1)[0]
	fa.append(C)

# Dq
D = []
T = []
for n in range(Nq):
	q = q_space[n]
	a = alfa[n]
	f = fa[n]
	
	tau = q*a-f
	Dq = tau/(q-1)
	
	D.append(Dq)
	T.append(tau) 

# Plot
pl.plot(alfa,fa,'o-')
pl.plot(alfa,alfa,'--')
pl.plot(fa,fa,'--')
#pl.plot(q_space,T,'o-')
#pl.plot(q_space,alfa,'o-')
#pl.axis([0,0.88,0,1.75])
#pl.plot(q_space,D,'o')
#pl.savefig('multifrac1.svg')
pl.show()

