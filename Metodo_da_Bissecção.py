import numpy as np
import Modulo_de_funcoes as det
### Entradas ###
f_x='sp.sin(x)-x**2'
Intervalo=[0,0.9]
erro=10**(-3)
### Entradas ###

### Algoritimo ###
a=Intervalo[0]
b=Intervalo[1]
cont=0
xm=0
while True:
    xm0=xm
    xm=((a+b)/2)
    f_a=float(det.Interativos.calcular(a,f_x))
    f_b=float(det.Interativos.calcular(b,f_x))
    f_xm=float(det.Interativos.calcular(xm,f_x))

    if f_xm==0:
        break
    if abs(xm-xm0)<erro:
        break
    if abs((xm-xm0)/f_xm)<erro:
        break
    if abs(f_xm)<erro:
        break
    if cont==100:
        break
    if (f_a * f_xm) > 0:
        a=xm
    else:
        b=xm       
    cont+=1

### Algoritimo ###
    

### Resultado ###
print(f'(Bissecção) Para f(X)= {f_x}A raiz para a função é x={xm:.4f}, apos {cont} interações')
### Resultado ###
