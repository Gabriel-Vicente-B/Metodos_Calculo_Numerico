import sympy as sp

P=[[-1,4],[0,1],[2,-1]]
x = sp.symbols('x')
N_linhas=len(P)
Pol_x=1
L = 1

for i in range(N_linhas):
    x0 , y0 = P[i]    
    for j in range(N_linhas):
        if i!=j:
            x1,args=P[j]
            L*= (x-x)/(x0-x1)
    Pol_x+=y0 * L

print(Pol_x)