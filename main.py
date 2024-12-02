import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.find)

    def find(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        res = cursor.execute(f'SELECT * FROM Coffee WHERE name like "{self.lineEdit.text()}"').fetchone()
        print(res)
        if res != None:
            self.lineEdit_2.setText(f'{res[0]}')
            self.lineEdit_3.setText(f'{res[1]}')
            self.lineEdit_4.setText(f'{res[2]}')
            self.lineEdit_5.setText(f'{res[4]}')
            self.lineEdit_6.setText(f'{res[5]}')
            self.lineEdit_7.setText(f'{res[6]}')
            self.lineEdit_8.setText(f'{res[7]}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
