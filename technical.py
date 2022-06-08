from PyQt5 import QtWebEngineWidgets, QtCore, QtGui, QtWidgets
import sys, importlib
import os
import state_DB
import technical_plot
import pandas as pd

class Technical_big_Ui_Form(object):   
    def openCompare(self):
        from Compare import Compare_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Compare_Form()
        self.ui.setupUi(self.window)
        self.window.show() 
    
    def openData(self):
        #self.my_func()
        from Result_new import Result_new_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Result_new_Form()
        self.ui.setupUi(self.window)
        self.window.show()   
        
    def openNews(self):
        from News import News_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = News_Form()
        self.ui.setupUi(self.window)
        self.window.show()    
                
    
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 500)
        Form.setFixedSize(1000, 500)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/technical.png"))
        self.label.setObjectName("label")
        self.Title_label = QtWidgets.QLabel(Form)
        self.Title_label.setGeometry(QtCore.QRect(280, 50, 447, 43))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(23)
        self.Title_label.setFont(font)

        models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
        for i in range(len(models_results)):
            if state_DB.info_title_name == str(models_results['stock_no'][i]):
                stock_selection = '{} {}'.format(models_results['stock_name'][i], models_results['stock_no'][i])
        self.Title_label.setText(stock_selection)
        
        self.Title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label.setObjectName("Title_label")
        
        
        self.content_label = QtWidgets.QLabel(Form)
        self.content_label.setGeometry(QtCore.QRect(12, 150, 971, 332))
        
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.content_label.setFont(font)
        self.content_label.setText("")
        self.content_label.setAlignment(QtCore.Qt.AlignCenter)
        self.content_label.setObjectName("content_label")        
        #self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        #self.verticalLayout.setObjectName("verticalLayout")
        #self.centralwidget = QtWidgets.QWidget(Form)
        #self.centralwidget.setObjectName("centralwidget")
        technical_plot.draw_technical_plot(state_DB.info_title_name)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.content_label)
        self.webEngineView.load(QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/technical_plot.html'))
        self.webEngineView.setGeometry(QtCore.QRect(3, 2, 965, 328))
        #self.verticalLayout.addWidget(self.webEngineView)
        #QtCore.QMetaObject.connectSlotsByName(Form)#?        
        
        

        self.Data_pushButton = QtWidgets.QPushButton(Form)
        self.Data_pushButton.setGeometry(QtCore.QRect(220, 110, 101, 28))
        self.Data_pushButton.setText("")
        self.Data_pushButton.setFlat(True)
        self.Data_pushButton.setObjectName("Data_pushButton")
        self.Data_pushButton.clicked.connect(self.openData) #開啟新視窗
        self.Data_pushButton.clicked.connect(Form.close) #關閉原視窗
        self.Compare_pushButton = QtWidgets.QPushButton(Form)
        self.Compare_pushButton.setGeometry(QtCore.QRect(330, 110, 211, 28))
        self.Compare_pushButton.setText("")
        self.Compare_pushButton.setFlat(True)
        self.Compare_pushButton.setObjectName("Compare_pushButton")
        self.Compare_pushButton.clicked.connect(self.openCompare) #開啟新視窗
        self.Compare_pushButton.clicked.connect(Form.close) #關閉原視窗        
        self.News_pushButton = QtWidgets.QPushButton(Form)
        self.News_pushButton.setGeometry(QtCore.QRect(674, 110, 101, 28))
        self.News_pushButton.setText("")
        self.News_pushButton.setFlat(True)
        self.News_pushButton.setObjectName("News_pushButton")
        self.News_pushButton.clicked.connect(self.openNews) #開啟新視窗
        self.News_pushButton.clicked.connect(Form.close) #關閉原視窗
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "股票分析系統"))
        Form.setWindowIcon(QtGui.QIcon("img/money.ico"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Technical_big_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
