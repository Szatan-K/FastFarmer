import customtkinter as ctk
from User import User

SERVERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, bot, **kwargs):
        super().__init__(master, **kwargs)
        self.bot = bot
        self.configure(width=400, height=300)
        self.btn_login = ctk.CTkButton(self, text='Login', command=lambda: bot.login(self.entry_login, self.entry_password, self.combobox_server, self.checkbox_remember_me))
        self.btn_quit = ctk.CTkButton(self, text='Quit', command=master.quit_myApp)
        self.label_server = ctk.CTkLabel(self,text='Server:')
        self.combobox_server = ctk.CTkComboBox(self, values=SERVERS, width=75)
        self.checkbox_remember_me = ctk.CTkCheckBox(self, text='Remember me')
        self.entry_login = ctk.CTkEntry(self, placeholder_text='Login')
        self.entry_password = ctk.CTkEntry(self, placeholder_text='Password', show='*')
        
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)      

        self.label_server.grid(row=0, column=0)
        self.combobox_server.grid(row=0, column=1)
        self.checkbox_remember_me.grid(row=1, column=0, columnspan=2)
        self.entry_login.grid(row=0, column=2, columnspan=2)
        self.entry_password.grid(row=1, column=2, columnspan=2)
        self.btn_login.grid(row=2, column=0, columnspan=2)
        self.btn_quit.grid(row=2, column=2, columnspan=2)

        creds = User.check_for_credentials()
        if creds:
            self.entry_login.insert(0, creds['login'])
            self.entry_password.insert(0, creds['password'])
            self.combobox_server.set(creds['server'])