active = True


while active:
    try:
        dicionario_produto_id = {

        }
        dicionario_valor_id = {

        }
        dicionario_qtd_id = {

        }
        criandoID = str

        for i in range(3):
            montarID = i + 1
            montarID = str(montarID)

            dicio1 = str(
                input(f"Informe o {montarID}º produto ou S para sair: "))  # produto

            if dicio1 == "S" or dicio1 == "s":
                active = False
                raise ValueError("SAINDO!")

            dicio2 = str(input(f"Informe o preço: -> {dicio1}: "))  # preço

            if dicio2 == "S" or dicio2 == "s":
                active = False
                raise ValueError("SAINDO!")
            if dicio2.find(","):
                dicio2 = float(dicio2.replace(",", "."))
            elif dicio2.find("."):
                dicio2 = float(dicio2)
            if not -99999.0 <= float(dicio2) <= 99999.0:
                raise ValueError("DADO INCORRETO!")

            dicio3 = str(
                input(f"Informe a quantidade do produto: -> {dicio1}: "))

            if dicio3 == "S" or dicio3 == "s":
                active = False
                raise ValueError("SAINDO!")
            if not -99999 <= int(dicio3) <= 99999:
                raise ValueError("DADO INCORRETO!")

            dicionario_produto_id.update({montarID: dicio1})
            dicionario_valor_id.update({montarID: dicio2})
            dicionario_qtd_id.update({montarID: dicio3})

        valor_pagamento = str(
            input("Informe o dinheiro disponível para as compras: "))

        if valor_pagamento == "S" or valor_pagamento == "s":
            active = False
            raise ValueError("SAINDO!")
        if valor_pagamento.find(","):
            valor_pagamento = float(valor_pagamento.replace(",", "."))
        elif valor_pagamento.find("."):
            valor_pagamento = float(valor_pagamento)
        elif not -99999.0 <= float(valor_pagamento) <= 99999.0:
            raise ValueError("DADO INCORRETO!")

        valor_final = 0.0
        print(f"PRODUTOS - PREÇOS - QNT -")
        for idd in dicionario_produto_id.keys():
            print(f"{dicionario_produto_id[idd]} - R$ {dicionario_valor_id[idd]} - {dicionario_qtd_id[idd]} uni")
            valor_final = valor_final + (dicionario_valor_id[idd] * float(dicionario_qtd_id[idd]))
        
        print(f"O valor total da compra foi: -> R$ {valor_final}")

        if valor_final > valor_pagamento:
            print(
                f"Você precisa de R$ {valor_final - valor_pagamento} para finalizar compra!")
            sair = str(input("S para sair C para continuar: -> "))
            if sair in "Ss":
                active=False
                raise ValueError("SAINDO!")
            elif sair in "Cc":
                active=True
                raise ValueError("REINICIANDO!")
            else:
                active=True
                raise ValueError("DADO INCORRETO - REINICIANDO!")
        elif valor_final == valor_pagamento:
            print(f"Compra efetuada com sucesso! Você não possui troco!")
            sair = str(input("S para sair C para continuar: -> "))
            if sair in "Ss":
                active=False
                raise ValueError("SAINDO!")
            elif sair in "Cc":
                active=True
                raise ValueError("REINICIANDO!")
            else:
                active=True
                raise ValueError("DADO INCORRETO - REINICIANDO!")
        elif valor_final < valor_pagamento:
            print(f"Você receberá de troco: -> R$ {valor_pagamento - valor_final}")
            sair = str(input("S para sair C para continuar: -> "))
            if sair in "Ss":
                active=False
                raise ValueError("SAINDO!")
            elif sair in "Cc":
                active=True
                raise ValueError("REINICIANDO!")
            else:
                active=True
                raise ValueError("DADO INCORRETO - REINICIANDO!")

    except ValueError as e:
        print("INFO -> ", e)
