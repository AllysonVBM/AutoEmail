from imap_tools import MailBox, AND
import os
import PyPDF2

# Caminho da pasta para onde os currículos serão salvos
way = "C:/Users/allys/OneDrive/Área de Trabalho/Curriculos"

# Credenciais do email
usuario = "..."
senha = "..."

# Login no email
meu_email = MailBox("imap.gmail.com").login(usuario, senha)

# Filtro de emails
lista_emails = meu_email.fetch(AND(subject="Curriculo")) # PRIMEIRO FILTRO DO HEADER DO EMAIL

def download_attachments(email): 
    if len(email.attachments) > 0:
        for anexo in email.attachments:  # INFORMAÇÕES DO ANEXO
            name_attachments = anexo.filename  # Coleta o nome do arquivo
            if anexo.content_type == "application/pdf":  # Filtra os documentos para baixar somente formato PDF
                print("E-mail encontrado, Baixando PDF....")
                download_dir = os.path.join(way, name_attachments)
                with open(download_dir, "wb") as document:
                    document.write(anexo.payload)
                return download_dir, name_attachments  # Retorna o caminho do arquivo e o nome do anexo
    return None, None

def analysi(file_path, file_name):
    if file_path is not None:
        pdf_file = open(file_path, 'rb')  # ABRE UM ARQUIVO PDF
        pdf_reader = PyPDF2.PdfReader(pdf_file)  # CRIA UM LEITOR DE PDF
        search_string = 'Python'  # A PALAVRA QUE DESEJA BUSCAR
        for page_number in range(len(pdf_reader.pages)):  # LOOP para ler páginas
            text = pdf_reader.pages[page_number].extract_text()
            if search_string in text:
                print(f'A palavra  "{search_string}" Foi encontrada no documento  "{file_name}" na pagina  {page_number + 1}')
                found = True
        pdf_file.close()  # FECHAR PDF
    else:
        print("Nenhum Arquivo PDF para analisar")
    return found 

# Processamento dos emails
for email in lista_emails:
    file_path, file_name = download_attachments(email)  # Passa o email para a função e recebe o caminho e nome do anexo

# Analisar todos os arquivos na pasta
def analyse_all_pdfs_in_folder(folder_path):
    total_found = 0 #Contador do documento que contem a palavra de busca
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(folder_path, file_name)
            if analysi(file_path, file_name):
                total_found += 1 #Adiciona 1 ao contador de documentos contendo a palavra buscada
    print(f"Total de documentos contendo a palavra buscada: {total_found}")

# Executa a análise para todos os PDFs na pasta especificada
analyse_all_pdfs_in_folder(way)
