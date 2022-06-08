from PyQt5 import QtCore, QtGui, QtWidgets
import random
from Result_new import Result_new_Form
import state_DB
import pandas as pd 

class Solution3_Ui_Form(object):

    data = []
    models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
    for i in range(len(models_results)):
        data.append('{} {}'.format(models_results['stock_name'][i],models_results['stock_no'][i]))

    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Result_new_Form()
        self.ui.setupUi(self.window)
        self.window.show()         
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(772, 474)
        Form.setFixedSize(750, 450)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 750, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/SOLU3.png"))
        self.label.setObjectName("label")
        self.Confirmed_Button = QtWidgets.QPushButton(Form)
        self.Confirmed_Button.setGeometry(QtCore.QRect(250, 360, 151, 41))
        self.Confirmed_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Confirmed_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/確認_底白.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Confirmed_Button.setIcon(icon)
        self.Confirmed_Button.setIconSize(QtCore.QSize(150, 40))
        self.Confirmed_Button.setDefault(False)
        self.Confirmed_Button.setFlat(False)
        self.Confirmed_Button.setObjectName("Confirmed_Button")
        self.Confirmed_Button.clicked.connect(self.openWindow) #開啟新視窗
        self.Confirmed_Button.clicked.connect(Form.close) #關閉原視窗
        self.GoBack_Button = QtWidgets.QPushButton(Form)
        #self.GoBack_Button.clicked.connect(self.re_random_choice())
        #self.GoBack_Button.clicked.connect(lambda: self.label_2.setText(random.choice(data)))
        self.GoBack_Button.setGeometry(QtCore.QRect(420, 360, 41, 41))
        self.GoBack_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GoBack_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/refresh_BUTT_底白.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GoBack_Button.setIcon(icon1)
        self.GoBack_Button.setIconSize(QtCore.QSize(40, 40))
        self.GoBack_Button.setAutoRepeatDelay(40)
        self.GoBack_Button.setAutoRepeatInterval(40)
        self.GoBack_Button.setDefault(False)
        self.GoBack_Button.setFlat(False)
        self.GoBack_Button.setObjectName("GoBack_Button")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(210, 240, 311, 41))
        
        self.GoBack_Button.clicked.connect(lambda: self.re_random_choice())
        
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(19)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setAcceptDrops(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        global data
                
        Form.setWindowTitle(_translate("Form", "股票分析系統"))
        Form.setWindowIcon(QtGui.QIcon("img/money.ico"))
                #logo = QtGui.QIcon("img/money.ico")
        random_stock_no = random.choice(self.data)
        self.label_2.setText(_translate("Form", random_stock_no))
        state_DB.info_title_name = random_stock_no.split(' ')[-1]

    def re_random_choice(self):
        _translate = QtCore.QCoreApplication.translate
        global data

        random_stock_no = random.choice(self.data)
        self.label_2.setText(_translate("Form", random_stock_no))
        state_DB.info_title_name = random_stock_no.split(' ')[-1]
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Solution3_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

