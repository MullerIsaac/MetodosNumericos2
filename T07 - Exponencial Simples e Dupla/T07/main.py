import NewtonCotes as nc
from math import tanh, sinh, cosh, pi
import numpy as np


def f1(x):
    return 1/(x ** (2/3))

def f2(x):
    return 1/((4 - (x ** 2)) ** 0.5)

def exp_simples(f, a, b, e):
    def x(s):
        return (a + b)/2 + ((b-a)/2) * tanh(s)
    def dx(s):
        return ((b-a)/2) * (1/cosh(s)**2)
    
    def nf(s):
        return f(x(s)) * dx(s)

    erro = np.Infinity
    integral = 0
    c = 0

    
    try:
        while (erro > e):
            c += 1
            integral_nova = nc.integral_fechada(nf, -c, c, e)
            erro = abs((integral_nova - integral)/integral_nova)
            integral = integral_nova
    except:
        return integral

    return integral

def exp_dupla(function, a, b, error):
    def x(s):
        return (a + b)/2 + ((b-a)/2) * tanh((pi/2) * sinh(s))
    def dx(s):
        return ((b-a)/2) * ((pi * cosh(s))/(2 * (cosh((pi * sinh(s))/2)) ** 2))
    
    def nf(s):
        return function(x(s)) * dx(s)

    erro = np.Infinity
    integral = 0
    c = 0

    try:
        while (erro > error):
            c += 0.5
            integral_nova = nc.integral_fechada(nf, -c, c, error)
            erro = abs((integral_nova - integral)/integral_nova)
            integral = integral_nova
    except:
        return integral
    return integral


def main():
    print(2 * exp_simples(f1, 0, 1, 0.001))
    print(2 * exp_dupla(f1, 0, 1, 0.001))
    print(exp_simples(f2, -2, 0, 0.001))
    print(exp_dupla(f2, -2, 0, 0.001))

main()

