# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| Code #3                       |#'
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
estado = np.array([])

for line in fpt:
	row = line.split()
	aber = float(row[3])
	fech = float(row[6])
	
	if (abs(aber-fech) < 0.01*aber):
		estado = np.append(estado, 0)
	elif aber > fech:
		estado = np.append(estado, 1)
	else:
		estado = np.append(estado, 2)
	
estado = np.flip(estado,0)		# Reverte a ordem

#############################################
## ENCONTRA MATRIZ DE TRANSICAO             #
#############################################
# 0 Neutro - 1 Bear - 2 Bull

P = [ [0.0 for n in range(3)] for p in range(3)]

N = len(estado)
Np = [0,0,0]

for n in range(1,N):
	for s1 in range(3):
		if estado[n-1] == s1:
			Np[s1] = Np[s1] + 1
			for s2 in range(3):
				if estado[n] == s2:
					P[s1][s2] = P[s1][s2] + 1

for s1 in range(3):
	for s2 in range(3):
		P[s1][s2] = 100*P[s1][s2]/Np[s1]
		
print P[0][0], P[0][1], P[0][2]
print P[1][0], P[1][1], P[1][2]
print P[2][0], P[2][1], P[2][2]	

P = [[0.87,0.06,0.07],[0.65,0.17,0.18],[0.73,0.09,0.18]]
	
M = [[0 for a in range(9)] for b in range(9)]		
		
for ni in range(3):
	for nj in range(3):
		n = ni*3+nj
		M[n][n] = M[n][n] + 1
		for nk in range(3):
			if nk != nj:
				m = nk*3+nj
				M[n][m] = M[n][m] - P[ni][nk]

print M
			
E = [[1] for a in range(9)]
mu = np.linalg.solve(M,E)

print mu
			
