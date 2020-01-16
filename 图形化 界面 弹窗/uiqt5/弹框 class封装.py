import sys
from PyQt5 import QtWidgets,QtGui,QtCore,Qt
print("功能为：在输入框中输入值过后，点击按钮就会打印出你输入的值，关闭窗口会有提示")
class GUI(QtWidgets.QWidget):
    def __init__(self):
        #初始化————init__
        super().__init__()
        self.initGUI()
    def initGUI(self):
        #设置窗口大小
        self.resize(500,500)
        #设置窗口位置(下面配置的是居于屏幕中间)
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        #设置窗口标题和图标
        self.setWindowTitle('如花')
        self.setWindowIcon(QtGui.QIcon('2.jpg'))
        #设置窗口提示
        self.setToolTip('窗口提示')
        #设置label信息
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 10, 100, 60))
        self.label.setText('这是lable信息')
        self.label.setObjectName('label')
        # 设置label提示
        self.label.setToolTip('label提示')
        #设置输入框
        self.textbox = Qt.QLineEdit(self)
        self.textbox.resize(100, 20)
        self.textbox.move(100, 50)
        # 设置输入框提示
        self.textbox.setToolTip('输入框提示')
        #设置按钮
        self.btn =QtWidgets.QPushButton('按钮',self)
        self.btn.resize(100,20)
        self.btn.move(200,50)
        # 设置按钮样式
        self.btn.setStyleSheet("background-color: rgb(164, 185, 255);"
            "border-color: rgb(170, 150, 163);"
            "font: 75 12pt \"Arial Narrow\";"
            "color: rgb(126, 255, 46);")
        # 设置按钮提示
        self.btn.setToolTip('按钮提示')
        #点击鼠标触发事件
        self.btn.clicked.connect(self.clickbtn)
        #展示窗口
        self.show();
        #点击鼠标触发函数
    def clickbtn(self):
        #打印出输入框的信息
        textboxValue = self.textbox.text()
        QtWidgets.QMessageBox.question(self, "信息", '你输入的输入框内容为:' + textboxValue,QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        #清空输入框信息
        self.textbox.setText('')
        #关闭窗口事件重写
    def closeEvent(self, QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self, '警告',"确定关闭当前窗口?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())