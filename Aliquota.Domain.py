import datetime


def calculo():

    print("Vamos Calcular o Imposto de Renda:")
    investimento = verificarInvest()
    retirada = verificarRetira()

    tempo = diferencatempo()
    tempoAno = (tempo)/365.25

    lucro = retirada - investimento
    imposto(investimento, retirada, lucro, tempoAno)


def verificarInvest():
    invest = leiaFloat("Digite o valor investido: ")
    while (invest <= 0):
        print("Valor não valido. Digite um valor valido.\n")
        invest = leiaFloat("Digite o valor investido: ")
        continue
    return invest


def verificarRetira():
    retir = leiaFloat("Digite o valor retirado: ")
    while (retir <= 0):
        print("Valor não valido. Digite um valor valido.\n")
        retir = leiaFloat("Digite o valor retirado: ")
        continue
    return retir


def leiaFloat(msg):
    while True:
        try:
            n = float((input(msg)).replace(",", "."))
        except ValueError:
            print("Valor não valido. Digite um valor valido.\n")
            continue
        else:
            return n


def data():
    anoAp = year()
    mesAp = month()
    diaAp = days(anoAp, mesAp)

    data = datetime.date(anoAp, mesAp, diaAp)
    return data


def year():
    ano = leiaInt("Digite o ano:")
    while (ano <= 0):
        print("Valor não valido. Digite um valor valido.\n")
        ano = leiaInt("Digite o ano:")
        continue
    return ano


def month():

    mes = leiaInt("Digite o mes:")
    while (mes <= 0 or mes >= 13):
        print("Valor não valido. Digite um valor valido.\n")
        mes = leiaInt("Digite o mes:")
        continue
    return mes


def days(anoAp, mesAp):

    anoBissexto = bissexto(anoAp, mesAp)
    dia = leiaInt("Digite o dia:")

    while((mesAp == 1 or mesAp == 3 or mesAp == 5 or
          mesAp == 7 or mesAp == 8 or mesAp == 10 or mesAp == 12)
          and (dia <= 0 or dia > 31)):
        print("Valor não valido. Digite um valor valido.\n")
        dia = leiaInt("Digite o dia:")
        continue
    while((mesAp == 4 or mesAp == 6 or mesAp == 9 or mesAp == 11)
          and (dia <= 0 or dia > 30)):
        print("Valor não valido. Digite um valor valido.\n")
        dia = leiaInt("Digite o dia:")
        continue
    while(mesAp == 2 and anoBissexto is True and
          (dia <= 0 or dia > 29)):
        print("Valor não valido. Digite um valor valido.\n")
        dia = leiaInt("Digite o dia:")
        continue
    while(mesAp == 2 and anoBissexto is False and
          (dia <= 0 or dia > 28)):
        print("Valor não valido. Digite um valor valido.\n")
        dia = leiaInt("Digite o dia:")
        continue

    return dia


def bissexto(anoAp, mesAp):
    if (anoAp % 4 == 0 and anoAp % 100 != 0) or (anoAp % 400 == 0):
        return True
    else:
        return False


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Valor não valido. Digite um valor valido.\n")
            continue
        else:
            return n


def diferencatempo():

    print("Defina a data de aplicação:")
    dataApli = data()

    print("Defina a data de Retirada:")
    dataReti = data()

    diferenca = dataReti - dataApli
    diferencaDia = diferenca.days

    while (diferencaDia <= 0):
        print("Valor não valido. Digite um valor valido.\n"
              "Redefina a data de Retirada:")
        dataReti = data()
        diferenca = dataReti - dataApli
        diferencaDia = diferenca.days
        continue
    return diferencaDia


def imposto(investimento, retirada, lucro, tempoAno):

    if lucro > 0:
        if (0 < tempoAno < 1):
            p = 22.5
        elif (1 <= tempoAno < 2):
            p = 18.5
        elif (tempoAno >= 2):
            p = 15
    else:
        p = 0

    ir = (lucro * p)/100
    retiradaReal = retirada - ir

    print(f"\nSeu investimento foi R${investimento: .2f},\n"
          f"Ficou {tempoAno: .2f} anos,\n"
          f"A porcentagem do imposto foi {p: .2f}%,\n"
          f"O valor do desconto foi R${ir: .2f},\n"
          f"O valor da retirada já com os descontos "
          f"é R$ {retiradaReal: .2f}.")


if __name__ == "__main__":
    calculo()
