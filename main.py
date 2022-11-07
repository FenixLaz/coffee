import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        for elem in result:
            pass
        self.label_8.setText(str(elem[0]))
        self.label_9.setText(str(elem[1]))
        self.label_10.setText(str(elem[2]))
        self.label_11.setText(str(elem[3]))
        self.label_12.setText(str(elem[4]))
        self.label_13.setText(str(elem[5]))
        self.label_14.setText(str(elem[6]))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())