#Padão SMT = padrão de e-mail

import smtplib
import email.message

#Criação de um email padrão
def enviar_email():
    corpo_email = """
    <p>Olá <b>Vitória</b></p>
    <p>Segue meu E-mail automático.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'Email@email.com'
    msg['To'] = 'Email@gmail.com'
    password = 'senha'

    #Configurções de segurança exigidas pelo E-mail
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    #Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()