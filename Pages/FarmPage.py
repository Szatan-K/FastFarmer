import selenium.common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Page import Page
import Constant

class FarmPage(Page):
    def __init__(self, driver, user):
        super().__init__(driver, user)

    def is_at(self):
        try:
            inner_quarter_d = Constant.Locator.inner_quarter
            inner_quarter_we = self.driver.find_element(inner_quarter_d['by'], inner_quarter_d['value'])
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(inner_quarter_we))
            return True
        except:
            return False
    
    def open_farm(self, index):
        try:
            farm_pos_d = Constant.Locator.farm_pos
            farm_pos_we = self.driver.find_element(farm_pos_d['by'], farm_pos_d['value'] + str(index))
            farm_pos_we.click()
        except:
            print(f'there was an error trying to click farm with index {index}')

    def close_farm(self):
        try:
            farm_close_button_d = Constant.Locator.farm_close_button
            farm_close_button_we = self.driver.find_element(farm_close_button_d['by'], farm_close_button_d['value'])
            WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(farm_close_button_we))
            farm_close_button_we.click()
        except Exception as e:
            print(f'error trying to close farm: {e}')
    
    def close_gather_box_dialog(self):
        try:
            close_gather_box_button_d = Constant.Locator.close_gather_box_button
            close_gather_box_button_we = self.driver.find_element(close_gather_box_button_d['by'], close_gather_box_button_d['value'])
            close_gather_box_button_we.click()
        except Exception as e:
            print(f'error trying to close gather dialog box: {e}')
    
    def close_news_main(self):
        try:
            close_newsbox_d = Constant.Locator.newsbox_close_button_1
            close_newsbox_we = self.driver.find_element(close_newsbox_d['by'], close_newsbox_d['value'])
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(close_newsbox_we))
            close_newsbox_we.click()
            print('newsbox closed')
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            print("newsbox didn't show up")
            
    def close_news_mini(self):
        #Worked with XPath, there are still issues getting it done by css selector
        #sometimes getting stale element exception if wait time == 5, works fine with 10(i guess)
        #changed css_selector, hope it works now 
        closed = 0
        for i in range(3):
            try:
                close_news_mini_d = Constant.Locator.mini_close_link_button_CSS
                close_news_mini_we = self.driver.find_element(close_news_mini_d['by'], close_news_mini_d['value'])
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(close_news_mini_we))
                close_news_mini_we.click()
                print('mini closed')
                closed +=1
            except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.StaleElementReferenceException):
                print(f"mini didn't show up")
        print(f'closed {closed} minis')

    def close_daily_login(self):
        #close_daily_button_d = Constant.Locator.daily_bonus_close_button
        try:
            claim_daily_button_d = Constant.Locator.daily_bonus_claim_button
            claim_daily_button_we = self.driver.find_element(claim_daily_button_d['by'], claim_daily_button_d['value'])
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(claim_daily_button_we))
            claim_daily_button_we.click()
            print('daily bonus claimed')
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
            print("daily bonus didn't show up")
        pass

    def close_news_all(self):
        self.close_news_main()
        self.close_news_mini()
        self.close_daily_login()
 
    def get_racks_items(farm_page) -> dict:
        rack_d = Constant.Locator.all_items
        rack_wes = farm_page.driver.find_elements(rack_d['by'], rack_d['value'])
        items = {}
        for element in rack_wes:
            #item's id
            items_id = element.get_attribute('id')

            #item's name
            item_d = Constant.Locator.items_name
            item_we = element.find_element(item_d['by'], item_d['value'])
            items_name = item_we.get_attribute('textContent')
            
            items[items_name] = items_id

        return items

    def get_areas(farm_page) -> list[tuple]:
        areas = []
        for i in range(6):
            try:
                pos_d = Constant.Locator.farm_pos
                pos_name_d = Constant.Locator.farm_pos_name1
                pos_we = farm_page.driver.find_element(pos_d['by'], pos_d['value'] + str(i + 1))
                pos_we_id = pos_we.get_attribute('id')
                pos_name = pos_we.find_element(pos_name_d['by'], '#' + pos_we_id + '_tt ' + pos_name_d['value'])
                field_name = pos_name.get_attribute(Constant.Attribute_HTML.text_css_selector)
                image_path = Constant.AREAS[field_name]
                if field_name in Constant.Message.all_locked:
                    field_name = Constant.LOCKED
                areas.append((field_name, image_path))
            except selenium.common.exceptions.NoSuchElementException:
                print("puste pole")
                areas.append((None, Constant.AREAS[None]))
        return areas