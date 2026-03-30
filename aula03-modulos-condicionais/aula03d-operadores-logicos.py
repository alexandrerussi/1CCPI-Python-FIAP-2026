# LÓGICA E (and)
# EMAIL     SENHA       LOGIN(RESULTADO)
# True      True        True
# True      False       False
# False     True        False
# False     False       False

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entra no programa.. executa...")

# LÓGICA OU (or)
logica_ou = False or False or False
print(logica_ou)

# OPERADOR DE NEGAÇÃO (not)
negacao = not False
print(negacao)

if not verifica_login:
    print("loga ai...")