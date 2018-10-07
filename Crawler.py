# -*- coding: utf-8 -*-
from selenium import webdriver
from util.extractor import *
import pdb
import time


if __name__ == "__main__":
    try:
        start_time = time.time()

        print("[0:경복궁, 1:창덕궁, 2:광화문, 3:덕수궁, 4:종묘, 5:숭례문, 6:동대문 (흥인지문), 7:경희궁, 8:보신각]")
        browser = CrawlBrowser(int(input()))
        browser.go_album()


        while(True):
            browser.go_next()
            browser.get_data_from_thumb()


        print(time.time()-start_time)


    except:
        print("error")
    finally:

        print("end")
