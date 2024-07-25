from imap_tools import MailBox
from data import pathFolder
from data import yourEmail,yourAcess_code #Remove this line when you using
import time

def processEmailPassword():
    startTimer = time.time()
    
    def loginIn():
        try:
            mailbox = MailBox("imap.gmail.com").login(yourEmail, yourAcess_code)
            print("Login Bem-sucedido!")
            return mailbox,True
        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return None ,False
        

    mailbox, sucess = loginIn()

    if sucess:
        endTimer = time.time()
        print(f"Tempo de execução: {int(endTimer - startTimer)} segundo/s")
        return mailbox
    else:
        print("Falha ao fazer login.")
        return None
    
    
# processEmailPassword()

