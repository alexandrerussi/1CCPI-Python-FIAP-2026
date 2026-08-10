eng2sp = dict()
print(eng2sp)

eng2sp ["one"] = "uno"
print(eng2sp)

eng2sp = {
    "one": "uno",
    "two": "dos",
    "three": "tres"
}
print(eng2sp["two"])

print(len(eng2sp))

# OPERADOR IN
print("uno" in eng2sp)

# valores..
valores_dict = eng2sp.values()
print('uno' in valores_dict)


# CONTADOR DE LETRAS
print()

def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("paralelepipedo")
print(dict_contagem)









