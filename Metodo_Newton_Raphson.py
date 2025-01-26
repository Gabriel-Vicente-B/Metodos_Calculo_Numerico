import sympy as sp
import numpy as np
import Modulo_de_funcoes as det

### Entrdas ###
f_x = 'sp.sin(x)-x**2'
erro=10**-3
x0=0
### Entradas ###

### Algoritimo ###
f_linhax=det.Interativos.derivada(f_x)
xn=x0
cont=0
while True:  
    x0=xn
    f_a=float(det.Interativos.calcular(xn,f_x))
    f_b=float(det.Interativos.calcular(xn,f_linhax))
    xn=xn-(f_a/f_b)
    f_xn=float(det.Interativos.calcular(xn,f_x))
    cont+=1
    if f_xn==0:
        break
    if abs(xn-x0) < erro:
        break
    if abs(f_xn)< erro:
        break
    if abs((xn-x0)/f_xn)<erro:
        break
    if cont==100:
        break
### Algoritimo ###

###Resultado###
print(f'(Newton Raphson Para f(x) = {f_x} A raiz para a função é x={xn:.4f}, apos {cont} interações')
###Resultado###
