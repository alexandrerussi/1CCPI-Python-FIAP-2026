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

    print(f"## | {"Nome":<15} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<15} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()

    # CONTROL!!
    # comparação entre a query digitada e o leads.json
    search_results = control.read_leads_search(query)

    print(f"## | {"Nome":<15} | E-mail")
    for i, lead in search_results:
        print(f"{i:02d} | {lead["name"]:<15} | {lead["email"]}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar para CSV")
    else:
        print(f"Exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail)")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()