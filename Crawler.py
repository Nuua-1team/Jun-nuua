# -*- coding: utf-8 -*-
from selenium import webdriver
from util.extractor import *
import pdb
import time

if __name__ == "__main__":
    try:
        start_time = time.time()

        browser = CrawlBrowser()
        # 일단 경복궁만

        browser.go_album()
        resDict = browser.get_data_from_thumb()
        for i in range(1):
            # 확인용 프린트
            #대충 여기서 넣고 디비에 넣고
            # print(resDict["media_id"])
            browser.go_next()
            resDict = browser.get_data_from_thumb()
            print(resDict)
        print(time.time()-start_time)


    except:
        print("error")
    finally:
        print("end")
