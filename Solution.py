from PyQt5 import QtCore, QtGui, QtWidgets
from Solution1 import Solution1_Ui_Form
from Solution2_1 import Solution2_1_Ui_Form
from Solution3 import Solution3_Ui_Form
from Solution4 import Solution4_Ui_Form

class Solution_Ui_MainWindow(object):
  
    def openWindow1(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Solution1_Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()       

    def openWindow2_1(self):
        #self.window = QtWidgets.QMainWindow()
        
        self.ui = Solution2_1_Ui_Form()
        #self.ui.setupUi(self.window)
        self.ui.setFixedSize(750, 450)
        self.ui.setWindowTitle("股票分析系統")
        self.ui.setWindowIcon(QtGui.QIcon("img/money.ico"))
        self.ui.show() 

    def openWindow3(self):  
        self.window = QtWidgets.QMainWindow()
        self.ui = Solution3_Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show() 
        
    def openWindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Solution4_Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()         
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(756, 490)
        MainWindow.setFixedSize(750, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 750, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/P1_NEW3 (1).png"))
        self.label.setObjectName("label")
        self.Solution1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow1())
        self.Solution1.setGeometry(QtCore.QRect(190, 200, 161, 111))
        self.Solution1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Solution1.setText("")
        self.Solution1.setFlat(True)
        self.Solution1.setObjectName("Solution1")
        self.Solution3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow3())
        self.Solution3.setGeometry(QtCore.QRect(370, 200, 161, 111))
        self.Solution3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Solution3.setText("")
        self.Solution3.setFlat(True)
        self.Solution3.setObjectName("Solution3")
        self.Solution2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow2_1())
        self.Solution2.setGeometry(QtCore.QRect(190, 320, 161, 111))
        self.Solution2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Solution2.setText("")
        self.Solution2.setAutoDefault(False)
        self.Solution2.setFlat(True)
        self.Solution2.setObjectName("Solution2")
        self.Solution4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow4())
        self.Solution4.setGeometry(QtCore.QRect(370, 320, 161, 111))
        self.Solution4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Solution4.setText("")
        self.Solution4.setFlat(True)
        self.Solution4.setObjectName("Solution4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
    ui = Solution_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

