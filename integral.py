from math import exp
def f(x):
    return x*exp(-x)
intgr1=0.0
x=0
xmax=50
dx=0.001
while x<xmax:
    intgr1+=dx*f(x)
    x+=dx
print("Integral=", intgr1, "error=", abs(1-intgr1))
 
