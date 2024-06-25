from filterMail import searchInPdf
import os


def analyse_all_pdfs_in_folder(folder_path, search_string):
    total_found = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(folder_path, file_name)
            found, page_number = searchInPdf(file_path, search_string)
            if found:
                print(f'A palavra "{search_string}" foi encontrada no documento "{file_name}" na página {page_number}')
                total_found += 1
    print(f"Total de documentos contendo a palavra '{search_string}': {total_found}")
