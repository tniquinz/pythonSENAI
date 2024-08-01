import random
import time



def menu():
    print("")
    time.sleep(1)
    print("♠♦Bem-vindo ao Menu Principal♠♦")
    time.sleep(0.5)

    print("Escolha uma das opções:")
    time.sleep(0.5)

    print("1 = Jogo de Adivinhação")
    time.sleep(0.5)

    print("2 = Jogo do Par ou Ímpar")
    time.sleep(0.5)

    print("3 = Sair")
    time.sleep(1)


def jogo_adivinhacao():
    print('')
    print("♣♦Jogo de Adivinhação♣♦ ")
    time.sleep(0.5)

    print("Tente adivinhar o número misterioso!")
    time.sleep(0.5)

    print("Escolha o modo de dificuldade:")
    time.sleep(0.5)

    print("1 = Fácil [0 a 50]")
    time.sleep(0.5)

    print("2 = Normal [0 a 100]")
    time.sleep(0.5)

    print("3 = Difícil [0 a 200]")
    time.sleep(0.5)

    print("4 = Extreme [0 a 1000]")
    time.sleep(0.5)

    try:

        modo = int(input("Escolha o modo: "))

        if modo == 1:

            numero_misterioso = random.randint(0, 50)

        elif modo == 2:

            numero_misterioso = random.randint(0, 100)

        elif modo == 3:

            numero_misterioso = random.randint(0, 200)

        elif modo == 4:

            numero_misterioso = random.randint(0, 1000)

        else:

            print("Opção inválida!")
            time.sleep(0.5)

            return
        tentativas = 0
        while True:

            chute = int(input("Faça seu chute: "))

            tentativas += 1

            if chute == numero_misterioso:
                print(f'seu numero de tentativas foi {tentativas}')
                time.sleep(0.5)
                print("Parabéns! Você acertou!")
                time.sleep(1)
                print("")
                break

            elif chute < numero_misterioso:

                print("O número misterioso é maior!")
                time.sleep(0.5)

            else:
                print("O número misterioso é menor!")

    except ValueError:

        print("Por favor, insira apenas números!")
        time.sleep(0.5)

    novamente = input("Deseja jogar novamente? [S/N]: ").upper()
    if novamente == 'S':
        jogo_adivinhacao()
    elif novamente == 'N':
        print('você será redirecionado para o menu')



def jogo_par_ou_impar():
    print('')
    print("♣Jogo do Par ou Ímpar♣")
    time.sleep(0.5)

    print("Escolha Par (P) ou Ímpar (I) e um número.")
    time.sleep(0.5)
    print("O computador escolherá o oposto.")
    time.sleep(0.5)

    try:

        escolha_usuario = input("Escolha [P] ou [I]: ").upper()

        numero_usuario = int(input("Escolha um número: "))

        if escolha_usuario not in ['P', 'I']:
            print("Escolha inválida!")
            print('você será redirecionado para o menu')
            return
        if escolha_usuario == 'P':

            escolha_computador = 'I'

        else:

            escolha_computador = 'P'

        numero_computador = random.randint(0, 10)

        resultado = (numero_usuario + numero_computador) % 2

        SomaFinal = (numero_usuario + numero_computador)

        if resultado == 0:

            vencedor = "P"

        else:

            vencedor = "I"
        if numero_usuario < 0 or numero_usuario > 10:
            print('numero invalido')
            time.sleep(0.5)
            print('você será redirecionado ao menu')
            time.sleep(0.5)
        else:
            print('')
            time.sleep(1)
            print(f"Você escolheu {escolha_usuario} e o seu número foi {numero_usuario}.")
            print('')
            time.sleep(1)

            print(f"O computador escolheu {escolha_computador} e o número dele foi {numero_computador}.")
            print('')
            time.sleep(1)

            print(f"A soma dos 2 numeros é de: {SomaFinal}")
            print('')
            time.sleep(1)
            if escolha_usuario == vencedor:
                print(f'você ganhou, deu {vencedor}')
                time.sleep(0.5)
            else:
                print(f'você perdeu, deu {vencedor}')
                time.sleep(0.5)
        print('')
        time.sleep(4)
        print('')
    except ValueError:
        print('')
        print("Por favor, insira um número válido!")
        print('você será redirecionado ao menu')
        time.sleep(1)

    while True:
        novamente = input("Deseja jogar novamente? [S/N]: ").upper()
        if novamente == 'S':
            jogo_par_ou_impar()
        elif novamente == 'N':
            print('você será redirecionado para o menu')
        break

while True:

    menu()

    try:

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:

            jogo_adivinhacao()


        elif opcao == 2:

            jogo_par_ou_impar()


        elif opcao == 3:

            print("Obrigado pela preferencia!")


            break

        else:

            print("Opção inválida!")
            print('você será redirecionado para o menu')

    except ValueError:

        print("Por favor, insira apenas números!")
        print('')
