'''
    Este programa resolve as questões 02 e 09 - Já tinha feito um código para obter juros simples e composto
assim sendo somente adicionei o problema das questões citadas

'''

active = True
while active:
    try:
        emprestimoFinal = 0.0
        salario = str(input("\nInforme o valor do seu salário ou digite S para sair: "))

        if salario in "Ss":
            print("\nDesligando!")
            break
        elif salario.find(","):
            salario = float(salario.replace(",", "."))
            qtd_salario = salario // 1100
            print("\nQuestão 09 resposta abaixo: ")
            print(f"\nSalário: R$ {salario} - [S.M.] -> {int(qtd_salario)}")
        elif salario.find("."):
            salario = float(salario)
            qtd_salario = salario // 1100
            print("\nQuestão 09 resposta abaixo: ")
            print(f"\nSalário: R$ {salario} - [S.M.] -> {int(qtd_salario)}")

        emprestimo = str(input("\nInforme o valor do Empréstimo desejado ou digite S para sair: "))

        if emprestimo in "Ss":
            print("\nDesligando!")
            break
        elif emprestimo.find(","):
            emprestimoFinal = float(emprestimo.replace(",", "."))
            print(f"\nEmprestimo: R$ {emprestimoFinal}")
        elif emprestimo.find("."):
            emprestimoFinal = float(emprestimo)
            print(f"\nEmprestimo: R$ {emprestimoFinal}")
        else:
            raise ValueError("\nInformação incorreta!")

        tax = str(input(f"\nInforme o valor dos juros: "))
        if tax.find(","):
            tax = float(tax.replace(",", "."))
            tax = round(tax, 4)
        elif tax.find("."):
            tax = float(tax)
            tax = round(tax, 4)

        if not -100.0 < float(tax) <= 100.0:
            raise ValueError("\nInforme um valor entre -100.0 e 100.0! Reiniciando o programa!")
        else:
            tax = float(tax) / 100
            tax = round(tax, 4)
            print(tax)

        tipo = str(input(f"\nJuros Simples ou Juros Composto [S ou C]: "))

        if emprestimoFinal <= 100:
            raise ValueError("\nValor muito pequeno!")
        
        if not tipo in "Cc" or tipo in "Ss":
            active = False
            raise ValueError("Informação incorreta! - REINICIANDO!")

        if tipo in "Cc" :
            # juros composto
            active = True
            while active:
                try:
                    escolha = input("\nPara empréstimos com juros composto você poderá escolher entre 5 e 20 prestações: ")
                    escolha = int(escolha)
                    if not 5 <= escolha <= 20:
                        raise ValueError("Valor incompatível!")
                    else:
                        parcelas = float(escolha)
                        break
                except ValueError as e:
                    print("!erro!", e)
            linha = "-" * 50
            print(linha)
            print("\ncom a fórmula o valor somente dos juros é este: ")
            calc = ((emprestimoFinal) * ((1 + tax) ** escolha)) - emprestimoFinal
            calc = round(calc, 2)
            print("fórmula: R$ ", calc)
            print("Ao que tudo indica a fórmula de juros compostos não tem exatidão!\n")
            
            emprestimoParcela = emprestimoFinal/parcelas
            emprestimoParcela = round(emprestimoParcela, 2)
            totalParcelas = 0.0
            calc = emprestimoParcela
            print(f"\nVocê solicitou {escolha} parcelas!")
            for i in range(escolha):
                cont = i + 1
                calc = calc + (calc * tax)
                calc = round(calc, 2)
                totalParcelas = totalParcelas + calc
                print(f"No {cont}º mês você pagará o valor de R$ {calc}")
                i += 1
                if cont == escolha:
                    ultima_parcela = calc

            valorFinalJuros = totalParcelas - emprestimoFinal
            valorFinalJuros = round(valorFinalJuros, 2)
            totalParcelas = round(totalParcelas, 2)
            tax2 = tax * 100
            tax2 = round(tax2, 2)
            print(f"\nValor solicitado: R$ {emprestimoFinal}\nValor final total com juros composto no valor de {tax2}%: R$ {totalParcelas}\nValor total dos juros adicionado: R$ {valorFinalJuros}\n")
            limite = (20 * salario)/ 100
            print(f"\nQuestão 02 resposta:\nO limite máximo de 20% de seu salário para obter empréstimo é: R$ {limite}")
            if ultima_parcela > limite:
                print(f"\nSimulação realizada, entretanto a última parcela do empréstimo solicitado é maior do que o limite mínimo de 20% do seu salário - R$ {limite}.\nDevido a este fator seu empréstimo não poderá ser concedido!")


        elif tipo in "Ss":
            # juros simples
            active = True
            while active:
                try:
                    escolha = input("\nPara empréstimos a juros simples você poderá escolher entre 3 e 12 prestações: ")
                    escolha = int(escolha)
                    if not 3 <= escolha <= 12:
                        raise ValueError("Valor incompatível!")
                    else:
                        parcelas = float(escolha)
                        break
                except ValueError as e:
                    print("!erro!", e)
            calc = emprestimoFinal * tax * parcelas
            calc = round(calc, 2)
            valorFinalJuros = emprestimoFinal + calc
            valorFinalJuros = round(valorFinalJuros, 2)

            valorParcela = (emprestimoFinal / parcelas) + (calc / parcelas)
            valorParcela = round(valorParcela, 2)
            tax2 = tax * 100 
            tax2 = round(tax2, 2)
            print(f"\nValor solicitado: R$ {emprestimoFinal}\nValor final total com juros simples no valor de {tax2}%: R$ {valorFinalJuros}\nValor total dos juros adicionado: R$ {calc}\nValor de cada uma das {escolha} parcelas: R$ {valorParcela}")
            limite = (20 * salario)/ 100
            print(f"\nQuestão 02 resposta:\nO limite máximo de 20% de seu salário para obter empréstimo é: {limite}")
            if valorParcela > limite:
                print(f"\nSimulação realizada, entretanto as parcelas do empréstimo solicitado são maiores do que o limite mínimo de 20% do seu salário - R$ {limite}.\nDevido a este fator seu emprestimo não poderá ser concedido!")

        else:
            active = True
            while active:
                try:
                    print(f"\nO valor {emprestimoFinal} não pode ser contratado!")
                    break
                except ValueError as e:
                    print("!erro!", e)
    except ValueError as e:
        print("!erro!", e)
