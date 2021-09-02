active = True

while active:
    try:
        dist = str(input("Informe a distância percorrida em km ou S para sair: "))

        if dist in "Ss":
            print("Desligando!")
            break

        if dist.find(","):
            dist = float(dist.replace(",", "."))
        elif dist.find("."):
            dist = float(dist)
        if not 0.0 <= float(dist) <= 99999.0:
            raise ValueError("Dado incorreto!")
        
        else:
            dist = float(dist)

        temp = str(input("Informe o tempo do percurso em horas: "))

        if temp in "Ss":
            print("Desligando!")
            break
        
        elif temp.find(","):
            temp = float(temp.replace(",", "."))
        elif temp.find("."):
            temp = float(temp)
        if not 0.0 <= float(temp) <= 99999.0:
            raise ValueError("Dado incorreto!")
        else:

            temp = float(temp)
        
        velocidade_media = dist / temp

        print(f"A velocidade média é : VM = dist / temp -> VM = {round(velocidade_media, 2)} km/h")

        velocidade_media = velocidade_media / 3.6
        print(f"O resultado covertido: V.M. {round(velocidade_media, 2)} m/s")
    except ValueError as e:
        print("Erro!", e)