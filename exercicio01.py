from datetime import datetime


now = datetime.now()
ano_atual = now.year

active = True

while active:
    try:
        ano_nascimento = str(input("Informe o ano do seu nascimento: "))
        nome = str(input("Informe o seu nome: "))
        idade = 0

        if not 1900 <= int(ano_nascimento) <= ano_atual:
            raise ValueError("Data informada incorreta! Quatro dígitos requerido!")
        cont = 0
        for i in ano_nascimento:
            cont += 1

        if cont == 4:
            idade = int(ano_atual) - int(ano_nascimento)

        if 10 <= idade <= 18:
            print("Você não tem idadde para acessar o sistema!")
        elif 18 <= idade <= 120:
            print(f"{idade} anos - {nome} -> sua entrada foi permitida!")
            break

    except ValueError as e:
        print("Erro!", e)
