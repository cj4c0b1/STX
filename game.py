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
price = np.array([])

for line in fpt:
	row = line.split()
	price = np.append(price, float(row[6]))
price = np.flip(price,0)		# Reverte a ordem

t_space = np.linspace(0.8,1,2000)

y = []

#for threshold in t_space:
# Inicializacoes

threshold = 0.885
#for threshold in t_space:
	
BTC = 1
BRL = 0
ativo = True
maximo = -1
minimo = 1E7

venda_x = []
venda_y = []
compra_x = []
compra_y = []

n = 0
for p in price:
	if p > maximo:
		maximo = p
	if p < minimo:
		minimo = p
		
	if p < maximo*threshold and ativo == True:
		# Vende
		BRL = BTC*p
		ativo = False
		minimo = 1E7
				
		venda_x = np.append(venda_x,n)
		venda_y = np.append(venda_y,p)		
	
	if p > minimo*(2-threshold) and ativo == False:
		# Compra
		BTC = BRL/p
		ativo = True
		maximo = -1	
				
		compra_x = np.append(compra_x,n)
		compra_y = np.append(compra_y,p)
		
	n = n+1
	#y = np.append(y,BTC)
	
#pl.semilogy(t_space,y)
			
print price[0]
print BTC, BRL
pl.semilogy(price)
pl.semilogy(compra_x,compra_y,'bo')
pl.semilogy(venda_x,venda_y,'r*')
pl.axis([1500,1700,1800,20000])
pl.legend(['','compra','venda'])

pl.show()	