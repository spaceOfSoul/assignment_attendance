from PyQt5.QtWidgets import QApplication
import sys

import crawling
from UI import AppUI

def save_excel(app_ui):
    id = app_ui.ID.text()
    pw = app_ui.PW.text()
    link = app_ui.qle.text()

    print(f"ID: {id}, PW: {pw}, Link: {link}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppUI()
    ex.btn.clicked.connect()  # 클래스 외부에서 콜백 함수 연결
    sys.exit(app.exec_())