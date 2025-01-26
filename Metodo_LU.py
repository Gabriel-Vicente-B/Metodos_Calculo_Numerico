from random import randint
import Modulo_de_funcoes as det
import numpy as np
np.set_printoptions(precision=2)
np.seterr(all='raise')


A=[[2,-1,-1],[2,2,2],[-1,-1,2]]
B=[-1,4,-5]

### permutando caso tenha 0 na primeira linha###
A_format,B_format=det.matrizes.permutacao(A,B)
### permutando caso tenha 0 na primeira linha###

num_colunas=len(A_format)
num_linhas=len(A_format)

A_format = np.array(A_format, dtype=float)
A_aux=np.zeros_like(A_format)

L=np.zeros_like(A_format)
###Eliminação de Gauss####
k=0
for i in range(num_colunas):
    if k==num_linhas:
        break   
    for j in range(num_linhas):
        if k==j or k>j:
            A_aux[k]=A_format[k]
            continue
        else:   
            p=A_format[i][i]
            m=A_format[j][i]/A_format[i][i]
            A_aux[j]=A_format[j]-m*A_format[i]
            L[j][i]=m
    k+=1
    A_format=A_aux
###Eliminação de Gauss####

for i in range(num_colunas):
    L[i][i]=1

U=A_format


###Resolvendo X ###
Y = np.linalg.solve(L, B)
X= np.linalg.solve(U, Y)
###Resolvendo X ###
print(f'(LU) A matriz L é: \n{L}\n\n A matriz U é: \n{U}\n\n A matriz L*Y=B: {Y}\n\n A matriz U*X=Y {X}\n')



