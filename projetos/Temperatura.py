import time
time.sleep(1)
def Celsius():
    while True:
        try:
            celsius = float(input("Digite a temperatura em Celsius: "))
            return celsius
        except ValueError:
            print("tente novamente")

def Kelvin():
    kelvim = Celsius + 273
    return kelvim
def Fahrenheit():
    fahrenheit = (Celsius * 1.8) + 32
    return fahrenheit






print("")
while True:
    try:
        print("escolha 1 oara Kelvin e 2 oara Fahrenheit")
        time.sleep(0.5)
        escolha = int(input("Digite o numero 1 ou 2: "))

        if escolha == 1:
            time.sleep(0.5)
            print("")
            time.sleep(0.5)
            print("seu numero escolhido foi ", Celsius, "celsius, transformando a temperatura em Kelvin")
            time.sleep(0.5)
            print("o resultado dá:", Kelvin, "Kelvin")
            break
        elif escolha == 2:
            time.sleep(0.5)
            print("")
            time.sleep(0.5)
            print("seu numero escolhido foi ", Celsius, "celsius, transformando a temperatura em Fahrenheit")
            time.sleep(0.5)
            print("o resultado dá:", Fahrenheit, "Fahrenheit")
            break
        else:
            raise ValueError
    except ValueError:
        time.sleep(0.5)
        print("")
        print("insira somente os numeros 1 e 2,tente novamente")
        print("")

Celsius = Celsius()
Kelvin = Kelvin()
Fahrenheit = Fahrenheit()
time.sleep(0.8)