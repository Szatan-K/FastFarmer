import customtkinter as ctk
from PIL import Image, ImageTk

class Background(ctk.CTkCanvas):
    def __init__(self):
        super().__init__()
        self.img = Image.open('Images/wolnifarmerzy.png')
        self.resized_img = self.img.resize((800,600))
        self.photo = ImageTk.PhotoImage(self.resized_img)
        #setting proper width and height of main app window
        super().configure(width=self.resized_img.width, height=self.resized_img.width)
        self.configure(width=self.resized_img.width, height=self.resized_img.height, borderwidth=0, highlightthickness=0)
        self.create_image(0,0, image=self.photo, anchor=ctk.NW)


        