lista_frutas = ["Maçã", "Banana", "Pêssego"]

# lista_frutas[0] = "Maçã"
# lista_frutas[1] = "Banana"
# lista_frutas[2] = "Pêssego"
print(lista_frutas[0])

lista_frutas.append("Uva")
print(lista_frutas)
# lista_frutas[3] = "Uva"

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)