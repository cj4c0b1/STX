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

colors_list = [(0,0,0), (1,0,0), (0,1,0), 'green']
cmap = colors.ListedColormap(colors_list)
bounds = [0,1,2,3]
norm = colors.BoundaryNorm(bounds, cmap.N)

L = 200

p,f = 0.05, 0.001

mapa = np.random.randint(0,3,size=(L,L))

empty = 0
burning = 1
tree = 2

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
		
fig = pl.figure(figsize=(10,6.25))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(mapa, cmap = cmap, norm = norm)

def animate(i):
	im.set_data(animate.X)
	animate.X = iterate(animate.X)
	
animate.X = mapa	
	
anim = animation.FuncAnimation(fig, animate, interval = 100)
pl.show()

