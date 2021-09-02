active = True

while active:
    try:
        num1 = str(input("Informe o primeiro número ou S para sair: "))

        if num1 in "Ss":
            print("Desligando!")
            break
        if not -99999.0 <= float(num1) <= 99999:
            raise ValueError("Dado incorreto!")

        if num1.find(","):
            num1 = float(num1.replace(",", "."))

        elif num1.find("."):
            num1 = float(num1)
            
        else:
            num1 = float(num1)

        num2 = str(input("Informe o segundo número ou S para sair: "))

        if num2 in "Ss":
            print("Desligando!")
            break
        if not -99999.0 <= float(num2) <= 99999:
            raise ValueError("Dado incorreto!")
        if num2.find(","):
            num2 = float(num2.replace(",", "."))
        elif num2.find("."):
            num2 = float(num2)
        else:
            num2 = float(num2)

        if num1 > num2:
            print(
                f"O primeiro número {num1} é maior que o segundo número {num2}")
        elif num1 < num2:
            print(
                f"O segundo número {num2} é maior que o primeiro número {num1}")
        elif num1 == num2:
            print(f"Os dois número são iguais:  {num1} = {num2}")

    except ValueError as e:
        print("erro!", e)
