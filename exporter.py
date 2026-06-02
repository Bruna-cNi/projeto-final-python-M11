import csv
from fpdf import FPDF

def exportar_csv(lista, nome_ficheiro):
    f = open(nome_ficheiro, "w", newline="", encoding="utf-8")
    escritor = csv.writer(f)
    escritor.writerow(["Nome", "Idade", "Email", "Escolaridade", "Curso", "Status"])
    for c in lista:
        escritor.writerow([c.nome, str(c.idade), c.email, c.escolaridade, c.curso, c.status])
    f.close()
    print("Exportado para " + nome_ficheiro + " com sucesso!")

def gerar_pdf(c, nome_ficheiro):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=16, style="B")
    pdf.cell(200, 10, text="Comprovativo de Inscricao", ln=1, align="C")
    
    pdf.set_font("Helvetica", size=12)
    pdf.cell(200, 10, text="Nome: " + c.nome, ln=1)
    pdf.cell(200, 10, text="Idade: " + str(c.idade), ln=1)
    pdf.cell(200, 10, text="Email: " + c.email, ln=1)
    pdf.cell(200, 10, text="Escolaridade: " + c.escolaridade, ln=1)
    pdf.cell(200, 10, text="Curso: " + c.curso, ln=1)
    
    if c.status == "Aceite":
        pdf.set_text_color(0, 128, 0)
    else:
        pdf.set_text_color(200, 0, 0)
        
    pdf.cell(200, 10, text="Status: " + c.status, ln=1)
    pdf.output(nome_ficheiro)
