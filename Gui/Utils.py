from selenium import webdriver
import Constant

def get_areas(driver: webdriver):
    ares = dict()
    pos_d = Constant.Locator.farm_pos
    for i in range(6):
        pos = driver.find_element(pos_d['by'], pos_d['value'] + str(i))
        print(pos)