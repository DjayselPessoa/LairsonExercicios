active = True

while active:
    try:
        num1 = str(input("Informe o valor do primeiro número ou S para sair: "))
        if num1 in "Ss":
            print("Desligando!")
            break
        num2 = str(input("Informe o valor do segundo número ou S para sair: "))
        if num2 in "Ss":
            print("Desligando!")
            break

        if not -99999999 <= int(num1) <= 99999999:
            raise ValueError("Dado incorreto!")
        else:
            calc1 = int(num1) % 2
        
        if calc1 == 0:
            print("O primeiro número é par!")
        else:
            print("O primeiro número é ímpar!")
        
        if not -99999999 <= int(num2) <= 99999999:
            raise ValueError("Dado incorreto!")
        else:
            calc2 = int(num2) % 2
        
        if calc2 == 0:
            print("O segundo número é par!")
        else:
            print("O segundo número é ímpar!")
    
    except ValueError as e:
        print("Erro", e)
