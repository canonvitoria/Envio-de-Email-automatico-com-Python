# Envio de Email Automático com Python

Este repositório contém um script em Python para enviar e-mails automaticamente. O código pode ser facilmente modificado para se adaptar às suas necessidades específicas, como enviar e-mails para diferentes destinatários, anexar arquivos, entre outros.

## Funcionalidades

- Envio de e-mails automáticos.
- Suporte para anexos.
- Personalização de mensagem (assunto, corpo do e-mail).
- Configuração fácil para diferentes provedores de e-mail (Gmail, Outlook, etc.).

## Pré-requisitos

Antes de começar, você precisará ter as seguintes bibliotecas Python instaladas:

- `smtplib`
- `email`
- `ssl`

Você pode instalar estas bibliotecas usando o pip:

```bash
pip install smtplib email ssl
```

## Configurações

<ol>
  <li>Clone este repositório:</li>
  
  ```bash
    git clone https://github.com/seu-usuario/envio-de-email-automatico-com-python.git
  ```

  <li>Navegue até o diretório do projeto:</li>

  ```bash
    cd envio-de-email-automatico-com-python
  ```

  <li>Crie o arquivo config.py e configure as informações de e-mail:</li>

  ```bash
    EMAIL_ADDRESS = 'seu-email@gmail.com'
    EMAIL_PASSWORD = 'sua-senha'
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465
  ```
</ol>
