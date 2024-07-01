from Pages.LoginPage import LoginPage
from Pages.FarmPage import FarmPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox as msgbox
import customtkinter as ctk
import Constant
import time

class Bot:
    def __init__(self, controller, driver, user):
        self.controller = controller
        self.driver = driver
        self.user = user
        self.money = None
        self.page = None

    def is_at_farm(self) -> bool:
        if isinstance(self.page, FarmPage):
            print(self.page.is_at())
            return self.page.is_at()
        else:
            print('naura')
            return False

    def plant(self, indexes: list[int]):
        for index in indexes:
            try:
                self.page.open_farm(index)
                time.sleep(1)
                self.plant_plants()
                self.water_plants()
                self.page.close_farm()
            except Exception as e :
                print(f'There was an error: {e}')

    def plant_plants(self):
        is_crop_chosen = False
        try:
            rack_item_d = Constant.Locator.rack_item17_test
            rack_item_we = self.driver.find_element(rack_item_d['by'], rack_item_d['value'])
            rack_item_we.click()
            is_crop_chosen = True
            time.sleep(1)
        except Exception as e:
            print(f'error choosing crop to plant: {e}')
        if is_crop_chosen:
            for i in range(120):
                try:
                    farm_field_d = Constant.Locator.farm_field
                    farm_field_we = self.driver.find_element(farm_field_d['by'], farm_field_d['value'] + str(i+1))
                    farm_field_we.click()
                except:
                    self.page.reclick(farm_field_we)
                    continue
            time.sleep(1)

    def water_plants(self):
        watercan_clicked = False
        try:
            water_crop_button_d = Constant.Locator.water_crop_button
            water_crop_button_we = self.driver.find_element(water_crop_button_d['by'], water_crop_button_d['value'])
            water_crop_button_we.click()
            watercan_clicked = True
        except Exception as e:
            print(f'error trying click watercan: {e}')
        if watercan_clicked:
            for i in range(120):
                try:
                    farm_field_d = Constant.Locator.farm_field
                    farm_field_we = self.driver.find_element(farm_field_d['by'], farm_field_d['value'] + str(i+1))
                    farm_field_we.click()
                except:
                    self.page.reclick(farm_field_we)
            time.sleep(1)

    def gather_plants(self, farm_indexes: list[int]):
        for index in farm_indexes:
            try:
                self.page.open_farm(index)
                gather_all_button_d = Constant.Locator.gather_all_button
                gather_all_button_we = self.driver.find_element(gather_all_button_d['by'], gather_all_button_d['value'])
                gather_all_button_we.click()
                time.sleep(1)
                self.page.close_gather_box_dialog()
                time.sleep(1)
                self.page.close_farm()
            except Exception as e:
                print(f'error trying to gather plants: {e}')
        pass

    def get_login_data(self, login_entry: ctk.CTkEntry, password_entry: ctk.CTkEntry, server_cmbbox: ctk.CTkComboBox):
        self.user.login = login_entry.get()
        self.user.password = password_entry.get()
        self.user.server = server_cmbbox.get()
        
    def login(self, login_entry: ctk.CTkEntry, password_entry: ctk.CTkEntry, server_cmbbox: ctk.CTkComboBox, remember_me: ctk.CTkComboBox):
        self.page = LoginPage(self.driver, self.user)                      # idk if it's good to load page every time u click a login button
        self.page.navigate()                                               # the problem is that i open a login page after clicking it, maybe should load login page on the start of an app, or change login button to 'try again' or smth
        self.get_login_data(login_entry, password_entry, server_cmbbox)
        if self.user.login == '' or self.user.password == '':
            msgbox.showerror('Error','Login and password fields can not be empty')
        else:
            self.page.input_login()
            self.page.input_password()
            self.page.choose_server()
            self.page.login_submit()
            if self.page.login_error_check():
                if remember_me.get():
                    self.user.save_credentials(self.user.login, self.user.password, self.user.server)
                
                self.page = FarmPage(self.driver, self.user)
                self.controller.myApp.set_to_game_window()
                self.page.accept_cookies()
                if not self.user.check_if_logged_today():
                    self.page.close_news_all()
