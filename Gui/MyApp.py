from .Views.LoginFrame import LoginFrame
from .Views.MainTabView import MainTabView
from Gui.Background import Background
from Controller import Controller
import customtkinter as ctk


class MyApp(ctk.CTk):
    def __init__(self, user):
        super().__init__()
        self.controller = Controller(self, user)
        #config
        self.title('SzybkiFarmer')
        self.geometry('800x600')
        self.resizable(False,False)
        self.background = Background()
        self.set_background()
        self.set_to_login_window()

    def set_background(self):
        self.background.place(x=0,y=0, anchor=ctk.NW)   
        self.background.update()                        #updates the height and width

    def set_to_login_window(self):
        new_frame = LoginFrame(self, self.controller.bot)
        x = self.background.winfo_width()
        y = self.background.winfo_height()
        self.background.create_window(x//2, y//2, window=new_frame, anchor=ctk.CENTER, tags='frame')
        new_frame.entry_login.focus()

    def set_to_game_window(self):
        self.background.delete('frame')
        new_frame = MainTabView(self, self.controller.bot)
        x = self.background.winfo_width()
        y = self.background.winfo_height()
        self.background.create_window(x//2, y//2, window=new_frame, anchor=ctk.CENTER, tags='frame')
        self.background.update()

    def quit_myApp(self):
        self.controller.driver.quit()
        self.destroy()