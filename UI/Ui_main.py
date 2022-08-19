# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\python_tring\spider\weatherSpide RE by pyqt\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow:QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 674)
        self.centralwidget_main = QtWidgets.QWidget(MainWindow)
        self.centralwidget_main.setObjectName("centralwidget_main")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget_main)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_date = QtWidgets.QLabel(self.centralwidget_main)
        self.label_date.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label_date.setObjectName("label_date")
        self.verticalLayout_4.addWidget(self.label_date)
        self.label_NanYang = QtWidgets.QLabel(self.centralwidget_main)
        self.label_NanYang.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label_NanYang.setObjectName("label_NanYang")
        self.verticalLayout_4.addWidget(self.label_NanYang)
        self.label_low_tmp = QtWidgets.QLabel(self.centralwidget_main)
        self.label_low_tmp.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label_low_tmp.setObjectName("label_low_tmp")
        self.verticalLayout_4.addWidget(self.label_low_tmp)
        self.label_airs = QtWidgets.QLabel(self.centralwidget_main)
        self.label_airs.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label_airs.setObjectName("label_airs")
        self.verticalLayout_4.addWidget(self.label_airs)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.plainTextEdit_clothes = QtWidgets.QPlainTextEdit(self.centralwidget_main)
        self.plainTextEdit_clothes.setMaximumSize(QtCore.QSize(96, 36))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.plainTextEdit_clothes.setFont(font)
        self.plainTextEdit_clothes.setObjectName("plainTextEdit_clothes")
        self.verticalLayout_5.addWidget(self.plainTextEdit_clothes)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_weekday = QtWidgets.QLabel(self.centralwidget_main)
        self.label_weekday.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label_weekday.setTextFormat(QtCore.Qt.AutoText)
        self.label_weekday.setObjectName("label_weekday")
        self.verticalLayout.addWidget(self.label_weekday)
        self.label_weather = QtWidgets.QLabel(self.centralwidget_main)
        self.label_weather.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label_weather.setObjectName("label_weather")
        self.verticalLayout.addWidget(self.label_weather)
        self.label_heigh_tmp = QtWidgets.QLabel(self.centralwidget_main)
        self.label_heigh_tmp.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label_heigh_tmp.setObjectName("label_heigh_tmp")
        self.verticalLayout.addWidget(self.label_heigh_tmp)
        self.label_rays = QtWidgets.QLabel(self.centralwidget_main)
        self.label_rays.setStyleSheet("font: 14pt \"Agency FB\";")
        self.label_rays.setObjectName("label_rays")
        self.verticalLayout.addWidget(self.label_rays)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.plainTextEdit_remind = QtWidgets.QPlainTextEdit(self.centralwidget_main)
        self.plainTextEdit_remind.setEnabled(True)
        self.plainTextEdit_remind.setMinimumSize(QtCore.QSize(300, 0))
        self.plainTextEdit_remind.setMaximumSize(QtCore.QSize(10000, 36))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.plainTextEdit_remind.setFont(font)
        self.plainTextEdit_remind.setMouseTracking(False)
        self.plainTextEdit_remind.setTabletTracking(False)
        self.plainTextEdit_remind.setTabChangesFocus(False)
        self.plainTextEdit_remind.setUndoRedoEnabled(True)
        self.plainTextEdit_remind.setReadOnly(False)
        self.plainTextEdit_remind.setTabStopWidth(80)
        self.plainTextEdit_remind.setBackgroundVisible(False)
        self.plainTextEdit_remind.setObjectName("plainTextEdit_remind")
        self.verticalLayout_2.addWidget(self.plainTextEdit_remind)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_getdocument = QtWidgets.QPushButton(self.centralwidget_main)
        self.button_getdocument.setCheckable(False)
        self.button_getdocument.setObjectName("button_getdocument")
        self.horizontalLayout_3.addWidget(self.button_getdocument)
        self.line_3 = QtWidgets.QFrame(self.centralwidget_main)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_statue = QtWidgets.QLabel(self.centralwidget_main)
        self.label_statue.setObjectName("label_statue")
        self.horizontalLayout_2.addWidget(self.label_statue)
        self.label_state_did = QtWidgets.QLabel(self.centralwidget_main)
        self.label_state_did.setText("")
        self.label_state_did.setObjectName("label_state_did")
        self.horizontalLayout_2.addWidget(self.label_state_did)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget_main)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.citysWeatherLayout = QtWidgets.QHBoxLayout()
        self.citysWeatherLayout.setObjectName("citysWeatherLayout")
        self.tableWidget_citysWeather = QtWidgets.QTableWidget(self.centralwidget_main)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget_citysWeather.setFont(font)
        self.tableWidget_citysWeather.setShowGrid(True)
        self.tableWidget_citysWeather.setObjectName("tableWidget_citysWeather")
        self.tableWidget_citysWeather.setColumnCount(0)
        self.tableWidget_citysWeather.setRowCount(0)
        self.tableWidget_citysWeather.horizontalHeader().setVisible(False)
        self.tableWidget_citysWeather.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_citysWeather.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_citysWeather.verticalHeader().setVisible(False)
        self.citysWeatherLayout.addWidget(self.tableWidget_citysWeather)
        self.verticalLayout_6.addLayout(self.citysWeatherLayout)
        MainWindow.setCentralWidget(self.centralwidget_main)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 531, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.saveSite_action = QtWidgets.QAction(MainWindow)
        self.saveSite_action.setObjectName("saveSite_action")
        self.lookingFiles_action = QtWidgets.QAction(MainWindow)
        self.lookingFiles_action.setObjectName("lookingFiles_action")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.menu.addAction(self.saveSite_action)
        self.menu.addAction(self.lookingFiles_action)
        self.menu.addSeparator()
        self.menu.addAction(self.about)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "天气预报"))
        self.label_date.setText(_translate("MainWindow", "公历"))
        self.label_NanYang.setText(_translate("MainWindow", "南阳市"))
        self.label_low_tmp.setText(_translate("MainWindow", "最低温度"))
        self.label_airs.setText(_translate("MainWindow", "空气质量"))
        self.plainTextEdit_clothes.setPlainText(_translate("MainWindow", "穿衣指数"))
        self.label_weekday.setText(_translate("MainWindow", "星期"))
        self.label_weather.setText(_translate("MainWindow", "天气"))
        self.label_heigh_tmp.setText(_translate("MainWindow", "最高温度"))
        self.label_rays.setText(_translate("MainWindow", "紫外线强度"))
        self.plainTextEdit_remind.setPlainText(_translate("MainWindow", "请输入温馨提醒"))
        self.button_getdocument.setText(_translate("MainWindow", "获取稿件"))
        self.label_statue.setText(_translate("MainWindow", "状态"))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.saveSite_action.setText(_translate("MainWindow", "选择保存位置"))
        self.lookingFiles_action.setText(_translate("MainWindow", "查看文件归档"))
        self.about.setText(_translate("MainWindow", "关于"))