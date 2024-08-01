import time

def numero1():
    while True:
        try:
            numero1 = int(input("Digite o primeiro numero: "))
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
            numero2 = int(input("Digite o segundo numero: "))
            return numero2
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor novamente')
            time.sleep(0.8)
            print('')


def calculoTotal(numero1, numero2):
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2

    print(' o valor da soma é ',soma, 'o valor da subtração é ',subtracao,'o valor da multiplicação é ',multiplicacao, 'o valor da divisão é ',divisao)

def soma(numero1, numero2):
    soma = numero1 + numero2
    return soma

def subtracao(numero1, numero2):
    subtracao = numero1 - numero2
    return subtracao

def multiplicacao(numero1, numero2):
    multiplicacao = numero1 * numero2
    return multiplicacao

def divisao(numero1, numero2):
    divisao = numero1 / numero2
    return divisao



def menu(soma, subtracao, multiplicacao, divisao, calculoTotal):
    while True:
        try:
            print('escolha uma das operações abaixo:')
            print('1 - Soma')
            print('2 - subtração')
            print('3 - multiplicação')
            print('4 - divisão')
            print('5 - todas')
            escolha = int(input("escolha um dos numeros da a cima: "))

            if escolha == 1:
                soma(numero1, numero2)
                break
            elif escolha == 2:
                subtracao(numero1, numero2)
                break
            elif escolha == 3:
                multiplicacao(numero1, numero2)
                break
            elif escolha == 4:
                divisao(numero1, numero2)
            elif escolha == 5:
                calculoTotal(numero1, numero2)
                break
            else:
                raise ValueError
        except ValueError:
            print("valor incorreto")
            time.sleep(0.8)
            print('informe um valor de 1 a 5 novamente')
            time.sleep(0.8)
            print('')


numero1 = numero1()
numero2 = numero2()
menu(soma, subtracao, multiplicacao, divisao, calculoTotal)
time.sleep(0.8)