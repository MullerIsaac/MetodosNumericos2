from math import sin

'''
Dupla:
Milton Cassul - 404877
Isaac Oliveira - 412489
'''

def func(x):
    return (sin(2*x) +4*(x**2) + 3*x)**2
        
def X(xi, xf, a):
    return (xi+xf)/2 + (xf-xi)*a/2

def calcQuadraturas(func, x, a, b, pnts, divs):
    raizes = []
    pesos = []
    
    if (pnts == 2):
        raizes = [-0.577350, 0.577350]
        pesos = [1,1]

    if (pnts == 3):
        raizes = [-0.774597, 0, 0.774597]
        pesos = [0.55555555555, 0.88888888888, 0.55555555555]

    if (pnts == 4):
        raizes = [0.861136,0.339981,-0.339981,-0.861136]
        pesos = [0.347854,0.652145,0.652145,0.347854]

    result = 0
    n_divs = 2**divs
    h = (b-a)/n_divs

    sub_result = 0
    
    for i in range(n_divs):
        xi = a + i*h            
        xf = xi + h

        for ak,wk in zip(raizes,pesos):
            sub_result += func(x(xi,xf,ak))*wk
     
    
    result = (xf-xi)/2 * sub_result
    
    return result

def integrar(f, x, a, b, pnts):
    tolerancia = 10**(-6)

    x0 = calcQuadraturas(f, x, a, b, pnts, 0)
    x1 = calcQuadraturas(f, x, a, b, pnts, 1)
    i = 1
        
    while(abs(x0-x1) > tolerancia):
        i +=1
        x0 = x1
        x1 = calcQuadraturas(f, x, a, b, pnts, i)
        
    return i, x1


def main():

    for k in range(2, 5):
        i, x = integrar(func, X, 0, 1, k)
        print("Quadratura com {} pontos = {}".format(k, x))
        print("Número de iterações = {}\n".format(i))

main()
        