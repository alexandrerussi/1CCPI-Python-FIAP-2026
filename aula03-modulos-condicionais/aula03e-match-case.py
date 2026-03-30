escolha_usuario = 1211212
# 0 > sai do programa
# 1 > entra no programa

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro!")