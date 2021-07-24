class mycanvas(FigureCanvas):
     def __init__(self,fig):
         self.fig=fig
         FigureCanvas.__init__(self,self.fig)
         FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
         FigureCanvas.updateGeometry(self)


class error1(QtWidgets.QWidget):#дочерний класс от Qwidjet
     def __init__(self,str1,str2):
        
        super(error1, self).__init__()
        self.setupUi(str1,str2)
        self.OK.clicked.connect(self.CB_1)
    
     def setupUi(self,str1,str2):
        self.resize(480, 150)
        self.OK = QtWidgets.QPushButton('OK',self)
        self.OK.setObjectName(u"OK")
        self.OK.setGeometry(QtCore.QRect(170, 80, 110, 40))
        self.label = QtWidgets.QLabel(str2,self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(30, 20, 415, 60))
        self.setWindowTitle(QtCore.QCoreApplication.translate("Errordiolog", str1, None))
        QtCore.QMetaObject.connectSlotsByName(self)
     def CB_1(self):
         self.hide()
class kolichestvoclasterovk_srednih(error1): #дочерний класс от класса error,для метода СB OK 
     global data_two,tab_2,dannie_na_vivod,kol
     def __init__(self,str1,str2):
        
        super(kolichestvoclasterovk_srednih, self).__init__(str1,str2)
        self.setupUi(str1,str2)
        self.Cancel.clicked.connect(self.CB_1)
        self.OK.clicked.connect(self.CB_2)
        
     def setupUi(self,str1,str2):
        self.resize(480, 235)
        self.OK = QtWidgets.QPushButton('ОК',self)
        self.OK.setObjectName(u"OK")
        self.OK.setGeometry(QtCore.QRect(100, 155, 110, 40))
        self.Cancel = QtWidgets.QPushButton('ОТМЕНА',self)
        self.Cancel.setObjectName(u"Cancel")
        self.Cancel.setGeometry(QtCore.QRect(250, 155, 110, 40))
        self.label = QtWidgets.QLabel( str2,self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(100, 20, 415, 60))
        self.SpinBox = QtWidgets.QSpinBox(self)
        self.SpinBox.setObjectName(u"SpinBox")
        self.SpinBox.setGeometry(QtCore.QRect(190, 90, 80, 45))
        self.SpinBox.setMinimum(1)
        self.setWindowTitle(QtCore.QCoreApplication.translate("Errordiolog", str1, None))
        self.SpinBox.setSingleStep(1)
        QtCore.QMetaObject.connectSlotsByName(self)
     def CB_2(self): 
        _chislo_klasterov = self.SpinBox.value()
        
        
        _do=data_two.iloc[:,1:].values
        _do=(_do-_do.mean(axis=0))/_do.std(axis=0)
        from scipy.cluster.vq import kmeans2
        from scipy.spatial.distance import cdist
        warnings.filterwarnings("error",category=UserWarning)
        try:
           _centers,_labels = kmeans2(_do,_chislo_klasterov,minit='++')
        except UserWarning:
           err2.show()
           return
        dannie_na_vivod.loc[:,'label1']=_labels
        self.zapolnenie_dinam_table('label1',tab_2)

     def zapolnenie_dinam_table(self,str1,tabname):
        global dannie_na_vivod,kol
        _name_tab=[]
        tabname.clear()
        _m=0
        for group in dannie_na_vivod.groupby(str1):
         _tab_name ="Группа №{}".format(_m+1) 
         _name_tab.append(QtWidgets.QWidget() )
         _layout = QtWidgets.QVBoxLayout(_name_tab[_m])
         _tableName = "Table_{}".format(_m) 
         _table1 = QtWidgets.QTableWidget(group[1].shape[0],dannie_na_vivod.shape[1]-1)
         _table1.setObjectName(str(_tableName))
         _table1.setHorizontalHeaderLabels(dannie_na_vivod.columns)
      
         for i in range(_table1.rowCount()):
            for j in range(_table1.columnCount()):
                _x = group[1].iloc[i, j]
                _table1.setItem(i,j, QtWidgets.QTableWidgetItem(str(_x)))
                if(j<=kol and j>0):
                 _table1.item(i, j).setBackground(QtGui.QColor(100, 100, 200))
              
         _table1.resizeColumnsToContents()
         _label = QtWidgets.QLabel('*-цветом обозначены признаки, по которым велось разбиение')
         _layout.addWidget(_label)
         _layout.addWidget(_table1)
         tabname.addTab(_name_tab[_m], _tab_name)
         _m=_m+1
        dannie_na_vivod =dannie_na_vivod.drop(str1,1) 
        tabname.show()
class dendrogramma_i_rabota_s_ney(kolichestvoclasterovk_srednih):
     global Z,tab_1
     def __init__(self,str1,str2):
        
        super(dendrogramma_i_rabota_s_ney, self).__init__(str1,str2)
        self.setupUi(str1,str2)
        self.Cancel.clicked.connect(self.CB_1)
        self.OK.clicked.connect(self.razdelenie)
     def setupUi(self,str1,str2):
        self.resize(1900, 1000)
        self._verticalLayoutWidget = QtWidgets.QWidget(self)
        self._verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self._verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1870, 800))
        self.verticalLayout = QtWidgets.QVBoxLayout(self._verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QtWidgets.QLabel(str2,self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(550, 850, 550, 40))
        self.OK = QtWidgets.QPushButton('OK',self)
        self.OK.setObjectName(u"OK")
        self.OK.setGeometry(QtCore.QRect(800, 900, 110, 40))
        self.Cancel = QtWidgets.QPushButton('Отмена',self)
        self.Cancel.setObjectName(u"pushButton_2")
        self.Cancel.setGeometry(QtCore.QRect(1000, 900,110, 40))
        self.doubleSpinBox =QtWidgets.QDoubleSpinBox(self)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QtCore.QRect(1080, 850, 80, 45))
        self.doubleSpinBox.setSingleStep(0.100000000000000)
        self.setWindowTitle(QtCore.QCoreApplication.translate("Errordiolog", str1, None))        
        QtCore.QMetaObject.connectSlotsByName(self)
     def razdelenie(self):
        
        from scipy.cluster.hierarchy import fcluster
        _chislo_klasterov = self.doubleSpinBox.value()
        _labs=fcluster(Z,_chislo_klasterov,criterion='distance')
        _b=numpy.unique(_labs)
        dannie_na_vivod.loc[:,'label']=_labs
        self.zapolnenie_dinam_table('label',tab_1)

class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
        global data_two,dannie_na_vivod,kol
        super(mywindow, self).__init__()
        self.setupUi()
       
        self.pushButton_1.clicked.connect(self.ClickButton)
        self.pushButton_2.clicked.connect(self.ClB_l)
        self.checkBox.stateChanged.connect(self.clickBox)
        self.checkBox_2.stateChanged.connect(self.clickBox_2)
        self.checkBox_3.stateChanged.connect(self.clickBox_3)
        self.checkBox_4.stateChanged.connect(self.clickBox_4)
        self.checkBox_5.stateChanged.connect(self.clickBox_5)
        self.checkBox_6.stateChanged.connect(self.clickBox_6)
        self.checkBox_7.stateChanged.connect(self.clickBox_7)
        self.checkBox_8.stateChanged.connect(self.clickBox_8)
        self.checkBox_9.stateChanged.connect(self.clickBox_9)
        self.checkBox_10.stateChanged.connect(self.clickBox_10)
        self.checkBox_11.stateChanged.connect(self.clickBox_11)
        self.checkBox_12.stateChanged.connect(self.clickBox_12)
        self.checkBox_13.stateChanged.connect(self.clickBox_13)
        self.checkBox_14.stateChanged.connect(self.clickBox_14)
        self.checkBox_15.stateChanged.connect(self.clickBox_15)
        self.checkBox_16.stateChanged.connect(self.clickBox_16)
        self.checkBox_17.stateChanged.connect(self.clickBox_17)
        self.checkBox_18.stateChanged.connect(self.clickBox_18)
        self.checkBox_19.stateChanged.connect(self.clickBox_19)
        self.checkBox_20.stateChanged.connect(self.clickBox_20)

    def setupUi(self):
        self.resize(1250, 700)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QtCore.QRect(20, 5, 1220, 500))
       
             
        
      
                
        