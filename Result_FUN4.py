from PyQt5 import QtCore, QtGui, QtWidgets
import state_DB
import pandas as pd
from technical_FUN4 import Technical_big_Ui_FUN4_Form

class FUN4_Ui_Form(object):

    models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')         
    
    def get_result(self, column_name):
        global models_results

        #print(models_results['stock_name'][0])
        for i in range(len(self.models_results)):
            #print(models_results['stock_no'][i],state_DB.info_title_name)
            if self.models_results['stock_no'][i] == int(state_DB.stock_list[state_DB.turn_page_i]):
                if 'rmse' in column_name or 'mape' in column_name:
                    return str(round(self.models_results[column_name][i],2))
                else:
                    return str(self.models_results[column_name][i])

    def openCompare(self):
        from Compare_FUN4 import Compare_Form_FUN4
        self.window = QtWidgets.QMainWindow()
        self.ui = Compare_Form_FUN4()
        self.ui.setupUi(self.window)
        self.window.show() 

    def openNews(self):
        from News_FUN4 import News_Form_FUN4
        self.window = QtWidgets.QMainWindow()
        self.ui = News_Form_FUN4()
        self.ui.setupUi(self.window)
        self.window.show()   

    def openTechnical(self):
        #from technical_FUN4 import Technical_big_Ui_FUN4_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Technical_big_Ui_FUN4_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    
    def NextData(self):
        state_DB.turn_page_i = (state_DB.turn_page_i + 1) % len(state_DB.stock_list)
        self.Title_label.setText('{} {}'.format(self.get_result('stock_name'),state_DB.stock_list[state_DB.turn_page_i]))

        _translate = QtCore.QCoreApplication.translate
        self.yesterday_price_label.setText(_translate("Form", self.get_result('yesterday_stock_price')))
        self.tomorrow_price_label.setText(_translate("Form", str(round(float(self.get_result('predict_stock_price')),2))))
        self.predict_fit_label.setText(_translate("Form", self.get_result('r2')))

        #self.suggest_action_label.setText(self.get_result('predict_state'))
        if float(self.get_result('predict_state')) == float(2.0):
            self.suggest_action_label.setText('買')
            self.suggest_action_label.setStyleSheet("color:red")
        elif float(self.get_result('predict_state')) == float(1.0):
            self.suggest_action_label.setText('賣')
            self.suggest_action_label.setStyleSheet("color:green")
        else:
            self.suggest_action_label.setText('不交易')

        self.recent_ave_price_label.setText(_translate("Form", self.get_result('average_stock_p')))
        self.RMSE10_label.setText(_translate("Form", self.get_result('rmse_10')))
        self.MAPE10_label.setText(_translate("Form", self.get_result('mape_10')))
        self.RMSE20_label.setText(_translate("Form", self.get_result('rmse_20')))
        self.MAPE20_label.setText(_translate("Form", self.get_result('mape_20')))



    def PrevData(self):
        state_DB.turn_page_i = (state_DB.turn_page_i - 1) % len(state_DB.stock_list)
        self.Title_label.setText('{} {}'.format(self.get_result('stock_name'),state_DB.stock_list[state_DB.turn_page_i]))

        _translate = QtCore.QCoreApplication.translate
        self.yesterday_price_label.setText(_translate("Form", self.get_result('yesterday_stock_price')))
        self.tomorrow_price_label.setText(_translate("Form", str(round(float(self.get_result('predict_stock_price')),2))))
        self.predict_fit_label.setText(_translate("Form", self.get_result('r2')))

        #self.suggest_action_label.setText(self.get_result('predict_state'))
        if float(self.get_result('predict_state')) == float(2.0):
            self.suggest_action_label.setText('買')
            self.suggest_action_label.setStyleSheet("color:red")
        elif float(self.get_result('predict_state')) == float(1.0):
            self.suggest_action_label.setText('賣')
            self.suggest_action_label.setStyleSheet("color:green")
        else:
            self.suggest_action_label.setText('不交易')

        self.recent_ave_price_label.setText(_translate("Form", self.get_result('average_stock_p')))
        self.RMSE10_label.setText(_translate("Form", self.get_result('rmse_10')))
        self.MAPE10_label.setText(_translate("Form", self.get_result('mape_10')))
        self.RMSE20_label.setText(_translate("Form", self.get_result('rmse_20')))
        self.MAPE20_label.setText(_translate("Form", self.get_result('mape_20')))




 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 450)
        Form.setFixedSize(750, 450)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 750, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/Result.png"))
        self.label.setObjectName("label")
        self.Title_label = QtWidgets.QLabel(Form)
        self.Title_label.setGeometry(QtCore.QRect(160, 17, 441, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(23)
        self.Title_label.setFont(font)
        self.Title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label.setObjectName("Title_label")
        #self.Title_label.setText(state_DB.stock_list[state_DB.turn_page_i])
        self.yesterday_price_label = QtWidgets.QLabel(Form)
        self.yesterday_price_label.setGeometry(QtCore.QRect(180, 140, 158, 27))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.yesterday_price_label.setFont(font)
        self.yesterday_price_label.setAlignment(QtCore.Qt.AlignCenter)
        self.yesterday_price_label.setObjectName("yesterday_price_label")
        
        self.Compare_pushButton = QtWidgets.QPushButton(Form)
        self.Compare_pushButton.setGeometry(QtCore.QRect(210, 75, 211, 28))
        self.Compare_pushButton.setText("")
        self.Compare_pushButton.setFlat(True)
        self.Compare_pushButton.setObjectName("Compare_pushButton")
        self.Compare_pushButton.clicked.connect(self.openCompare) #開啟新視窗
        self.Compare_pushButton.clicked.connect(Form.close) #關閉原視窗    
        
        self.Index_pushButton = QtWidgets.QPushButton(Form)
        self.Index_pushButton.setGeometry(QtCore.QRect(433, 75, 101, 28))
        self.Index_pushButton.setText("")
        self.Index_pushButton.setFlat(True)
        self.Index_pushButton.setObjectName("Index_pushButton")
        self.Index_pushButton.clicked.connect(self.openTechnical) #開啟新視窗
        self.Index_pushButton.clicked.connect(Form.close) #關閉原視窗    
        
        self.News_pushButton = QtWidgets.QPushButton(Form)
        self.News_pushButton.setGeometry(QtCore.QRect(547, 75, 101, 28))
        self.News_pushButton.setText("")
        self.News_pushButton.setFlat(True)
        self.News_pushButton.setObjectName("News_pushButton")
        self.News_pushButton.clicked.connect(self.openNews) #開啟新視窗
        self.News_pushButton.clicked.connect(Form.close) #關閉原視窗         
        
        self.tomorrow_price_label = QtWidgets.QLabel(Form)
        self.tomorrow_price_label.setGeometry(QtCore.QRect(180, 205, 158, 27))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.tomorrow_price_label.setFont(font)
        self.tomorrow_price_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tomorrow_price_label.setObjectName("tomorrow_price_label")
        self.predict_fit_label = QtWidgets.QLabel(Form)
        self.predict_fit_label.setGeometry(QtCore.QRect(180, 280, 158, 27))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.predict_fit_label.setFont(font)
        self.predict_fit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.predict_fit_label.setObjectName("predict_fit_label")
        self.suggest_action_label = QtWidgets.QLabel(Form)
        self.suggest_action_label.setGeometry(QtCore.QRect(180, 360, 158, 27))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.suggest_action_label.setFont(font)
        self.suggest_action_label.setAlignment(QtCore.Qt.AlignCenter)
        self.suggest_action_label.setObjectName("suggest_action_label")
        self.recent_ave_price_label = QtWidgets.QLabel(Form)
        self.recent_ave_price_label.setGeometry(QtCore.QRect(540, 140, 161, 27))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.recent_ave_price_label.setFont(font)
        self.recent_ave_price_label.setAlignment(QtCore.Qt.AlignCenter)
        self.recent_ave_price_label.setObjectName("recent_ave_price_label")
        self.RMSE10_label = QtWidgets.QLabel(Form)
        self.RMSE10_label.setGeometry(QtCore.QRect(540, 200, 161, 27))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.RMSE10_label.setFont(font)
        self.RMSE10_label.setAlignment(QtCore.Qt.AlignCenter)
        self.RMSE10_label.setObjectName("RMSE10_label")
        self.MAPE10_label = QtWidgets.QLabel(Form)
        self.MAPE10_label.setGeometry(QtCore.QRect(540, 255, 161, 27))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.MAPE10_label.setFont(font)
        self.MAPE10_label.setAlignment(QtCore.Qt.AlignCenter)
        self.MAPE10_label.setObjectName("MAPE10_label")
        self.RMSE20_label = QtWidgets.QLabel(Form)
        self.RMSE20_label.setGeometry(QtCore.QRect(540, 315, 161, 27))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.RMSE20_label.setFont(font)
        self.RMSE20_label.setAlignment(QtCore.Qt.AlignCenter)
        self.RMSE20_label.setObjectName("RMSE20_label")
        self.MAPE20_label = QtWidgets.QLabel(Form)
        self.MAPE20_label.setGeometry(QtCore.QRect(540, 380, 161, 27))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(14)
        self.MAPE20_label.setFont(font)
        self.MAPE20_label.setAlignment(QtCore.Qt.AlignCenter)
        self.MAPE20_label.setObjectName("MAPE20_label")
        self.Next_Button = QtWidgets.QPushButton(Form)
        self.Next_Button.setGeometry(QtCore.QRect(605, 20, 41, 41))
        self.Next_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Next_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/right-chevron (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next_Button.setIcon(icon)
        self.Next_Button.setIconSize(QtCore.QSize(40, 40))
        self.Next_Button.setAutoRepeatDelay(32)
        self.Next_Button.setAutoRepeatInterval(32)
        self.Next_Button.setDefault(False)
        self.Next_Button.setFlat(True)
        self.Next_Button.setObjectName("Next_Button")
        self.Prev_Button = QtWidgets.QPushButton(Form)
        self.Prev_Button.setGeometry(QtCore.QRect(105, 20, 41, 39))
        self.Prev_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Prev_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/FotoJet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Prev_Button.setIcon(icon1)
        self.Prev_Button.setIconSize(QtCore.QSize(40, 40))
        self.Prev_Button.setAutoRepeatDelay(32)
        self.Prev_Button.setAutoRepeatInterval(32)
        self.Prev_Button.setDefault(False)
        self.Prev_Button.setFlat(True)
        self.Prev_Button.setObjectName("Prev_Button")
        
        self.Next_Button.clicked.connect(self.NextData) 
        self.Prev_Button.clicked.connect(self.PrevData)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        i = state_DB.turn_page_i
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "股票分析系統"))
        Form.setWindowIcon(QtGui.QIcon("img/money.ico"))

        self.Title_label.setText(_translate("Form", '{} {}'.format(self.get_result('stock_name'),state_DB.stock_list[state_DB.turn_page_i])))

        self.yesterday_price_label.setText(_translate("Form", self.get_result('yesterday_stock_price')))
        self.tomorrow_price_label.setText(_translate("Form", str(round(float(self.get_result('predict_stock_price')),2))))
        self.predict_fit_label.setText(_translate("Form", self.get_result('r2')))

        #self.suggest_action_label.setText(self.get_result('predict_state'))
        if float(self.get_result('predict_state')) == float(2.0):
            self.suggest_action_label.setText('買')
            self.suggest_action_label.setStyleSheet("color:red")
        elif float(self.get_result('predict_state')) == float(1.0):
            self.suggest_action_label.setText('賣')
            self.suggest_action_label.setStyleSheet("color:green")
        else:
            self.suggest_action_label.setText('不交易')

        self.recent_ave_price_label.setText(_translate("Form", self.get_result('average_stock_p')))
        self.RMSE10_label.setText(_translate("Form", self.get_result('rmse_10')))
        self.MAPE10_label.setText(_translate("Form", self.get_result('mape_10') + '%'))
        self.RMSE20_label.setText(_translate("Form", self.get_result('rmse_20')))
        self.MAPE20_label.setText(_translate("Form", self.get_result('mape_20') + '%'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = FUN4_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
