from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QPushButton
from PyQt5 import uic
import sys
import state_DB
from Result_new import Result_new_Form
import pandas as pd
from PyQt5.QtWidgets import QMessageBox


class Solution2_1_Ui_Form(QtWidgets.QMainWindow):
    click1 = False
    click2 = False
    
    def openWindow(self):
        global click1
        global click2
        if self.click1 and self.click2:
            #self.button.clicked.connect(self.close)
            self.window = QtWidgets.QMainWindow()
            self.ui = Result_new_Form()
            self.ui.setupUi(self.window)
            self.window.show()
            self.click1 = False
            self.click2 = False
        elif not self.click1:
            QMessageBox.warning(None, '請注意', '請選擇股票業別!')
        elif not self.click2:
            QMessageBox.warning(None, '請注意', '請選擇股號!')
    def __init__(self):
        super(Solution2_1_Ui_Form, self).__init__()
        #self.setWindowTitle('Login')
        # Load the ui file
        uic.loadUi("Solution2.ui", self)
        self.subWindow = Result_new_Form()
        # Define our widgets
        self.combo1 = self.findChild(QComboBox, "comboBox_1")
        self.combo2 = self.findChild(QComboBox, "comboBox_2")
        self.button = self.findChild(QPushButton, "pushButton")

        data = {'水泥':['1101','1102'],
                '半導體':['2330', '2454', '2303', '3711', '3034', '2379', '6415', '2408'],
                '其他電子':['2317', '2474'],
                '電子零組件':['2308', '2327','8046'],
                '金融':['2880','2801','2881', '2882','2887', '2891', '2886', '2884', '2885', '2892','5876', '5880'],
                '塑膠':['1301','1303','1326'],
                '鋼鐵':['2002'],
                '通信網路':['2412','3045','4904'],
                '食品工業':['1216'],
                '光電':['3008'],
                '電腦及週邊設備':['2357','2382','4938','2395','6669'],
                '汽車工業':['2207'],
                '油電燃氣':['6505'],
                '貿易百貨':['2912'],
                '電機機械':['1590'],
                '紡織纖維':['1402'],
                '其他':['5871','9910'],
                '橡膠工業':['2105'],
                '航運':['2633']} 
        keys = list(data.keys())
        values = list(data.values())
        #print(keys,'\n',values)
        # Add items to the comboBox
        self.combo1.addItem('')
        for i in range(len(keys)):
          self.combo1.addItem(keys[i], values[i])
        # Click The Dropdown Box
        self.combo1.activated.connect(self.clicker)
        self.combo2.activated.connect(self.clicker2)
        #self.button.clicked.connect(self.close)
        self.button.clicked.connect(self.openWindow)
        

    def clicker(self, index):
        global click1
        self.click1 = True
        
        # Clear the second box
        self.combo2.clear()
        # Do the dependent thing
        
        classifications = []
        #self.combo1.itemData(index)為list
        models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
        for stock_no in self.combo1.itemData(index):
            for i in range(len(models_results)):
                if stock_no == str(models_results['stock_no'][i]):
                    stock_selection = '{} {}'.format(models_results['stock_name'][i], models_results['stock_no'][i])
                    classifications.append(stock_selection)
                    break
        self.combo2.addItem('')
        self.combo2.addItems(classifications)
        #self.combo2.addItems(self.combo1.itemData(index))

    def clicker2(self):
        global click2
        self.click2 = True
        
        state_DB.info_title_name = self.combo2.currentText().split(' ')[-1]
        #print(self.combo2.currentText())

        
# Initialize The App       
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Solution2_1_Ui_Form()
    demo.setFixedSize(750, 450)
    demo.setWindowTitle("股票分析系統")
    demo.setWindowIcon(QtGui.QIcon("img/money.ico"))
    demo.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
