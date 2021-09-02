active = True

while active:
    try:
        num1 = str(input("Informe o valor do primeiro número ou S para sair: "))
        if num1 in "Ss":
            print("Desligando!")
            break
        if not -99999.0 <= float(num1) <= 99999.0:
            raise ValueError("dado incorreto!")
        elif num1.find(","):
            num1 = float(num1.replace(",", "."))
        elif num1.find("."):
            num1 = float(num1)
        else:
            num1 = float(num1)

        num2 = str(input("Informe o valor do segundo número ou S para sair: "))
        if num2 in "Ss":
            print("Desligando!")
            break
        if not -99999.0 <= float(num2) <= 99999.0:
            raise ValueError("dado incorreto!")
        elif num2.find(","):
            num2 = float(num2.replace(",", "."))
        elif num2.find("."):
            num2 = float(num2)
        else:
            num2 = float(num2)

        num3 = float

        num3 = num1
        num1 = num2
        num2 = num3

        print(f"Os valores informados agora estão trocados: número 1 -> {num1} - número 2 -> {num2}")
    except ValueError as e:
        print("Erro!", e)