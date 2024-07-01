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

    #from toolbar
    water_crop_button = {'by': By.ID, 'value': 'giessen'}
    gather_all_button = {'by': By.ID, 'value': 'cropall'}
    close_gather_box_button = {'by': By.ID, 'value': 'globalbox_close'}

    #plants
    all_items = {'by': By.CSS_SELECTOR, 'value': '#rackItems .sack'}
    items_name = {'by': By.CLASS_NAME, 'value': 'headline'} # used on a webElement

    pass

class Plant:
    all_plants = {
        'Marchewki': {'price': 0.16, 'size': 1},
        'Zboże': {'price': 0.50, 'size': 2},
        'Ogórki': {'price': 0.52, 'size': 1},
        'Truskawki': {'price': 1.44, 'size': 1},
        'Kukurydza': {'price': 1.10, 'size': 4},
        'Rzodkiewki': {'price': 1.02, 'size': 1},
        'Pomidory': {'price': 1.96, 'size': 1},
        'Cebule': {'price': 2.28, 'size': 1},
        'Szpinak': {'price': 3.80, 'size': 1},
        'Koniczyna': {'price': 1.34, 'size': 2},
        'Rzepak': {'price': 2.75, 'size': 4},
        'Kalafiory': {'price': 3.69, 'size': 1},
        'Buraki pastewne': {'price': 3.95, 'size': 4},
        'Zioła': {'price': 8.05, 'size': 4},
        'Ziemniaki': {'price': 4.38, 'size': 1},
        'Słonecznik': {'price': 17.80, 'size': 4},          #have to check the name
        'Bławatek': {'price': 18.50, 'size': 4},            #
        'Szparagi': {'price': 12.40, 'size': 2},            #
        'Cukinia': {'price': 3.49, 'size': 1},              #
        'Jagoda': {'price': 5.19, 'size': 1},               #
        'Malina': {'price': 8.15, 'size': 1},               #
        'Porzeczka': {'price': 6.00, 'size': 1},            #
        'Jeżyna': {'price': 15.63, 'size': 1},              #
        'Mirabelka': {'price': 16.88, 'size': 4},           #
        'Jabłko': {'price': 37.50, 'size': 4},              #
        'Dynia': {'price': 3.90, 'size': 1},                #
        'Gruszka': {'price': 52.44, 'size': 4},             #
        'Wiśnia': {'price': 51.75, 'size': 4},              #
        'Śliwka': {'price': 60.25, 'size': 4},              #
        'Orzech włoski': {'price': 58.13, 'size': 4},       #
        'Oliwka': {'price': 66.19, 'size': 4},              #
        'Czerwona kapusta': {'price': 70.70, 'size': 4},    #
        'Stokrotki': {'price': 3.72, 'size': 2},        
    }
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

BY_ID = By.ID

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