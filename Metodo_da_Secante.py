import sympy as sp
import numpy as np
import Modulo_de_funcoes as det
import math as math
### Entradas ###
f_x ='sp.sin(x)-x**2'
erro=10**-3
x0=0
x1=1
### Entradas ###

### Algoritimo ###
cont=0
xn=x0
xn1=x1
while True:  
    f_xn=float(det.Interativos.calcular(xn,f_x))
    f_xn_1=float(det.Interativos.calcular(xn1,f_x))
    xn = ((xn * f_xn_1) - (xn1 * f_xn)) / (f_xn_1 - f_xn)
    f_xn=float(det.Interativos.calcular(xn,f_x))
    cont+=1
    if f_xn==0:
        break
    if abs(xn1-xn) < erro:
        break
    if abs(f_xn)< erro:
        break
    if abs((xn1-xn)/f_xn)<erro:
        break
    if cont==100:
        break
    xn1=xn
    xn=x1
### Algoritimo ###

###Resultado###
print(f'(Secante) Para f(x) = {f_x}A raiz para a função é x={xn:.4f}, apos {cont} interações')
###Resultado###
