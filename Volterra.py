import matplotlib.pyplot as pl
import numpy as np

a = 0.25
b = 0.76
d = 0.51
g = 0.88

dt = 0.1

V = 1


xn = 1.1
yn = 2.1
V1 = a*np.log(yn)+g*np.log(xn)-b*yn-d*xn
print V1

x = []
y = []

for it in range(400):
	xn1 = xn/(1-dt*a+dt*b*yn)
	yn1 = yn*(1-dt*g+dt*d*xn1)

	xn = xn1
	yn = yn1
	
	x.append(xn)
	y.append(yn)
	
pl.plot(x)
pl.plot(y)
pl.savefig('Volterra2.svg')
pl.show()

quit()
xn = 3.1
yn = 1.1
V2 = a*np.log(yn)+g*np.log(xn)-b*yn-d*xn
print V2

x = []
y = []

for it in range(100):
	xn1 = xn/(1-dt*a+dt*b*yn)
	yn1 = yn*(1-dt*g+dt*d*xn1)

	xn = xn1
	yn = yn1
	
	x.append(xn)
	y.append(yn)
	
pl.plot(x,y)

xn = 2.5
yn = 1.7
V3 = a*np.log(yn)+g*np.log(xn)-b*yn-d*xn
print V3

x = []
y = []

for it in range(100):
	xn1 = xn/(1-dt*a+dt*b*yn)
	yn1 = yn*(1-dt*g+dt*d*xn1)

	xn = xn1
	yn = yn1
	
	x.append(xn)
	y.append(yn)
	
pl.plot(x,y)
pl.xlabel('Popula$\c{c}\~a$o de presas')
pl.ylabel('Popula$\c{c}\~a$o de predadores')
pl.legend([V1,V2,V3])
#pl.savefig('Volterra.svg')
pl.plot([g/d],[a/b],'o')
print g/d,a/b

pl.show()
