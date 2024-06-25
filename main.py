import os
from imap_tools import MailBox, AND
import PyPDF2
from offtest.data import path_to_folder
import time
from offtest.data import my_email,acess_code
def process_email_password(email, password):

    
    way = path_to_folder
    startTimer = time.time()

    def login_email(usuario, senha):  
        try:    
            mailbox = MailBox("imap.gmail.com").login(usuario, senha)
            print("Login bem-sucedido")
            return mailbox
        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return None

    def fetch_emails(mailbox, subject_filter="Curriculo"):
        try:
            emails = list(mailbox.fetch(AND(subject=subject_filter)))
            print(f"{len(emails)} emails encontrados com o assunto '{subject_filter}'")
            return emails
        except Exception as e:
            print(f"Erro ao buscar emails: {e}")
            return []

    def download_attachments(email, folder_path):
        if email.attachments:
            for anexo in email.attachments:
                if anexo.content_type == "application/pdf":
                    file_path = os.path.join(folder_path, anexo.filename)
                    with open(file_path, "wb") as document:
                        document.write(anexo.payload)
                    print(f"Anexo {anexo.filename} salvo em {file_path}")
                    return file_path, anexo.filename
        return None, None

    def search_in_pdf(file_path, search_string):
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page_number in range(len(pdf_reader.pages)):
                    text = pdf_reader.pages[page_number].extract_text()
                    if search_string in text:
                        print(f'A palavra "{search_string}" foi encontrada na página {page_number + 1}')
                        return True, page_number + 1
            print(f'A palavra "{search_string}" não foi encontrada no PDF {file_path}')
            return False, None
        except Exception as e:
            print(f"Erro ao ler o PDF {file_path}: {e}")
            return False, None

    def analyse_all_pdfs_in_folder(folder_path, search_string):
        total_found = 0
        for file_name in os.listdir(folder_path):
        
            if file_name.endswith('.pdf'):
                file_path = os.path.join(folder_path, file_name)
                found, page_number = search_in_pdf(file_path, search_string)
                if found:
                    print(f'A palavra "{search_string}" foi encontrada no documento "{file_name}" na página {page_number}')
                    total_found += 1
        print(f"Total de documentos contendo a palavra '{search_string}': {total_found}")

    mailbox = login_email(email, password)
    if not mailbox:
        return "Erro ao fazer login."

    lista_emails = fetch_emails(mailbox)
    if not lista_emails:
        print("Nenhum email encontrado")
    
    for email in lista_emails:
        download_attachments(email, way)

    # Se você quiser ler PDFs em uma pasta específica ----  analyse_all_pdfs_in_folder(way, 'Curriculo')


    endTimer = time.time()
    dif = (endTimer - startTimer)
    return f"Processamento concluído em {round(dif)} segundos."

if __name__ == "__main__":
    email =  my_email  # Substitua pelo seu email
    password = acess_code  # Substitua pela sua senha

    resultado = process_email_password(email, password)
    print(resultado)
