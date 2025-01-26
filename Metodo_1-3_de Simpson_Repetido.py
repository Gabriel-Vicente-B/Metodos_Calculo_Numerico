import numpy as np
import Modulo_de_funcoes as det
### Entradas ###
f_x='x**(1/2)'
intervalo=[1,4]
n=20

h=(intervalo[1]-intervalo[0])/n

vetor_x=np.linspace(intervalo[0],intervalo[1],n+1)
vetor_fx=[]

for i in vetor_x:
    fx=float(det.Interativos.calcular(i,f_x))
    vetor_fx.append(fx)

par=0
impar=0

for i,v in enumerate(vetor_fx):
    if i==0:
        continue
    if i==len(vetor_fx)-1:
        continue
    if i % 2 == 0:
        par+=v
    else:
        impar+=v


valor_final=(h/3)*(vetor_fx[0]+4*impar+2*par+vetor_fx[-1])


print(f'(1/3 de Simpson Repetido) O valor da integral é: {valor_final}')

