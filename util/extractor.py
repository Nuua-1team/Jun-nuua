# -*- coding: utf-8 -*-
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
import re;
import pymysql;
import os;
from selenium.webdriver.common.keys import Keys

class CrawlBrowser:
    # browser = None
    # option = None
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        self.browser = webdriver.Chrome('chromedriver', chrome_options=options)
        print("크롤링할 앨범 키워드 입력:")
        self.keyword = input()
        self.resDict = {'media_id': [], 'img_url': [], 'review_url': [], 'display_date': [],'keyword':self.keyword}
        self.url = "https://www.tripadvisor.co.kr"

        try:
            self.conn = pymysql.connect(
            host='image-crawling-db.cmvxqjttnu3v.ap-northeast-2.rds.amazonaws.com',
            port=3306,user='nuua',
            passwd=os.environ['NUUA_DB_PASS'],
            db='image_crawling',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.conn.cursor()

        except pymysql.Error as e:
            print ("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit()


    def go_album(self):
        self.browser.get(self.url+"/Search?uiOrigin=MASTHEAD&q="+self.keyword)
        print("url로 접속")
        # self.browser.implicitly_wait(10)

        # self.browser.execute_script("placementEvCall('taplc_masthead_search_0', 'deferred/lateHandlers.showSearchOverlay', event, this);");
        # self.browser.implicitly_wait(10)
        # self.browser.find_elements_by_css_selector("#mainSearch")[0].send_keys(self.keyword)
        # self.browser.implicitly_wait(10)
        # self.browser.find_elements_by_css_selector("#mainSearch")[0].send_keys(Keys.ENTER)
        # self.browser.find_elements_by_css_selector("#mainSearch")[0].send_keys(Keys.ENTER)
        # self.browser.implicitly_wait(10)
        # pdb.set_trace();
        self.browser.implicitly_wait(10)
        self.url+=self.browser.find_elements_by_xpath("//div[@class='result-title']//span[text()='"+self.keyword+"']/parent::*")[0].get_attribute("onclick").split("'")[3]
        self.browser.implicitly_wait(10)
        self.browser.get(self.url)

        self.browser.execute_script("ta.plc_resp_photo_mosaic_ar_responsive_0_handlers.openPhotoViewer();")
        print("앨범 클릭")
        self.browser.implicitly_wait(10)
        self.browser.find_elements_by_css_selector(".photoGridImg")[0].click()
        print("첫번째 사진 클릭")
        self.browser.implicitly_wait(10)


    def get_data_from_thumb(self):
        print(str(len(self.browser.find_elements_by_css_selector(".tinyThumb")))+"개 가져와따")
        for thumb in self.browser.find_elements_by_css_selector(".tinyThumb"):
            self.resDict['media_id'].append(thumb.get_attribute("data-mediaid"))
            self.resDict['img_url'].append(thumb.get_attribute("data-bigurl"))
            self.resDict['review_url'].append(thumb.get_attribute("data-reviewurl"))
            self.resDict['display_date'].append(thumb.get_attribute("data-displaydate"))



        return self.resDict


    def __del__(self):
        self.browser.close()
        print ("browser closed")

    def go_next(self):
        origin_url = self.browser.current_url
        new_url = origin_url.replace(re.findall("\d+", origin_url)[-1], self.resDict["media_id"][-1])
        self.browser.get("https://www.tripadvisor.co.kr/")
        self.browser.get(new_url)
        print(new_url)
        self.browser.implicitly_wait(10)
        self.resDict = {'media_id': [], 'img_url': [], 'review_url': [], 'display_date': []}
        # self.browser.execute_script("location.reload();")
        self.browser.implicitly_wait(10)
