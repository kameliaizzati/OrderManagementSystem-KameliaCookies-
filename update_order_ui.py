# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_order.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)
#import image_rc

class Ui_UpdateOrderW3(object):
    def setupUi(self, UpdateOrderW3):
        if not UpdateOrderW3.objectName():
            UpdateOrderW3.setObjectName(u"UpdateOrderW3")
        UpdateOrderW3.resize(400, 550)
        self.actionnew_customer = QAction(UpdateOrderW3)
        self.actionnew_customer.setObjectName(u"actionnew_customer")
        self.actionnew_customer.setCheckable(False)
        self.actionnew_customer.setChecked(False)
        self.actionnew_customer.setShortcutContext(Qt.ApplicationShortcut)
        self.actionnew_customer.setAutoRepeat(False)
        self.actionnew_customer.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionnew_customer.setShortcutVisibleInContextMenu(False)
        self.actionexisting_customer = QAction(UpdateOrderW3)
        self.actionexisting_customer.setObjectName(u"actionexisting_customer")
        self.actionlist_kuih_raya = QAction(UpdateOrderW3)
        self.actionlist_kuih_raya.setObjectName(u"actionlist_kuih_raya")
        self.actionnew_order = QAction(UpdateOrderW3)
        self.actionnew_order.setObjectName(u"actionnew_order")
        self.actionupdate_order = QAction(UpdateOrderW3)
        self.actionupdate_order.setObjectName(u"actionupdate_order")
        self.actionpreview_order = QAction(UpdateOrderW3)
        self.actionpreview_order.setObjectName(u"actionpreview_order")
        self.actionpreview_stocks = QAction(UpdateOrderW3)
        self.actionpreview_stocks.setObjectName(u"actionpreview_stocks")
        self.centralwidget = QWidget(UpdateOrderW3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 161, 51))
        font = QFont()
        font.setFamilies([u"Lucida Handwriting"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 60, 361, 451))
        font1 = QFont()
        font1.setFamilies([u"Georgia"])
        self.groupBox.setFont(font1)
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 30, 321, 31))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.CustomerNameLabel = QLabel(self.formLayoutWidget)
        self.CustomerNameLabel.setObjectName(u"CustomerNameLabel")
        self.CustomerNameLabel.setFont(font1)
        self.CustomerNameLabel.setLayoutDirection(Qt.LeftToRight)
        self.CustomerNameLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.CustomerNameLabel)

        self.CustomerNameInputW3 = QLineEdit(self.formLayoutWidget)
        self.CustomerNameInputW3.setObjectName(u"CustomerNameInputW3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.CustomerNameInputW3)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 60, 321, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 319, 249))
        self.horizontalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 40, 281, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.W3Kuih01 = QComboBox(self.horizontalLayoutWidget)
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.addItem("")
        self.W3Kuih01.setObjectName(u"W3Kuih01")

        self.horizontalLayout.addWidget(self.W3Kuih01)

        self.w3Qkuih01 = QSpinBox(self.horizontalLayoutWidget)
        self.w3Qkuih01.setObjectName(u"w3Qkuih01")
        self.w3Qkuih01.setContextMenuPolicy(Qt.NoContextMenu)
        self.w3Qkuih01.setAlignment(Qt.AlignCenter)
        self.w3Qkuih01.setMinimum(-100)
        self.w3Qkuih01.setMaximum(200)

        self.horizontalLayout.addWidget(self.w3Qkuih01)

        self.horizontalLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 10, 281, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 120, 281, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.W3Kuih03 = QComboBox(self.horizontalLayoutWidget_3)
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.addItem("")
        self.W3Kuih03.setObjectName(u"W3Kuih03")

        self.horizontalLayout_3.addWidget(self.W3Kuih03)

        self.w3Qkuih03 = QSpinBox(self.horizontalLayoutWidget_3)
        self.w3Qkuih03.setObjectName(u"w3Qkuih03")
        self.w3Qkuih03.setAlignment(Qt.AlignCenter)
        self.w3Qkuih03.setMinimum(-100)
        self.w3Qkuih03.setMaximum(200)

        self.horizontalLayout_3.addWidget(self.w3Qkuih03)

        self.horizontalLayoutWidget_4 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 80, 281, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.W3Kuih02 = QComboBox(self.horizontalLayoutWidget_4)
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.addItem("")
        self.W3Kuih02.setObjectName(u"W3Kuih02")

        self.horizontalLayout_4.addWidget(self.W3Kuih02)

        self.w3Qkuih02 = QSpinBox(self.horizontalLayoutWidget_4)
        self.w3Qkuih02.setObjectName(u"w3Qkuih02")
        self.w3Qkuih02.setAlignment(Qt.AlignCenter)
        self.w3Qkuih02.setMinimum(-100)
        self.w3Qkuih02.setMaximum(200)

        self.horizontalLayout_4.addWidget(self.w3Qkuih02)

        self.horizontalLayoutWidget_5 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(20, 160, 281, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.W3Kuih04 = QComboBox(self.horizontalLayoutWidget_5)
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.addItem("")
        self.W3Kuih04.setObjectName(u"W3Kuih04")

        self.horizontalLayout_5.addWidget(self.W3Kuih04)

        self.w3Qkuih04 = QSpinBox(self.horizontalLayoutWidget_5)
        self.w3Qkuih04.setObjectName(u"w3Qkuih04")
        self.w3Qkuih04.setAlignment(Qt.AlignCenter)
        self.w3Qkuih04.setMinimum(-100)
        self.w3Qkuih04.setMaximum(200)

        self.horizontalLayout_5.addWidget(self.w3Qkuih04)

        self.horizontalLayoutWidget_7 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(20, 200, 281, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.W3Kuih05 = QComboBox(self.horizontalLayoutWidget_7)
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.addItem("")
        self.W3Kuih05.setObjectName(u"W3Kuih05")

        self.horizontalLayout_7.addWidget(self.W3Kuih05)

        self.w3Qkuih05 = QSpinBox(self.horizontalLayoutWidget_7)
        self.w3Qkuih05.setObjectName(u"w3Qkuih05")
        self.w3Qkuih05.setAlignment(Qt.AlignCenter)
        self.w3Qkuih05.setMinimum(-100)
        self.w3Qkuih05.setMaximum(200)

        self.horizontalLayout_7.addWidget(self.w3Qkuih05)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_6 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(130, 360, 211, 21))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.W3CurDepo = QLabel(self.horizontalLayoutWidget_6)
        self.W3CurDepo.setObjectName(u"W3CurDepo")
        self.W3CurDepo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.W3CurDepo)

        self.horizontalLayoutWidget_9 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(130, 340, 211, 22))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.horizontalLayoutWidget_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.W3Total = QLabel(self.horizontalLayoutWidget_9)
        self.W3Total.setObjectName(u"W3Total")
        self.W3Total.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.W3Total)

        self.horizontalLayoutWidget_10 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(130, 380, 211, 22))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.W3AddOnDepo = QLineEdit(self.horizontalLayoutWidget_10)
        self.W3AddOnDepo.setObjectName(u"W3AddOnDepo")
        self.W3AddOnDepo.setMaxLength(32750)
        self.W3AddOnDepo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.W3AddOnDepo)

        self.horizontalLayoutWidget_11 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(130, 400, 211, 21))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.W3Balance = QLabel(self.horizontalLayoutWidget_11)
        self.W3Balance.setObjectName(u"W3Balance")
        self.W3Balance.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.W3Balance)

        self.horizontalLayoutWidget_12 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(130, 420, 211, 25))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.AddUpdateOrderButton = QPushButton(self.horizontalLayoutWidget_12)
        self.AddUpdateOrderButton.setObjectName(u"AddUpdateOrderButton")

        self.horizontalLayout_12.addWidget(self.AddUpdateOrderButton)

        self.horizontalLayoutWidget_13 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(130, 320, 211, 21))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.horizontalLayoutWidget_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.W3TotalAddOn = QLabel(self.horizontalLayoutWidget_13)
        self.W3TotalAddOn.setObjectName(u"W3TotalAddOn")
        self.W3TotalAddOn.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.W3TotalAddOn)

        UpdateOrderW3.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(UpdateOrderW3)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        font2 = QFont()
        font2.setFamilies([u"Georgia"])
        font2.setPointSize(10)
        self.menubar.setFont(font2)
        self.menubar.setLayoutDirection(Qt.LeftToRight)
        self.menulist_kuih_raya = QMenu(self.menubar)
        self.menulist_kuih_raya.setObjectName(u"menulist_kuih_raya")
        UpdateOrderW3.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(UpdateOrderW3)
        self.statusbar.setObjectName(u"statusbar")
        UpdateOrderW3.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menulist_kuih_raya.menuAction())
        self.menulist_kuih_raya.addAction(self.actionlist_kuih_raya)
        self.menulist_kuih_raya.addAction(self.actionnew_order)
        self.menulist_kuih_raya.addAction(self.actionupdate_order)
        self.menulist_kuih_raya.addAction(self.actionpreview_order)
        self.menulist_kuih_raya.addAction(self.actionpreview_stocks)

        self.retranslateUi(UpdateOrderW3)

        QMetaObject.connectSlotsByName(UpdateOrderW3)
    # setupUi

    def retranslateUi(self, UpdateOrderW3):
        UpdateOrderW3.setWindowTitle(QCoreApplication.translate("UpdateOrderW3", u"MainWindow", None))
        self.actionnew_customer.setText(QCoreApplication.translate("UpdateOrderW3", u"new customer", None))
        self.actionexisting_customer.setText(QCoreApplication.translate("UpdateOrderW3", u"existing customer", None))
        self.actionlist_kuih_raya.setText(QCoreApplication.translate("UpdateOrderW3", u"list kuih raya", None))
        self.actionnew_order.setText(QCoreApplication.translate("UpdateOrderW3", u"new order", None))
        self.actionupdate_order.setText(QCoreApplication.translate("UpdateOrderW3", u"update order", None))
        self.actionpreview_order.setText(QCoreApplication.translate("UpdateOrderW3", u"preview order", None))
        self.actionpreview_stocks.setText(QCoreApplication.translate("UpdateOrderW3", u"preview stocks", None))
        self.label.setText(QCoreApplication.translate("UpdateOrderW3", u"KameliaCookies", None))
        self.groupBox.setTitle(QCoreApplication.translate("UpdateOrderW3", u"Update Order for Existing Customer", None))
        self.CustomerNameLabel.setText(QCoreApplication.translate("UpdateOrderW3", u"Name :", None))
        self.W3Kuih01.setItemText(0, QCoreApplication.translate("UpdateOrderW3", u"None", None))
        self.W3Kuih01.setItemText(1, QCoreApplication.translate("UpdateOrderW3", u"Almond_London", None))
        self.W3Kuih01.setItemText(2, QCoreApplication.translate("UpdateOrderW3", u"Cookies", None))
        self.W3Kuih01.setItemText(3, QCoreApplication.translate("UpdateOrderW3", u"Cornflakes_Crunchy", None))
        self.W3Kuih01.setItemText(4, QCoreApplication.translate("UpdateOrderW3", u"Dahlia", None))
        self.W3Kuih01.setItemText(5, QCoreApplication.translate("UpdateOrderW3", u"Makmur", None))
        self.W3Kuih01.setItemText(6, QCoreApplication.translate("UpdateOrderW3", u"Rainbow", None))
        self.W3Kuih01.setItemText(7, QCoreApplication.translate("UpdateOrderW3", u"Red_Pearl", None))
        self.W3Kuih01.setItemText(8, QCoreApplication.translate("UpdateOrderW3", u"Semperit", None))
        self.W3Kuih01.setItemText(9, QCoreApplication.translate("UpdateOrderW3", u"Suji", None))
        self.W3Kuih01.setItemText(10, QCoreApplication.translate("UpdateOrderW3", u"Tart_Nenas", None))

        self.label_2.setText(QCoreApplication.translate("UpdateOrderW3", u"Kuih :", None))
        self.label_3.setText(QCoreApplication.translate("UpdateOrderW3", u"Quantity :", None))
        self.W3Kuih03.setItemText(0, QCoreApplication.translate("UpdateOrderW3", u"None", None))
        self.W3Kuih03.setItemText(1, QCoreApplication.translate("UpdateOrderW3", u"Almond_London", None))
        self.W3Kuih03.setItemText(2, QCoreApplication.translate("UpdateOrderW3", u"Cookies", None))
        self.W3Kuih03.setItemText(3, QCoreApplication.translate("UpdateOrderW3", u"Cornflakes_Crunchy", None))
        self.W3Kuih03.setItemText(4, QCoreApplication.translate("UpdateOrderW3", u"Dahlia", None))
        self.W3Kuih03.setItemText(5, QCoreApplication.translate("UpdateOrderW3", u"Makmur", None))
        self.W3Kuih03.setItemText(6, QCoreApplication.translate("UpdateOrderW3", u"Rainbow", None))
        self.W3Kuih03.setItemText(7, QCoreApplication.translate("UpdateOrderW3", u"Red_Pearl", None))
        self.W3Kuih03.setItemText(8, QCoreApplication.translate("UpdateOrderW3", u"Semperit", None))
        self.W3Kuih03.setItemText(9, QCoreApplication.translate("UpdateOrderW3", u"Suji", None))
        self.W3Kuih03.setItemText(10, QCoreApplication.translate("UpdateOrderW3", u"Tart_Nenas", None))

        self.W3Kuih02.setItemText(0, QCoreApplication.translate("UpdateOrderW3", u"None", None))
        self.W3Kuih02.setItemText(1, QCoreApplication.translate("UpdateOrderW3", u"Almond_London", None))
        self.W3Kuih02.setItemText(2, QCoreApplication.translate("UpdateOrderW3", u"Cookies", None))
        self.W3Kuih02.setItemText(3, QCoreApplication.translate("UpdateOrderW3", u"Cornflakes_Crunchy", None))
        self.W3Kuih02.setItemText(4, QCoreApplication.translate("UpdateOrderW3", u"Dahlia", None))
        self.W3Kuih02.setItemText(5, QCoreApplication.translate("UpdateOrderW3", u"Makmur", None))
        self.W3Kuih02.setItemText(6, QCoreApplication.translate("UpdateOrderW3", u"Rainbow", None))
        self.W3Kuih02.setItemText(7, QCoreApplication.translate("UpdateOrderW3", u"Red_Pearl", None))
        self.W3Kuih02.setItemText(8, QCoreApplication.translate("UpdateOrderW3", u"Semperit", None))
        self.W3Kuih02.setItemText(9, QCoreApplication.translate("UpdateOrderW3", u"Suji", None))
        self.W3Kuih02.setItemText(10, QCoreApplication.translate("UpdateOrderW3", u"Tart_Nenas", None))

        self.W3Kuih04.setItemText(0, QCoreApplication.translate("UpdateOrderW3", u"None", None))
        self.W3Kuih04.setItemText(1, QCoreApplication.translate("UpdateOrderW3", u"Almond_London", None))
        self.W3Kuih04.setItemText(2, QCoreApplication.translate("UpdateOrderW3", u"Cookies", None))
        self.W3Kuih04.setItemText(3, QCoreApplication.translate("UpdateOrderW3", u"Cornflakes_Crunchy", None))
        self.W3Kuih04.setItemText(4, QCoreApplication.translate("UpdateOrderW3", u"Dahlia", None))
        self.W3Kuih04.setItemText(5, QCoreApplication.translate("UpdateOrderW3", u"Makmur", None))
        self.W3Kuih04.setItemText(6, QCoreApplication.translate("UpdateOrderW3", u"Rainbow", None))
        self.W3Kuih04.setItemText(7, QCoreApplication.translate("UpdateOrderW3", u"Red_Pearl", None))
        self.W3Kuih04.setItemText(8, QCoreApplication.translate("UpdateOrderW3", u"Semperit", None))
        self.W3Kuih04.setItemText(9, QCoreApplication.translate("UpdateOrderW3", u"Suji", None))
        self.W3Kuih04.setItemText(10, QCoreApplication.translate("UpdateOrderW3", u"Tart_Nenas", None))

        self.W3Kuih05.setItemText(0, QCoreApplication.translate("UpdateOrderW3", u"None", None))
        self.W3Kuih05.setItemText(1, QCoreApplication.translate("UpdateOrderW3", u"Almond_London", None))
        self.W3Kuih05.setItemText(2, QCoreApplication.translate("UpdateOrderW3", u"Cookies", None))
        self.W3Kuih05.setItemText(3, QCoreApplication.translate("UpdateOrderW3", u"Cornflakes_Crunchy", None))
        self.W3Kuih05.setItemText(4, QCoreApplication.translate("UpdateOrderW3", u"Dahlia", None))
        self.W3Kuih05.setItemText(5, QCoreApplication.translate("UpdateOrderW3", u"Makmur", None))
        self.W3Kuih05.setItemText(6, QCoreApplication.translate("UpdateOrderW3", u"Rainbow", None))
        self.W3Kuih05.setItemText(7, QCoreApplication.translate("UpdateOrderW3", u"Red_Pearl", None))
        self.W3Kuih05.setItemText(8, QCoreApplication.translate("UpdateOrderW3", u"Semperit", None))
        self.W3Kuih05.setItemText(9, QCoreApplication.translate("UpdateOrderW3", u"Suji", None))
        self.W3Kuih05.setItemText(10, QCoreApplication.translate("UpdateOrderW3", u"Tart_Nenas", None))

        self.label_5.setText(QCoreApplication.translate("UpdateOrderW3", u"Current Deposit :", None))
        self.W3CurDepo.setText(QCoreApplication.translate("UpdateOrderW3", u"RM?", None))
        self.label_8.setText(QCoreApplication.translate("UpdateOrderW3", u"             Total         :", None))
        self.W3Total.setText(QCoreApplication.translate("UpdateOrderW3", u"RM?", None))
        self.label_6.setText(QCoreApplication.translate("UpdateOrderW3", u"Add On Deposit   :", None))
        self.W3AddOnDepo.setText("")
        self.label_10.setText(QCoreApplication.translate("UpdateOrderW3", u"        Balance        :", None))
        self.W3Balance.setText(QCoreApplication.translate("UpdateOrderW3", u"RM?", None))
        self.AddUpdateOrderButton.setText(QCoreApplication.translate("UpdateOrderW3", u"Update Order", None))
        self.label_12.setText(QCoreApplication.translate("UpdateOrderW3", u"     Total Add-On  :", None))
        self.W3TotalAddOn.setText(QCoreApplication.translate("UpdateOrderW3", u"RM?", None))
        self.menulist_kuih_raya.setTitle(QCoreApplication.translate("UpdateOrderW3", u"cookies!", None))
    # retranslateUi

