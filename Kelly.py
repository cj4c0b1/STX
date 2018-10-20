import numpy as np
import random as rd
import matplotlib.pyplot as pl

N = 4
ro = 0.5
r = np.array([[0.96], [0.8], [0.3], [0.65]])
S = np.array([[(r[j][0]-ro)*(r[k][0]-ro) for j in range(N)] for k in range(N)])

def erro(ul):
	global S, ro, r, N	
	
	I = np.array([[1] for n in range(N)])
		
	ac = 0
	for el in np.dot(S,ul) + (ro-1)*(r-ro*I):
		ac = ac + el**2

	return np.sqrt(ac)

threshold = 0.3
u = np.array([[threshold/N] for n in range(N)])
delta = 0.0001
beta = 50

lastE = 1E5
y = []
IT = 1000000
for it in range(IT):
	pos = rd.randint(0,N-1)

	t = u.copy()
	
	if t[pos] > delta and (np.asarray(t) < threshold-delta/(N-1)).sum() >= N-1:
		for n in range(N):
			if n == pos:
				t[n] = t[n] - delta
			else:
				t[n] = t[n] + delta/(N-1)
	
	E = erro(t)

	if E < lastE:
		u = t.copy()
		lastE = E
	elif rd.random() < np.exp(-beta*(E-lastE)):
		u = t.copy()
		lastE = E
		
	y.append(E)
	beta = beta + 10000.0/IT
	
print u	
print u.sum()
pl.plot(y)
pl.show()