import json
from models import Candidato

ficheiro = "candidates.json"

def carregar_dados():
    try:
        f = open(ficheiro, "r", encoding="utf-8")
        dados = json.load(f)
        f.close()
        
        lista = []
        for d in dados:
            c = Candidato(d["nome"], d["idade"], d["email"], d["escolaridade"], d["curso"], d["nota_mat"], d["nota_por"], d["negativas"])
            c.status = d["status"]
            lista.append(c)
        return lista
    except:
        return []

def guardar_dados(lista):
    f = open(ficheiro, "w", encoding="utf-8")
    dados_guardar = []
    for c in lista:
        dados_guardar.append(c.para_dicionario())
    json.dump(dados_guardar, f, indent=4)
    f.close()
