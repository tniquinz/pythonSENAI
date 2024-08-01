import time
def lado1():
    while True:
        try:
            Lado1 = float(input('informe o número do lado do triangulo: '))
            return Lado1
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')

def lado2():
    while True:
        try:
            Lado2 = float(input('informe o seguinte número do lado do triangulo: '))
            return Lado2
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')

def lado3():
    while True:
        try:
            Lado3 = float(input('escreva ultimo número do triangulo: '))
            return Lado3
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')


lado1 = lado1()
lado2 = lado2()
lado3 = lado3()


def calculo_lados(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        print('')
        print("o triangulo é considerado um equilatero")
    elif lado1 == lado2 and lado1 != lado3:
        print('')
        print("o triangulo é considerado um isoceles")
    elif lado2 == lado3 and lado1 != lado3:
        print('')
        print("o triangulo é considerado um isoceles")
    else:
        print('')
        print('o triangulo é considerado um escaleno')


calculo_lados(lado1, lado2, lado3)
time.sleep(0.8)