# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| Code #1                       |#'
print '| -------                       |#'
print '|                               |#'
print '| By.: Prof. Carlo R. da Cunha  |#'
print '|                               |#'
print '|                     Fev/2017  |#'
print '\'-------------------------------\'#'
print '  ################################'
print ''
print 'Importing Libraries:'

import numpy as np
import matplotlib.pyplot as pl

print 'Simulating...'
print ''

# DADOS
P = [10366.7, 9664.73, 9813.07, 10301.1, 10005, 10690.4, 11403.7, 11225.3, 10551.8,
     11112.7, 10233.9, 10166.4, 9494.63, 8598.31, 8926.57, 8129.97, 8621.9, 8736.98,
     8265.59, 7621.3, 7754, 6955.27, 8277.01, 9174.91, 8830.75, 9170.54, 10221.1,
     10106.3, 11296.4, 11786.3]
X = np.arange(len(P))     
pl.figure(1)
pl.subplot(211)
pl.plot(X,P,'bo-')

# ESTATISTICA
m = np.mean(P)
v = np.var(P,ddof=1)
s = np.sqrt(v)
print '<P>    = ' + str(m)
print 'VAR(P) = ' + str(v)
print 'STD(P) = ' + str(s) 

Ym = [m for x in X]
Ys1 = [m+s for x in X]
Ys2 = [m-s for x in X]
pl.plot(X, Ym, '-.')
pl.plot(X, Ys1, 'g:')
pl.plot(X, Ys2, 'g:')

# REGRESSAO
a = np.cov(X,P)[0][1]/np.var(X)
b = np.mean(P)-a*np.mean(X)
Y = [a*x + b for x in X]
pl.plot(X,Y)

# SCEDASTICIDADE: BREUSCH-PAGAN
E = [(p-y)**2 for p,y in zip(P,Y)]	# Residuos
S = np.sum(E)/len(E)						# Variancia
U = [e/S for e in E]						# Normalizacao
pl.subplot(212)
pl.plot(X,U,'o')

a = np.cov(X,U)[0][1]/np.var(X)		# Regressao
b = np.mean(U)-a*np.mean(X)
R = [a*x + b for x in X]
pl.plot(X,R)

T = [(u-r)**2 for u,r in zip(U,R)]	# Residuos

s = 0.5*np.sum(T)
print 'Chi^2  = ' + str(s)

# JACKKNIFE
set1 = [10106.3, 11296.4, 11786.3]
set2 = [10221.1, 11296.4, 11786.3]
set3 = [10221.1, 10106.3, 11786.3]
set4 = [10221.1, 10106.3, 11296.4]

mu1 = np.mean(set1)
mu2 = np.mean(set2)
mu3 = np.mean(set3)
mu4 = np.mean(set4)

mu = np.mean([mu1, mu2, mu3, mu4])
var = 0.75*((mu-mu1)**2 + (mu-mu2)**2 + (mu-mu3)**2 + (mu-mu4)**2)
std = np.sqrt(var)

x = [26, 27, 28, 29]
y = [mu for ix in x]
y1 = [mu+std for ix in x]
y2 = [mu-std for ix in x]

pl.subplot(211)
pl.plot(x,y,'c')
pl.plot(x,y1,'g:')
pl.plot(x,y2,'g:')

# BOOTSTRAPPING
y = [10221.1, 10106.3, 11296.4, 11786.3]
a = np.cov(x,y)[0][1]/np.var(x)
b = np.mean(y)-a*np.mean(x)
Y = [a*ix+b for ix in x]
E = [y1 - y2 for y1,y2 in zip(y,Y)]

na = 0
nb = 0
for k in range(300):
	Es = [E[np.random.randint(len(E))] for n in x]
	Ys = [y1 + e for y1,e in zip(Y,Es)]
	a = np.cov(x,Ys)[0][1]/np.var(x)
	na = na + a/300
	nb = nb + (np.mean(Ys)-a*np.mean(x))/300

X = [26, 27, 28, 29, 30]
Y = [na*x + nb for x in X]
pl.plot(X,Y,'.-')

pl.savefig('stat.svg')
pl.show()