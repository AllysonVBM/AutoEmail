import customtkinter as ctk
from customtkinter import *
from core.loginEmail import login_email
from filterInterface import NextWindow


class AutoEmailLogin:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("AutoEmail")
        self.widthWindow = 800
        self.heightWindow = 170
        self.width_info = self.root.winfo_screenwidth()
        self.height_info = self.root.winfo_screenheight()
        
        self.posx = int(self.width_info / 2 - self.widthWindow / 2)
        self.posy = int(self.height_info / 2 - self.heightWindow / 2 - 50)

        self.root.geometry(f"{self.widthWindow}x{self.heightWindow}+{self.posx}+{self.posy}")
        self.root.resizable(width=False, height=False)
        ctk.set_appearance_mode("dark")

        self.create_widgets()

    
    def create_widgets(self):
        email_login = ctk.CTkLabel(self.root, text="E-mail: ", font=ctk.CTkFont(size=20))
        email_login.place(x=86, y=20)
        
        email_password = ctk.CTkLabel(self.root, text="PasswordKey: ", font=ctk.CTkFont(size=20))
        email_password.place(x=20, y=60)
        
        self.email_text_box = ctk.CTkEntry(master=self.root, width=530, height=30, corner_radius=20, font=ctk.CTkFont(size=20))
        self.email_text_box.place(x=190, y=20)
        
        self.password_text_box = ctk.CTkEntry(master=self.root, width=530, height=30, corner_radius=20, font=ctk.CTkFont(size=20))
        self.password_text_box.place(x=190, y=60)
        self.password_text_box.bind('<KeyRelease>', self.format_password)
        
        emailConfirmButton = ctk.CTkButton(master=self.root, width=5, height=40, text="Confirmar", corner_radius=50, command=self.confirm_email_password)
        emailConfirmButton.place(x=370, y=110)

    def format_password(self, event):
        content = self.password_text_box.get().replace(" ", "")
        if len(content) > 16:
            content = content[:16]
        
        formatted_content = ' '.join(content[i:i+4] for i in range(0, len(content), 4))
        self.password_text_box.delete(0, END)
        self.password_text_box.insert(0, formatted_content)


    def confirm_email_password(self):
        email = self.email_text_box.get()
        password = self.password_text_box.get()
        result = login_email(email, password)
        if result:
            self.root.destroy()
            self.root.update()
            winInterfaceFilter = NextWindow()
            winInterfaceFilter.next_window()
        
            

            
            
        print(result)  # Exibir resultado no console para depuração

        
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    AutoEmailLogin().run()
