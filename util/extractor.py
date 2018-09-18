"""Methods to extract the data for the given usernames profile"""
# from time import sleep
# from re import findall
# import math
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
# import requests
# from util.settings import Settings
# from .util import web_adress_navigator
# from util.extractor_posts import extract_post_info
# import datetime
# from util.instalogger import InstaLogger
# from util.exceptions import PageNotFound404,NoInstaProfilePageFound,NoInstaPostPageFound
from selenium import webdriver
import pdb;


def go_album(url,browser):
    browser.get(url)
    browser.implicitly_wait(5)
    browser.execute_script("ta.plc_resp_photo_mosaic_ar_responsive_0_handlers.openPhotoViewer();")
    browser.implicitly_wait(5)
    browser.find_elements_by_css_selector(".photoGridImg")[0].click()
    browser.implicitly_wait(5)

def get_data_from_thumb(browser):
    resDict = { 'media_id' : [], 'img_url' : [],'review_url':[],'display_date':[] }
    for thumb in browser.find_elements_by_css_selector(".tinyThumb"):
        resDict['media_id'].append(thumb.get_attribute("data-mediaid"))
        resDict['img_url'].append(thumb.get_attribute("data-bigurl"))
        resDict['review_url'].append(thumb.get_attribute("data-reviewurl"))
        resDict['display_date'].append(thumb.get_attribute("data-displaydate"))
    return resDict
