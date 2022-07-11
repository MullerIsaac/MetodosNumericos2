#intA e intB são os limites de integracao
# i = o indice do Xi que queremos calcular
def calcXi(intA, intB, i, numInt):
    return intA + i * (intB - intA) / numInt


def funcao(x):
    return x**3 - 4 * x + 9


# I = [(b-a) / 2] * [(f(x0) + f(x1)]
class TrapezioFechado:
    def integrar(self, a, b, n):
        integral = 0
        h = (b - a) / n

        for i in range(0, n):
            x0 = a + i * h
            x1 = a + (i + 1) * h
            integral += (x1 - x0) / 2 * (funcao(x0) + funcao(x1))

        return integral


# I = [(b-a) / 3] * [(f(x0) + f(x1)]
class TrapezioAberto:
    def integrar(self, a, b, n):
        integral = 0
        h = (b - a) / n
        for i in range(0, n):
            b = a + h
            x1 = calcXi(a, b, 1, 3)
            x2 = calcXi(a, b, 2, 3)
            integral += funcao(x1) + funcao(x2)
            a = b
        integral *= h / 2

        return integral


def main():

    numero_particoes = 8
    a = 1
    b = 5

    NCfechado = TrapezioFechado()
    NCaberto = TrapezioAberto()

    print("Newton-Cotes fechado: ")

    for i in range(1, int(numero_particoes)):
        valor_atual = NCfechado.integrar(a, b, i)

        print('Iteração {0}: {1}'.format(i, valor_atual))
        print('\n')

    print("--------------------------------------------------------")
    print("Newton-Cotes aberto: ")

    for i in range(1, int(numero_particoes)):
        valor_atual = NCaberto.integrar(a, b, i)

        print('Iteração {0}: {1}'.format(i, valor_atual))
        print('\n')


main()
