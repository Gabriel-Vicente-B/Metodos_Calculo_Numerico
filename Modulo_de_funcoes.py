import sympy as sp
import numpy as np
from random import randint
from sympy import symbols, sqrt
import Modulo_de_funcoes as det
import sympy as sp
import sys
import math as math

class Interativos: 
    def calcular(x,f):
        if type(f)==str:
            return eval(f)
        else:
            v=x
            x = sp.symbols('x')
            x=f.subs(x,v)
            return x
        
    def derivada(func):
        x = sp.symbols('x')
        y = sp.symbols('y')
        f_x=eval(func)
        f_linha=sp.diff(f_x,x)
        return f_linha

    def intervalo(f_x):
        cont=0
        while True:
            teste_a=randint(-5,5)
            teste_b=randint(-5,5)
        
            if teste_a!=teste_b: 
                if teste_a>teste_b:
                    b=teste_a
                    a=teste_b
                else:
                    a=teste_a
                    b=teste_b
            else:
                continue

            teste_a=Interativos.calcular(a,f_x)
            teste_b=Interativos.calcular(b,f_x)


            if type(teste_a)==float or type(teste_a)==int:
                if type(teste_b)==float or type(teste_b)==int :
                    if teste_a*teste_b<0:
                        intervalo=[a,b]
                        return intervalo
                    if cont==100:
                        break
                else:
                    continue
            else:
                continue
            cont+=1  

    def continuidade(f_x,intervalo):
        a=intervalo[0]
        b=intervalo[1]
        try:
            f_a=Interativos.calcular(a,f_x)
            f_b=Interativos.calcular(b,f_x)
            
            if f_a==sp.zoo or f_b==sp.zoo:
                return False
            else:
                return True
        except ZeroDivisionError:
            return False
        except Exception:
            return False

    def convergencia(f,intervalo):
        x = symbols('x')
        limite=[]
        f=eval(f)
        solucao = sp.solve(f-1, x)
        tam=len(solucao)
        if tam==1:
            valor =solucao[0]
            a=intervalo[0]
            b=intervalo[1]
            if a>=valor and b>=valor:
                return True
            else:
                return False  
        for i in solucao:
            i=str(i)
            if '-' in i :
                valor=i
                valor=valor.replace("*","")
                valor= valor.replace("I","")
                valor=valor.strip()
                valor=eval(valor)
                valor=float(valor)
                a=intervalo[0]
                b=intervalo[1]
                if a>=valor and b>=valor:
                    return True
                else:
                    return False  
class matrizes:
    def permutacao(A,B):
        n_linha=len(A)
        while True:
            n_lin=randint(0,n_linha-1)
            if 0 != n_lin:
                if A[n_lin][0]==0:
                    aux=A[0]
                    aux2=B[0]
                    A[0]=A[n_lin]
                    A[n_lin]=aux
                    B[0]=B[n_lin]
                    B[n_lin]=aux2
            else:
                A=np.array(A)
                B=np.array(B)
                return A,B
    def convergencia(x0,x1):
        xe=x1-x0
        max_abs_d=max(abs(xe))
        max_abs_x1=max(abs(x1))
        d=max_abs_d/max_abs_x1
        
        return d