import os
import PyPDF2
from imap_tools import MailBox, AND
from imap_tools import *
from offtest.data import path_to_folder
import time

way = path_to_folder
startTimer = time.time()

def fetchEmails(mailbox, subject_filter="Curriculo"):
    try:
        emails = list(mailbox.fetch(AND(subject=subject_filter)))
        print(f"{len(emails)} emails encontrados com o assunto '{subject_filter}'")
        return emails
    except Exception as e:
        print(f"Erro ao buscar emails: {e}")
        return []

def downloadAttachments(email, folder_path):
    if email.attachments:
        for anexo in email.attachments:
            if anexo.content_type == "application/pdf":
                file_path = os.path.join(folder_path, anexo.filename)
                with open(file_path, "wb") as document:
                    document.write(anexo.payload)
                print(f"Anexo {anexo.filename} salvo em {file_path}")
                return file_path, anexo.filename
    print("Nenhum anexo PDF encontrado neste email")
    return None, None

def searchInPdf(file_path, search_string):
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

