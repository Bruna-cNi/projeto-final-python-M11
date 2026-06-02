from models import Candidato
from storage import carregar_dados, guardar_dados

lista_candidatos = carregar_dados()

def email_existe(email_procurado):
    for c in lista_candidatos:
        if c.email.lower() == email_procurado.lower():
            return True
    return False

def avaliar_candidato(c):

        if c.idade >= 15 and c.idade <= 18:
            if c.escolaridade == "Ensino básico" or c.escolaridade == "Mudança de curso" or c.escolaridade == "Ensino Profissional":
                if c.nota_mat >= 2 and c.nota_por >= 2:
                    if c.negativas <= 2:
                        return True
        else:
            return False


def registar(nome, idade, email, escolaridade, curso, mat, por, neg):
    c = Candidato(nome, idade, email, escolaridade, curso, mat, por, neg)
    
    aceite = avaliar_candidato(c)
    if aceite == True:
        c.status = "Aceite"
    else:
        c.status = "Rejeitado"
        
    lista_candidatos.append(c)
    guardar_dados(lista_candidatos)
    return c
