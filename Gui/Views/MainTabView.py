import customtkinter as ctk
from Gui.Components.FarmTab import FarmTab

class MainTabView(ctk.CTkTabview):
    def __init__(self, master, bot,  **kwargs):
        super().__init__(master, **kwargs)
        self.bot = bot
        self.add("Farma")
        self.add("Market")

        self.farmTab = FarmTab(self.tab('Farma'), bot=self.bot)
        self.farmTab.configure(width=700, height=500)
        self.farmTab.pack_propagate(False)
        self.farmTab.pack(expand=True, fill=ctk.BOTH)