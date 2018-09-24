# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| Code #5                       |#'
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
from matplotlib import animation
from matplotlib import colors

print 'Simulating...'
print ''

#https://scipython.com/blog/the-forest-fire-model/

L = 100

p,f = 0.05, 0.001

mapa = np.random.randint(0,3,size=(L,L))

empty = 0
burning = 1
tree = 2
replacement = 3

#############################################

def iterate(before):
	NLines = len(before)
	NCols = len(before[0])
	after = np.zeros((NLines,NCols))
	
	for ny in range(1,NLines-1):
		for nx in range(1,NCols-1):
			state = before[ny][nx]
			next_state = state
			
			if state == burning:
				next_state = empty
			if state == tree:
				b_val = False
				for ty in range(-1,2):
					for tx in range(-1,2):
						if before[ny+ty][nx+tx] == burning:
							b_val = b_val or True
				if b_val == True or np.random.random() <= f:
					next_state = burning
			if state == empty:
				if np.random.random() <= p:
					next_state = tree
					
			after[ny][nx] = next_state
			
	return after
		
def flood(mp,y,x,c):
	NLines = len(mp)
	NCols = len(mp)
	
	in_x_boundaries = x > 1 and x < NCols-1
	in_y_boundaries = y > 1 and y < NCols-1
	in_boundaries = in_x_boundaries and in_y_boundaries

	if mp[y][x] != c or not in_boundaries:
		return 0
	else:
		mp[y][x] = replacement
		val = 1
		
		val = val + flood(mp,y,x-1,c)
		val = val + flood(mp,y,x+1,c)
		val = val + flood(mp,y-1,x,c)
		val = val + flood(mp,y+1,x,c)
			
		return val
		
def num2(mp,c):
	NLines = len(mp)
	NCols = len(mp)
	
	h = [0 for n in range(NLines*NCols)]	
	
	for y in range(NCols):
		for x in range(NLines):
			dv = flood(mp,y,x,c)
			h[dv] = h[dv] + 1		
			
	return h
	
def num(mp):
	NLines = len(mp)
	NCols = len(mp)
	
	n = [0,0,0]	

	for y in range(NLines):
		for x in range(NCols):
			for c in range(3):
				if mp[y][x] == c:
					n[c] = n[c] + 1
					
	return n
				

if False:	
	ntree = []
	nempt = []
	nburn = []
	for it in range(100):
		n = num(mapa)
		ntree = np.append(ntree, n[0])
		nempt = np.append(nempt, n[1])
		nburn = np.append(nburn, n[2])
		mapa = iterate(mapa)
	
	pl.plot(ntree)
	pl.plot(nempt)
	pl.plot(nburn)
if True:
	for it in range(100):
		mapa = iterate(mapa)
	pl.loglog(num2(mapa,empty),'*')


pl.show()