import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtWidgets, uic, QtCore
from menu_ui import MenuWindow1

from main_ui import Ui_Form
from db_conn import ConnectDatabase


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.log_App = login_UI()
        self.log_App.show()
class login_UI(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("login.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Create an instance of ConnectDatabase
        self.connectDatabase = ConnectDatabase()
        self.connectDatabase.connect_db()

        self.setWindowOpacity(0.98)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.toolButton.clicked.connect(lambda: self.login_def())
        self.toolButton_2.clicked.connect(lambda: self.register_def())
        self.toolButton2.clicked.connect(lambda: self.background.setCurrentIndex(1))
        self.toolButton_3.clicked.connect(lambda: self.background.setCurrentIndex(0))



    def login_def(self):
        try:
            username = self.lineEdit.text()
            password = self.lineEdit2.text()

            mycursor = self.connectDatabase.cursor
            mycursor.execute("SELECT * FROM login WHERE Username=%s AND Password=%s", (username, password))
            result = mycursor.fetchone()
            if result:
                self.close()
                self.window = MenuWindow1()
                self.window.show()
            else:
                print("Incorrect Information")
        except Exception as e:
            print("An error occurred:", e)

    def register_def(self):
        try:
            username = self.lineEdit_2.text()
            email = self.lineEdit_3.text()
            password = self.lineEdit_4.text()

            mycursor = self.connectDatabase.cursor
            mycursor.execute("SELECT * FROM login WHERE Username=%s OR Email=%s", (username, email))
            result = mycursor.fetchone()

            if result:
                print("User already exists")
            else:
                # Insert new user
                sql = "INSERT INTO login (Username, Email, Password) VALUES (%s, %s, %s)"
                val = (username, email, password)
                mycursor.execute(sql, val)
                self.connectDatabase.con.commit()
                print("User registered successfully")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())