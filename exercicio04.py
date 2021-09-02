active = True

while active:
    try:
        num1 = str(input("Informe o valor desejado ou S para sair: "))
        if num1 in "Ss":
            print("Desligando")
            break

        if not -99999.0 <= float(num1) <= 99999.0:
            raise ValueError("Dado incorreto!")
        else:
            num1 = float(num1)
        if num1 < 20:
            print("O número informado é menor que 20!")
        elif num1 == 20:
            print("O número informado é igual a 20!")
        elif num1 > 20:
            print("O número informado é maior a 20!")
    except ValueError as e:
        print("Erro!", e)