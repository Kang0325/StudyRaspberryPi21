# QT5 사용자 윈도우클래스 생성 예제
import sys
from PyQt5.QtWidgets import *

# declare Window Class
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)

#button = QPushButton('Click me')
#button.show()
#label = QLabel('Hello QT5')
#label.show()

win = MyWindow()
win.show()

app.exec_()