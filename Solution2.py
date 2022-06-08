from PyQt5 import QtCore, QtGui, QtWidgets
#from Result import Result_Form

class Solution2_Ui_Form(object):
    
    #def openWindow(self):
     #   self.window = QtWidgets.QMainWindow()
      #  self.ui = Result_Form()
       # self.ui.setupUi(self.window)
        #self.window.show()           
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(772, 474)
        Form.setFixedSize(750, 450)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 750, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/SOLU2.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 352, 151, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/確認_底白.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(150, 40))
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.clicked.connect(self.openWindow) #開啟新視窗
        #self.pushButton.clicked.connect(Form.close) #關閉原視窗
        self.comboBox_1 = QtWidgets.QComboBox(Form)
        self.comboBox_1.setGeometry(QtCore.QRect(200, 210, 320, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setAutoFillBackground(True)
        self.comboBox_1.setMaxVisibleItems(10)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 280, 320, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(6)
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setObjectName("comboBox_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "股票分析系統"))
        Form.setWindowIcon(QtGui.QIcon("img/money.ico"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Solution2_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

