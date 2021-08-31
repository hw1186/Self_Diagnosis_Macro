from selenium import webdriver
from selenium.webdriver.support.ui import Select # 콤보 박스를 선택할수 있게 해주는 라이브러리
import schedule
import time
import telegram


def startScreen():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.get("https://hcs.eduro.go.kr/#/none")  # 자가진단 들어가기
    driver.find_element_by_id('btnConfirm2').click()  # 자가진단 로그인 시작!

def startDm():
    telgm_token = '1923774179:AAHEXsSgs5mDMqf8PVVNTn1kOb2S_SFX2Ng'
    bot = telegram.Bot(token=telgm_token)
    bot.sendMessage(chat_id='1931273588', text="자가진단 실행")


def inputBaseInfo():
    driver.find_element_by_id('schul_name_input').click()
    select = Select(driver.find_element_by_id('sidolabel'))  # 콤보 박스 선택
    select.select_by_index(1)
    select = Select(driver.find_element_by_id('crseScCode'))
    select.select_by_index(4)
    elem = driver.find_element_by_class_name("searchArea")
    elem.send_keys("세명컴퓨터고등학교")
    driver.find_element_by_class_name("searchBtn").click()
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
    driver.find_element_by_class_name("layerFullBtn").click()
    elem = driver.find_element_by_id("user_name_input")
    elem.send_keys("이현우")
    elem = driver.find_element_by_id("birthday_input")
    elem.send_keys("050306")
    driver.find_element_by_id("btnConfirm").click()
    time.sleep(1)


def inputPassword():
    driver.find_element_by_class_name("input_text_common").click()
    time.sleep(1)
    elements3_2 = driver.find_elements_by_class_name("transkey_div_3_2")
    elements3_3 = driver.find_elements_by_class_name("transkey_div_3_3")
    elements = elements3_2 + elements3_3
    realKeys = {}
    for element in elements:
        realKeys[str(element.get_attribute('aria-label'))] = element

    # 0306
    time.sleep(1)
    realKeys['0'].click()
    realKeys['3'].click()
    realKeys['0'].click()
    realKeys['6'].click()
    driver.find_element_by_id('btnConfirm').click()
    time.sleep(1)

def inputCheak():
    driver.find_element_by_class_name('btn').click()
    driver.find_element_by_id('survey_q1a1').click()
    driver.find_element_by_id('survey_q2a1').click()
    driver.find_element_by_id('survey_q3a1').click()
    driver.find_element_by_id('btnConfirm').click()

def sendDm():
    telgm_token = '1923774179:AAHEXsSgs5mDMqf8PVVNTn1kOb2S_SFX2Ng'
    bot = telegram.Bot(token=telgm_token)
    bot.sendMessage(chat_id='1931273588', text="자가진단 완료했다 학교가라")


def selfDiagnosisMacro():
    startDm()
    startScreen()
    inputBaseInfo()
    inputPassword()
    inputCheak()
    sendDm()


if __name__ == "__main__":
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--window-size=1920, 1080')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--user-agent-Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    driver = webdriver.Chrome('./chromedriver', options=option)
    driver.implicitly_wait(10)  # 로딩이 될때 까지 최소 10초 기다린다
    schedule.every().day.at("06:00").do(selfDiagnosisMacro)

    while True:
        schedule.run_pending()


        '''
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")
    # driver = webdriver.Chrome('chromedriver', chrome_options=options)'''


