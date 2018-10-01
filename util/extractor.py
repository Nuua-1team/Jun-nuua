# -*- coding: utf-8 -*-
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
# from util.instalogger im port InstaLogger
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
    def __init__(self,keyword):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        self.browser = webdriver.Chrome('chromedriver', chrome_options=options)

        self.keyword = keyword
        # self.resDict = {'media_id': [], 'img_url': [], 'review_url': [], 'display_date': [],'keyword':self.keyword}

        self.url = "https://www.tripadvisor.co.kr"
        # 나중에 database 클래스를 따로 뺄 예정
        #trip_review_url,trip_gallery_id


        self.trip_sql = '''
        INSERT IGNORE INTO trip_metadata (trip_gallery_id,trip_review_url) VALUES (%s, %s)
        '''
        self.img_sql ='''
        INSERT IGNORE INTO image_info (search_keyword,image_url,trip_idx,crawling_date) VALUES (\'''' + self.keyword+'''\', %s,%s,now())
        '''

        try:
            self.conn = pymysql.connect(
            # host='image-crawling-db.cmvxqjttnu3v.ap-northeast-2.rds.amazonaws.com',
            host="",
            port=3306,
            # user='nuua',
            user='root',
            # passwd=os.environ['NUUA_DB_PASS'],
            passwd=os.environ['MYSQL_PASS'],
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


    def insert_data(self,trip_list,img_list):
        self.cursor.executemany(self.trip_sql,trip_list)
        print(self.cursor.fetchall())
        first_id = self.conn.insert_id()
        for idx , val in enumerate(range(first_id,first_id+len(img_list))):
            img_list[idx].append(val)

        self.cursor.executemany(self.img_sql,img_list)
        print(self.cursor.fetchall())
        self.cursor.connection.commit()

    def get_data_from_thumb(self):
        print(str(len(self.browser.find_elements_by_css_selector(".tinyThumb")))+"개 가져와따")

        trip_list=[]
        img_list=[]
        for thumb in self.browser.find_elements_by_css_selector(".tinyThumb"):
            trip_list.append([thumb.get_attribute("data-mediaid"),thumb.get_attribute("data-reviewurl")])
            img_list.append([thumb.get_attribute("data-bigurl")])

        self.insert_data(trip_list,img_list)





    def __del__(self):
        self.browser.close()
        print ("browser closed")
        self.cursor.close()

    def go_next(self):
        origin_url = self.browser.current_url
        sql = 'select trip_gallery_id from trip_metadata order by trip_idx desc limit 1;'
        self.cursor.execute(sql)
        last_media_id = self.cursor.fetchone()['trip_gallery_id']

        new_url = origin_url.replace(re.findall("\d+", origin_url)[-1], last_media_id)
        self.browser.get("https://www.tripadvisor.co.kr/")
        self.browser.get(new_url)
        print(new_url)
        self.browser.implicitly_wait(10)
