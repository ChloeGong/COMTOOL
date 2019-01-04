#窗口：name+path 
# button:cancel+save 
#窗口一定要有 _init_ init initEvent closeEvent
from PyQt5.QtCore import pyqtSignal,Qt,QRect
from PyQt5.QtWidgets import (QApplication, QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget,QMainWindow,
                             QVBoxLayout,QHBoxLayout,QGridLayout,QTextEdit,QLabel,QRadioButton,QCheckBox,
                             QLineEdit,QGroupBox,QSplitter,QDialog)
from Combobox import ComboBox
test = "save file"
class Ui_TestSave(QWidget):#窗口设计  
    def init(self):
        self.setObjectName("Save File")
        self.resize(500,400)#窗口的大小
        self.frameWidget = QWidget()
        self.mainWidget = QSplitter(Qt.Horizontal) 
        self.frameLayout = QHBoxLayout()
        self.settingWidget = QWidget()
        self.settingWidget.setProperty("class","settingWidget")
        self.settingLayout = QVBoxLayout()
        self.mainLayout = QHBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)
        self.settingWidget.setLayout(self.settingLayout)
        self. mainLayout.addWidget(self.settingWidget)
        self.frameLayout.addWidget(self.mainWidget)
        self.frameWidget.setLayout(self.frameLayout)
       
        



    def __init__(self,parent = None):
        super(Ui_TestSave,self).__init__(parent)
        self.init()
        self.show()

        
