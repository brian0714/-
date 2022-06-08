from PyQt5 import QtCore, QtGui, QtWidgets
from random import sample
from Result_FUN4 import FUN4_Ui_Form
import state_DB
import pandas as pd

class Solution4_Ui_Form(object):
    pick_ups = 7
    models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
    stock_dict = {}
    for i in range(len(models_results)):
        stock_dict[models_results['stock_no'][i]] = models_results['risk'][i]
    risks = sorted(models_results['risk'].values.tolist())[:pick_ups]

    low_risk_stock = []
    for risk in risks:
        for stock_no in stock_dict:
            if stock_dict[stock_no] == risk and stock_no not in low_risk_stock:#避免風險一樣
                low_risk_stock.append(stock_no)
                break
    #print(low_risk_stock)

    stock_name_dict = {}
    for i in range(len(models_results)):
        stock_name_dict[models_results['stock_no'][i]] = models_results['stock_name'][i]

    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = FUN4_Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()           
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(772, 474)
        Form.setFixedSize(750, 450)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 750, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/SOLU4.png"))
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
        self.GoBack_Button.clicked.connect(self.retry_button_clicked)
        
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
        self.label_2.setGeometry(QtCore.QRect(100, 200, 541, 150))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
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


    def random_button_clicked(self): #隨機五支 (用不到)
        data = ['台泥  1101', '亞泥  1102', '統一  1216', '台塑  1301', '南亞  1303', '台化 1326', 
                '遠東新1402', '亞德客-KY  1590', '中鋼  2002', '正新  2105', '和泰車  2207', '聯電  2303', 
                '台達電  2308', '鴻海  2317', '國巨  2327', '台積電  2330', '華碩  2357', '瑞昱  2379', 
                '廣達  2382', '研華  2395', '南亞科  2408', '中華電  2412','聯發科2454', '可成  2474', 
                '台灣高鐵  2633', '彰銀  2801', '華南金  2880', '富邦金  2881', '國泰金  2882', '玉山金  2884', 
                '元大金  2885', '兆豐金  2886', '台新金  2887', '中信金  2891', '第一金  2892', '統一超  2912', 
                '大立光  3008','聯詠  3034', '台灣大  3045', '日月光  3711', '遠傳  4904', '和碩  4938', 
                '中租-KY  5871', '上海商  5876', '合作金  5880', '矽力  6415', '台塑化  6505', '緯穎  6669', 
                '南電  8046', '豐泰  9910']  
        
        List = sample(data, 5)
        S = ''
        for i in List:
            S += i+'\n'
        self.label_2.setText(S)
        

    def retry_button_clicked(self):
        global low_risk_stock
        global stock_name_dict
        
        List = sample(self.low_risk_stock, 5)
        S = ''
        for stock_no in List:
            S += self.stock_name_dict[stock_no] + ' ' + str(stock_no) + '\n'
        self.label_2.setText(S)
        state_DB.stock_list = [str(stock_no) for stock_no in List]

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "股票分析系統"))
        Form.setWindowIcon(QtGui.QIcon("img/money.ico"))

        global low_risk_stock
        global stock_name_dict
        
        List = sample(self.low_risk_stock, 5)
        S = ''
        for stock_no in List:
            S += self.stock_name_dict[stock_no] + ' ' + str(stock_no) + '\n'
        self.label_2.setText(_translate("Form", S))
        state_DB.stock_list = [str(stock_no) for stock_no in List]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Solution4_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
