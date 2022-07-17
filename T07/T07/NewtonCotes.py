from numbers import Integral
import numpy as np

'''Usado polinômio de grau 3'''
def integral_fechada(f, inf, sup, error):
    def aproximador(f, a, b, N): 
        integral_aux = 0
        delta = (b-a)/N


        h = delta/3
        for k in range (1, N+1):
            xi = a + (k-1) * delta
            xf = xi + delta
            integral_aux += 3 * h * (f(xi) + 3 * (f(xi + h) + f(xi + 2 * h)) + f(xf))/8


        return integral_aux

    integral = 0
    N = 1

    erro = np.Infinity
    while (erro > error):
        N *= 2
        integral_nova = aproximador(f, inf, sup, N)
        erro = abs((integral_nova - integral)/integral_nova)
        integral = integral_nova

    return integral