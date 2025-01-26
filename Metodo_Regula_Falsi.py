import sympy as sp
import numpy as np
import Modulo_de_funcoes as det

### Entradas ###
f_x = 'sp.sin(x)-x**2'
erro=10**-2
intervalo=[0,0.9]



### Entradas ###

### Algoritimo ###
a=intervalo[0]
b=intervalo[1]
cont=0

while True:  
    f_a=float(det.Interativos.calcular(a,f_x))
    f_b=float(det.Interativos.calcular(b,f_x))
    xn = ((a * f_b) - (b * f_a)) / (f_b - f_a)
    f_xn=float(det.Interativos.calcular(xn,f_x))
    cont+=1
    if f_xn==0:
        break
    if abs(a-xn) < erro:
        break
    if abs(f_xn)< erro:
        break
    if abs((a-xn)/f_xn)<erro:
        break
    if cont==100:
        break
    b=xn
### Algoritimo ###

###Resultado###
print(f'(Regula Falsi) Para f(x) = {f_x} A raiz para a função é x={xn:.4f}, apos {cont} interações')
###Resultado###
