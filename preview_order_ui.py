# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_order.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_PreviewOrderW4(object):
    def setupUi(self, PreviewOrderW4):
        if not PreviewOrderW4.objectName():
            PreviewOrderW4.setObjectName(u"PreviewOrderW4")
        PreviewOrderW4.resize(400, 550)
        self.actionnew_customer = QAction(PreviewOrderW4)
        self.actionnew_customer.setObjectName(u"actionnew_customer")
        self.actionnew_customer.setCheckable(False)
        self.actionnew_customer.setChecked(False)
        self.actionnew_customer.setShortcutContext(Qt.ApplicationShortcut)
        self.actionnew_customer.setAutoRepeat(False)
        self.actionnew_customer.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionnew_customer.setShortcutVisibleInContextMenu(False)
        self.actionexisting_customer = QAction(PreviewOrderW4)
        self.actionexisting_customer.setObjectName(u"actionexisting_customer")
        self.actionlist_kuih_raya = QAction(PreviewOrderW4)
        self.actionlist_kuih_raya.setObjectName(u"actionlist_kuih_raya")
        self.actionnew_order = QAction(PreviewOrderW4)
        self.actionnew_order.setObjectName(u"actionnew_order")
        self.actionupdate_order = QAction(PreviewOrderW4)
        self.actionupdate_order.setObjectName(u"actionupdate_order")
        self.actionpreview_order = QAction(PreviewOrderW4)
        self.actionpreview_order.setObjectName(u"actionpreview_order")
        self.actionpreview_stocks = QAction(PreviewOrderW4)
        self.actionpreview_stocks.setObjectName(u"actionpreview_stocks")
        self.centralwidget = QWidget(PreviewOrderW4)
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

        self.CustomerNameInputW4 = QLineEdit(self.formLayoutWidget)
        self.CustomerNameInputW4.setObjectName(u"CustomerNameInputW4")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.CustomerNameInputW4)

        self.horizontalLayoutWidget_6 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(130, 330, 211, 21))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.TotalW4 = QLabel(self.horizontalLayoutWidget_6)
        self.TotalW4.setObjectName(u"TotalW4")
        self.TotalW4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.TotalW4)

        self.horizontalLayoutWidget_10 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(130, 350, 211, 22))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.DepoW4 = QLabel(self.horizontalLayoutWidget_10)
        self.DepoW4.setObjectName(u"DepoW4")
        self.DepoW4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.DepoW4)

        self.horizontalLayoutWidget_11 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(130, 370, 211, 21))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.BalanceW4 = QLabel(self.horizontalLayoutWidget_11)
        self.BalanceW4.setObjectName(u"BalanceW4")
        self.BalanceW4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.BalanceW4)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 80, 102, 19))
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.PreviewOrderW4Button = QPushButton(self.groupBox)
        self.PreviewOrderW4Button.setObjectName(u"PreviewOrderW4Button")
        self.PreviewOrderW4Button.setGeometry(QRect(170, 402, 171, 31))
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 110, 321, 192))
        self.tableWidget.setMaximumSize(QSize(321, 16777215))
        self.tableWidget.setFont(font1)
        PreviewOrderW4.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PreviewOrderW4)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        font2 = QFont()
        font2.setFamilies([u"Georgia"])
        font2.setPointSize(10)
        self.menubar.setFont(font2)
        self.menubar.setLayoutDirection(Qt.LeftToRight)
        self.menulist_kuih_raya = QMenu(self.menubar)
        self.menulist_kuih_raya.setObjectName(u"menulist_kuih_raya")
        PreviewOrderW4.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PreviewOrderW4)
        self.statusbar.setObjectName(u"statusbar")
        PreviewOrderW4.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menulist_kuih_raya.menuAction())
        self.menulist_kuih_raya.addAction(self.actionlist_kuih_raya)
        self.menulist_kuih_raya.addAction(self.actionnew_order)
        self.menulist_kuih_raya.addAction(self.actionupdate_order)
        self.menulist_kuih_raya.addAction(self.actionpreview_order)
        self.menulist_kuih_raya.addAction(self.actionpreview_stocks)

        self.retranslateUi(PreviewOrderW4)

        QMetaObject.connectSlotsByName(PreviewOrderW4)
    # setupUi

    def retranslateUi(self, PreviewOrderW4):
        PreviewOrderW4.setWindowTitle(QCoreApplication.translate("PreviewOrderW4", u"MainWindow", None))
        self.actionnew_customer.setText(QCoreApplication.translate("PreviewOrderW4", u"new customer", None))
        self.actionexisting_customer.setText(QCoreApplication.translate("PreviewOrderW4", u"existing customer", None))
        self.actionlist_kuih_raya.setText(QCoreApplication.translate("PreviewOrderW4", u"list kuih raya", None))
        self.actionnew_order.setText(QCoreApplication.translate("PreviewOrderW4", u"new order", None))
        self.actionupdate_order.setText(QCoreApplication.translate("PreviewOrderW4", u"update order", None))
        self.actionpreview_order.setText(QCoreApplication.translate("PreviewOrderW4", u"preview order", None))
        self.actionpreview_stocks.setText(QCoreApplication.translate("PreviewOrderW4", u"preview stocks", None))
        self.label.setText(QCoreApplication.translate("PreviewOrderW4", u"KameliaCookies", None))
        self.groupBox.setTitle(QCoreApplication.translate("PreviewOrderW4", u"Preview Order", None))
        self.CustomerNameLabel.setText(QCoreApplication.translate("PreviewOrderW4", u"Name :", None))
        self.label_5.setText(QCoreApplication.translate("PreviewOrderW4", u"           Total       :", None))
        self.TotalW4.setText(QCoreApplication.translate("PreviewOrderW4", u"RM?", None))
        self.label_6.setText(QCoreApplication.translate("PreviewOrderW4", u"            Deposit     :", None))
        self.DepoW4.setText(QCoreApplication.translate("PreviewOrderW4", u"RM?", None))
        self.label_10.setText(QCoreApplication.translate("PreviewOrderW4", u"        Balance      :", None))
        self.BalanceW4.setText(QCoreApplication.translate("PreviewOrderW4", u"RM?", None))
        self.label_12.setText(QCoreApplication.translate("PreviewOrderW4", u"The Orders :", None))
        self.PreviewOrderW4Button.setText(QCoreApplication.translate("PreviewOrderW4", u"Preview Order", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PreviewOrderW4", u"Kuih Raya", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PreviewOrderW4", u"Quantity", None));
        self.menulist_kuih_raya.setTitle(QCoreApplication.translate("PreviewOrderW4", u"cookies!", None))
    # retranslateUi

