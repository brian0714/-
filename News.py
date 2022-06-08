from PyQt5 import QtCore, QtGui, QtWidgets
#from Compare import Compare_Form
import pandas as pd
import state_DB

class News_Form(object):
    

    def openTechnical(self):
        from technical import Technical_big_Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Technical_big_Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCompare(self):
        import Compare
        self.window = QtWidgets.QMainWindow()
        self.ui = Compare.Compare_Form()
        self.ui.setupUi(self.window)
        self.window.show()    
    
    def openData(self):
        import Result_new
        #self.my_func()
        self.window = QtWidgets.QMainWindow()
        self.ui = Result_new.Result_new_Form()
        self.ui.setupUi(self.window)
        self.window.show()        
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(793, 481)
        Form.setFixedSize(793, 481)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 750, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/News.png"))
        self.label.setObjectName("label")
        self.Title_label = QtWidgets.QLabel(Form)
        self.Title_label.setGeometry(QtCore.QRect(160, 17, 441, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(23)
        self.Title_label.setFont(font)
        self.Title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label.setObjectName("Title_label")
        self.Data_pushButton = QtWidgets.QPushButton(Form)
        self.Data_pushButton.setGeometry(QtCore.QRect(97, 75, 101, 28))
        self.Data_pushButton.setText("")
        self.Data_pushButton.setFlat(True)
        self.Data_pushButton.setObjectName("Data_pushButton")
        self.Data_pushButton.clicked.connect(self.openData)
        self.Data_pushButton.clicked.connect(Form.close)  
        self.Compare_pushButton = QtWidgets.QPushButton(Form)
        self.Compare_pushButton.setGeometry(QtCore.QRect(207, 75, 211, 28))
        self.Compare_pushButton.setText("")
        self.Compare_pushButton.setFlat(True)
        self.Compare_pushButton.setObjectName("Compare_pushButton")
        self.Compare_pushButton.clicked.connect(self.openCompare)
        self.Compare_pushButton.clicked.connect(Form.close)  
        self.Index_pushButton = QtWidgets.QPushButton(Form)
        self.Index_pushButton.setGeometry(QtCore.QRect(433, 75, 101, 28))
        self.Index_pushButton.setText("")
        self.Index_pushButton.setFlat(True)
        self.Index_pushButton.setObjectName("Index_pushButton")
        self.Index_pushButton.clicked.connect(self.openTechnical)
        self.Index_pushButton.clicked.connect(Form.close)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 120, 711, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setLineWidth(2)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 686, 1000))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(200, 1000))
        self.scrollAreaWidgetContents_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.scrollAreaWidgetContents_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setGeometry(QtCore.QRect(10, 10, 671, 1500))
        self.widget.setMinimumSize(QtCore.QSize(661, 1500))
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 620, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setScaledContents(False)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(130, 50, 451, 261))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/CH.jpg"))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(30, 330, 620, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 600))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "股票分析系統"))
        Form.setWindowIcon(QtGui.QIcon("img/money.ico"))

        models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
        for i in range(len(models_results)):
            if state_DB.info_title_name == str(models_results['stock_no'][i]):
                stock_selection = '{} {}'.format(models_results['stock_name'][i], models_results['stock_no'][i])
        self.Title_label.setText(stock_selection)
        
        self.label_3.setText(_translate("Form", "<a href=\"http://www.google.com\">1. 鴻海退出群創董事會 震撼業界</a>"))
        self.label_2.setText(_translate("Form", "面板大廠群創將在六月二十四日舉行股東常會並改選董事，公司公告的董事候選人名單中，四席董事、五席獨董全由自然人擔任，鴻海集團並未參選，是群創自二○○三年成立以來，鴻海集團首度撤出群創董事會，震撼業界。\n"
"\n"
"鴻海集團目前透過旗下鴻揚創投掌握群創兩席董事，此次群創改選未見鴻海集團推派所屬勢力參選，時值面板景氣反轉之際，鴻海集團退出群創董事會，引發外界產生「淡化鴻海色彩」聯想。至昨日截稿前，無法取得群創回應；鴻海對此也沒有回應。\n"
"\n"
"攤開群創今年提名的董事名單，四席自然人董事為群創董事長洪進揚、群創教育基金會董事長王志超、群創總經理楊柱祥，及群創執行副總暨群豐駿科技董事長丁景隆，均與現任四席董事完全相同。唯一不同之處，是楊柱祥與丁景隆原是以鴻揚創投法人董事代表人名義出任，今年改為自然人身分。這意味參與創立群創光電的鴻揚創投將退出群創董事會，引起關注。\n"
"\n"
"群創二○○三年成立，在富爸爸鴻海的加持下，二○○五年繳出轉虧為盈的成績單，在監視器面板躋身全球前三大供應商，二○○六年群創上市，二○一○年完成合併奇美電、統寶的「三合一」，躍升為台灣面板廠一哥。群創受面板報價去年下半年起走跌與需求疲弱影響，今年首季稅後純益降至十八點八九億元，季減百分之六十八點二，年減百分之八十三點七，每股純益○點一八元，下探近六季低點。"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = News_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
