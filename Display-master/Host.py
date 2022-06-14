import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import time


f = open('PWD.txt', 'r', encoding='utf-8')
form_thirdwindow = uic.loadUiType("Host.ui")[0]
door_password = f.readline()
password =""


class Host(QDialog,QWidget,form_thirdwindow):
    def __init__(self):
        super(Host,self).__init__()
        self.initUI()
        self.show()


    def initUI(self):
        self.setupUi(self)


        #버튼에 대한 정의
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.cancel.setText(_translate("MainWindow", "취소"))
        self.confirm.setText(_translate("MainWindow", "확인"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.textlabel.setText(_translate("MainWindow", "Host"))
        self.btnBack2.setText(_translate("MainWindow", "Back"))
        
        # 버튼 액션 추가
        self.btn1.clicked.connect(self.action1)
        self.btn2.clicked.connect(self.action2)
        self.btn3.clicked.connect(self.action3)
        self.btn4.clicked.connect(self.action4)
        self.btn5.clicked.connect(self.action5)
        self.btn6.clicked.connect(self.action6)
        self.btn7.clicked.connect(self.action7)
        self.btn8.clicked.connect(self.action8)
        self.btn9.clicked.connect(self.action9)
        self.btn0.clicked.connect(self.action0)
        self.cancel.clicked.connect(self.action_cancel)
        self.confirm.clicked.connect(self.action_confirm)
        self.btnBack2.clicked.connect(self.back_to_main)

    #각 버튼들에 대한 정의
    def action0(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "0")

    def action1(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "1")

    def action2(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "2")

    def action3(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "3")

    def action4(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "4")

    def action5(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "5")

    def action6(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "6")

    def action7(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "7")

    def action8(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "8")

    def action9(self):
        # appending label text
        text = self.MainWindow_2.text()
        self.MainWindow_2.setText(text + "9")

    def action_cancel(self):
        # clearing the label text
        self.MainWindow_2.setText("")
        
    def back_to_main(self):
        self.close()
    
    def action_confirm(self):
        password = self.MainWindow_2.text()
        print("password : " + password)        
        print("door_PWD: " + door_password)
        if door_password == password: # if password 5 and matched suc activate
            print("Success")
            GPIO.setmode(GPIO.BCM)
            
            GPIO.setwarnings(False)
            GPIO.setup(17, GPIO.OUT)

            print("Open")
            GPIO.output(17, GPIO.LOW)
            time.sleep(1)

            GPIO.output(17, GPIO.HIGH)
            time.sleep(7)

            print("close")
            GPIO.output(17, GPIO.LOW)
            time.sleep(1)

            GPIO.output(17, GPIO.HIGH)
            time.sleep(7)
            GPIO.cleanup
            
            password = ""
            self.MainWindow_2.setText("")
            
        elif door_password != password: # if password is not matched fail activate
            print("Fail")
            password =""
            self.MainWindow_2.setText("")
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Host()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
