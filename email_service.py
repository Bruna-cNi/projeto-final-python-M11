import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

servidor = "smtp.gmail.com"
porta = 587
email_envio = "candidaturacursos@gmail.com"
senha_envio = "qvwy ckog rykt nidz" 

def enviar_email(c):
    print("\nA enviar email para " + c.email + "...")
    
    assunto = "Resultado da candidatura para " + c.curso
    
    if c.status == "Aceite":
        texto = "Olá " + c.nome + ",\n\nParabéns! Foste aceite.\nEquipa de Admissões."
    else:
        texto = "Olá " + c.nome + ",\n\nInfelizmente foste rejeitado.\nEquipa de Admissões."
        
    msg = MIMEMultipart()
    msg['From'] = email_envio
    msg['To'] = c.email
    msg['Subject'] = assunto
    msg.attach(MIMEText(texto, 'plain', 'utf-8'))
    
    try:
        s = smtplib.SMTP(servidor, porta)
        s.starttls()
        s.login(email_envio, senha_envio)
        s.send_message(msg)
        s.quit()
        print("Email enviado com sucesso!")
    except:
        print("Erro ao enviar email.")
