'''
Quadraturas especiais para n=2, 3 e 4. Não há partição!
Membros: Isaac Miller
	 Milton Cassul
'''

from math import sin, sqrt, pi

def f(x):
    return (sin(2*x) + 4*(x**2) + 3*x)**2

def gauss_hermite_quad(f, n):

    result=0
    sqrt_pi = sqrt(pi)
    
    raizes = [
        [-1/sqrt(2), 1/sqrt(2)],
        [-sqrt(3/2), 0, sqrt(3/2)],
        [sqrt((3+sqrt(6))/2), sqrt((3-sqrt(6))/2), - sqrt((3-sqrt(6))/2), -sqrt((3+sqrt(6))/2)]
      ]

    pesos = [
        [sqrt_pi/2, sqrt_pi/2],
        [sqrt_pi/6, (2 * sqrt_pi)/3, sqrt_pi/6],
        [(sqrt_pi * (3-sqrt(6)))/12, (sqrt_pi * (3+sqrt(6)))/12, (sqrt_pi * (3+sqrt(6)))/12, (sqrt_pi * (3- sqrt(6)))/12]
    ]

    for k in range(n):
        result = result + pesos[n-2][k] * f(raizes[n-2][k])

    
    return result

def gauss_laguerre_quad(f, n):
    result = 0

    raizes = [
        [2 - sqrt(2), 2 + sqrt(2)],
        [0.41577, 2.29428, 6.28994],
        [0.32254, 1.74576, 4.53662, 9.39507]
    ]

    pesos = [
        [(2+sqrt(2))/4, (2-sqrt(2))/4],
        [0.71109, 0.27851, 0.01038],
        [0.60335, 0.35742, 0.03888, 0.00053]
    ]

    for k in range(n):
        result = result + pesos[n-2][k] * f(raizes[n-2][k])
        

    return result

def gauss_chebyshev_quad(f, n):
    result = 0

    pi_n = pi/n
    
    raizes = [
        [-(1/sqrt(2)), 1/sqrt(2)],
        [-(sqrt(3)/2), 0, sqrt(3)/2],
        [sqrt(2+sqrt(2))/2, sqrt(2-sqrt(2))/2, -sqrt(2+sqrt(2))/2, -sqrt(2-sqrt(2))/2]
    ]

    for k in range(n):
        result = result + pi_n  * f(raizes[n-2][k])

    return result



def main():

    for k in range(2, 5):
        r = gauss_hermite_quad(f, k)
        print('Valor de quadratura de Gauss-Hermite com {} pontos: {}\n'.format(k, r))
        r = gauss_laguerre_quad(f, k)
        print('Valor de quadratura de Gauss-Laguerre com {} pontos: {}\n'.format(k, r))
        r = gauss_chebyshev_quad(f, k)
        print('Valor de quadratura de Gauss-Chebyshev com {} pontos: {}\n'.format(k, r))

        print('\n---------------------------------------------------------------------------------------\n')

main()