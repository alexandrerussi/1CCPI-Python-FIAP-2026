from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    status = input("Etapa no funil de vendas: ")

    # validar os dados...
    # depois de validado... precisamos modelar os dados
    # vamos modelar o lead como um dicionario
    print(model_lead(name, email, status))

    # depois do meu lead modelado como dict
    # precisamos enviar esse dict para o leads.json
    # vamos usar o control para isso
    control.create_lead(model_lead(name, email, status))

    print("Lead adicionado (func)")

def list_leads():
    leads = control.read_leads()
    print(leads)
    # +1 desafio: formatar como tabela

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()