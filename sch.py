from selenium import webdriver
import schedule
import time
import telegram

def startScreen():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get("http://www.goyang.go.kr/www/index.do")

def start():
    startScreen()



if __name__ == "__main__":
    option = webdriver.ChromeOptions()