from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Page import Page
import Constant

class LoginPage(Page):
    def __init__(self, driver, user):
        super().__init__(driver, user)

    def navigate(self):
        self.driver.get(Constant.Url.login_page)

    def input_login(self):
        login_d = Constant.Locator.login_input
        login_we = self.driver.find_element(login_d['by'], login_d['value'])
        login_we.send_keys(self.user.login)

    def input_password(self):
        password_d = Constant.Locator.password_input
        password_we = self.driver.find_element(password_d['by'], password_d['value'])
        password_we.send_keys(self.user.password)

    def choose_server(self):
        server_d = Constant.Locator.server_select
        server_we = Select(self.driver.find_element(server_d['by'], server_d['value']))
        server_we.select_by_visible_text(self.user.server)

    def login_submit(self):
        login_button_d = Constant.Locator.login_button
        login_button_we = self.driver.find_element(login_button_d['by'], login_button_d['value'])
        login_button_we.click()

    def login_error_check(self) -> bool:
        try:
            login_error_button_d = Constant.Locator.close_error_login_button
            login_error_button_we = self.driver.find_element(login_error_button_d['by'], login_error_button_d['value'])
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(login_error_button_we))
            print('zlapalem error logina')
            return False
        except:
            print("dane logowania poprawne")
            return True
            