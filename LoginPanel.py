# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girişPaneliYeni.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 373)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow\n"
"{\n"
"background-image:url(C:/Users/cansa_wk0xmvi/Desktop/PythonProjelerim/depofoto.jpg);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 301, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 50, 271, 261))
        self.label.setStyleSheet("background-color: rgb(39, 37, 33);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.grsBtn = QtWidgets.QPushButton(self.frame)
        self.grsBtn.setGeometry(QtCore.QRect(50, 210, 211, 41))
        self.grsBtn.setStyleSheet("background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.grsBtn.setObjectName("grsBtn")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 20, 101, 91))
        self.pushButton_2.setStyleSheet("border-radius:60px;\n"
"background-color:white;\n"
"background-image:url(C:/Users/cansa_wk0xmvi/Desktop/PythonProjelerim/kfotopng.png);")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("kprofil.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(110, 110))
        self.pushButton_2.setAutoRepeatDelay(100)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textbox1 = QtWidgets.QLineEdit(self.frame)
        self.textbox1.setGeometry(QtCore.QRect(60, 140, 201, 20))
        self.textbox1.setStyleSheet("background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid#717072;\n"
"font-family:century gothic;")
        self.textbox1.setInputMask("")
        self.textbox1.setDragEnabled(False)
        self.textbox1.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.textbox1.setClearButtonEnabled(True)
        self.textbox1.setObjectName("textbox1")
        self.textbox2 = QtWidgets.QLineEdit(self.frame)
        self.textbox2.setGeometry(QtCore.QRect(60, 180, 201, 20))
        self.textbox2.setStyleSheet("background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid#717072;\n"
"font-family:century gothic;")
        self.textbox2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textbox2.setReadOnly(False)
        self.textbox2.setClearButtonEnabled(True)
        self.textbox2.setObjectName("textbox2")
        self.kytBtn = QtWidgets.QPushButton(self.frame)
        self.kytBtn.setGeometry(QtCore.QRect(50, 260, 211, 41))
        self.kytBtn.setStyleSheet("background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.kytBtn.setObjectName("kytBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grsBtn.setText(_translate("MainWindow", "GİRİŞ"))
        self.textbox1.setText(_translate("MainWindow", "Kullancı Adı"))
        self.textbox2.setText(_translate("MainWindow", "Şifre"))
        self.kytBtn.setText(_translate("MainWindow", "KAYIT OL"))
