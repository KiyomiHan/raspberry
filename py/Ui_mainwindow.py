# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sysmainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QTabWidget,QPushButton,QMessageBox
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2 


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import *

from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QTableView, QAbstractItemView
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import view

class Ui_sysmainwindow(object):


    def setupUi(self, sysmainwindow):

        sysmainwindow.setObjectName("sysmainwindow")
        sysmainwindow.resize(800, 600)
        sysmainwindow.setStyleSheet("QWidget{\n"
#"background-color:rgb(238,241,245);\n"
        "background-color: rgb(255,255,255,5);\n"
        "color:white;\n"
"}\n"
"\n"
"QWidget#menu{\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background-color:rgb(49,54,61);\n"
"}\n"
"QPushButton#Newstu_buttn, QPushButton#Updata_buttn, QPushButton#Ident_buttn, QPushButton#Spk_buttn, QPushButton#Log_buttn, QPushButton#Offic_buttn, \n"
"QPushButton#Teach_buttn{\n"
"color:rgb(175,170,170);\n"
"height: 45px;\n"
"background-color:rgb(49,54,61);\n"
"border-width: 0px;\n"
"border-color: #e36a75;\n"
"border-style: solid;\n"
"padding: 3px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QPushButton#mini_buttn,\n"
"QPushButton#close_buttn\n"
"{\n"
"    background-color:rgb(200, 200, 200,90);\n"
"    border:none;\n"
"    min-width: 21px;\n"
"    max-width: 21px;\n"
"    min-height: 21px;\n"
"    max-height: 21px;\n"
"}\n"
"QPushButton#mini_buttn\n"
"{\n"
"    background-image:url(./img/mini.png);\n"
"}\n"
"QPushButton#close_buttn\n"
"{\n"
"    background-image:url(./img/close.png);\n"
"}\n"
"QPushButton#mini_buttn:hover\n"
"{\n"
"    background-color:rgb(236,240,245,90);\n"
"}\n"
"QPushButton#close_buttn:hover\n"
"{\n"
"    background-color:rgb(255,0,0,90);\n"
"}\n"
"QPushButton#Newstu_buttn:hover, QPushButton#Updata_buttn:hover, QPushButton#Ident_buttn:hover, QPushButton#Spk_buttn:hover, QPushButton#Log_buttn:hover, QPushButton#Offic_buttn:hover, \n"
"QPushButton#Teach_buttn:hover{\n"
"background-color: rgb(110,110,110);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#Newstu_buttn:selected, QPushButton#Updata_buttn:selected, QPushButton#ident_buttn:selected,\n"
"QPushButton#info_buttn:selected\n"
" QPushButton#log_buttn:selected\n"
" QPushButton#offic_buttn:selected, \n"
"QPushButton#teach_buttn:selected{\n"
"background-color: rgb(110,110,110);\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane {\n"
"        border: none;\n"
"        border-top: 3px solid rgb(225, 225, 225,80);\n"
"        background: Transparent;\n"
        "color:white;"
"}\n"
"QTabWidget::tab-bar {\n"
"        border: none;\n"
"}\n"

"QTabBar::tab {\n"
"        border: none;\n"
"        border-top-left-radius: 4px;\n"
"        border-top-right-radius: 4px;\n"
"        color: white;\n"
"        background: rgb(225, 225, 225,80);\n"
"        height: 28px;\n"
"        min-width: 85px;\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"        color: white;\n"
 "background-color: rgb(21, 131 ,221,20);\n"
"}\n"
"QTabBar::tab:selected {\n"
"        color: white;\n"
 "background-color: rgb(21, 131 ,221,20);\n"
"}\n"
"QPushButton#spkHome_buttn\n"
"{\n"
"    background-image:url(./img/spkbackhome.png);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(sysmainwindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(140, 30, 661, 551))
        self.stackedWidget.setAutoFillBackground(True)
        self.stackedWidget.setStyleSheet("QComboBox {\n"
"        height: 20px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(209 , 209 , 209);\n"
"        background: white;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(255,255,255);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"QComboBox:enabled:hover, QComboBox:enabled:focus {\n"
"        border: 1px solid rgb(21 , 131 , 221);\n"
"}\n"
"QComboBox::drop-down {\n"
"        width: 20px;\n"
"        border: none;\n"
"        background: transparent;\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgb(255, 255, 255, 30);\n"
"}\n"
"QComboBox::down-arrow {\n"
"        image: url(:/White/arrowBottom);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"        /**top: 1px;**/\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        background: rgb(110,120,120,70);\n"
"        outline: none;\n"
"}\n"   
"QLineEdit\n"
"{\n"
"    background:white;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-radius:3px;\n"
"    border: 1px solid rgb(209 , 209 , 209);\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    padding-top:0px ;\n"
"    border: 1px solid rgb(21 , 131 , 221);\n"
"}\n"
"\n"
"QWidget{\n"
"background:transparent;\n"
"}\n"
"QPushButton{\n"
"color:white;\n"
"background-color:rgb(110,120,120,97);\n"
"border:0px;\n"
"border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
 "background-color: rgb(21, 131 ,221,20);\n"
"border:0px;\n"
"border-radius:4px;\n"
"}\n"

"\n"
"QMessageBox\n"
"{\n"
"border-color:#32435E; border-width:1px; border-radius: 3px;\n"
"min-width:30px; min-height:23px;\n"
"height: 300px;\n"
"width: 200px;\n"
"border: none;\n"
"}\n"
"QWidget#newstu_page,QWidget#ident_page,QWidget#spk_page,QWidget#updata_page,QWidget#log_page6,QWidget#newtea_page,QWidget#newoff_page{\n"
"background:rgb(255,255,255,50);\n"
"}\n"
"QPushButton#newteaSuccess_buttn,\n"
"QPushButton#newoffSuccess_buttn\n"
"{\n"
"    background-image:url(./img/click.png);\n"
"}\n"
"QPushButton#newteaSuccess_buttn:hover,\n"
"QPushButton#newoffSuccess_buttn:hover\n"
"{\n"
     "background-color: rgb(21, 131 ,221,20);\n"
"    background-image:url(./img/click.png);\n"
"}\n"
"QPushButton#spkHome_buttn\n"
"{\n"
"    background-image:url(./img/spkbackhome.png);\n"
"}\n"
"QPushButton#spkHome_buttn:hover\n"
"{\n"
 "background-color: rgb(21,131,221,20);\n"
"    background-image:url(./img/spkbackhome.png);\n"
"}\n"

"QHeaderView::section\n"
 "{\n"
"background-color: rgb(110,110,110,30);\n"
 " border:1px solid rgb(255,255,255,50);\n"
"height:20px;\n"      
  "}\n"
        
"QTableView{ \n" 
"background-color: rgb(110,110,110,30)\n;  "
"alternate-background-color: rgb(200, 200, 200,50);\n"
"selection-background-color: rgb(130, 190, 100,50); \n" 
"}\n "
"﻿QProgressBar {"
"   border: 2px solid rgb(255,255,255);"
"   border-radius: 5px;"
"   background-color: #FFFFFF;"
"}"
 
"QProgressBar::chunk {"
"   background-color: rgb(20 , 131 , 211,80);"
"   width: 20px;"
"}"
 
"QProgressBar {"
"   border: 2px solid grey;"
"   border-radius: 5px;"
"   text-align: center;"
"}"
)
        self.stackedWidget.setObjectName("stackedWidget")
        self.newstu_page = QtWidgets.QWidget()
###lihao
        self.lihaoTimer = QTimer()
        self.cap = cv2.VideoCapture(0)
        self.lihaoTabIndex = -1
        self.lihaoTimer.timeout.connect(self.lihaoViewCam)
        self.lihaoTimer.start(20)
 
###lihao end

        self.newstu_page.setObjectName("newstu_page")
        self.newstu_tabWidget = QtWidgets.QTabWidget(self.newstu_page)
        self.newstu_tabWidget.setGeometry(QtCore.QRect(10, 0, 641, 541))
        self.newstu_tabWidget.setMaximumSize(QtCore.QSize(16777212, 16777215))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        self.newstu_tabWidget.setFont(font)
        self.newstu_tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newstu_tabWidget.setAutoFillBackground(False)
        self.newstu_tabWidget.setStyleSheet("")
        self.newstu_tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.newstu_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.newstu_tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.newstu_tabWidget.setUsesScrollButtons(False)
        self.newstu_tabWidget.setDocumentMode(False)
        self.newstu_tabWidget.setTabsClosable(False)
        self.newstu_tabWidget.setMovable(False)
        self.newstu_tabWidget.setTabBarAutoHide(False)
        self.newstu_tabWidget.setObjectName("newstu_tabWidget")
        self.register_tab = QtWidgets.QWidget()
        self.register_tab.setStyleSheet("")
        self.register_tab.setObjectName("register_tab")
        self.stu_idcard = QtWidgets.QLabel(self.register_tab)
        self.stu_idcard.setGeometry(QtCore.QRect(170, 10, 131, 191))
        self.stu_idcard.setObjectName("stu_idcard")
        self.newstuShowclass_label = QtWidgets.QLabel(self.register_tab)
        self.newstuShowclass_label.setGeometry(QtCore.QRect(430, 430, 141, 16))
        self.newstuShowclass_label.setText("")
        self.newstuShowclass_label.setObjectName("newstuShowclass_label")
        self.line_5 = QtWidgets.QFrame(self.register_tab)
        self.line_5.setGeometry(QtCore.QRect(0, 230, 321, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.register_tab)
        self.line_6.setGeometry(QtCore.QRect(310, 10, 16, 481))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.newstuShowid_label = QtWidgets.QLabel(self.register_tab)
        self.newstuShowid_label.setGeometry(QtCore.QRect(430, 400, 141, 16))
        self.newstuShowid_label.setText("")
        self.newstuShowid_label.setObjectName("newstuShowid_label")
        self.stu_id = QtWidgets.QLabel(self.register_tab)
        self.stu_id.setGeometry(QtCore.QRect(330, 400, 51, 16))
        self.stu_id.setObjectName("stu_id")
        self.stu_name = QtWidgets.QLabel(self.register_tab)
        self.stu_name.setGeometry(QtCore.QRect(330, 370, 51, 16))
        self.stu_name.setObjectName("stu_name")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.register_tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 260, 251, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.camera_Vlayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.camera_Vlayout_2.setContentsMargins(0, 0, 0, 0)
        self.camera_Vlayout_2.setObjectName("camera_Vlayout_2")

        self.viewfinder2 = QCameraViewfinder(self.verticalLayoutWidget_3)
        self.viewfinder2.setObjectName("viewfinder2")
        self.lihaoLabel2 = QLabel("XXX2")
        self.camera_Vlayout_2.addWidget(self.lihaoLabel2)

        self.stu_fingers = QtWidgets.QLabel(self.register_tab)
        self.stu_fingers.setGeometry(QtCore.QRect(10, 10, 131, 221))
        self.stu_fingers.setObjectName("stu_fingers")
        self.line_7 = QtWidgets.QFrame(self.register_tab)
        self.line_7.setGeometry(QtCore.QRect(150, 10, 20, 221))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.newstuShowname_label = QtWidgets.QLabel(self.register_tab)
        self.newstuShowname_label.setGeometry(QtCore.QRect(430, 370, 131, 16))
        self.newstuShowname_label.setText("")
        self.newstuShowname_label.setObjectName("newstuShowname_label")
        self.stu_photoimg = QtWidgets.QLabel(self.register_tab)
        self.stu_photoimg.setGeometry(QtCore.QRect(340, 30, 91, 131))
        self.stu_photoimg.setObjectName("stu_photoimg")
        self.stu_idimg = QtWidgets.QLabel(self.register_tab)
        self.stu_idimg.setGeometry(QtCore.QRect(330, 320, 51, 31))
        self.stu_idimg.setObjectName("stu_idimg")
        self.stu_fingerimg = QtWidgets.QLabel(self.register_tab)
        self.stu_fingerimg.setGeometry(QtCore.QRect(340, 180, 91, 121))
        self.stu_fingerimg.setObjectName("stu_fingerimg")
        self.takphoto_buttn_2 = QtWidgets.QPushButton(self.register_tab)
        self.takphoto_buttn_2.setGeometry(QtCore.QRect(220, 440, 61, 41))
        self.takphoto_buttn_2.setObjectName("takphoto_buttn_2")
        self.takphoto_buttn_2.clicked.connect(sysmainwindow.lihaoTakePhoto2)
        self.stu_fin_buttn = QtWidgets.QPushButton(self.register_tab)
        self.stu_fin_buttn.setGeometry(QtCore.QRect(532, 460, 91, 31))
        self.stu_fin_buttn.setObjectName("stu_fin_buttn")
        self.stu_clas = QtWidgets.QLabel(self.register_tab)
        self.stu_clas.setGeometry(QtCore.QRect(330, 430, 51, 16))
        self.stu_clas.setObjectName("stu_clas")
        self.stu_nocard_buttn = QtWidgets.QPushButton(self.register_tab)
        self.stu_nocard_buttn.setGeometry(QtCore.QRect(210, 210, 91, 21))
        self.stu_nocard_buttn.setObjectName("stu_nocard_buttn")
        self.pissucc_label = QtWidgets.QLabel(self.register_tab)
        self.pissucc_label.setGeometry(QtCore.QRect(520, 70, 31, 31))
        self.pissucc_label.setObjectName("pissucc_label")
        self.fissucc_label = QtWidgets.QLabel(self.register_tab)
        self.fissucc_label.setGeometry(QtCore.QRect(520, 225, 31, 31))
        self.fissucc_label.setObjectName("fissucc_label")
        self.newstu_tabWidget.addTab(self.register_tab, "")

        #newstu upload
        self.newstu_tabWidget.addTab(self.register_tab, "")
        self.upload_tab = QtWidgets.QWidget()
        self.upload_tab.setObjectName("upload_tab")
        self.newstuLook_buttn = QtWidgets.QPushButton(self.upload_tab)
        self.newstuLook_buttn.setGeometry(QtCore.QRect(190, 460, 113, 32))
        self.newstuLook_buttn.setObjectName("newstuLook_buttn")
        self.newstuUpload_buttn = QtWidgets.QPushButton(self.upload_tab)
        self.newstuUpload_buttn.setGeometry(QtCore.QRect(510, 460, 113, 32))
        self.newstuUpload_buttn.setObjectName("newstuUpload_buttn")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.upload_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 281, 361))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(17)
        self.gridLayout_2.setVerticalSpacing(21)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.photoframe = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.photoframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.photoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.photoframe.setObjectName("photoframe")
        self.newstuPhotoimg_label = QtWidgets.QLabel(self.photoframe)
        self.newstuPhotoimg_label.setGeometry(QtCore.QRect(10, 10, 81, 111))
        self.newstuPhotoimg_label.setObjectName("newstuPhotoimg_label")
        self.gridLayout_2.addWidget(self.photoframe, 0, 0, 1, 2)
        self.newstuId_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.newstuId_label.setObjectName("newstuId_label")
        self.gridLayout_2.addWidget(self.newstuId_label, 2, 0, 1, 1)
        self.newstuName_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.newstuName_label.setObjectName("newstuName_label")
        self.gridLayout_2.addWidget(self.newstuName_label, 1, 0, 1, 1)
        self.newstuId_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.newstuId_lineEdit.setObjectName("newstuId_lineEdit")
        self.gridLayout_2.addWidget(self.newstuId_lineEdit, 2, 1, 1, 1)
        self.newstuFace_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.newstuFace_label.setObjectName("newstuFace_label")
        self.gridLayout_2.addWidget(self.newstuFace_label, 5, 0, 1, 1)
        self.newstuClass_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.newstuClass_lineEdit.setObjectName("newstuClass_lineEdit")
        self.gridLayout_2.addWidget(self.newstuClass_lineEdit, 3, 1, 1, 1)
        self.newstuFinger_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.newstuFinger_label.setObjectName("newstuFinger_label")
        self.gridLayout_2.addWidget(self.newstuFinger_label, 4, 0, 1, 1)
        self.newstuFinger_combox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.newstuFinger_combox.setObjectName("newstuFinger_combox")
        self.newstuFinger_combox.addItem("")
        self.newstuFinger_combox.addItem("")
        self.newstuFinger_combox.addItem("")
        self.gridLayout_2.addWidget(self.newstuFinger_combox, 4, 1, 1, 1)
        self.newstuName_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.newstuName_lineEdit.setObjectName("newstuName_lineEdit")
        self.gridLayout_2.addWidget(self.newstuName_lineEdit, 1, 1, 1, 1)
        self.newstuClass_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.newstuClass_label.setObjectName("newstuClass_label")
        self.gridLayout_2.addWidget(self.newstuClass_label, 3, 0, 1, 1)
        self.newstuFinger_combox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.newstuFinger_combox_2.setObjectName("newstuFinger_combox_2")
        self.newstuFinger_combox_2.addItem("")
        self.newstuFinger_combox_2.addItem("")
        self.newstuFinger_combox_2.addItem("")
        self.gridLayout_2.addWidget(self.newstuFinger_combox_2, 5, 1, 1, 1)
        self.newstuChoicall_checkbox = QtWidgets.QCheckBox(self.upload_tab)
        self.newstuChoicall_checkbox.setGeometry(QtCore.QRect(340, 460, 87, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newstuChoicall_checkbox.setFont(font)
        self.newstuChoicall_checkbox.setObjectName("newstuChoicall_checkbox")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.upload_tab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(340, 10, 291, 441))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

#~newstu_table######
        self.newstu_tableview = view.View("registerStudent", self.verticalLayoutWidget_6)
        self.newstu_tableview.filter('', '', '', 'All', 'All')
        self.newstu_tableview.setObjectName("newstu_tableview")
        self.verticalLayout_3.addWidget(self.newstu_tableview)
        self.newstu_tabWidget.addTab(self.upload_tab, "")
        self.stackedWidget.addWidget(self.newstu_page)

#ident_page
        self.ident_page = QtWidgets.QWidget()
        self.ident_page.setObjectName("ident_page")
        self.ident_tab = QtWidgets.QTabWidget(self.ident_page)
        self.ident_tab.setGeometry(QtCore.QRect(10, 10, 641, 551))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        self.ident_tab.setFont(font)
        self.ident_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ident_tab.setObjectName("ident_tab")
        self.input_tab = QtWidgets.QWidget()
        self.input_tab.setObjectName("input_tab")
        self.ident_fin_buttn = QtWidgets.QPushButton(self.input_tab)
        self.ident_fin_buttn.setGeometry(QtCore.QRect(520, 470, 113, 32))
        self.ident_fin_buttn.setObjectName("ident_fin_buttn")
        self.ident_idimg = QtWidgets.QLabel(self.input_tab)
        self.ident_idimg.setGeometry(QtCore.QRect(340, 320, 51, 31))
        self.ident_idimg.setObjectName("ident_idimg")
        self.line_3 = QtWidgets.QFrame(self.input_tab)
        self.line_3.setGeometry(QtCore.QRect(160, 10, 16, 231))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(self.input_tab)
        self.line.setGeometry(QtCore.QRect(10, 240, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ident_id_2 = QtWidgets.QLabel(self.input_tab)
        self.ident_id_2.setGeometry(QtCore.QRect(340, 400, 51, 16))
        self.ident_id_2.setObjectName("ident_id_2")
        self.ident_fingerimg = QtWidgets.QLabel(self.input_tab)
        self.ident_fingerimg.setGeometry(QtCore.QRect(340, 180, 91, 121))
        self.ident_fingerimg.setObjectName("ident_fingerimg")
        self.takphoto_buttn = QtWidgets.QPushButton(self.input_tab)
        self.takphoto_buttn.setGeometry(QtCore.QRect(230, 440, 71, 41))
        self.takphoto_buttn.setObjectName("takphoto_buttn")
        self.takphoto_buttn.clicked.connect(sysmainwindow.lihaoTakePhoto)
        self.line_2 = QtWidgets.QFrame(self.input_tab)
        self.line_2.setGeometry(QtCore.QRect(320, 10, 16, 501))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.showname = QtWidgets.QLabel(self.input_tab)
        self.showname.setGeometry(QtCore.QRect(440, 370, 151, 16))
        self.showname.setText("")
        self.showname.setObjectName("showname")
        self.showId = QtWidgets.QLabel(self.input_tab)
        self.showId.setGeometry(QtCore.QRect(440, 400, 151, 16))
        self.showId.setText("")
        self.showId.setObjectName("showId")
        self.ident_idcard = QtWidgets.QLabel(self.input_tab)
        self.ident_idcard.setGeometry(QtCore.QRect(180, 20, 131, 191))
        self.ident_idcard.setObjectName("ident_idcard")
        self.ident_name = QtWidgets.QLabel(self.input_tab)
        self.ident_name.setGeometry(QtCore.QRect(340, 370, 51, 16))
        self.ident_name.setObjectName("ident_name")
        self.ident_clas = QtWidgets.QLabel(self.input_tab)
        self.ident_clas.setGeometry(QtCore.QRect(340, 430, 51, 16))
        self.ident_clas.setObjectName("ident_clas")
        self.showclass = QtWidgets.QLabel(self.input_tab)
        self.showclass.setGeometry(QtCore.QRect(440, 430, 161, 16))
        self.showclass.setText("")
        self.showclass.setObjectName("showclass")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.input_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 270, 251, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.camera_Vlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.camera_Vlayout.setContentsMargins(0, 0, 0, 0)
        self.camera_Vlayout.setObjectName("camera_Vlayout")

        self.viewfinder = QCameraViewfinder(self.verticalLayoutWidget_2)
        self.viewfinder.setObjectName("viewfinder")
        self.lihaoLabel = QLabel("XXX1")
        self.camera_Vlayout.addWidget(self.lihaoLabel)

        self.ident_fingers = QtWidgets.QLabel(self.input_tab)
        self.ident_fingers.setGeometry(QtCore.QRect(20, 20, 131, 211))
        self.ident_fingers.setObjectName("ident_fingers")
        self.ident_photoimg = QtWidgets.QLabel(self.input_tab)
        self.ident_photoimg.setGeometry(QtCore.QRect(340, 20, 91, 131))
        self.ident_photoimg.setObjectName("ident_photoimg")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.input_tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(460, 50, 160, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.same_Vlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.same_Vlayout.setContentsMargins(0, 0, 0, 0)
        self.same_Vlayout.setObjectName("same_Vlayout")
        self.ident_sametext_ph0 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.ident_sametext_ph0.setObjectName("ident_sametext_ph0")
        self.same_Vlayout.addWidget(self.ident_sametext_ph0)
        self.ident_samebar_pho = QtWidgets.QProgressBar(self.verticalLayoutWidget_4)
        self.ident_samebar_pho.setProperty("value", 24)
        self.ident_samebar_pho.setObjectName("ident_samebar_pho")
        self.same_Vlayout.addWidget(self.ident_samebar_pho)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.input_tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(460, 200, 160, 80))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ident_sametext_fin = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.ident_sametext_fin.setObjectName("ident_sametext_fin")
        self.verticalLayout_5.addWidget(self.ident_sametext_fin)
        self.ident_samebar_fin = QtWidgets.QProgressBar(self.verticalLayoutWidget_5)
        self.ident_samebar_fin.setProperty("value", 24)
        self.ident_samebar_fin.setObjectName("ident_samebar_fin")
        self.verticalLayout_5.addWidget(self.ident_samebar_fin)
        self.identNocard_buttn_2 = QtWidgets.QPushButton(self.input_tab)
        self.identNocard_buttn_2.setGeometry(QtCore.QRect(230, 220, 81, 21))
        self.identNocard_buttn_2.setObjectName("identNocard_buttn_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.input_tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.identchoiceexam_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.identchoiceexam_label.setObjectName("identchoiceexam_label")
        self.horizontalLayout_3.addWidget(self.identchoiceexam_label)
        self.identchoiceexam_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.identchoiceexam_comboBox.setObjectName("identchoiceexam_comboBox")
        self.horizontalLayout_3.addWidget(self.identchoiceexam_comboBox)
        self.ident_tab.addTab(self.input_tab, "")

        #ident-upload
        self.Upload_tab = QtWidgets.QWidget()
        self.Upload_tab.setObjectName("Upload_tab")
        self.search_buttn = QtWidgets.QPushButton(self.Upload_tab)
        self.search_buttn.setGeometry(QtCore.QRect(190, 470, 101, 31))
        self.search_buttn.setObjectName("search_buttn")
        self.infosamerate = QtWidgets.QLabel(self.Upload_tab)
        self.infosamerate.setGeometry(QtCore.QRect(510, 40, 60, 16))
        self.infosamerate.setObjectName("infosamerate")
        self.info_samebar = QtWidgets.QProgressBar(self.Upload_tab)
        self.info_samebar.setGeometry(QtCore.QRect(480, 80, 118, 23))
        self.info_samebar.setProperty("value", 24)
        self.info_samebar.setObjectName("info_samebar")
        self.line_4 = QtWidgets.QFrame(self.Upload_tab)
        self.line_4.setGeometry(QtCore.QRect(310, 10, 20, 481))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.info_photo = QtWidgets.QLabel(self.Upload_tab)
        self.info_photo.setGeometry(QtCore.QRect(340, 20, 81, 101))
        self.info_photo.setObjectName("info_photo")
        self.layoutWidget = QtWidgets.QWidget(self.Upload_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 271, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setHorizontalSpacing(8)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.identExamnum_label = QtWidgets.QLabel(self.layoutWidget)
        self.identExamnum_label.setObjectName("identExamnum_label")
        self.gridLayout_5.addWidget(self.identExamnum_label, 1, 0, 1, 1)
        self.identId_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.identId_lineEdit.setMaximumSize(QtCore.QSize(180, 16777215))
        self.identId_lineEdit.setObjectName("identId_lineEdit")
        self.gridLayout_5.addWidget(self.identId_lineEdit, 2, 1, 1, 1)
        self.identId_label = QtWidgets.QLabel(self.layoutWidget)
        self.identId_label.setMaximumSize(QtCore.QSize(65, 16777215))
        self.identId_label.setObjectName("identId_label")
        self.gridLayout_5.addWidget(self.identId_label, 2, 0, 1, 1)
        self.identExamnum_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.identExamnum_comboBox.setObjectName("identExamnum_comboBox")
        self.gridLayout_5.addWidget(self.identExamnum_comboBox, 1, 1, 1, 1)
        self.identName_label = QtWidgets.QLabel(self.layoutWidget)
        self.identName_label.setMaximumSize(QtCore.QSize(65, 16777215))
        self.identName_label.setObjectName("identName_label")
        self.gridLayout_5.addWidget(self.identName_label, 3, 0, 1, 1)
        self.identName_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.identName_lineEdit.setMaximumSize(QtCore.QSize(180, 16777215))
        self.identName_lineEdit.setObjectName("identName_lineEdit")
        self.gridLayout_5.addWidget(self.identName_lineEdit, 3, 1, 1, 1)
        self.identClass_label = QtWidgets.QLabel(self.layoutWidget)
        self.identClass_label.setMaximumSize(QtCore.QSize(65, 16777215))
        self.identClass_label.setObjectName("identClass_label")
        self.gridLayout_5.addWidget(self.identClass_label, 4, 0, 1, 1)
        self.identClass_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.identClass_lineEdit.setMaximumSize(QtCore.QSize(180, 16777215))
        self.identClass_lineEdit.setObjectName("identClass_lineEdit")
        self.gridLayout_5.addWidget(self.identClass_lineEdit, 4, 1, 1, 1)
        self.identFinger_label = QtWidgets.QLabel(self.layoutWidget)
        self.identFinger_label.setMaximumSize(QtCore.QSize(65, 16777215))
        self.identFinger_label.setObjectName("identFinger_label")
        self.gridLayout_5.addWidget(self.identFinger_label, 5, 0, 1, 1)
        self.identFinger_combox = QtWidgets.QComboBox(self.layoutWidget)
        self.identFinger_combox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.identFinger_combox.setObjectName("identFinger_combox")
        self.identFinger_combox.addItem("")
        self.identFinger_combox.addItem("")
        self.identFinger_combox.addItem("")
        self.gridLayout_5.addWidget(self.identFinger_combox, 5, 1, 1, 1)
        self.identFace_label = QtWidgets.QLabel(self.layoutWidget)
        self.identFace_label.setMaximumSize(QtCore.QSize(65, 16777215))
        self.identFace_label.setObjectName("identFace_label")
        self.gridLayout_5.addWidget(self.identFace_label, 6, 0, 1, 1)
        self.identFace_combox = QtWidgets.QComboBox(self.layoutWidget)
        self.identFace_combox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.identFace_combox.setObjectName("identFace_combox")
        self.identFace_combox.addItem("")
        self.identFace_combox.addItem("")
        self.identFace_combox.addItem("")
        self.gridLayout_5.addWidget(self.identFace_combox, 6, 1, 1, 1)
        self.identIC_label = QtWidgets.QLabel(self.layoutWidget)
        self.identIC_label.setMaximumSize(QtCore.QSize(65, 16777215))
        self.identIC_label.setObjectName("identIC_label")
        self.gridLayout_5.addWidget(self.identIC_label, 7, 0, 1, 1)
        self.identIC_combox = QtWidgets.QComboBox(self.layoutWidget)
        self.identIC_combox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.identIC_combox.setObjectName("identIC_combox")
        self.identIC_combox.addItem("")
        self.identIC_combox.addItem("")
        self.identIC_combox.addItem("")
        self.gridLayout_5.addWidget(self.identIC_combox, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 8, 0, 1, 1)
        self.identIsmatch_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.identIsmatch_comboBox.setObjectName("identIsmatch_comboBox")
        self.identIsmatch_comboBox.addItem("")
        self.identIsmatch_comboBox.addItem("")
        self.identIsmatch_comboBox.addItem("")
        self.gridLayout_5.addWidget(self.identIsmatch_comboBox, 8, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 9, 0, 1, 1)
        self.identIsappend_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.identIsappend_comboBox.setObjectName("identIsappend_comboBox")
        self.identIsappend_comboBox.addItem("")
        self.identIsappend_comboBox.addItem("")
        self.identIsappend_comboBox.addItem("")
        self.gridLayout_5.addWidget(self.identIsappend_comboBox, 9, 1, 1, 1)
        self.identUpload_buttn = QtWidgets.QPushButton(self.Upload_tab)
        self.identUpload_buttn.setGeometry(QtCore.QRect(500, 470, 113, 32))
        self.identUpload_buttn.setObjectName("identUpload_buttn")
        self.identChoicall_checkbox = QtWidgets.QCheckBox(self.Upload_tab)
        self.identChoicall_checkbox.setGeometry(QtCore.QRect(340, 470, 87, 20))
        self.identChoicall_checkbox.setObjectName("identChoicall_checkbox")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.Upload_tab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(340, 140, 281, 321))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView = view.View("examRecord", self.verticalLayoutWidget_7)
        self.tableView.filter('', '', '', '', 'All', 'All', 'All', 'All', 'All')
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.ident_tab.addTab(self.Upload_tab, "")
        self.stackedWidget.addWidget(self.ident_page)

        #spk
        self.spk_page = QtWidgets.QWidget()
        self.spk_page.setObjectName("spk_page")
        self.spk_tabWidget = QtWidgets.QTabWidget(self.spk_page)
        self.spk_tabWidget.setGeometry(QtCore.QRect(10, 0, 641, 551))
        self.spk_tabWidget.setObjectName("spk_tabWidget")
        self.input_tab_2 = QtWidgets.QWidget()
        self.input_tab_2.setObjectName("input_tab_2")
        self.spk_stackedWidget = QtWidgets.QStackedWidget(self.input_tab_2)
        self.spk_stackedWidget.setGeometry(QtCore.QRect(90, 70, 481, 321))
        self.spk_stackedWidget.setObjectName("spk_stackedWidget")
        self.sokStart_pages = QtWidgets.QWidget()
        self.sokStart_pages.setObjectName("sokStart_pages")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.sokStart_pages)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 60, 131, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spkStart_buttn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.spkStart_buttn.setObjectName("spkStart_buttn")
        self.verticalLayout_2.addWidget(self.spkStart_buttn)
        self.spkContinue_buttn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.spkContinue_buttn.setObjectName("spkContinue_buttn")
        self.verticalLayout_2.addWidget(self.spkContinue_buttn)
        self.spkEnd_buttn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.spkEnd_buttn.setObjectName("spkEnd_buttn")
        self.verticalLayout_2.addWidget(self.spkEnd_buttn)
        self.spk_stackedWidget.addWidget(self.sokStart_pages)
        self.spkIdcard_page = QtWidgets.QWidget()
        self.spkIdcard_page.setObjectName("spkIdcard_page")
        self.spk_nocard_buttn = QtWidgets.QPushButton(self.spkIdcard_page)
        self.spk_nocard_buttn.setGeometry(QtCore.QRect(380, 280, 101, 32))
        self.spk_nocard_buttn.setObjectName("spk_nocard_buttn")
        self.spk_palcard_label = QtWidgets.QLabel(self.spkIdcard_page)
        self.spk_palcard_label.setGeometry(QtCore.QRect(200, 30, 81, 31))
        self.spk_palcard_label.setObjectName("spk_palcard_label")
        self.spkcard_label = QtWidgets.QLabel(self.spkIdcard_page)
        self.spkcard_label.setGeometry(QtCore.QRect(90, 80, 291, 171))
        self.spkcard_label.setObjectName("spkcard_label")
        self.spk_stackedWidget.addWidget(self.spkIdcard_page)
        self.spkInput_page = QtWidgets.QWidget()
        self.spkInput_page.setObjectName("spkInput_page")
        self.formLayoutWidget = QtWidgets.QWidget(self.spkInput_page)
        self.formLayoutWidget.setGeometry(QtCore.QRect(130, 50, 231, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.spkn_card_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.spkn_card_label.setObjectName("spkn_card_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.spkn_card_label)
        self.spk_name_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.spk_name_lineEdit.setObjectName("spk_name_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spk_name_lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.spkn_id_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.spkn_id_label.setObjectName("spkn_id_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.spkn_id_label)
        self.spkn_id_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.spkn_id_lineEdit.setObjectName("spkn_id_lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spkn_id_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.spkn_class_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.spkn_class_label.setObjectName("spkn_class_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.spkn_class_label)
        self.spkn_class_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.spkn_class_lineEdit.setObjectName("spkn_class_lineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spkn_class_lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.spkBackcard_buttn = QtWidgets.QPushButton(self.spkInput_page)
        self.spkBackcard_buttn.setGeometry(QtCore.QRect(130, 270, 91, 31))
        self.spkBackcard_buttn.setObjectName("spkBackcard_buttn")
        self.spkFinish_buttn = QtWidgets.QPushButton(self.spkInput_page)
        self.spkFinish_buttn.setGeometry(QtCore.QRect(270, 270, 91, 31))
        self.spkFinish_buttn.setObjectName("spkFinish_buttn")
        self.spk_stackedWidget.addWidget(self.spkInput_page)
        self.spkFinish_pages = QtWidgets.QWidget()
        self.spkFinish_pages.setObjectName("spkFinish_pages")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.spkFinish_pages)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(120, 70, 264, 181))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_4.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setContentsMargins(1, 0, 10, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.spkName_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.spkName_label.setObjectName("spkName_label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.spkName_label)
        self.spkshowName_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.spkshowName_label.setMinimumSize(QtCore.QSize(200, 19))
        self.spkshowName_label.setText("")
        self.spkshowName_label.setObjectName("spkshowName_label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spkshowName_label)
        self.spkId_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.spkId_label.setObjectName("spkId_label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.spkId_label)
        self.spkshowId_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.spkshowId_label.setMinimumSize(QtCore.QSize(200, 19))
        self.spkshowId_label.setText("")
        self.spkshowId_label.setObjectName("spkshowId_label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spkshowId_label)
        self.spkClass_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.spkClass_label.setObjectName("spkClass_label")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.spkClass_label)
        self.spkshowClass_label = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.spkshowClass_label.setMinimumSize(QtCore.QSize(200, 19))
        self.spkshowClass_label.setText("")
        self.spkshowClass_label.setObjectName("spkshowClass_label")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spkshowClass_label)
        self.continue_buttn = QtWidgets.QPushButton(self.spkFinish_pages)
        self.continue_buttn.setGeometry(QtCore.QRect(290, 270, 101, 32))
        self.continue_buttn.setObjectName("continue_buttn")
        self.spk_stackedWidget.addWidget(self.spkFinish_pages)
        self.spkSpeechname_pages = QtWidgets.QWidget()
        self.spkSpeechname_pages.setObjectName("spkSpeechname_pages")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.spkSpeechname_pages)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 110, 351, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spkSpeechname_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.spkSpeechname_label.setObjectName("spkSpeechname_label")
        self.horizontalLayout.addWidget(self.spkSpeechname_label)
        self.spkSubmit_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.spkSubmit_lineEdit.setObjectName("spkSubmit_lineEdit")
        self.horizontalLayout.addWidget(self.spkSubmit_lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.spkSpeechname_pages)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 160, 351, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spkSpeechroom_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.spkSpeechroom_label.setObjectName("spkSpeechroom_label")
        self.horizontalLayout_2.addWidget(self.spkSpeechroom_label)
        self.spkSubmitroom_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.spkSubmitroom_lineEdit.setObjectName("spkSubmitroom_lineEdit")
        self.horizontalLayout_2.addWidget(self.spkSubmitroom_lineEdit)
        self.spkSubmit_buttn = QtWidgets.QPushButton(self.spkSpeechname_pages)
        self.spkSubmit_buttn.setGeometry(QtCore.QRect(360, 220, 60, 21))
        self.spkSubmit_buttn.setMinimumSize(QtCore.QSize(60, 19))
        self.spkSubmit_buttn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spkSubmit_buttn.setObjectName("spkSubmit_buttn")
        self.spk_stackedWidget.addWidget(self.spkSpeechname_pages)
        self.spkHome_buttn = QtWidgets.QPushButton(self.input_tab_2)
        self.spkHome_buttn.setGeometry(QtCore.QRect(80, 40, 31, 31))
        self.spkHome_buttn.setObjectName("spkHome_buttn")
        self.spkCurspeech_label = QtWidgets.QLabel(self.input_tab_2)
        self.spkCurspeech_label.setGeometry(QtCore.QRect(70, 10, 541, 16))
        self.spkCurspeech_label.setText("")
        self.spkCurspeech_label.setObjectName("spkCurspeech_label")
        self.spk_tabWidget.addTab(self.input_tab_2, "")


        #spk-uoload

        self.upload_tab_2 = QtWidgets.QWidget()
        self.upload_tab_2.setObjectName("upload_tab_2")
        self.spkUpload_buttn = QtWidgets.QPushButton(self.upload_tab_2)
        self.spkUpload_buttn.setGeometry(QtCore.QRect(500, 480, 113, 32))
        self.spkUpload_buttn.setObjectName("spkUpload_buttn")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.upload_tab_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 160, 291, 171))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spkspeechName_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.spkspeechName_label.setObjectName("spkspeechName_label")
        self.gridLayout_3.addWidget(self.spkspeechName_label, 0, 0, 1, 1)
        self.spkspeech_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.spkspeech_lineEdit.setObjectName("spkspeech_lineEdit")
        self.gridLayout_3.addWidget(self.spkspeech_lineEdit, 0, 1, 1, 2)
        self.spkFind_buttn = QtWidgets.QPushButton(self.upload_tab_2)
        self.spkFind_buttn.setGeometry(QtCore.QRect(210, 340, 93, 19))
        self.spkFind_buttn.setObjectName("spkFind_buttn")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.upload_tab_2)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(330, 10, 291, 461))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.spk_tableView = view.View("speechSpeech", self.verticalLayoutWidget_9)
        self.spk_tableView.filter('')
        self.spk_tableView.setObjectName("spk_tableView")
        self.verticalLayout_7.addWidget(self.spk_tableView)
        self.spk_tabWidget.addTab(self.upload_tab_2, "")
        self.stackedWidget.addWidget(self.spk_page)


        #updata
        self.updata_page = QtWidgets.QWidget()
        self.updata_page.setObjectName("updata_page")
        self.updata_tabWidget = QtWidgets.QTabWidget(self.updata_page)
        self.updata_tabWidget.setGeometry(QtCore.QRect(10, 10, 641, 541))
        self.updata_tabWidget.setObjectName("updata_tabWidget")
        self.updata_exam = QtWidgets.QWidget()
        self.updata_exam.setObjectName("updata_exam")
        self.upexamAll_checkBox = QtWidgets.QCheckBox(self.updata_exam)
        self.upexamAll_checkBox.setGeometry(QtCore.QRect(30, 470, 87, 20))
        self.upexamAll_checkBox.setObjectName("upexamAll_checkBox")
        self.upexam_buttn = QtWidgets.QPushButton(self.updata_exam)
        self.upexam_buttn.setGeometry(QtCore.QRect(480, 470, 131, 21))
        self.upexam_buttn.setObjectName("upexam_buttn")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.updata_exam)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(30, 20, 581, 431))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.upexam_tableView = QtWidgets.QTableView(self.verticalLayoutWidget_11)
        self.upexam_tableView = view.View("examExamServer", self.verticalLayoutWidget_11)
        self.upexam_tableView.filter('', '', '', '')
        self.upexam_tableView.setObjectName("upexam_tableView")
        self.verticalLayout_9.addWidget(self.upexam_tableView)
        self.updata_tabWidget.addTab(self.updata_exam, "")
        self.updata_user = QtWidgets.QWidget()
        self.updata_user.setObjectName("updata_user")
        self.updata_user_2 = QtWidgets.QPushButton(self.updata_user)
        self.updata_user_2.setGeometry(QtCore.QRect(60, 20, 151, 21))
        self.updata_user_2.setObjectName("updata_user_2")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.updata_user)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(60, 50, 551, 431))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.updata_tableView = view.View("loginUser", self.verticalLayoutWidget_10)
        self.updata_tableView.filter()
        self.updata_tableView.setObjectName("updata_tableView")
        self.verticalLayout_8.addWidget(self.updata_tableView)
        self.updata_tabWidget.addTab(self.updata_user, "")
        self.updata_delete = QtWidgets.QWidget()
        self.updata_delete.setObjectName("updata_delete")
        self.updatadelect_buttn = QtWidgets.QPushButton(self.updata_delete)
        self.updatadelect_buttn.setGeometry(QtCore.QRect(250, 180, 151, 32))
        self.updatadelect_buttn.setObjectName("updatadelect_buttn")
        self.updataDeiniti_buttn = QtWidgets.QPushButton(self.updata_delete)
        self.updataDeiniti_buttn.setGeometry(QtCore.QRect(250, 250, 151, 31))
        self.updataDeiniti_buttn.setObjectName("updataDeiniti_buttn")
        self.updata_tabWidget.addTab(self.updata_delete, "")
        self.stackedWidget.addWidget(self.updata_page)
    #log
        self.log_page6 = QtWidgets.QWidget()
        self.log_page6.setObjectName("log_page6")
        self.textBrowser = QtWidgets.QTextBrowser(self.log_page6)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 611, 511))
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.log_page6)

        #newtea
        self.newtea_page = QtWidgets.QWidget()
        self.newtea_page.setObjectName("newtea_page")
        self.newtea_tabWidget = QtWidgets.QTabWidget(self.newtea_page)
        self.newtea_tabWidget.setGeometry(QtCore.QRect(10, 0, 631, 571))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        self.newtea_tabWidget.setFont(font)
        self.newtea_tabWidget.setObjectName("newtea_tabWidget")
        self.inputinfo = QtWidgets.QWidget()
        self.inputinfo.setObjectName("inputinfo")
        self.newtea_stackedWidget = QtWidgets.QStackedWidget(self.inputinfo)
        self.newtea_stackedWidget.setGeometry(QtCore.QRect(150, 130, 341, 241))
        self.newtea_stackedWidget.setObjectName("newtea_stackedWidget")
        self.card = QtWidgets.QWidget()
        self.card.setObjectName("card")
        self.nocard_buttn = QtWidgets.QLabel(self.card)
        self.nocard_buttn.setGeometry(QtCore.QRect(20, 20, 291, 171))
        self.nocard_buttn.setObjectName("nocard_buttn")
        self.newtea_card = QtWidgets.QPushButton(self.card)
        self.newtea_card.setGeometry(QtCore.QRect(260, 210, 71, 21))
        self.newtea_card.setObjectName("newtea_card")
        self.newtea_stackedWidget.addWidget(self.card)
        self.input = QtWidgets.QWidget()
        self.input.setObjectName("input")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.input)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(90, 70, 181, 85))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.name_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.name_label.setObjectName("name_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.passwd_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.passwd_label.setObjectName("passwd_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwd_label)
        self.secpasswd_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.secpasswd_label.setObjectName("secpasswd_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.secpasswd_label)
        self.name_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.pass_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pass_lineEdit)
        self.secpasswd_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.secpasswd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secpasswd_lineEdit.setObjectName("secpasswd_lineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.secpasswd_lineEdit)
        self.ok_buttn = QtWidgets.QPushButton(self.input)
        self.ok_buttn.setGeometry(QtCore.QRect(210, 180, 81, 21))
        self.ok_buttn.setObjectName("ok_buttn")
        self.newteaback_buttn = QtWidgets.QPushButton(self.input)
        self.newteaback_buttn.setGeometry(QtCore.QRect(80, 180, 81, 21))
        self.newteaback_buttn.setObjectName("newteaback_buttn")
        self.newtea_stackedWidget.addWidget(self.input)
        self.success = QtWidgets.QWidget()
        self.success.setObjectName("success")
        self.newteaSuccess_buttn = QtWidgets.QPushButton(self.success)
        self.newteaSuccess_buttn.setGeometry(QtCore.QRect(120, 70, 101, 101))
        self.newteaSuccess_buttn.setText("")
        self.newteaSuccess_buttn.setObjectName("newteaSuccess_buttn")
        self.newtea_stackedWidget.addWidget(self.success)
        self.newtea_tabWidget.addTab(self.inputinfo, "")

        #newtea-upload
        self.uploadinfo = QtWidgets.QWidget()
        self.uploadinfo.setObjectName("uploadinfo")
        self.newteaupload_buttn = QtWidgets.QPushButton(self.uploadinfo)
        self.newteaupload_buttn.setGeometry(QtCore.QRect(520, 440, 101, 31))
        self.newteaupload_buttn.setObjectName("newteaupload_buttn")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.uploadinfo)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(30, 30, 591, 401))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.newtea_tableView = view.View("loginUserAdd", self.verticalLayoutWidget_8)
        self.newtea_tableView.filter(24)
        self.newtea_tableView.selectAll()
        self.newtea_tableView.setObjectName("newtea_tableView")
        self.verticalLayout_6.addWidget(self.newtea_tableView)
        self.newtea_tabWidget.addTab(self.uploadinfo, "")
        self.stackedWidget.addWidget(self.newtea_page)

        #newoff
        self.newoff_page = QtWidgets.QWidget()
        self.newoff_page.setObjectName("newoff_page")
        self.newoff_TabWeiget = QtWidgets.QTabWidget(self.newoff_page)
        self.newoff_TabWeiget.setGeometry(QtCore.QRect(10, 0, 641, 541))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        self.newoff_TabWeiget.setFont(font)
        self.newoff_TabWeiget.setObjectName("newoff_TabWeiget")
        self.inputinfo_2 = QtWidgets.QWidget()
        self.inputinfo_2.setObjectName("inputinfo_2")
        self.newoff_stackedWidget = QtWidgets.QStackedWidget(self.inputinfo_2)
        self.newoff_stackedWidget.setGeometry(QtCore.QRect(150, 130, 341, 241))
        self.newoff_stackedWidget.setObjectName("newoff_stackedWidget")
        self.card_2 = QtWidgets.QWidget()
        self.card_2.setObjectName("card_2")
        self.nocard_buttn_2 = QtWidgets.QLabel(self.card_2)
        self.nocard_buttn_2.setGeometry(QtCore.QRect(20, 20, 291, 171))
        self.nocard_buttn_2.setObjectName("nocard_buttn_2")
        self.newoff_card = QtWidgets.QPushButton(self.card_2)
        self.newoff_card.setGeometry(QtCore.QRect(260, 210, 71, 21))
        self.newoff_card.setObjectName("newoff_card")
        self.newoff_stackedWidget.addWidget(self.card_2)
        self.input_2 = QtWidgets.QWidget()
        self.input_2.setObjectName("input_2")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.input_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(90, 70, 181, 85))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.name_label_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.name_label_2.setObjectName("name_label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label_2)
        self.passwd_label_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.passwd_label_2.setObjectName("passwd_label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwd_label_2)
        self.secpasswd_label_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.secpasswd_label_2.setObjectName("secpasswd_label_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.secpasswd_label_2)
        self.name_lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.name_lineEdit_2.setObjectName("name_lineEdit_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit_2)
        self.pass_lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.pass_lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit_2.setObjectName("pass_lineEdit_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pass_lineEdit_2)
        self.secpasswd_lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.secpasswd_lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secpasswd_lineEdit_2.setObjectName("secpasswd_lineEdit_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.secpasswd_lineEdit_2)
        self.newoffok_buttn = QtWidgets.QPushButton(self.input_2)
        self.newoffok_buttn.setGeometry(QtCore.QRect(210, 180, 81, 21))
        self.newoffok_buttn.setObjectName("newoffok_buttn")
        self.newoffback_buttn_2 = QtWidgets.QPushButton(self.input_2)
        self.newoffback_buttn_2.setGeometry(QtCore.QRect(70, 180, 81, 21))
        self.newoffback_buttn_2.setObjectName("newoffback_buttn_2")
        self.newoff_stackedWidget.addWidget(self.input_2)
        self.success_2 = QtWidgets.QWidget()
        self.success_2.setObjectName("success_2")
        self.newoffSuccess_buttn = QtWidgets.QPushButton(self.success_2)
        self.newoffSuccess_buttn.setGeometry(QtCore.QRect(120, 70, 101, 101))
        self.newoffSuccess_buttn.setText("")
        self.newoffSuccess_buttn.setAutoDefault(False)
        self.newoffSuccess_buttn.setDefault(False)
        self.newoffSuccess_buttn.setFlat(False)
        self.newoffSuccess_buttn.setObjectName("newoffSuccess_buttn")
        self.newoff_stackedWidget.addWidget(self.success_2)
        self.newoff_TabWeiget.addTab(self.inputinfo_2, "")

        #newoff-upload
        self.uploadinfo_2 = QtWidgets.QWidget()
        self.uploadinfo_2.setObjectName("uploadinfo_2")
        self.newoffupload_buttn = QtWidgets.QPushButton(self.uploadinfo_2)
        self.newoffupload_buttn.setGeometry(QtCore.QRect(520, 440, 101, 31))
        self.newoffupload_buttn.setObjectName("newoffupload_buttn")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.uploadinfo_2)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(30, 30, 591, 401))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.newoff_tableView = view.View("loginUserAdd", self.verticalLayoutWidget_12)
        self.newoff_tableView.filter(35)
        self.newoff_tableView.selectAll()
        self.newoff_tableView.setObjectName("newoff_tableView")
        self.verticalLayout_10.addWidget(self.newoff_tableView)
        self.newoff_TabWeiget.addTab(self.uploadinfo_2, "")
        self.stackedWidget.addWidget(self.newoff_page)

        #menu
        self.menu = QtWidgets.QWidget(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 0, 141, 461))
        self.menu.setStyleSheet("")
        self.menu.setObjectName("menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout.setContentsMargins(0, 11, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.Newstu_buttn = QtWidgets.QPushButton(self.menu)
        self.Newstu_buttn.setStyleSheet("")
        self.Newstu_buttn.clicked.connect(self.lihaoFunc)
        self.Newstu_buttn.setObjectName("Newstu_buttn")
        self.verticalLayout.addWidget(self.Newstu_buttn)
        self.Updata_buttn = QtWidgets.QPushButton(self.menu)
        self.Updata_buttn.setObjectName("Updata_buttn")
        self.verticalLayout.addWidget(self.Updata_buttn)
        self.Ident_buttn = QtWidgets.QPushButton(self.menu)
        self.Ident_buttn.setStyleSheet("")
        self.Ident_buttn.clicked.connect(self.lihaoFunc2)
        self.Ident_buttn.setObjectName("Ident_buttn")
        self.verticalLayout.addWidget(self.Ident_buttn)
        self.Spk_buttn = QtWidgets.QPushButton(self.menu)
        self.Spk_buttn.setStyleSheet("")
        self.Spk_buttn.setObjectName("Spk_buttn")
        self.verticalLayout.addWidget(self.Spk_buttn)
        self.Teach_buttn = QtWidgets.QPushButton(self.menu)
        self.Teach_buttn.setObjectName("Teach_buttn")
        self.verticalLayout.addWidget(self.Teach_buttn)
        self.Offic_buttn = QtWidgets.QPushButton(self.menu)
        self.Offic_buttn.setObjectName("Offic_buttn")
        self.verticalLayout.addWidget(self.Offic_buttn)
        self.Log_buttn = QtWidgets.QPushButton(self.menu)
        self.Log_buttn.setObjectName("Log_buttn")
        self.verticalLayout.addWidget(self.Log_buttn)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.close_buttn = QtWidgets.QPushButton(self.centralwidget)
        self.close_buttn.setGeometry(QtCore.QRect(776, 3, 21, 21))
        self.close_buttn.setText("")
        self.close_buttn.setObjectName("close_buttn")
        self.mini_buttn = QtWidgets.QPushButton(self.centralwidget)
        self.mini_buttn.setGeometry(QtCore.QRect(755, 3, 21, 21))
        self.mini_buttn.setText("")
        self.mini_buttn.setObjectName("mini_buttn")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(140, 0, 661, 581))
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.stackedWidget.raise_()
        self.menu.raise_()
        self.welcome_label.raise_()
        self.close_buttn.raise_()
        self.mini_buttn.raise_()

        self.text_widget = QtWidgets.QWidget(self.centralwidget)
        self.text_widget.setGeometry(QtCore.QRect(0, 460, 141, 141))
        self.text_widget.setObjectName("text_widget")
        self.text_label = QtWidgets.QLabel(self.text_widget)
        self.text_label.setGeometry(QtCore.QRect(0, 0, 141, 141))
        self.text_label.setStyleSheet("QLabel#text_label\n"
                                      "{\n"
                                      "background-color:rgb(49,54,61);\n"
                                      "}")
        self.text_label.setText("")
        self.text_label.setObjectName("text_label")
        sysmainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(sysmainwindow)
        self.stackedWidget.setCurrentIndex(0)
        self.newstu_tabWidget.setCurrentIndex(0)
        self.ident_tab.setCurrentIndex(0)
        self.spk_tabWidget.setCurrentIndex(0)
        self.spk_stackedWidget.setCurrentIndex(0)
        self.newtea_tabWidget.setCurrentIndex(0)
        self.newtea_stackedWidget.setCurrentIndex(0)
        self.newoff_TabWeiget.setCurrentIndex(0)
        self.newoff_stackedWidget.setCurrentIndex(0)
        self.updata_tabWidget.setCurrentIndex(0)

        ##################信号槽###################
        # self.Newstu_buttn.pressed.connect(sysmainwindow.stopcamera)
        # self.Ident_buttn.pressed.connect(sysmainwindow.stopcamera)
        # self.Log_buttn.pressed.connect(sysmainwindow.stopcamera)
        # self.Offic_buttn.pressed.connect(sysmainwindow.stopcamera)
        # self.Spk_buttn.pressed.connect(sysmainwindow.stopcamera)
        # self.Teach_buttn.pressed.connect(sysmainwindow.stopcamera)
        # self.Updata_buttn.pressed.connect(sysmainwindow.stopcamera)
        
        self.mini_buttn.clicked.connect(sysmainwindow.minimize)
        self.close_buttn.clicked.connect(sysmainwindow.closewindow)

        self.Ident_buttn.clicked.connect(sysmainwindow.idenshow)
        self.Spk_buttn.clicked.connect(sysmainwindow.spkshow)
        self.Updata_buttn.clicked.connect(sysmainwindow.updatashow)
        self.Newstu_buttn.clicked.connect(sysmainwindow.newstushow)
        self.Log_buttn.clicked.connect(sysmainwindow.logshow)
        self.Teach_buttn.clicked.connect(sysmainwindow.teashow)
        self.Offic_buttn.clicked.connect(sysmainwindow.offshow)
        # self.takphoto_buttn.clicked.connect(sysmainwindow.captureImage)
        # self.takphoto_buttn_2.clicked.connect(sysmainwindow.captureImage)

        self.identNocard_buttn_2.clicked.connect(sysmainwindow.shownew_ident)
        self.stu_nocard_buttn.clicked.connect(sysmainwindow.shownew_newstu)

        self.newstuLook_buttn.clicked.connect(sysmainwindow.newstuFind)
        self.newstuUpload_buttn.clicked.connect(sysmainwindow.newstuUpload)
        self.newstuChoicall_checkbox.clicked.connect(sysmainwindow.newstuChoicall)

        self.search_buttn.clicked.connect(sysmainwindow.identFind)
        self.identUpload_buttn.clicked.connect(sysmainwindow.identUpload)
        self.identChoicall_checkbox.clicked.connect(sysmainwindow.identChoicall)

        self.newtea_card.clicked.connect(sysmainwindow.newtea_nocard)
        self.newoff_card.clicked.connect(sysmainwindow.newoff_nocard)

        self.stu_fin_buttn.clicked.connect(sysmainwindow.finish_stu)
        self.ident_fin_buttn.clicked.connect(sysmainwindow.finish_ident)

        self.ok_buttn.clicked.connect(sysmainwindow.tea_success)
        self.newoffok_buttn.clicked.connect(sysmainwindow.off_success)

        self.spkStart_buttn.clicked.connect(sysmainwindow.spkstart)
        self.spkSubmit_buttn.clicked.connect(sysmainwindow.submitSpeechname)
        self.spkContinue_buttn.clicked.connect(sysmainwindow.spkcon)
        self.continue_buttn.clicked.connect(sysmainwindow.spkDB)
        self.spkEnd_buttn.clicked.connect(sysmainwindow.spkend)
        self.spkFinish_buttn.clicked.connect(sysmainwindow.spksubmitinfo)
        self.spkHome_buttn.clicked.connect(sysmainwindow.spkbackhome)
        self.spkBackcard_buttn.clicked.connect(sysmainwindow.spkback)
        self.spk_nocard_buttn.clicked.connect(sysmainwindow.spkNocard)
        self.spkFind_buttn.clicked.connect(sysmainwindow.spkFind)
        self.spkUpload_buttn.clicked.connect(sysmainwindow.spkUpload)

        self.newteaSuccess_buttn.clicked.connect(sysmainwindow.newteacontinue)
        self.newoffSuccess_buttn.clicked.connect(sysmainwindow.newoffcontinue)
        self.newteaback_buttn.clicked.connect(sysmainwindow.newteacontinue)
        self.newoffback_buttn_2.clicked.connect(sysmainwindow.newoffcontinue)
        self.newteaupload_buttn.clicked.connect(sysmainwindow.newteaUpload)
        self.newoffupload_buttn.clicked.connect(sysmainwindow.newoffUpload)

        self.upexam_buttn.clicked.connect(sysmainwindow.updataUpeaxm)
        self.updata_user_2.clicked.connect(sysmainwindow.updataUpuser)
        self.updatadelect_buttn.clicked.connect(sysmainwindow.updataDel)
        self.upexamAll_checkBox.clicked.connect(sysmainwindow.upexamAll)
        self.updataDeiniti_buttn.clicked.connect(sysmainwindow.resertAll)

        ######自定义信号槽#########
        #self.showId.setText.connect(sysmainwindow.changestuid)

        #self.upload_tab.ifshow.connect(sysmainwindow.newstutableview)

        self.spkHome_buttn.setToolTip("返回至'开始新讲座'、'继续当前讲座'、'结束当前讲座'界面")
        self.newstu_tableview.clicked.connect(sysmainwindow.new_showphoto)
        self.tableView.clicked.connect(sysmainwindow.ident_showphoto)

        QtCore.QMetaObject.connectSlotsByName(sysmainwindow)



    def retranslateUi(self, sysmainwindow):
        _translate = QtCore.QCoreApplication.translate
        sysmainwindow.setWindowTitle(_translate("sysmainwindow", "MainWindow"))
        self.stu_idcard.setText(_translate("sysmainwindow", "idcard"))
        self.stu_id.setText(_translate("sysmainwindow", "学     号"))
        self.stu_name.setText(_translate("sysmainwindow", "姓     名"))
        self.stu_fingers.setText(_translate("sysmainwindow", "finger"))
        self.stu_photoimg.setText(_translate("sysmainwindow", "photo"))
        self.stu_idimg.setText(_translate("sysmainwindow", "IDcard"))
        self.stu_fingerimg.setText(_translate("sysmainwindow", "finger"))
        self.takphoto_buttn_2.setText(_translate("sysmainwindow", "拍照2"))
        self.stu_fin_buttn.setText(_translate("sysmainwindow", "完成录入"))
        self.stu_clas.setText(_translate("sysmainwindow", "班     级"))
        self.stu_nocard_buttn.setText(_translate("sysmainwindow", "无学生卡"))
        self.pissucc_label.setText(_translate("sysmainwindow", "is_sucess"))
        self.fissucc_label.setText(_translate("sysmainwindow", "is_sucess"))
        self.newstu_tabWidget.setTabText(self.newstu_tabWidget.indexOf(self.register_tab),
                                         _translate("sysmainwindow", "录入"))
        self.newstuLook_buttn.setText(_translate("sysmainwindow", "查找"))
        self.newstuUpload_buttn.setText(_translate("sysmainwindow", "上传"))
        self.newstuPhotoimg_label.setText(_translate("sysmainwindow", "photo"))
        self.newstuId_label.setText(_translate("sysmainwindow", "学号"))
        self.newstuName_label.setText(_translate("sysmainwindow", "姓名"))
        self.newstuFace_label.setText(_translate("sysmainwindow", "是否录入照片"))
        self.newstuFinger_label.setText(_translate("sysmainwindow", "是否录入指纹"))
        self.newstuFinger_combox.setItemText(0, _translate("sysmainwindow", "All"))
        self.newstuFinger_combox.setItemText(1, _translate("sysmainwindow", "False"))
        self.newstuFinger_combox.setItemText(2, _translate("sysmainwindow", "True"))
        self.newstuClass_label.setText(_translate("sysmainwindow", "班级"))
        self.newstuFinger_combox_2.setItemText(0, _translate("sysmainwindow", "All"))
        self.newstuFinger_combox_2.setItemText(1, _translate("sysmainwindow", "False"))
        self.newstuFinger_combox_2.setItemText(2, _translate("sysmainwindow", "True"))
        self.newstuChoicall_checkbox.setText(_translate("sysmainwindow", "全选"))
        self.newstu_tabWidget.setTabText(self.newstu_tabWidget.indexOf(self.upload_tab),
                                         _translate("sysmainwindow", "上传"))
        self.ident_fin_buttn.setText(_translate("sysmainwindow", "完成录入"))
        self.ident_idimg.setText(_translate("sysmainwindow", "IDcard"))
        self.ident_id_2.setText(_translate("sysmainwindow", "学     号"))
        self.ident_fingerimg.setText(_translate("sysmainwindow", "finger"))
        self.takphoto_buttn.setText(_translate("sysmainwindow", "拍照1"))
        self.ident_idcard.setText(_translate("sysmainwindow", "idcard"))
        self.ident_name.setText(_translate("sysmainwindow", "姓     名"))
        self.ident_clas.setText(_translate("sysmainwindow", "班     级"))
        self.ident_fingers.setText(_translate("sysmainwindow", "finger"))
        self.ident_photoimg.setText(_translate("sysmainwindow", "photo"))
        self.ident_sametext_ph0.setText(_translate("sysmainwindow", "匹配程度"))
        self.ident_sametext_fin.setText(_translate("sysmainwindow", "匹配程度"))
        self.identNocard_buttn_2.setText(_translate("sysmainwindow", "无学生卡"))
        self.identchoiceexam_label.setText(_translate("sysmainwindow", "请选择考场"))
        self.ident_tab.setTabText(self.ident_tab.indexOf(self.input_tab), _translate("sysmainwindow", "身份比对"))
        self.search_buttn.setText(_translate("sysmainwindow", "查找"))
        self.infosamerate.setText(_translate("sysmainwindow", "匹配程度"))
        self.info_photo.setText(_translate("sysmainwindow", "photo"))
        self.identExamnum_label.setText(_translate("sysmainwindow", "考场号"))
        self.identId_label.setText(_translate("sysmainwindow", "学号"))
        self.identName_label.setText(_translate("sysmainwindow", "姓名"))
        self.identClass_label.setText(_translate("sysmainwindow", "班级"))
        self.identFinger_label.setText(_translate("sysmainwindow", "是否有指纹"))
        self.identFinger_combox.setItemText(0, _translate("sysmainwindow", "All"))
        self.identFinger_combox.setItemText(1, _translate("sysmainwindow", "False"))
        self.identFinger_combox.setItemText(2, _translate("sysmainwindow", "True"))
        self.identFace_label.setText(_translate("sysmainwindow", "是否有照片"))
        self.identFace_combox.setItemText(0, _translate("sysmainwindow", "All"))
        self.identFace_combox.setItemText(1, _translate("sysmainwindow", "False"))
        self.identFace_combox.setItemText(2, _translate("sysmainwindow", "True"))
        self.identIC_label.setText(_translate("sysmainwindow", "是否有IC卡"))
        self.identIC_combox.setItemText(0, _translate("sysmainwindow", "All"))
        self.identIC_combox.setItemText(1, _translate("sysmainwindow", "False"))
        self.identIC_combox.setItemText(2, _translate("sysmainwindow", "True"))
        self.label.setText(_translate("sysmainwindow", "是否比对成功"))
        self.identIsmatch_comboBox.setItemText(0, _translate("sysmainwindow", "All"))
        self.identIsmatch_comboBox.setItemText(1, _translate("sysmainwindow", "False"))
        self.identIsmatch_comboBox.setItemText(2, _translate("sysmainwindow", "True"))
        self.label_2.setText(_translate("sysmainwindow", "是否为考场考生"))
        self.identIsappend_comboBox.setItemText(0, _translate("sysmainwindow", "All"))
        self.identIsappend_comboBox.setItemText(1, _translate("sysmainwindow", "False"))
        self.identIsappend_comboBox.setItemText(2, _translate("sysmainwindow", "True"))
        self.identUpload_buttn.setText(_translate("sysmainwindow", "上传"))
        self.identChoicall_checkbox.setText(_translate("sysmainwindow", "全选"))
        self.ident_tab.setTabText(self.ident_tab.indexOf(self.Upload_tab), _translate("sysmainwindow", "数据上传"))
        self.spkStart_buttn.setText(_translate("sysmainwindow", "开启新讲座"))
        self.spkContinue_buttn.setText(_translate("sysmainwindow", "继续当前讲座"))
        self.spkEnd_buttn.setText(_translate("sysmainwindow", "结束当前讲座"))
        self.spk_nocard_buttn.setText(_translate("sysmainwindow", "无学生卡登记"))
        self.spk_palcard_label.setText(_translate("sysmainwindow", "请放置学生卡"))
        self.spkcard_label.setText(_translate("sysmainwindow", "card"))
        self.spkn_card_label.setText(_translate("sysmainwindow", "姓名"))
        self.spkn_id_label.setText(_translate("sysmainwindow", "学号"))
        self.spkn_class_label.setText(_translate("sysmainwindow", "班级"))
        self.spkBackcard_buttn.setText(_translate("sysmainwindow", "返回刷卡页面"))
        self.spkFinish_buttn.setText(_translate("sysmainwindow", "完成录入"))
        self.spkName_label.setText(_translate("sysmainwindow", "姓   名:"))
        self.spkId_label.setText(_translate("sysmainwindow", "学   号:"))
        self.spkClass_label.setText(_translate("sysmainwindow", "班   级:"))
        self.continue_buttn.setText(_translate("sysmainwindow", "继续录入"))
        self.spkSpeechname_label.setText(_translate("sysmainwindow", "请输入讲座名称"))
        self.spkSpeechroom_label.setText(_translate("sysmainwindow", "请输入进行讲座的教室"))
        self.spkSubmit_buttn.setText(_translate("sysmainwindow", "提交"))
        self.spk_tabWidget.setTabText(self.spk_tabWidget.indexOf(self.input_tab_2), _translate("sysmainwindow", "讲座签到"))
        self.spkUpload_buttn.setText(_translate("sysmainwindow", "上传"))
        self.spkspeechName_label.setText(_translate("sysmainwindow", "讲座名称"))
        self.spkFind_buttn.setText(_translate("sysmainwindow", "查找"))
        self.spk_tabWidget.setTabText(self.spk_tabWidget.indexOf(self.upload_tab_2),
                                      _translate("sysmainwindow", "上传数据"))
        self.upexamAll_checkBox.setText(_translate("sysmainwindow", "全选"))
        self.upexam_buttn.setText(_translate("sysmainwindow", "下载到本地数据库"))
        self.updata_tabWidget.setTabText(self.updata_tabWidget.indexOf(self.updata_exam),
                                         _translate("sysmainwindow", "下载考场信息"))
        self.updata_user_2.setText(_translate("sysmainwindow", "更新本地所有用户数据"))
        self.updata_tabWidget.setTabText(self.updata_tabWidget.indexOf(self.updata_user),
                                         _translate("sysmainwindow", "下载用户信息"))
        self.updatadelect_buttn.setText(_translate("sysmainwindow", "一键清除本机存储数据"))
        self.updataDeiniti_buttn.setText(_translate("sysmainwindow", "恢复出厂设置"))
        self.updata_tabWidget.setTabText(self.updata_tabWidget.indexOf(self.updata_delete),
                                         _translate("sysmainwindow", "清除本机数据"))
        self.nocard_buttn.setText(_translate("sysmainwindow", "card"))
        self.newtea_card.setText(_translate("sysmainwindow", "无职工卡"))
        self.name_label.setText(_translate("sysmainwindow", "用  户  名"))
        self.passwd_label.setText(_translate("sysmainwindow", "密        码"))
        self.secpasswd_label.setText(_translate("sysmainwindow", "确认密码"))
        self.ok_buttn.setText(_translate("sysmainwindow", "确定"))
        self.newteaback_buttn.setText(_translate("sysmainwindow", "返回刷卡"))
        self.newtea_tabWidget.setTabText(self.newtea_tabWidget.indexOf(self.inputinfo),
                                         _translate("sysmainwindow", "录入"))
        self.newteaupload_buttn.setText(_translate("sysmainwindow", "上传"))
        self.newtea_tabWidget.setTabText(self.newtea_tabWidget.indexOf(self.uploadinfo),
                                         _translate("sysmainwindow", "上传"))
        self.nocard_buttn_2.setText(_translate("sysmainwindow", "card"))
        self.newoff_card.setText(_translate("sysmainwindow", "无职工卡"))
        self.name_label_2.setText(_translate("sysmainwindow", "用  户  名"))
        self.passwd_label_2.setText(_translate("sysmainwindow", "密        码"))
        self.secpasswd_label_2.setText(_translate("sysmainwindow", "确认密码"))
        self.newoffok_buttn.setText(_translate("sysmainwindow", "确认"))
        self.newoffback_buttn_2.setText(_translate("sysmainwindow", "返回刷卡"))
        self.newoff_TabWeiget.setTabText(self.newoff_TabWeiget.indexOf(self.inputinfo_2),
                                         _translate("sysmainwindow", "录入"))
        self.newoffupload_buttn.setText(_translate("sysmainwindow", "上传"))
        self.newoff_TabWeiget.setTabText(self.newoff_TabWeiget.indexOf(self.uploadinfo_2),
                                         _translate("sysmainwindow", "上传"))
        self.Newstu_buttn.setText(_translate("sysmainwindow", "新生注册"))
        self.Updata_buttn.setText(_translate("sysmainwindow", "数据更新"))
        self.Ident_buttn.setText(_translate("sysmainwindow", "监考模式"))
        self.Spk_buttn.setText(_translate("sysmainwindow", "讲座模式"))
        self.Teach_buttn.setText(_translate("sysmainwindow", "认证教师"))
        self.Offic_buttn.setText(_translate("sysmainwindow", "认证管理员"))
        self.Log_buttn.setText(_translate("sysmainwindow", "查看日志文件"))

    def lihaoViewCam(self):
        if self.lihaoTabIndex == 2:
            ret,self.image0 = self.cap.read()#从摄像头读取图片
            self.image = cv2.cvtColor(self.image0,cv2.COLOR_BGR2RGB)#格式转换
            height,width,channel = self.image.shape#获取图片大小
            step = channel * width #更具图片大小获得step
            qImg = QImage(self.image.data, width,height,step,QImage.Format_RGB888)#根据图片大小产生QImage
            self.lihaoLabel.setPixmap(QPixmap.fromImage(qImg));print("0")#显示图片
        elif self.lihaoTabIndex == 0:
            ret,self.image0 = self.cap.read()#从摄像头读取图片
            self.image = cv2.cvtColor(self.image0,cv2.COLOR_BGR2RGB)#格式转换
            height,width,channel = self.image.shape#获取图片大小
            step = channel * width #更具图片大小获得step
            qImg = QImage(self.image.data, width,height,step,QImage.Format_RGB888)#根据图片大小产生QImage
            self.lihaoLabel2.setPixmap(QPixmap.fromImage(qImg));print("2")#显示图片
    def lihaoFunc(self):
        self.lihaoTabIndex = 0 
    def lihaoFunc2(self):
        self.lihaoTabIndex = 2 
    def lihaoTakePhoto(self):
        cv2.imwrite("temp.jpg",self.image0)
        self.image1 = cv2.cvtColor(self.image0,cv2.COLOR_BGR2RGB)#格式转换
        height,width,channel = self.image1.shape#获取图片大小
        step = channel * width #更具图片大小获得step
        qImg = QImage(self.image1.data, width,height,step,QImage.Format_RGB888)#根据图片大小产生QImage
        self.ident_photoimg.setPixmap(QPixmap.fromImage(qImg));print("0")#显示图片
    def lihaoTakePhoto2(self):
        cv2.imwrite("temp_2.jpg",self.image0)
        self.image1 = cv2.cvtColor(self.image0,cv2.COLOR_BGR2RGB)#格式转换
        height,width,channel = self.image1.shape#获取图片大小
        step = channel * width #更具图片大小获得step
        qImg = QImage(self.image1.data, width,height,step,QImage.Format_RGB888)#根据图片大小产生QImage
        self.stu_photoimg.setPixmap(QPixmap.fromImage(qImg));print("0")#显示图片
