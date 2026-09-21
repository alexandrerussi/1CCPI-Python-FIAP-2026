from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREATE / READ / UPDATE / DELETE

# READ
def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

# CREATE - DESAFIO: corrigir a inserção de novos leads
def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

# BUSCAR LEADS PELA QUERY
def read_leads_search(query):
    """Função que busca por leads a partir da query e RETORNA uma lista com resultados"""
    leads = read_leads()
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]}".lower()

        if query.lower() in txt_lead:
            results.append((i, lead))

    return results

# EXPORTAR LEADS PARA CSV
def export_csv():
    """Exporta TODOS os leads para CSV e RETORNA o CAMINHO do arquivo CSV"""
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()
            for dict_row in leads:
                writer.writerow(dict_row)
        return path_csv
    except PermissionError:
        return None

