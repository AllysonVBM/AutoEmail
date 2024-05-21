from imap_tools import *
import os



#caminho da pasta para onde os curriculos serão salvos
way = ("C:/Users/allys/OneDrive/Área de Trabalho/Curriculos")

#credenciais do email
usuario =     #SEU EMAIL VAI AQUI
senha =       #A SENHA É A KEY DE ACESSO QUE O SEU EMAIL VAI FORNECER

meu_email = MailBox("imap.gmail.com").login(usuario,senha)


lista_emails = meu_email.fetch(AND(subject="Curriculo")) #PRIMEIRO FILTRO DO HEADER DO EMAIL
anexos_emails = meu_email.fetch(AND(body="Curriculo")) #SEGUNDO FILTRO DO BODY

def download_attachments(): 
    if len(email.attachments) > 0:
        for anexo in email.attachments:       #INFORMAÇÕES DO ANEXO
            name_attachments = anexo.filename   #Coleta o nome do arquivo
            if anexo.content_type == "application/pdf":   #filtra os documentos para baixar somente formato PDF
                download_dir = os.path.join(way, name_attachments)
                # if name_attachments:
                #     informacoes_anexo = anexo.payload
                with open(download_dir, "wb") as document:
                    document.write(anexo.payload)



for email in lista_emails:
    download_attachments()