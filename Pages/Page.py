import selenium.common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Constant
import time

class Page:
    '''
    Base Class to interact with every Page
    '''
    def __init__(self, driver, user):
        self.driver = driver
        self.user = user

    def refresh(self):
        self.driver.refresh()

    def quit(self):
        self.driver.quit()

    def accept_cookies(self):
        cookie_button_d = Constant.Locator.cookies_accept_button
        cookie_button_we = self.driver.find_element(cookie_button_d['by'], cookie_button_d['value'])
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(cookie_button_we))
            cookie_button_we.click()
            print("Cookies accepted")
        except selenium.common.exceptions.TimeoutException:
            print("Cookies didn't show up")

    def reclick(self, web_element, i):
        clicked = False
        attempt = 0
        while attempt < 100 and not clicked:
            try:
                print('reclick invoked')
                web_element.click()
                clicked = True
                continue
            except selenium.common.exceptions.StaleElementReferenceException:
                attempt += 1
            continue
        if not clicked:
            print('critical error trying to reclick')
            