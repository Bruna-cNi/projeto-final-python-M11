class Candidato:
    def __init__(self, nome, idade, email, escolaridade, curso, nota_mat, nota_por, negativas):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.escolaridade = escolaridade
        self.curso = curso
        self.nota_mat = nota_mat
        self.nota_por = nota_por
        self.negativas = negativas
        self.status = "Pendente"

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email,
            "escolaridade": self.escolaridade,
            "curso": self.curso,
            "nota_mat": self.nota_mat,
            "nota_por": self.nota_por,
            "negativas": self.negativas,
            "status": self.status
        }
