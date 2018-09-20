# -*- coding: utf-8 -*- 
from selenium import webdriver
from util.extractor import *
import pdb

if __name__ == "__main__":
    try:
        browser = CrawlBrowser()
        # 일단 경복궁만
        url = "https://www.tripadvisor.co.kr/Attraction_Review-g294197-d324888-Reviews-Gyeongbokgung_Palace-Seoul.html"
        browser.go_album(url)
        resDict = browser.get_data_from_thumb()
        for i in range(10):
            # 확인용 프린트
            #대충 여기서 넣고 디비에 넣고
            # print(resDict["media_id"])
            browser.go_next()
            resDict = browser.get_data_from_thumb()


    except:
        print("error")
    finally:
        browser.close()
