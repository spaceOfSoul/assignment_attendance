import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton


class AppUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('id', self)
        label1.move(30,40)
        label2 = QLabel('pw', self)
        label2.move(30,60)
        label3 = QLabel('link', self)
        label3.move(30,100)
        
        self.ID = QLineEdit(self)
        self.ID.move(60, 40)
        
        self.PW = QLineEdit(self)
        self.PW.move(60, 60)

        self.qle = QLineEdit(self)
        self.qle.move(60, 100)
        
        btn = QPushButton(self)
        btn.setText('과제수행여부 저장')
        btn.move(60, 120)

        self.setWindowTitle('과제 출결')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        