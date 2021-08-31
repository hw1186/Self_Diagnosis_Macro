from selenium import webdriver
from selenium.webdriver.support.ui import Select  # 콤보 박스를 선택할수 있게 해주는 라이브러리
import time
import telegram


class SelfDiagnosisMacro: # 자가진단 클래스 생성

    def __init__(self): # driver 초기화
        self.driver = webdriver.Chrome('./chromedriver') # 크롬 드라이버 초기화
        self.driver.implicitly_wait(10)


    def startScreen(self): # 자가진단 홈페이지 함수
        self.driver.get("https://hcs.eduro.go.kr/#/none")  # 자가진단 들어가기
        self.driver.find_element_by_id('btnConfirm2').click()  # 자가진단 로그인 시작!

    def inputBaseInfo(self): # 정보선택
        self.driver.find_element_by_id('schul_name_input').click()
        select = Select(self.driver.find_element_by_id('sidolabel'))  # 콤보 박스 선택
        select.select_by_index(1) # 첫번째 인덱스 선텍
        select = Select(self.driver.find_element_by_id('crseScCode'))
        select.select_by_index(4) # 네번째 인덱그 선택
        elem = self.driver.find_element_by_class_name("searchArea")
        elem.send_keys("세명컴퓨터고등학교") # elem 안에 있는 항목에 세명컴퓨터고등학교 입룍
        self.driver.find_element_by_class_name("searchBtn").click()
        self.driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
        self.driver.find_element_by_class_name("layerFullBtn").click()
        elem = self.driver.find_element_by_id("user_name_input")
        elem.send_keys("이현우") # 이현우 입력
        elem = self.driver.find_element_by_id("birthday_input")
        elem.send_keys("050306") # 050306 입력
        self.driver.find_element_by_id("btnConfirm").click()
        time.sleep(1) # 1초 쉬어라

    def inputPassword(self): # 페스워드 입력
        self.driver.find_element_by_class_name("input_text_common").click()
        time.sleep(1)
        elements3_2 = self.driver.find_elements_by_class_name("transkey_div_3_2") # 3_2 키를 모두 담는다
        elements3_3 = self.driver.find_elements_by_class_name("transkey_div_3_3") # 3_3 키를 모두 담는다
        elements = elements3_2 + elements3_3 # 전체 키
        realKeys = {} # 담을 aria-label 값
        for element in elements:
            realKeys[str(element.get_attribute('aria-label'))] = element

        # 0306
        time.sleep(1)
        realKeys['0'].click()
        realKeys['3'].click()
        realKeys['0'].click()
        realKeys['6'].click()
        self.driver.find_element_by_id('btnConfirm').click()
        time.sleep(1)

    def inputCheak(self):
        self.driver.find_element_by_class_name('btn').click()
        self.driver.find_element_by_id('survey_q1a1').click()
        self.driver.find_element_by_id('survey_q2a1').click()
        self.driver.find_element_by_id('survey_q3a1').click()
        self.driver.find_element_by_id('btnConfirm').click()

    def sendDm(self):
        telgm_token = '1923774179:AAHEXsSgs5mDMqf8PVVNTn1kOb2S_SFX2Ng'
        bot = telegram.Bot(token=telgm_token)
        bot.sendMessage(chat_id='1931273588', text="자가진단 완료했다 학교가라")

    def startMacro(self):
        self.startScreen()
        self.inputBaseInfo()
        self.inputPassword()
        self.inputCheak()
        self.sendDm()


