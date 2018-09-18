from selenium import webdriver
from util.extractor import *
import pdb

if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    browser = webdriver.Chrome('chromedriver', chrome_options=options)
    try:
        # 일단 경복궁만



        url = "https://www.tripadvisor.co.kr/Attraction_Review-g294197-d324888-Reviews-Gyeongbokgung_Palace-Seoul.html"
        resDict =go_album(url,browser)

        for res in resDict:
            print(res)
            for r in resDict[res]:
                print(r)


    except:
        print("e")
    finally:
        browser.close()
    #
    #
#
#
#
#
#
#
