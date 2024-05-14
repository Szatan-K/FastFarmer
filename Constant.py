from selenium.webdriver.common.by import By

class Url:
    server = 0
    login_page = 'https://www.wolnifarmerzy.pl'
    #farm_page = f'https://s{server}.wolnifarmerzy.pl/main.php?ref='

class Locator:
    
    #LoginPage -----------------------------------------------------------------------------------------------------
    login_input = {'by': By.ID, 'value': 'loginusername'}
    password_input = {'by': By.ID, 'value': 'loginpassword'}
    server_select = {'by': By.ID, 'value': 'loginserver'}
    login_button = {'by': By.ID, 'value': 'loginbutton'}
    newsbox_close_button_1 = {'by': By.ID, 'value': 'newsbox_close'}
    mini_close_link_button_CSS = {'by': By.CSS_SELECTOR, 'value': '#specialoffer_new_content > div.mini_close.link'}
    mini_close_link_button_XPATH = {'by': By.XPATH, 'value': '//*[@id="specialoffer_new_content"]/div[15]'}

    daily_bonus_claim_button = {'by': By.ID, 'value': 'loginbonus_button'} # not sure
    daily_bonus_close_button = {'by': By.CSS_SELECTOR, 'value': '#loginbonus .mini_close link'}

    #cookies
    cookies_accept_button = {'by': By.CLASS_NAME, 'value': 'cookiemon-btn-accept'}
    
    close_error_login_button = {'by': By.ID, 'value': 'errorback'}

    #FarmPage ------------------------------------------------------------------------------------------------------
    farm_pos = {'by': By.ID, 'value': 'farm1_pos'} #need to add a number in range 1-6 at the end of the value
    farm_pos_name = {'by': By.XPATH, 'value': '//*[@id="farm1_pos1_tt"]/div'}
    farm_pos_name1 = {'by': By.CSS_SELECTOR, 'value': 'div'}
    inner_quarter = {'by': By.ID, 'value': 'farm_inner_headquarter'}    
    
    farm_field = {'by': By.ID, 'value':'field'} #need to add a number in range 1-120 at the end of the value
    rack_item_name = {'by': By.CSS_SELECTOR, 'value': '#rackitem1_tt > div.headline'} #have to divide it into 2 parts
    
    farm_close_button = {'by': By.ID, 'value': 'gardencancel'}

    rack_item17_test = {'by': By.ID, 'value': 'rackitem17'}
    pass

class Price:
      pass

class Attribute_HTML:
    text_xpath = 'innerHTML'
    text_css_selector = 'textContent'

class Message:
    field_3_locked = 'Zwolnić miejsce pod zabudowę?1.000,00 ft'
    field_4_locked = 'Zwolnić miejsce pod zabudowę?4.300,00 ft' 
    field_5_locked = 'Zwolnić miejsce pod zabudowę?10.000,00 ft'
    field_6_locked = 'Zwolnić miejsce pod zabudowę?22.800,00 ft'
    all_locked = [field_3_locked, field_4_locked, field_5_locked, field_6_locked]

class MyImage:
    field = 'Images/Field.png'
    blank = 'Images/None.png'
    locked_3 = 'Images/Locked_3.png'
    locked_4 = 'Images/Locked_4.png'
    locked_5 = 'Images/Locked_5.png'
    locked_6 = 'Images/Locked_6.png'
    coop_lvl2 = 'Images/Coop_lvl2.png'
    barn_lvl2 = 'Images/Barn_lvl2.png'

AREAS = {'Pole': MyImage.field,
         None: MyImage.blank,
         Message.field_3_locked: MyImage.locked_3,
         Message.field_4_locked: MyImage.locked_4,
         Message.field_5_locked: MyImage.locked_5,
         Message.field_6_locked: MyImage.locked_6,
         'Kurnik': MyImage.coop_lvl2,
         'Obora': MyImage.barn_lvl2
         }

LOCKED = 'Zablokowane'

SERVERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']