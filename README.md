# 트립 어드바이저 이미지 크롤러

* selenium을 사용 해야함.
  1. 각각의 키워드 검색 ,  앨범에 들어감
  2. 그 앨범 클릭 후 상세 보기 에서 아래 썸네일 리스트에 모든 정보들이 담겨있음 (한번에 48개씩 / tinyThumb이라는 클래스로)
  3. 크롤링 후 섬네일 리스트의 맨 끝 번호를 찾아서 다시 그 번호를 통해 상세보기 접근 
  4. 그러면 그 뒷 썸네일 새로운 48개 보임 그거 또 크롤링 
  5. 반복
     - 상세보기로 바로 url접근 하면 가끔 안되어서 홈으로 한번 이동 후 가는거로 하기도 함



## 서버에 chrome-driver 설치해야함.


### Versions
```bash
CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`
SELENIUM_STANDALONE_VERSION=3.4.0
SELENIUM_SUBDIR=$(echo "$SELENIUM_STANDALONE_VERSION" | cut -d"." -f-2)
```
##### Remove existing downloads and binaries so we can start from scratch. 
```bash
sudo apt-get remove google-chrome-stable
rm ~/selenium-server-standalone-*.jar
rm ~/chromedriver_linux64.zip
sudo rm /usr/local/bin/chromedriver
sudo rm /usr/local/bin/selenium-server-standalone.jar
```
#### Install dependencies.
```bash
sudo apt-get update
sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4
```
### Install Chrome.
```bash
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
```
### Install ChromeDriver.

```bash
wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver
```
### Install Selenium.
```bash
wget -N http://selenium-release.storage.googleapis.com/$SELENIUM_SUBDIR/selenium-server-standalone-$SELENIUM_STANDALONE_VERSION.jar -P ~/
sudo mv -f ~/selenium-server-standalone-$SELENIUM_STANDALONE_VERSION.jar /usr/local/bin/selenium-server-standalone.jar
sudo chown root:root /usr/local/bin/selenium-server-standalone.jar
sudo chmod 0755 /usr/local/bin/selenium-server-standalone.jar

```

 https://developers.supportbee.com/blog/setting-up-cucumber-to-run-with-Chrome-on-Linux/
 https://gist.github.com/curtismcmullan/7be1a8c1c841a9d8db2c
 http://stackoverflow.com/questions/10792403/how-do-i-get-chrome-working-with-selenium-using-php-webdriver
 http://stackoverflow.com/questions/26133486/how-to-specify-binary-path-for-remote-chromedriver-in-codeception
 http://stackoverflow.com/questions/40262682/how-to-run-selenium-3-x-with-chrome-driver-through-terminal
 http://askubuntu.com/questions/760085/how-do-you-install-google-chrome-on-ubuntu-16-04





