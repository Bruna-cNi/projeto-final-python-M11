import manager
import exporter
import email_service

def menu():
    while True:
        print("\n=== Sistema de Inscrição ===")
        print("1 - Registar aluno")
        print("2 - Mostrar todos")
        print("3 - Procurar aluno")
        print("4 - Exportar CSV")
        print("5 - Gerar PDF")
        print("0 - Sair")
        
        opcao = input("O que deseja fazer? ")
        
        if opcao == '1':
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            
            while True:
                email = input("Email: ")
                if manager.email_existe(email) == True:
                    print("Erro, email já existe!")
                else:
                    break
                    
            print("1 - Ensino básico")
            print("2 - Mudança de curso")
            print("3 - Ensino Vocacional / Profissional")
            op_esc = input("Escolaridade (1 a 3): ")
            if op_esc == '1':
                esc = "Ensino básico"
            elif op_esc == '2':
                esc = "Mudança de curso"
            elif op_esc == '3':
                esc = "Ensino Profissional"
            else:
                esc="Inválida"
                
            print("Cursos:")
            print("Área Científico-Humanística:")
            print("  1 - Ciências e Tecnologias")
            print("  2 - Línguas e Humanidades")
            print("  3 - Ciências Socioeconómicas")
            print("  4 - Artes Visuais")
            print("\nÁrea Profissional / Tecnológica:")
            print("  5 - Técnico de Informática de Gestão")
            print("  6 - Técnico de Multimédia")
            print("  7 - Técnico de Eletrónica, Automação e Computadores")
            print("  8 - Técnico de Desporto")
            print("\nÁrea para aqueles que já são maiores de idade: ")
            print("  9 - Curso EFA (Ensino para Adultos / Trabalhador-Estudante)")
            print("\nOUTRO: ")
            print(" 10 - Outro")
            op_cur = input("Curso (1 a 10): ")
            if op_cur == "1":
                curso = "Ciências e Tecnologias"
            elif op_cur == "2":
                curso = "Línguas e Humanidades"
            elif op_cur == "3":
                curso = "Ciências Socioeconómicas"
            elif op_cur == "4":
                curso = "Artes Visuais"
            elif op_cur == "5":
                curso = "Técnico de Informática de Gestão"
            elif op_cur == "6":
                curso = "Técnico de Multimédia"
            elif op_cur == "7":
                curso = "Técnico de Eletrónica, Automação e Computadores"
            elif op_cur == "8":
                curso = "Técnico de Desporto"
            elif op_cur == "9":
                curso = "Curso EFA"
                op_esc = "Curso EFA / Trabalhador"
            elif op_cur == "10":
                curso = input("Insira o nome do curso pretendido: ")
            else:
                curso = "Invalido"
                
            mat = float(input("Qual foi sua nota em Matemática no 9º? (1-5) : "))
            por = float(input("Qual foi sua nota em Português no 9º? (1-5) : "))
            neg = int(input("Quantas negativas tiveste no 9º ano?: "))
            
            c = manager.registar(nome, idade, email, esc, curso, mat, por, neg)
            print("Status: " + c.status)
            email_service.enviar_email(c)
            
        elif opcao == '2':
            for c in manager.lista_candidatos:
                print(c.nome + " - " + c.curso + " - " + c.status)
                
        elif opcao == '3':
            texto = input("Nome ou email: ").lower()
            encontrou = False
            for c in manager.lista_candidatos:
                if texto in c.nome.lower() or texto in c.email.lower():
                    print(c.nome + " | " + c.email + " | " + c.status)
                    encontrou = True
            
            if encontrou == False:
                print("Ninguém encontrado.")
                
        elif opcao == '4':
            tipo = input("1 para Todos, 2 para Aceites, 3 para Rejeitados: ")
            
            if tipo == '1':
                exporter.exportar_csv(manager.lista_candidatos, "todos.csv")
            elif tipo == '2':
                lista_aceites = []
                for c in manager.lista_candidatos:
                    if c.status == "Aceite":
                        lista_aceites.append(c)
                exporter.exportar_csv(lista_aceites, "aceites.csv")
            elif tipo == '3':
                lista_rej = []
                for c in manager.lista_candidatos:
                    if c.status == "Rejeitado":
                        lista_rej.append(c)
                exporter.exportar_csv(lista_rej, "rejeitados.csv")
                
        elif opcao == '5':
            email = input("Email do candidato: ")
            encontrou = False
            for c in manager.lista_candidatos:
                if c.email == email:
                    n = "comprovativo_" + c.nome.replace(" ", "_") + ".pdf"
                    exporter.gerar_pdf(c, n)
                    encontrou = True
                    break
            
            if encontrou == False:
                print("Email não existe!")
                
        elif opcao == '0':
            break
        else:
            print("Opção errada.")

if __name__ == "__main__":
    menu()
