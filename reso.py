import matplotlib.pyplot as pl
import numpy as np

beta_space = np.linspace(0.5,100,1000)
SNR1 = []
SNR2 = []
SNR3 = []
D = []

a1 = 1
a2 = 1.5
a3 = 2
b = 1
epsilon = 1

for beta in beta_space:
	S = np.sqrt(2)*a1*(beta**2)*(epsilon**2)*np.exp(-(beta*(a1**2))/(4*b))
	SNR1 = np.append(SNR1, S)
	S = np.sqrt(2)*a2*(beta**2)*(epsilon**2)*np.exp(-(beta*(a2**2))/(4*b))
	SNR2 = np.append(SNR2, S)
	S = np.sqrt(2)*a3*(beta**2)*(epsilon**2)*np.exp(-(beta*(a3**2))/(4*b))
	SNR3 = np.append(SNR3, S)
	D = np.append(D, 1/beta)
	
pl.semilogy(D,SNR1)
pl.semilogy(D,SNR2)
pl.semilogy(D,SNR3)
pl.axis([0,2,0.1,15])
pl.savefig('SNR.svg')
pl.show() 

