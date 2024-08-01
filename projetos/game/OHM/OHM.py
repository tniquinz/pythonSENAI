import time

def numero1():
    while True:
        try:
            numero1 = float(input("Digite o valor da tensão: "))
            return numero1
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')


def numero2():
    while True:
        try:
            numero2 = float(input("Digite o valor da corrente: "))
            return numero2
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')
def numero3():
    while True:
        try:
            numero3 = float(input("Digite o valor da resistencia: "))
            return numero3
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')
def numero4():
    while True:
        try:
            numero4 = float(input("Digite o valor da tensão da fonte: "))
            return numero4
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')

def numero5():
    while True:
        try:
            numero5 = float(input("Digite o valor da tensão do dispositivo: "))
            return numero5
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')

def tensao(numero3, numero2):
    tensao = numero3 * numero2
    return tensao
def resistencia(numero1, numero2):
    resistencia = numero1 / numero2
    return resistencia

def corrente(numero1, numero3):
    corrente = numero1 / numero3
    return corrente

def Resistencia_Resistor(numero4, numero5, numero2):
    resistencia_do_resistor = ((numero4 - numero5) / numero2)
    return resistencia_do_resistor

def menu():
    print('♦Calculadora de Ohm♦')
    print('')
    print('1 - Resistencia')
    print('2 - Corrente')
    print('3 - tensão')
    print('4 - Resistor')
    print('5 - sair')
    escolha()
def escolha():
    while True:
        try:
            escolha1 = int(input('digite um numero conforme a sua escolha, lembrando tem que ser de 1 a 5: '))
            if escolha1 == 1:
                print('')
                print('calculando resistencia')
                print('.')
                time.sleep(0.4)
                print('..')
                time.sleep(0.4)
                print('...')
                time.sleep(0.4)
                print(resistencia(numero1(), numero2()))
                print('foi calculado com sucesso')
                time.sleep(0.4)
                return escolha1

            elif escolha1 == 2:
                print('')
                print('calculando corrente')
                print('.')
                time.sleep(0.4)
                print('..')
                time.sleep(0.4)
                print('...')
                time.sleep(0.4)
                print(corrente(numero1(), numero3(),))
                print('foi calculado com sucesso')
                time.sleep(0.4)
                return escolha1

            elif escolha1 == 3:
                print('')
                print('calculando tensão')
                print('.')
                time.sleep(0.4)
                print('..')
                time.sleep(0.4)
                print('...')
                time.sleep(0.4)
                print(tensao(numero3(), numero2()))
                print('foi calculado com sucesso')
                time.sleep(0.4)
                return escolha1

            elif escolha1 == 4:
                print('')
                print('calculando resistencia do resistor')
                print('.')
                time.sleep(0.4)
                print('..')
                time.sleep(0.4)
                print('...')
                time.sleep(0.4)
                print(Resistencia_Resistor(numero4(), numero5(), numero2()))
                print('foi calculado com sucesso')
                time.sleep(0.4)
                return escolha1

            elif escolha1 == 5:
                print('')
                print('saindo')
                time.sleep(0.4)
                print('.')
                time.sleep(0.4)
                print('..')
                time.sleep(0.4)
                print('...')
                time.sleep(0.4)
                print('tchau')
                time.sleep(0.4)
                return escolha1
            else:
                print('escolha invalida')
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')





time.sleep(0.5)