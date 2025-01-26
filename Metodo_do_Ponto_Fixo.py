import sympy as sp
import numpy as np
import sys
import Modulo_de_funcoes as det
from random import randint

### Entradas ###
f_x = '(x**2)+x-6'
g_x = '(6/x)-1'
erro=10**-3
x0=-2.5
### Entradas ###

####achadno derivada da g_x######
g_linhax=det.Interativos.derivada(g_x)
####achando derivada da g_x######
"""
####achando intervalo e verificando######
while True:
#### g(x) e g'(x) devem ser continuas no intervalo####
    cont_gx=float(det.Interativos.continuidade(g_x,intervalo))
    cont_glx=float(det.Interativos.continuidade(g_linhax,intervalo))
#### g(x) e g'(x) devem ser continuas no intervalo####
####  |g'(x)| <= k < 1####
    val_g_x=str(g_linhax)
    conv=det.Interativos.convergencia(val_g_x,intervalo)
####  |g'(x)| <= k < 1####
    if cont_gx == True and cont_glx == True and conv == True:
        break
####achando intervalo e verificando###### 
"""
xn=x0
cont=0
while True:

    xn=float(det.Interativos.calcular(x0,g_x))
    f_xn=float(det.Interativos.calcular(xn,f_x))
   
    if abs(xn-x0)<erro:

        break
    if abs(f_xn)<erro:
        break
    if cont==100:
        break
    x0=xn
    cont+=1


print(f'(Ponto Fixo) Para f(x) = {f_x}A raiz para a função é x={xn:.4f}, apos {cont} interações')
