from PyQt5 import QtCore, QtGui, QtWidgets
import state_DB
from Result_new import Result_new_Form
import pandas as pd
from PyQt5.QtWidgets import QMessageBox

class Solution1_Ui_Form(object):
    #select_stock_no = '0'
    click = False
    
    def openWindow(self):
        global click
        
        if self.click:
            #self.pushButton.clicked.connect(Form.close)
            self.window = QtWidgets.QMainWindow()
            self.ui = Result_new_Form()
            self.ui.setupUi(self.window)
            self.window.show()
            #self.pushButton.clicked.connect(Form.close)
        else:
            '''msg = QMessageBox()
            msg.setIcon(QtGui.QIcon("img/money.ico"))

            msg.setText("This is a message box")
            #msg.setWindowIcon(QtGui.QIcon("img/money.ico"))
            msg.exec_()'''
            QMessageBox.warning(None, '請注意', '請直接輸入股號或從選單尋找!')

        
        
    def clicker(self):
        global click

        self.click = True
        self.ui = Result_new_Form()
        #print('content:',self.comboBox.currentText())
        state_DB.info_title_name = self.comboBox.currentText().split(' ')[0]
        #print(state_DB.info_title_name)
    
    def setupUi(self, Form):
        self.ui = Result_new_Form()
        Form.setObjectName("Form")
        Form.setFixedSize(750, 450)
        #Form.resize(772, 474)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 750, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/SOLU1.png"))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(210, 220, 311, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.activated.connect(self.clicker)
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)

        
        #print('text',self.comboBox.currentText())
        self.pushButton.clicked.connect(self.openWindow) #開啟新視窗
        #self.pushButton.clicked.connect(Form.close)#關閉原視窗
    
            
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "股票分析系統"))
        Form.setWindowIcon(QtGui.QIcon("img/money.ico"))
        models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
        for i in range(len(models_results)):
            stock_selection = '{} {}'.format(models_results['stock_no'][i],models_results['stock_name'][i])
            self.comboBox.setItemText(i+1, _translate("Form", stock_selection))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Solution1_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

