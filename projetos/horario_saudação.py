from datetime import datetime
import time
print("")
print("agora é exatamente")
print(datetime.now().hour,(":"),datetime.now().minute,("."),datetime.now().second)
def nome_solicitado():
    nome = input("Digite seu nome: ")
    return nome

def horario_atual():
    horario = datetime.now().hour
    if horario >= 0 and horario <= 5:
        saudacao = "boa madrugada"
        return saudacao
    elif horario >= 6 and horario <= 12:
        saudacao = "bom dia"
        return saudacao
    elif horario >= 13 and horario <= 18:
        saudacao = "boa tarde"
        return saudacao
    elif horario >= 19 and horario <= 24:
        saudacao = "boa noite"
        return saudacao
time.sleep(0.4)
print(horario_atual(),nome_solicitado())
time.sleep(0.8)

