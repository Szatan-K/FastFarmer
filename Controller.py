from selenium import webdriver
from Bot import Bot

class Controller:
    def __init__(self, myApp, user):
        #additional option to prevent browser's autoclose
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.myApp = myApp
        self.bot = Bot(self, self.driver, user)
    