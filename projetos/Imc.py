import time
def massa_corporal():
    while True:
        try:
            massa_corporal = float(input('Digite o peso que você quer informar: '))
            return massa_corporal
        except ValueError:
            print('digite um valor valido!')

def altura():
    while True:
        try:
            altura = float(input('Digite a altura desejada: '))
            return altura
        except ValueError:
            print('digite um valor valido!')

peso = massa_corporal()
altura = altura()

def imc(peso, altura):
    imc = peso * (altura * altura)
    if imc > 0 and imc < 18.5:
        print('de acordo com as nossas analises o seu indice de massa corporal é magreza')
    elif imc >= 18.5 and imc < 24.9:
        print('de acordo com as nossas analises o seu indice de massa corporal é normal')
    elif imc >= 25 and imc < 29.9:
        print('de acordo com as nossas analises o seu indice de massa corporal é sobrepeso')
    elif imc >= 30 and imc < 34.9:
        print('de acordo com as nossas analises o seu indice de massa corporal é obesidade de 1* grau')
        print('cuidado, obesidade mata, cuide da sua sáude.')
    elif imc >= 35 and imc < 39.9:
        print('de acordo com as nossas analises o seu indice de massa corporal é obesidade de 2* grau')
        print('vá há um medico, cuide da sua sáude, é serio...')
    elif imc > 40:
        print('de acordo com as nossas analises o seu indice de massa corporal é obesidade de 3*grau')
        print('vá há um medico, e cuide da sua sáude, obesidade não é brincadeira')
    else:
        print('invalido')

imc(peso, altura)
time.sleep(0.8)