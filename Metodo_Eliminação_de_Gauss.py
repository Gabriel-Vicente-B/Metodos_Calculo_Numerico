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

###juntando matrizes A e B e transformando em array float###
AB = np.column_stack((A, B))
AB = np.array(AB, dtype=float)
AB_AUX = np.zeros_like(AB)
###juntando matrizes A e B e transformando em array float###


num_colunas=len(AB)+1
num_linhas=len(AB)


###Eliminação de Gauss####
k=0
for i in range(num_colunas):
    if k==num_linhas:
        break   
    for j in range(num_linhas):
        if k==j or k>j:
            AB_AUX[k]=AB[k]
            continue
        else:   
            p=AB[i][i]
            m=AB[j][i]/AB[i][i]
            AB_AUX[j]=AB[j]-m*AB[i]
    k+=1
    AB=AB_AUX
###Eliminação de Gauss####

###separando A e B###
A=AB[:, :-1]
B=AB[:, -1]
###separando A e B###

###Resolvendo X ###
X = np.linalg.solve(A, B)
###Resolvendo X ###
print(f'(Eliminação de Gauss) A matriz X é:{X}\n')

