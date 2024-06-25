from imap_tools import MailBox, AND
from offtest.data import my_email,acess_code


def login_email(usuario, senha):
    global loginIn
    loginIn = False
    try:
        mailbox = MailBox("imap.gmail.com").login(usuario, senha)
        print("OK")
        loginIn = True
        # print(loginIn)
        return mailbox,loginIn
        
        
    except Exception as e:
        print(f"Erro ao fazer login: {e}")
        loginIn = False
        # print(loginIn)
        return None




if __name__ == "__main__":
    usuario = my_email
    senha = acess_code
    resultado = login_email(usuario, senha)
    print(resultado)
    
    