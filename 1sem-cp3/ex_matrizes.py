temperaturas = [
    [28, 31, 34, 33], # temperaturas da sala 1
    [25, 27, 29, 28], # temperaturas da sala 2...
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

sala_maior_risco = 0
maior_risco = 0

for i, temperaturas_sala in enumerate(temperaturas):
    # print(temperaturas_sala)

    soma = 0
    registro_critico = 0
    for temperatura in temperaturas_sala:
        # print(temperatura)
        soma += temperatura # acumulador

        if temperatura >= 33:
            registro_critico += 1 # contador

    media = sum(temperaturas_sala) / len(temperaturas_sala)

    print(f"Sala {i+1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {registro_critico}")
    print()

    if registro_critico > maior_risco:
        maior_risco = registro_critico
        sala_maior_risco = i + 1

print(f"Sala com maior risco: Sala {sala_maior_risco}")