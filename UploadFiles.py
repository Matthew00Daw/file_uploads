# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UploadFiles.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UploadFiles(object):
    def setupUi(self, UploadFiles):
        UploadFiles.setObjectName("UploadFiles")
        UploadFiles.resize(540, 360)
        self.centralwidget = QtWidgets.QWidget(UploadFiles)
        self.centralwidget.setObjectName("centralwidget")
        self.FindFolderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.FindFolderBtn.setGeometry(QtCore.QRect(20, 60, 161, 30))
        self.FindFolderBtn.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 255, 127);")
        self.FindFolderBtn.setObjectName("FindFolderBtn")
        self.CreateGoogleFolder = QtWidgets.QPushButton(self.centralwidget)
        self.CreateGoogleFolder.setGeometry(QtCore.QRect(20, 110, 161, 30))
        self.CreateGoogleFolder.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 255, 127);")
        self.CreateGoogleFolder.setObjectName("CreateGoogleFolder")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(220, 10, 310, 310))
        self.listWidget.setObjectName("listWidget")
        self.AuthorizationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AuthorizationBtn.setGeometry(QtCore.QRect(20, 10, 161, 30))
        self.AuthorizationBtn.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 255, 127);")
        self.AuthorizationBtn.setObjectName("AuthorizationBtn")
        self.UploadFilesBtn = QtWidgets.QPushButton(self.centralwidget)
        self.UploadFilesBtn.setGeometry(QtCore.QRect(20, 160, 161, 30))
        self.UploadFilesBtn.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 255, 127);")
        self.UploadFilesBtn.setObjectName("UploadFilesBtn")
        self.getYears = QtWidgets.QSpinBox(self.centralwidget)
        self.getYears.setGeometry(QtCore.QRect(20, 220, 42, 22))
        self.getYears.setObjectName("getYears")
        self.getMonth = QtWidgets.QSpinBox(self.centralwidget)
        self.getMonth.setGeometry(QtCore.QRect(80, 220, 42, 22))
        self.getMonth.setMaximum(12)
        self.getMonth.setObjectName("getMonth")
        self.getDays = QtWidgets.QSpinBox(self.centralwidget)
        self.getDays.setGeometry(QtCore.QRect(140, 220, 42, 22))
        self.getDays.setMaximum(31)
        self.getDays.setObjectName("getDays")
        self.GetTimer = QtWidgets.QPushButton(self.centralwidget)
        self.GetTimer.setGeometry(QtCore.QRect(20, 260, 161, 30))
        self.GetTimer.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 255, 127);")
        self.GetTimer.setObjectName("GetTimer")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 186, 181, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 300, 181, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 200, 31, 16))
        self.label_3.setObjectName("label_3")
        UploadFiles.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UploadFiles)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        UploadFiles.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UploadFiles)
        self.statusbar.setObjectName("statusbar")
        UploadFiles.setStatusBar(self.statusbar)

        self.retranslateUi(UploadFiles)
        QtCore.QMetaObject.connectSlotsByName(UploadFiles)

    def retranslateUi(self, UploadFiles):
        _translate = QtCore.QCoreApplication.translate
        UploadFiles.setWindowTitle(_translate("UploadFiles", "Программа"))
        self.FindFolderBtn.setText(_translate("UploadFiles", "Найти папки"))
        self.CreateGoogleFolder.setText(_translate("UploadFiles", "Создать папки в облаке"))
        self.AuthorizationBtn.setText(_translate("UploadFiles", "Авторизоваться"))
        self.UploadFilesBtn.setText(_translate("UploadFiles", "Выгрузить файлы"))
        self.GetTimer.setText(_translate("UploadFiles", "Задать таймер обновления "))
        self.label.setText(_translate("UploadFiles", "Год"))
        self.label_2.setText(_translate("UploadFiles", "Месяц"))
        self.label_3.setText(_translate("UploadFiles", "День"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UploadFiles = QtWidgets.QMainWindow()
    ui = Ui_UploadFiles()
    ui.setupUi(UploadFiles)
    UploadFiles.show()
    sys.exit(app.exec_())