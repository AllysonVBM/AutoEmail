import os
import PyPDF2


def searchInPdf(pdf_path, searchString):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for pageNumber in range(len(pdf_reader.pages)):
                text = pdf_reader.pages[pageNumber].extract_text()
                if searchString in text:
                    return True, pageNumber + 1
        return False, None
    except Exception as e:
        print(f"Erro ao ler o PDF {pdf_path}: {e}")
        return False, None
    
def analyse_all_pdfs_in_folder(folder_path, searchString):
    totalFound = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file_name)
            found, pageNumber = searchInPdf(pdf_path,searchString)
            if found:
                print(f'A palavra "{searchString}" foi encontrada no documento "{file_name}" na página {pageNumber}')
                totalFound += 1
    print(f"Total de documentos contendo a palavra '{searchString}': {totalFound}")


if __name__ == "__main__":
    searchString = 'Python'
    path_folder = "C:/Users/allys/OneDrive/Área de Trabalho/Curriculos"
    analyse_all_pdfs_in_folder(path_folder,searchString)


