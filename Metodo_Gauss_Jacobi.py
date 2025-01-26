import numpy as np
import Modulo_de_funcoes as det
np.set_printoptions(precision=4)
np.seterr(all='raise')


A=[[2,-1,-1],[2,2,2],[-1,-1,2]]
B=[-1,4,-5]
x_0=[0,0,0]
lim_interações=100
erro=0.00001



def matriz_isolada(A,B):
    m_final=np.zeros_like(A,dtype=float)
    for i in range(len(A)):
        for j in range(len(A)):
            if i==j:
                m_final[i][j]=B[i]/A[i][j]
            else:
                m_final[i][j]=(-1*A[i][j]/A[i][i])

    return m_final

def metodo_interativo(matriz,x0):
    linha_aux=[]
    matriz_aux=[]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i==j:
                linha_aux.append(matriz[i][j])
            else:
                linha_aux.append(matriz[i][j]*x0[j])
        matriz_aux.append(linha_aux)
        linha_aux=[]

    x1= np.sum(matriz_aux,axis=1)
    return x1




matriz_P_interação=matriz_isolada(A,B)
cont=0

while True:

    X_1=metodo_interativo(matriz_P_interação,x_0)
    e=det.matrizes.convergencia(x_0,X_1)

    if e<erro:
        break
    if cont == lim_interações:
        break
    x_0=X_1 

    cont+=1


print(f'(GAUSS JACOBI) A matriz X é:{X_1}\n , após {cont} interações.')