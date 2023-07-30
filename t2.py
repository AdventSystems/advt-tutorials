
area = input("Escreva a área do projeto: ")
print("A área é", area, "m2")


while area != "sair":
    area_numero = float(area)
    if area_numero < 50:
        print("Área muito pequena")
    else:
        print("Área Correta")
    area = input("Escreva a área do projeto: ")
    
print("fim de programa")

