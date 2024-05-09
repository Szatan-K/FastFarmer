from Pages.LoginPage import LoginPage
from Pages.FarmPage import FarmPage
import customtkinter as ctk

class Bot:
    def __init__(self, controller, driver, user):
        self.controller = controller
        self.driver = driver
        self.user = user
        self.money = None
        self.page = None

    def is_at_farm(self):
        
        
        pass

    def get_login_data(self, login_entry: ctk.CTkEntry, password_entry: ctk.CTkEntry, server_cmbbox: ctk.CTkComboBox):
        self.user.login = login_entry.get()
        self.user.password = password_entry.get()
        self.user.server = server_cmbbox.get()
        
    def login(self, login_entry: ctk.CTkEntry, password_entry: ctk.CTkEntry, server_cmbbox: ctk.CTkComboBox, remember_me: ctk.CTkComboBox):
        self.page = LoginPage(self.driver, self.user)                      # idk if it's good to load page every time u click a login button
        self.page.navigate()                                               # the problem is that i open a login page after clicking it, maybe should load login page on the start of an app, or change login button to 'try again' or smth
        self.get_login_data(login_entry, password_entry, server_cmbbox)
        self.page.input_login()
        self.page.input_password()
        self.page.choose_server()
        self.page.login_submit()
        if self.page.login_error_check():
            if remember_me.get():
                self.user.save_credentials(self.user.login, self.user.password, self.user.server)
            
            self.page = FarmPage(self.driver, self.user)
            self.page.close_news_all()
            self.page.accept_cookies()
            self.controller.myApp.set_to_game_window()