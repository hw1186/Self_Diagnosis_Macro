from selenium import webdriver
from selenium.webdriver.support.ui import Select  # 콤보 박스를 선택할수 있게 해주는 라이브러리
import time
from class_example import CONNECT_URL, MY_SCHOOL, MY_NAME, MY_BIRTH, MY_PASSWORD


class SelfDiagnosisMacro: # 자가진단 클래스 생성
    def __init__(self): # driver 초기화
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--window-size=1920, 1080')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--user-agent-Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 ' 
                            '(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        self.driver = webdriver.Chrome('../chromedriver', options=option)
        self.driver.implicitly_wait(10)  # 로딩이 될때 까지 최소 10초 기다린다

    def start_macro(self):
        self.connect_url()
        self.input_base_info()
        self.input_password()
        self.input_cheak()

    def connect_url(self):
        self.driver.get(CONNECT_URL)    # 자가진단 들어가기
        self.driver.find_element_by_id('btnConfirm2').click()  # 자가진단 로그인 시작!

    def input_base_info(self):
        self.driver.find_element_by_id('schul_name_input').click()
        select = Select(self.driver.find_element_by_id('sidolabel'))  # 콤보 박스 선택
        select.select_by_index(1)
        select = Select(self.driver.find_element_by_id('crseScCode'))
        select.select_by_index(4)
        elem = self.driver.find_element_by_class_name("searchArea")
        elem.send_keys(MY_SCHOOL)
        self.driver.find_element_by_class_name("searchBtn").click()
        self.driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
        self.driver.find_element_by_class_name("layerFullBtn").click()
        elem = self.driver.find_element_by_id("user_name_input")
        elem.send_keys(MY_NAME)
        elem = self.driver.find_element_by_id("birthday_input")
        elem.send_keys(MY_BIRTH)
        self.driver.find_element_by_id("btnConfirm").click()
        time.sleep(1)

    def input_password(self):
        self.driver.find_element_by_class_name("input_text_common").click()
        time.sleep(1)
        elements3_2 = self.driver.find_elements_by_class_name("transkey_div_3_2")
        elements3_3 = self.driver.find_elements_by_class_name("transkey_div_3_3")
        elements = elements3_2 + elements3_3
        realKeys = {}
        for element in elements:
            realKeys[str(element.get_attribute('aria-label'))] = element
        time.sleep(1)
        realKeys[MY_PASSWORD[0]].click() # 저 비번에서 0번쨰 1 번쨰
        realKeys[MY_PASSWORD[1]].click()
        realKeys[MY_PASSWORD[2]].click()
        realKeys[MY_PASSWORD[3]].click()
        self.driver.find_element_by_id('btnConfirm').click()
        time.sleep(1)

    def input_cheak(self):
        self.driver.find_element_by_class_name('btn').click()
        self.driver.find_element_by_id('survey_q1a1').click()
        self.driver.find_element_by_id('survey_q2a1').click()
        self.driver.find_element_by_id('survey_q3a1').click()
        self.driver.find_element_by_id('btnConfirm').click()