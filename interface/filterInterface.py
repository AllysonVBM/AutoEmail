import customtkinter as ctk
from customtkinter import *



class NextWindow:
    def next_window(self):
            self.root = ctk.CTkToplevel()
            self.root.title("AutoEmail")
            self.widthWindow = 800
            self.heightWindow = 400
            self.width_info = self.root.winfo_screenwidth()
            self.height_info = self.root.winfo_screenheight()
            self.posx = int(self.width_info / 2 - self.widthWindow / 2)
            self.posy = int(self.height_info / 2 - self.heightWindow / 2 - 50)
            self.root.geometry(f"{self.widthWindow}x{self.heightWindow}+{self.posx}+{self.posy}")
            self.root.resizable(width=False, height=False)
            ctk.set_appearance_mode("dark")

            self.create_widgets2()


    def create_widgets2(self):
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
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    NextWindow().run()