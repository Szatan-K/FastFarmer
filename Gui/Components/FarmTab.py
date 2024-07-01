from PIL import Image, ImageTk
from Pages.FarmPage import FarmPage
import Constant
import customtkinter as ctk
import threading


class FarmTab(ctk.CTkFrame):
    def __init__(self, master, bot, **kwargs):
        super().__init__(master, **kwargs)
        self.bot = bot
        self.farm_preview = FarmTabAreas(self, self.bot)                                                               #name to be changed
        self.farm_preview.configure(width=700, fg_color='cyan')
        self.control_panel = FarmTabPanel(self, bot=self.bot, farmTab=self)

        self.farm_preview.pack_propagate(False)
        self.farm_preview.grid_areas(self.farm_preview.areas)
        self.farm_preview.grid_set_weight()
        self.farm_preview.pack(expand=True, fill=ctk.BOTH)
        self.control_panel.pack(expand=True, fill=ctk.BOTH)

    def execute_plant(self):
        indexes = self.farm_preview.check_checkboxes()
        chosen_crop = self.control_panel.combobox_plant.get()
        self.bot.plant(indexes, chosen_crop)
        
    def execute_gather_all(self):
        # to be changed, so that fields with name 'pole' are taken
        indexes = self.farm_preview.check_checkboxes()
        self.bot.gather_plants(indexes)

    def execute_get_racks_items(self):
        print(type(self.bot.page))
        print(self.bot.page.get_racks_items())

class FarmTabPanel(ctk.CTkFrame):
    def __init__(self, master, bot, farmTab, **kwargs):
        super().__init__(master, **kwargs)
        self.bot = bot
        self.farmTab = farmTab
        self.load_farm_button = ctk.CTkButton(self, text='Load Farm', command=farmTab.farm_preview.load_areas)
        
        self.plant_button = ctk.CTkButton(self, text='Plant', command = farmTab.execute_plant)

        self.gather_button = ctk.CTkButton(self, text='Gather plants', command = farmTab.execute_gather_all)

        self.combobox_plant = ctk.CTkComboBox(self, values = [key for key in Constant.Plant.all_plants.keys()], width=150)

        self.test_button = ctk.CTkButton(self, text='testuje rack itemy', command = farmTab.execute_get_racks_items)


        self.load_farm_button.grid(row=0, column=0, rowspan=2)
        self.plant_button.grid(row=0, column=1,)
        self.combobox_plant.grid(row=1, column=1)
        self.gather_button.grid(row=0, column=2, rowspan=2)
        self.test_button.grid(row=0, column=3, rowspan=2)

class FarmTabImage(ctk.CTkFrame):
    def __init__(self, master, name, image, **kwargs):
        super().__init__(master, **kwargs)
        self.img = Image.open(image)
        self.resized_img = self.img.resize((110,110))
        self.photo = ImageTk.PhotoImage(self.resized_img)
        self.canvas = ctk.CTkCanvas(self, width=self.resized_img.width, height=self.resized_img.height)
        self.canvas.configure(borderwidth=0, highlightthickness=0, bg='black')
        self.canvas.create_image(0,0, image=self.photo, anchor=ctk.NW)
        
        self.configure(fg_color='red')
        self.canvas.grid(row=0, column=0)
        
        if name == 'Pole':
            self.description = ctk.CTkCheckBox(self, text=name, width=0)  # width 0 helps with positioning the checkbox to the middle
            self.description.grid(row=1, column=0, pady=10)    
        else:
            self.description = ctk.CTkLabel(self, text=name)
            self.description.grid(row=1, column=0 , pady=10)

class FarmTabAreas(ctk.CTkFrame):
    def __init__(self, master, bot, **kwargs):
        super().__init__(master, **kwargs)
        self.bot = bot
        self.configure(width=700, height=500, fg_color='yellow')
        self.areas = self.initialize_areas()

    def check_checkboxes(self) -> list[int]:
        indexes = []
        for i in range(len(self.areas)):
            if isinstance(self.areas[i].description, ctk.CTkCheckBox):
                if self.areas[i].description.get():
                    indexes.append(i+1)
        return indexes

    def load_areas(self):
        if not isinstance(self.bot.page, FarmPage):
            self.bot.page = FarmPage
        areas = FarmPage.get_areas(self.bot.page)
        created_areas = self.create_areas(areas)
        self.areas = created_areas
        self.grid_areas(created_areas)

    def grid_areas(self, areas: list[FarmTabImage]):
        for i in range(2):
            for j in range(3):
                index = i * 3 + j
                areas[index].grid(row=i, column=j)
        for child in self.winfo_children():
           child.grid_configure(padx=10, pady=10)
        
    def grid_set_weight(self):
        for column_num in range(self.grid_size()[0]):
            self.grid_columnconfigure(column_num, weight=1)

    def create_areas(self, areas: list[tuple]) -> list[FarmTabImage]:
        created_areas = []
        for tpl in areas:
            name, image = tpl
            area = FarmTabImage(self, name, image)
            created_areas.append(area)
        return created_areas

    def initialize_areas(self) -> list[FarmTabImage]: # add initializing from the credentials or another file, add saving the areas
        created_areas = []
        for i in range(6):
            area = FarmTabImage(self, None, Constant.AREAS[None])
            created_areas.append(area)
        return created_areas