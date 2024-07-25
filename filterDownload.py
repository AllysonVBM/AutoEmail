from imap_tools import MailBox, AND
import os
from loginMail import processEmailPassword
from data import pathFolder
from pdfUtils import searchInPdf, analyse_all_pdfs_in_folder



def Filter():
    def fetchEmail(mailbox, subjectFilter = "Curriculo"): #Seach for that word in the email header
        try:
            headerFilter = list(mailbox.fetch(AND(subject=subjectFilter)))
            print(f"{len(headerFilter)} emails encontrados com o assunto {subjectFilter}")
            return headerFilter
        
        except Exception as e:
            print(f"Nenhum email Encontrado! {e}")
            return []
        
    def downloadAttachments(email, file_path):
        if email.attachments:
            for anexo in email.attachments: 
                if anexo.content_type == "application/pdf":
                    file_path = os.path.join(pathFolder,anexo.filename)
                    with open(file_path, "wb") as document:
                        document.write(anexo.payload)
                    print(f"Anexo {anexo.filename} salvo em {file_path}")
                    return file_path, anexo.filename
        return None, None    
    

    mailbox = processEmailPassword()
    def Status(status):
        if status == True:
            print(f"status: OK!")

        else:
            print(f"status: Erro!")

    if not mailbox:
        print("Não foi possivel fazer o login e obter o mailbox.")
        status = False 
        return
        
    emailsList = fetchEmail(mailbox)


    for email in emailsList:
        file_path,filename = downloadAttachments(email,pathFolder)
        status = True
        if file_path:
            Status(status)


if __name__ == "__main__":
    result = Filter()
    searchString = 'Python'   #search for that word in the PDF document 
    analyse_all_pdfs_in_folder(pathFolder, searchString)
    





