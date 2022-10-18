import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.Ui_main import Ui_MainWindow
from spider.weather_main import Weathers
import pickle
from appTools import Signal
import time
wea = Weathers()
sig = Signal()


class AppConfig():
    def __init__(self):
        self.savePath = r'D:\天气预报'

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()


        # app_window = QtWidgets.QMainWindow()
        self.setupUi(self)
        self.setWindowTitle('生成天气预报')
        icon = QtGui.QIcon()
        ico_path = ico_path = os.path.join(
            os.path.dirname(__file__), 'logo.png')
        icon.addPixmap(QtGui.QPixmap(ico_path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.label_statue.setText('初始化')
        self.config = AppConfig()
        if os.path.exists('config') == False:
            os.mkdir('config')
        if os.path.exists('config/user.pickl'):
            self.loadConfig()
        self.startThread()

        self.plainTextEdit_remind.textChanged.connect(self.setRemind)
        self.plainTextEdit_clothes.textChanged.connect(self.setClothes)
        self.button_getdocument.clicked.connect(self.getDocument)
        self.saveSite_action.triggered.connect(self.selectSavePath)
        self.lookingFiles_action.triggered.connect(self.lookingFiles)

    def loadConfig(self):
        with open('config/user.pickl', 'rb') as config_file:
            self.config = pickle.load(config_file)

    def startThread(self):  # 启动多线程
        def doThread(_):
            self.get_data()
            self.get_weather()
            self.getPBarState()
            self.getPBarStateDid()
        self.thread = RunthreadStart()  # 利用一个子线程去激活其他子线程
        self.thread.isStart.connect(doThread)
        self.thread.start()

    def get_weather(self):  # 获取天气信息
        def setWeatherMsg(wea: Weathers):  # 将天气信息设置到窗口
            self.label_heigh_tmp.setText('最高温度'+wea.temHigh)
            self.label_low_tmp.setText('最低温度'+wea.temLow)
            self.label_weather.setText(wea.wea)
            self.label_airs.setText('空气质量'+wea.airs)
            self.label_rays.setText('紫外线强度'+wea.rays)
            self.tableWidget_citysWeather.setColumnCount(8)
            self.tableWidget_citysWeather.setRowCount(9)
            for row, rowStr in enumerate(wea.weatherList.split('\n')):
                for col, colStr in enumerate(rowStr.split()):
                    self.tableWidget_citysWeather.setItem(
                        row, col, QtWidgets.QTableWidgetItem(colStr))
            self.app_progressBar(self.progressBar.value()+20)
            sig.setWeatherMsgIsDid = True
        self.t1 = RunthreadGetWeather()  # 创建一个线程，在子线程中执行获取天气信息的操作
        self.t1.proBar_single.connect(setWeatherMsg)  # 子线程运行结束
        sig.setWeatherMsgIsDo = True
        self.label_statue.setText('正在获取各地区天气情况')
        self.t1.start()
        # self.label_low_tmp.setText(self.label_low_tmp.text()+self.wea.temLow)

    def get_data(self):
        def setDataMsg(wea: Weathers):
            self.label_weekday.setText('星期'+wea.weekday)
            self.label_date.setText(f'{wea.month}月{wea.day}日')
            self.app_progressBar(self.progressBar.value()+30)
            sig.setDataMsgIsDid = True
        self.t2 = RunthreadGetData()
        self.t2.proBar_single.connect(setDataMsg)
        sig.setDataMsgIsDo = True
        self.label_statue.setText('正在获取日期')
        self.t2.start()

    def getPBarState(self):
        def updatePBar(state: str):
            self.label_statue.setText(state)
        self.t3 = RunthreadShowPBarState()
        self.t3.loadingState.connect(updatePBar)
        self.t3.start()

    def getPBarStateDid(self):
        def updatePBar(state: str):
            self.label_state_did.setText(state)
        self.threadPbarDid = RunthreadShowPBarStateDid()
        self.threadPbarDid.loadingState.connect(updatePBar)
        self.threadPbarDid.start()

    def setRemind(self):
        self.label_statue.setText('温馨提示已修改')
        wea.remind = self.plainTextEdit_remind.toPlainText()
        if sig.setRemindIsNotDid:
            self.app_progressBar(self.progressBar.value()+25)
            sig.setRemindIsNotDid = False
        if self.progressBar.value() == 100:
            self.label_statue.setText('就绪')

    def setClothes(self):
        self.label_statue.setText('穿衣指数已修改')
        wea.clothes = self.plainTextEdit_clothes.toPlainText()
        if sig.setClothesIsNotDid:
            self.app_progressBar(self.progressBar.value()+25)
            sig.setClothesIsNotDid = False
        if self.progressBar.value() == 100:
            self.label_statue.setText('就绪')

    def app_progressBar(self, per: int):  # 修改进度条
        self.progressBar.setProperty("value", per)

    def getDocument(self):
        wea.doc_path = self.config.savePath
        if self.progressBar.value() == 100:
            self.threadGetDoc()
        elif self.progressBar.value() >= 50 and sig.setWeatherMsgIsDid and sig.setDataMsgIsDid:
            msg_box = QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Warning, '警告', '尚未填写穿衣指数或温馨提示')
            msg_box.exec_()
            self.threadGetDoc()
        else:
            msg_box = QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Warning, '警告', '请等待初始化完成')
            msg_box.exec_()

    def selectSavePath(self):
        try:
            self.config.savePath = QtWidgets.QFileDialog.getExistingDirectory(
                None, "选取文件夹", self.config.savePath)
            with open('config/user.pickl', 'wb') as f:
                pickle.dump(obj=self.config, file=f)
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "错误", f"出现未知错误{e}")

    def lookingFiles(self):
        os.startfile(self.config.savePath)

    def threadGetDoc(self):
        def getDoc(_):
            wea.get_docx()
        self.tGetDoc = RunthreadGetDocument()
        self.tGetDoc.getDoc.connect(getDoc)
        self.tGetDoc.start()


# 子线程

class RunthreadStart(QtCore.QThread):
    isStart = QtCore.pyqtSignal(int)

    def __init__(self):
        super(RunthreadStart, self).__init__()

    def run(self):
        self.isStart.emit(1)


class RunthreadGetWeather(QtCore.QThread):
    proBar_single = QtCore.pyqtSignal(Weathers)  # 更新进度条

    def __init__(self):
        super(RunthreadGetWeather, self).__init__()

    def run(self):
        wea.getweather()
        self.proBar_single.emit(wea)


class RunthreadGetData(QtCore.QThread):
    proBar_single = QtCore.pyqtSignal(Weathers)

    def __init__(self):
        super(RunthreadGetData, self).__init__()

    def run(self):
        wea.getData()
        self.proBar_single.emit(wea)


class RunthreadShowPBarState(QtCore.QThread):
    loadingState = QtCore.pyqtSignal(str)

    def __init__(self):
        super(RunthreadShowPBarState, self).__init__()

    def run(self):
        while True:
            if sig.setDataMsgIsDid and sig.setWeatherMsgIsDid:
                if sig.setClothesIsNotDid:
                    self.loadingState.emit('穿衣指数尚未修改')
                    time.sleep(1)
                if sig.setRemindIsNotDid:
                    self.loadingState.emit('温馨提示尚未修改')
                    time.sleep(1)
                if sig.setClothesIsNotDid is False and sig.setRemindIsNotDid is False:
                    break
            else:
                time.sleep(1)


class RunthreadShowPBarStateDid(QtCore.QThread):
    loadingState = QtCore.pyqtSignal(str)

    def __init__(self):
        super(RunthreadShowPBarStateDid, self).__init__()

    def run(self):
        while True:

            if sig.setDataMsgIsDid and sig.setWeatherMsgIsDid:
                if sig.setWeatherMsgIsDid:
                    self.loadingState.emit('已获取天气信息')
                    time.sleep(1)
                if sig.setDataMsgIsDid:
                    self.loadingState.emit('已获取日期信息')
                    time.sleep(1)
            else:
                time.sleep(1)


class RunthreadGetDocument(QtCore.QThread):
    getDoc = QtCore.pyqtSignal(int)

    def __init__(self):
        super(RunthreadGetDocument, self).__init__()

    def run(self):
        self.getDoc.emit(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainapp = MainApp()
    mainapp.show()
    app.exec()
