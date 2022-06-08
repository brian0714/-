from PyQt5 import QtCore, QtGui, QtWidgets
import state_DB
import pandas as pd

class Compare_Form(object):
    
    def openTechnical(self):
        from technical import Technical_big_Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Technical_big_Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show() 
    
    def openData(self):
        import Result_new
        #self.my_func()
        self.window = QtWidgets.QMainWindow()
        self.ui = Result_new.Result_new_Form()
        self.ui.setupUi(self.window)
        self.window.show()   
        
    def openNews(self):
        import News
        self.window = QtWidgets.QMainWindow()
        self.ui = News.News_Form()
        self.ui.setupUi(self.window)
        self.window.show()    
        
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 450)
        Form.setFixedSize(750, 450)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 750, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/Compare.png"))
        self.label.setObjectName("label")
        self.Title_label = QtWidgets.QLabel(Form)
        self.Title_label.setGeometry(QtCore.QRect(160, 17, 441, 41))
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
        self.Data_pushButton = QtWidgets.QPushButton(Form)
        self.Data_pushButton.setGeometry(QtCore.QRect(97, 75, 101, 28))
        self.Data_pushButton.setText("")
        self.Data_pushButton.clicked.connect(self.openData)
        self.Data_pushButton.clicked.connect(Form.close)
        self.Data_pushButton.setFlat(True)
        self.Data_pushButton.setObjectName("Data_pushButton")
        self.Index_pushButton = QtWidgets.QPushButton(Form)
        self.Index_pushButton.setGeometry(QtCore.QRect(433, 75, 101, 28))
        self.Index_pushButton.setText("")
        self.Index_pushButton.setFlat(True)
        self.Index_pushButton.clicked.connect(self.openTechnical)
        self.Index_pushButton.clicked.connect(Form.close)
        self.Index_pushButton.setObjectName("Index_pushButton")
        self.News_pushButton = QtWidgets.QPushButton(Form)
        self.News_pushButton.setGeometry(QtCore.QRect(547, 75, 101, 28))
        self.News_pushButton.setText("")
        self.News_pushButton.clicked.connect(self.openNews)
        self.News_pushButton.clicked.connect(Form.close)
        self.News_pushButton.setFlat(True)
        self.News_pushButton.setObjectName("News_pushButton")
        self.Content_label = QtWidgets.QLabel(Form)
        self.Content_label.setGeometry(QtCore.QRect(50, 125, 650, 300))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.Content_label.setFont(font)
        self.Content_label.setText("")
        
        img = QtGui.QPixmap("compare_img/{}_compare.png".format(state_DB.info_title_name))
        img = img.scaled(750, 320, QtCore.Qt.KeepAspectRatio)
        self.Content_label.setPixmap(img)
        
        self.Content_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Content_label.setObjectName("Content_label")

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
    ui = Compare_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
