import matplotlib.pyplot as plt
import numpy as np
import math

p = 20
e = 1e-3
def funk(x): return math.cos(x) - p * x
def funkfp(x): return -math.sin(x)-p
def funksp(x): return -math.cos(x)

def dikhtomia(a,b):
    c = abs(a + b) / 2
    print("a = "+str(a))
    print("b = "+str(b))
    print("f(a)*f(b) = " + str(funk(a) * funk(b)) + "\n")
    if abs(b - a) > e:
        if funk(c) == 0:
            return c
        elif funk(a) * funk(c) < 0:
            return dikhtomia(a,c)
        else:
            return dikhtomia(b,c)
    else:
        print("Result of Dichotomy = " + str(c))
        return c


def newton(a,b):
    if funk(a) * funksp(a) >= 0:
        x0 = a
    elif funk(b) * funksp(b) >=0:
        x0 = b
    else:
        print("Error")
        return
    x1 = x0 - funk(x0)/funkfp(x0)
    print("f("+str(round(x1,5))+") = "+str(funk(x1)))
    while abs(funk(x1)) > e:
        x0 = x1
        x1 = x0 - funk(x0)/funkfp(x0)
        print("f("+str(round(x1,5))+") = "+str(funk(x1)))
        if abs(x0-x1) < e: break
    print("Result of Newton = "+str(x1))



x = np.arange(-math.pi, math.pi, 0.01)
y = np.cos(x)
py = p * x
plt.plot(x,y,x,py)


a,b = 0.0, 1.0
print('При p=1 получаем точку пересечения графиков на ['+str(a)+', '+str(b)+']')
print("f(a)*f(b) = "+str(funk(a) * funk(b))+'\n')
# При p=1 получаем точку пересечения графиков на [0.6, 0.8]


plt.show()
#dikhtomia(a, b)
newton(a,b)
