import schedule
from class_example import START_TIME
from class_example.self_diagnosis_macro import SelfDiagnosisMacro
from class_example.send_telegram import SendTelegram


def self_diagnosis_macro():
    macro = SelfDiagnosisMacro()
    dm = SendTelegram()

    dm.send_message('자가진단 실행')
    macro.start_macro()
    dm.send_message('자가진단 완료했다 학교가라')


if __name__ == "__main__":
    schedule.every().day.at(START_TIME).do(self_diagnosis_macro)
    while True:
        schedule.run_pending()
