import numpy as np
import Modulo_de_funcoes as det
### Entradas ###
f_x='x**(1/2)'
intervalo=[1,4]
n=238

h=(intervalo[1]-intervalo[0])/n

vetor_x=np.linspace(intervalo[0],intervalo[1],n+1)
vetor_fx=[]

for i in vetor_x:
    fx=float(det.Interativos.calcular(i,f_x))
    vetor_fx.append(fx)


valor_final=(h/2)*(vetor_fx[0]+2*(sum(vetor_fx[1:-1]))+vetor_fx[-1])

print(f'(Trapezio Repetido) O valor da integral é: {valor_final}')
