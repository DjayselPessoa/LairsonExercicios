active = True

while active:
    try:
        num1 = str(input("Informe o valor do primeiro número ou S para sair: "))
        if num1 in "Ss":
            print("Desligando!")
            break

        if not -99999.0 <= float(num1) <= 99999.0:
            raise ValueError("Dado incorreto!")
        else:
            if num1.find(","):
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
            raise ValueError("Dado incorreto!")
        else:
            if num2.find(","):
                num2 = float(num2.replace(",", "."))
            elif num1.find("."):
                num2 = float(num2)
            else:
                num2 = float(num2) 

        num3 = str(input("Informe o valor do segundo número ou S para sair: "))
        if num3 in "Ss":
            print("Desligando!")
            break

        if not -99999.0 <= float(num3) <= 99999.0:
            raise ValueError("Dado incorreto!")
        else:
            if num3.find(","):
                num3 = float(num3.replace(",", "."))
            elif num3.find("."):
                num3 = float(num3)
            else:
                num3 = float(num3) 

        if num1 == num2 and num2 == num3:
            print(f"Todos os números são iguais:  {num1, num2, num3}")
            break
        elif num1 == num2:
            if num1 > num3:
                print(f"O primeiro e o segundo número {num1, num2}  são os maiores números informados!")
                break
            else:
                print(f"O terceiro número {num3} é o maior número informado!")
                break
        elif num1 == num3:
            if num1 > num2:
                print(f"O primeiro e o terceiro número {num1, num3} são os maiores números informados!")
                break
            else:
                print(f"O segundo número {num2} é o maior número informado!")
                break
        elif num2 == num3:
            if num2 > num1:
                print(f"O segundo e o terceiro números {num2, num3} são os maiores números informados!")
                break
            else:
                print(f"O primeiro número {num1} é o maior número informado!")
                break
        

        if num1 > num2:
            if num1 > num3:
                print(f"O primeiro número {num1} é o maior número informado!")
                break
            else:
                print(f"O terceiro número {num3} é o maior número informado!")
                break
        else:
            if num2 > num3:
                print(f"O segundo número {num2} é o maior número informado!")
                break
            else:
                print(f"O terceiro número {num3} é o maior número informado!")
                break

    except ValueError as e:
        print("Erro!", e)