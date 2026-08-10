t = ('a', 'b', 'c', 'd', 'e')
print(t)

t1 = 'a',
print(t1, type(t1))

t = tuple("fiap")
print(t)

print(t[1:3])

t = ('F',) + t[1:]
print(t)

# ATRIBUIÇÃO COM TUPLAS
print()
a = 5
b = 10
print(f"a: {a}, b: {b}")

temp = a # temp = 5
a = b # a = 10
b = temp
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")

end_email = "fulano@gmail.com"
nome_usuario, dominio = end_email.split("@")

print(nome_usuario)
print(dominio)