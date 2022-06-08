from PyQt5 import QtCore, QtGui, QtWidgets
#from FirstPage import FirstPage_Ui_Form
from Solution import Solution_Ui_MainWindow
import pandas as pd
import numpy as np
import datetime
import state_DB
import math
import crawl_stock_data
import calculate_compare
import data_preprocessing
import trading_strategy
from PyQt5.QtWidgets import QMessageBox

import tensorflow as tf

class Ui_MainWindow(object):
    msg = '''請稍等3-4分鐘，請勿關閉程式！\n若久日未登入此系統，
        則需要等待較久時間以供系統做爬蟲及預測\n(一日未登，需等3-4分鐘；2日未登需等6-8分鐘；以此類推)'''
    #QMessageBox.warning(None, '請詳閱',msg)
    def update_data(self):
    #檢查該股是否需爬蟲或將csv資料整合
        models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
        #stock_no_data = pd.read_csv('stocks_csv/{}.csv'.format(state_DB.info_title_name),encoding='UTF-8')

        def calculate_risk(stock_no_data):
            #print(stock_no_data)
            samples = 20 #以20日價差判斷浮動
            #print(stock_no_data['收盤價'])
            stock_no_data['漲跌價差'].replace( ('X0.00'),(np.NaN) , inplace=True)
            stock_no_data = stock_no_data.dropna(axis=0,how='any')#.astype(float)
            
            difs = stock_no_data['漲跌價差'][:samples].astype('float').values
            d = 0
            for dif in difs:
                d += (dif - np.mean(difs))**2
            SD = math.sqrt(d/(samples-1))
            return SD
            
        #print(stock_no_data)
        for i in range(len(models_results)):
            #比對日期
            western_date = datetime.date.today()
            western_date_month = western_date.month
            if western_date.month < 10:
                western_date_month = '0' + str(western_date.month)
            taiwan_date = '{}/{}/{}'.format(western_date.year-1911,western_date_month,western_date.day)
            #print(models_results['last_update_date'][i], taiwan_date)
            if models_results['last_update_date'][i] != taiwan_date:
                #爬蟲
                crawl_state = crawl_stock_data.crawl_stock_data(str(models_results['stock_no'][i]))
                modify_error_data = models_results['error_data'].values.tolist()
                modify_error_data[i] = crawl_state
                models_results['error_data'] = modify_error_data
                
                #儲存新爬蟲資料
                stock_no = models_results['stock_no'][i]
                stock_no_data = pd.read_csv('stocks_csv/{}.csv'.format(stock_no),encoding='UTF-8')
                modify_current_stock_p = models_results['current_stock_price'].values.tolist()
                modify_current_stock_p[i] = stock_no_data['收盤價'][0]
                models_results['current_stock_price'] = modify_current_stock_p
                
                modify_yesterday_stock_p = models_results['yesterday_stock_price'].values.tolist()
                modify_yesterday_stock_p[i] = stock_no_data['收盤價'][1]
                models_results['yesterday_stock_price'] = modify_yesterday_stock_p

                modify_last_update_date = models_results['last_update_date'].values.tolist()    
                modify_last_update_date[i] = taiwan_date
                models_results['last_update_date'] = modify_last_update_date

                #計算風險
                modify_risk = models_results['risk'].values.tolist()
                modify_risk[i] = calculate_risk(stock_no_data)
                models_results['risk'] = modify_risk

                #資料處理+訓練模型
                predict_stock_price = data_preprocessing.model_training(stock_no)
                
                modify_last_training_date = models_results['last_training_date'].values.tolist()
                modify_last_training_date[i] = taiwan_date
                models_results['last_training_date'] = modify_last_training_date

                modify_predict_stock_price = models_results['predict_stock_price'].values.tolist()    
                modify_predict_stock_price[i] = predict_stock_price
                models_results['predict_stock_price'] = modify_predict_stock_price

                predict_state = models_results['predict_state'].values.tolist()
                print(models_results['predict_stock_price'][i],models_results['current_stock_price'][i])
                predict_state[i] = trading_strategy.trading_strategy(models_results['predict_stock_price'][i],models_results['current_stock_price'][i])
                models_results['predict_state'] = predict_state

                #計算績效並儲存績效資料
                calculate_compare.draw_compare_plot(stock_no)
                
                modify_rmse_10 = models_results['rmse_10'].values.tolist()
                modify_mape_10 = models_results['mape_10'].values.tolist()
                modify_rmse_10[i], modify_mape_10[i] = calculate_compare.calculate_performance(stock_no, 10)
                models_results['rmse_10'] = modify_rmse_10
                models_results['mape_10'] = modify_mape_10

                modify_rmse_20 = models_results['rmse_20'].values.tolist()
                modify_mape_20 = models_results['mape_20'].values.tolist()  
                modify_rmse_20[i], modify_mape_20[i] = calculate_compare.calculate_performance(stock_no, 20)
                models_results['rmse_20'] = modify_rmse_20
                models_results['mape_20'] = modify_mape_20  
                
                models_results.to_csv('DB_csv/models_results.csv',encoding='ANSI', index=False)


    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Solution_Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()    
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 450)
        MainWindow.setFixedSize(750, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Letsgo_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.Letsgo_Button.setGeometry(QtCore.QRect(280, 310, 201, 71))
        self.Letsgo_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Letsgo_Button.setAccessibleDescription("")
        self.Letsgo_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/START_BUTT-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Letsgo_Button.setIcon(icon)
        self.Letsgo_Button.setIconSize(QtCore.QSize(193, 62))
        self.Letsgo_Button.setAutoExclusive(False)
        self.Letsgo_Button.setAutoDefault(False)
        self.Letsgo_Button.setDefault(False)
        self.Letsgo_Button.setFlat(True)
        self.Letsgo_Button.setObjectName("Letsgo_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 750, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/HOME-nobutt.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.Letsgo_Button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "股票分析系統"))
        MainWindow.setWindowIcon(QtGui.QIcon("img/money.ico"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.update_data()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

