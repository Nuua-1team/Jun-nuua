# -*- coding: utf-8 -*-
from selenium import webdriver
from util.extractor import *
import pdb
import time

if __name__ == "__main__":
    try:
        keyword = ['경복궁', '창덕궁', '광화문', '덕수궁', '종묘', '숭례문', '동대문', '경희궁', '보신각']
        start_time = time.time()
        print("크롤링할 앨범 키워드 입력:")
        a = input()
        browser = CrawlBrowser(a)

        browser.go_album()

        # browser.get_data_from_thumb()
        # browser.insert()
        for i in range(100):
            browser.go_next()
            browser.get_data_from_thumb()



        print(time.time()-start_time)


    except:
        print("error")
    finally:
        print("end")
