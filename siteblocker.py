

from PyQt5 import QtCore, QtGui, QtWidgets
import time
from datetime import datetime as dt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color:black;")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(250, 320, 351, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 280, 361, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(310, 400, 241, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n" "background-color:white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(300,50,800,200))
        self.mainImage = QtGui.QPixmap('images.png')
        self.imageLabel.setPixmap(self.mainImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ENTER THE SITE TO BE BLOCKED...."))
        self.pushButton.setText(_translate("MainWindow", "BLOCK!"))
        self.menuMenu.setTitle(_translate("MainWindow", "menu"))
        self.actionExit.setText(_translate("MainWindow", "exit"))
        
        self.pushButton.clicked.connect(self.block_func)
        self.actionExit.triggered.connect(self.exit)
        
    def block_func(self):
        hosts_path = "C:\Windows\System32\drivers\etc\hosts"
        hosts_temp = "hosts"
        redirect = "127.0.0.1"
        text = self.textEdit.toPlainText()
        website_list = text
        
        while True:
            if dt(dt.now().year,dt.now().month,dt.now().day,16) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
                print("Working hours...")
                with open(hosts_path,'r+') as file:
                    content=file.read()
                    for website in website_list:
                        if website in content:
                            pass
                        else:
                            file.write(redirect+" "+ website+"\n")
            else:
                with open(hosts_path,'r+') as file:
                    content=file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                    file.truncate()
                print("Fun hours...")
            time.sleep(5)




    
        
    def exit(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

