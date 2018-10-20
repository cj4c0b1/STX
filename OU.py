import matplotlib.pyplot as pl
import numpy as np
import numpy.random as rd

dt = 1
eta = 0.019

T = np.array([[-0.1, 0.1*eta],[0.1*eta,-0.1]])
B = np.array([[1, 0],[0,1]])
X = np.array([[0.3],[0.45]])

x = []
y = []
cnt = 0
last = True
his = [0 for n in range(1000)]
for loop in range(10000):
	r1 = rd.normal(loc = 0, scale = np.sqrt(dt))
	r2 = rd.normal(loc = 0, scale = np.sqrt(dt))
	dW = np.array([[r1], [r2]])

	A = np.dot(T,X)
	X = X + A*dt + np.dot(B,dW)

	x = np.append(x, X[0][0])
	y = np.append(y, X[1][0])
	
	updn = X[0][0] > X[1][0]
	if updn ^ last:
		if cnt < 1000:
			his[cnt] = his[cnt] + 1
		cnt = 0
	else:
		cnt = cnt + 1
		
	last = updn
		
#pl.plot(x,y,'.')
#pl.plot(x)
#pl.plot(y)
pl.loglog(his[1:25])
pl.show()