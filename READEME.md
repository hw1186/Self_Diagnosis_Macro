    <자가진단 메크로>

- 프로그램 기능 

먼저 이 프로그램을 실행시킬려면 자가진단에 로그인이 돼 있어야 한다

1. 로그인 상태의 자가진단의 보안 비밀번호를 자동으로 입력한다

2. 모든 설문조사를 아니요를 해서 제출한다

3. 자가진단 종료

- 프로그램의 사용될 기능

1. 웹 크롤링 - 메크로

2. 가상환경 (Selenium, venv) - 메크로를 실행할 공간

3. BeautifulSoup - aria_label 의 지정된 값을 넘겨줄때 사용

4. from selenium.webdriver.support.ui import Select - 콤보 박스를 쓰게 되는 상황이 나오는데 콤보 박스를 선택할수 있게 해주는 라이브러리

5. schedule - 주기별로 실행

(미정) 오토 핫 키 - (최악의 경우) 이미지를 인식하고 위치를 찾아 로그인할수 있게하는 기능 


< 완성 코드 요약 >

1. def startScreen():

자가진단 메인 화면 들어간다
자가잔단 시작을 클릭

2. def inputBaseInfo():

학교선택은 콤보박스로 설정 돼 있다 

from selenium.webdriver.support.ui import Select

콤보 박스 선택을 위한 라이브러리
콤보 박스에 첫번째 위치에 있는 서울시를 클릭
두번째 콤보박스는 4번째에 있는 고등학교 클릭

학교 생년월일 입력

3. inputPassword():

비밀번호를 입력하기 위해선 먼저 숫자들의 Area-label 을 입력받아야 한다

먼저 element 값을 입력한다 

key 의 값을 입력할수 있는 딕셔너리를 하나 만든다

모든 for 을 이용해 element 안에 있는 area-label 값을 입력 받는다

key 안에 있는 비밀번호를 꺼내 입력한다

4. def inputcheak():

모든 요소를 아니요를 누른 다음 제출을 한다



