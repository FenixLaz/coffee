import sys
import sqlite3
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
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
        self.pushButton.clicked.connect(self.update)
        con.close()

    def update(self):
        ex2.show()

class Upgrade_Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.pushButton_2.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton.clicked.connect(self.save_results)
        self.pushButton_4.clicked.connect(self.append)
        self.modified = {}
        self.titles = None

    def update_result(self):
        try:
            self.con = sqlite3.connect("coffee.sqlite")
            cur = self.con.cursor()
            result = cur.execute("SELECT * FROM coffee WHERE id=?",
                                (item_id := self.lineEdit.text(), )).fetchall()
            self.tableWidget.setRowCount(len(result))
            if not result:
                self.statusBar().showMessage('Ничего не нашлось')
                return
            else:
                self.statusBar().showMessage(f"Нашлась запись с id = {item_id}")
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.modified = {}
            self.con.close() 
        except Exception:
            print('Error')
    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            self.con = sqlite3.connect("coffee.sqlite")
            cur = self.con.cursor()
            que = "UPDATE coffee SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                            for key in self.modified.keys()])
            que += "WHERE id = ?"
            cur.execute(que, (self.lineEdit.text(),))
            self.con.commit()
            self.modified.clear()
            self.con.close() 

    def append(self):
        self.con = sqlite3.connect("coffee.sqlite")
        stepen = self.comboBox_2.currentText()
        moloty = self.comboBox.currentText()
        name = self.lineEdit_4.text()
        about = self.lineEdit_7.text()
        price = self.lineEdit_8.text() 
        volume = self.lineEdit_9.text()
        cur = self.con.cursor()
        cur.execute("""INSERT INTO coffee(name_sort, degree, ground_or_grains, taste_description, price, packing_volume) VALUES(?, ?, ?, ?, ?, ?) 
                                            """, (name, stepen, moloty, about, price, volume)).fetchall()    
        self.statusBar().showMessage(f"Запись с параметрами\nНазвание сорта: {name}, Степень обжарки: {stepen}, Молотый/в зернах: {moloty}, Информация о вкусе: {about}, Цена: {price}, Объём: {volume}")                                                                            
        self.con.commit()
        self.con.close()  

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex2 = Upgrade_Coffee()
    sys.exit(app.exec_())