# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

__author__ = """Prof. Carlo R. da Cunha, Ph.D. <creq@if.ufrgs.br>"""

import os

os.system('clear')
print '.-------------------------------.'
print '| Perceptron                    |#'
print '| ----------                    |#'
print '|                               |#'
print '| By.: Prof. Carlo R. da Cunha  |#'
print '|                               |#'
print '|                     Ago/2018  |#'
print '\'-------------------------------\'#'
print '  ################################'
print ''
print 'Importing Libraries:'

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as pl

print 'Simulating...'
print ''

nh1  = 0
nh2  = 1
nout = 2

#================================#
# CLASSE: Neuron                 #		
#================================#
class Neuron:
	# Initiation function
	def __init__(self, th = 0):
		self.theta = th
		self.sinapse = []	
	
	# Saida Neuronal
	def out(self,z):
		return 1/(1+np.exp(-z))
	
	# Derivada da ativacao
	def g(self,z):
		return np.exp(-z)/((1+np.exp(-z))**2)
	
#================================#
# CLASSE: Neural Network         #		
#================================#	
class Network:
	# Initiation function
	def __init__(self):
		self.neuron = [Neuron() for n in range(5)]
		
		# Biases
		self.biash = np.array([[1],[1]])
		self.bias4 = 1
			
		# Ponderacoes
		self.Wh = rd.random((2,2))
		self.Wo = rd.random((1,2))
		
		# Taxas de aprendizado e inercia
		self.eta = 0.05
		self.alfa = 0.5
		
		self.cWo = self.Wo
		self.cWh = self.Wh
		self.cdb = np.array([[0],[0]])
		
	# Saida da rede
	def out(self,i0,i1):
		I = np.array([[i0],[i1]])
		zh = np.add(np.dot(self.Wh, I), self.biash)
		h = np.array([[self.neuron[n].out(zh[n][0])] for n in range(2)])
		z4 = np.dot(self.Wo, h)[0][0] + self.bias4
		o = self.neuron[4].out(z4)
		
		return o
		
	# Treina a rede
	def train(self,i0,i1,d):
		# Propaga para frente
		I = np.array([[i0],[i1]])
		zh = np.add(np.dot(self.Wh, I), self.biash)
		h = np.array([[self.neuron[n].out(zh[n][0])] for n in range(2)])
		z4 = np.dot(self.Wo, h)[0][0] + self.bias4
		o = self.neuron[4].out(z4)
			
		# Propaga para tras
		Do = (d-o)
		D2 = Do*self.Wo[0][0]
		D3 = Do*self.Wo[0][1]

		dWo = np.multiply(self.eta*Do*self.neuron[4].g(z4), h.T)
		Dh = np.array([[D2*self.neuron[2].g(zh[0][0])],[D3*self.neuron[3].g(zh[1][0])]])
		dWh = np.dot(np.multiply(self.eta, Dh), I.T)		
		db = np.multiply(self.eta, Dh)

		# Incorpora inercia
		self.cWo = np.add(np.multiply(1-self.alfa, dWo), np.multiply(self.alfa, self.cWo))
		self.cWh = np.add(np.multiply(1-self.alfa, dWh), np.multiply(self.alfa, self.cWh))
		self.cdb = np.add(np.multiply(1-self.alfa,db), np.multiply(self.alfa, self.cdb))

		self.Wo = np.add(self.Wo, self.cWo)
		self.Wh = np.add(self.Wh, self.cWh)
		self.biash = np.add(self.biash, self.cdb)
		
	def erro(self):
		return self.out(0,0)**2 + (self.out(0,1)-1)**2 + (self.out(1,0)-1)**2 + self.out(1,1)**2 

###############################
##           MAIN            ##
###############################		
net = Network()
er = []
err = 1
while err > 0.1:
	net.train(0,0,0)
	net.train(0,1,1)
	net.train(1,0,1)
	net.train(1,1,0)
	err = net.erro()
	er.append(err)

print net.out(0,0)
print net.out(0,1)
print net.out(1,0)
print net.out(1,1)


pl.plot(er)
pl.show()
