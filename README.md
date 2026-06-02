# projeto-final-python-M11
# Sistema de Inscrição e Seleção de Alunos

## 📖 Sobre o Projeto

Este projeto foi desenvolvido em Python com o objetivo de automatizar o processo de inscrição e seleção de alunos para cursos. O sistema permite registar candidatos, avaliar automaticamente a sua elegibilidade com base em critérios pré-definidos e gerir todas as informações de forma organizada.

Além da gestão de candidaturas, o sistema permite exportar dados para CSV, gerar comprovativos em PDF e enviar notificações por e-mail aos candidatos.

---

## 🚀 Funcionalidades

- Registo de candidatos
- Avaliação automática de candidaturas
- Aceitação ou rejeição com base em critérios definidos
- Pesquisa de candidatos por nome ou e-mail
- Listagem de todas as candidaturas
- Armazenamento persistente em ficheiros JSON
- Exportação de dados para CSV
- Geração de comprovativos em PDF
- Envio automático de e-mails de aceitação ou rejeição
- Interface de linha de comandos (CLI)

---

## 📋 Dados Recolhidos

O sistema regista as seguintes informações:

- Nome completo
- Idade
- E-mail
- Escolaridade
- Curso pretendido
- Nota de Matemática
- Nota de Português
- Número de negativas do 9.º ano

---

## ⚙️ Critérios de Avaliação

Cada candidato é avaliado automaticamente de acordo com os critérios definidos para o curso escolhido.

Exemplos de critérios:

- Faixa etária permitida
- Notas mínimas exigidas
- Número máximo de negativas
- Escolaridade mínima necessária

---

## 🏗️ Estrutura do Projeto

```text
├── models.py          # Estrutura da classe Candidato
├── storage.py         # Gestão de dados JSON
├── manager.py         # Lógica de negócio e avaliação
├── exporter.py        # Exportação CSV e geração PDF
├── email_service.py   # Serviço de envio de e-mails
├── main.py            # Interface principal (CLI)
├── candidatos.json    # Base de dados dos candidatos
└── README.md
```

---

## 💾 Persistência de Dados

As candidaturas são armazenadas em formato JSON, permitindo que os dados permaneçam guardados mesmo após o encerramento do programa.

---

## 📊 Exportação de Dados

O sistema permite exportar todos os candidatos para um ficheiro CSV compatível com:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc

---

## 📄 Geração de PDF

É possível gerar um comprovativo de inscrição em PDF para cada candidato.

O documento inclui:

- Dados do candidato
- Curso escolhido
- Estado da candidatura (Aceite/Rejeitado)

---

## 📧 Notificações por E-mail

Após a avaliação da candidatura, o sistema pode enviar automaticamente um e-mail ao candidato informando o resultado da sua inscrição.

---

## 🖥️ Como Executar

1. Clonar o repositório:

```bash
git clone https://github.com/SEU_UTILIZADOR/NOME_DO_REPOSITORIO.git
```

2. Aceder à pasta do projeto:

```bash
cd NOME_DO_REPOSITORIO
```

3. Instalar as dependências necessárias:

```bash
pip install fpdf
```

4. Executar o programa:

```bash
python main.py
```

---

## 👨‍💻 Tecnologias Utilizadas

- Python 3
- JSON
- CSV
- FPDF
- SMTP (smtplib)

---

## 🎓 Projeto Académico

Projeto Final desenvolvido na disciplina de Programação e Sistemas de Informação (PSI), no curso Técnico de Gestão e Programação de Sistemas Informáticos (TGPSI).

**Autores:**
- Bruna Nicole
- Christian

**Ano Letivo:** 2025/2026
