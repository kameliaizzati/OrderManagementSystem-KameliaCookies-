# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_stocks.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_PreviewStocksW5(object):
    def setupUi(self, PreviewStocksW5):
        if not PreviewStocksW5.objectName():
            PreviewStocksW5.setObjectName(u"PreviewStocksW5")
        PreviewStocksW5.resize(400, 550)
        self.actionnew_customer = QAction(PreviewStocksW5)
        self.actionnew_customer.setObjectName(u"actionnew_customer")
        self.actionnew_customer.setCheckable(False)
        self.actionnew_customer.setChecked(False)
        self.actionnew_customer.setShortcutContext(Qt.ApplicationShortcut)
        self.actionnew_customer.setAutoRepeat(False)
        self.actionnew_customer.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionnew_customer.setShortcutVisibleInContextMenu(False)
        self.actionexisting_customer = QAction(PreviewStocksW5)
        self.actionexisting_customer.setObjectName(u"actionexisting_customer")
        self.actionlist_kuih_raya = QAction(PreviewStocksW5)
        self.actionlist_kuih_raya.setObjectName(u"actionlist_kuih_raya")
        self.actionnew_order = QAction(PreviewStocksW5)
        self.actionnew_order.setObjectName(u"actionnew_order")
        self.actionupdate_order = QAction(PreviewStocksW5)
        self.actionupdate_order.setObjectName(u"actionupdate_order")
        self.actionpreview_order = QAction(PreviewStocksW5)
        self.actionpreview_order.setObjectName(u"actionpreview_order")
        self.actionpreview_stocks = QAction(PreviewStocksW5)
        self.actionpreview_stocks.setObjectName(u"actionpreview_stocks")
        self.centralwidget = QWidget(PreviewStocksW5)
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
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 60, 102, 19))
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ChosenKuihW5 = QComboBox(self.groupBox)
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.addItem("")
        self.ChosenKuihW5.setObjectName(u"ChosenKuihW5")
        self.ChosenKuihW5.setGeometry(QRect(18, 30, 321, 22))
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 90, 321, 231))
        self.tableWidget.setFont(font1)
        self.PreviewStocksW5Button = QPushButton(self.groupBox)
        self.PreviewStocksW5Button.setObjectName(u"PreviewStocksW5Button")
        self.PreviewStocksW5Button.setGeometry(QRect(184, 340, 151, 31))
        PreviewStocksW5.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PreviewStocksW5)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        font2 = QFont()
        font2.setFamilies([u"Georgia"])
        font2.setPointSize(10)
        self.menubar.setFont(font2)
        self.menubar.setLayoutDirection(Qt.LeftToRight)
        self.menulist_kuih_raya = QMenu(self.menubar)
        self.menulist_kuih_raya.setObjectName(u"menulist_kuih_raya")
        PreviewStocksW5.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PreviewStocksW5)
        self.statusbar.setObjectName(u"statusbar")
        PreviewStocksW5.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menulist_kuih_raya.menuAction())
        self.menulist_kuih_raya.addAction(self.actionlist_kuih_raya)
        self.menulist_kuih_raya.addAction(self.actionnew_order)
        self.menulist_kuih_raya.addAction(self.actionupdate_order)
        self.menulist_kuih_raya.addAction(self.actionpreview_order)
        self.menulist_kuih_raya.addAction(self.actionpreview_stocks)

        self.retranslateUi(PreviewStocksW5)

        QMetaObject.connectSlotsByName(PreviewStocksW5)
    # setupUi

    def retranslateUi(self, PreviewStocksW5):
        PreviewStocksW5.setWindowTitle(QCoreApplication.translate("PreviewStocksW5", u"MainWindow", None))
        self.actionnew_customer.setText(QCoreApplication.translate("PreviewStocksW5", u"new customer", None))
        self.actionexisting_customer.setText(QCoreApplication.translate("PreviewStocksW5", u"existing customer", None))
        self.actionlist_kuih_raya.setText(QCoreApplication.translate("PreviewStocksW5", u"list kuih raya", None))
        self.actionnew_order.setText(QCoreApplication.translate("PreviewStocksW5", u"new order", None))
        self.actionupdate_order.setText(QCoreApplication.translate("PreviewStocksW5", u"update order", None))
        self.actionpreview_order.setText(QCoreApplication.translate("PreviewStocksW5", u"preview order", None))
        self.actionpreview_stocks.setText(QCoreApplication.translate("PreviewStocksW5", u"preview stocks", None))
        self.label.setText(QCoreApplication.translate("PreviewStocksW5", u"KameliaCookies", None))
        self.groupBox.setTitle(QCoreApplication.translate("PreviewStocksW5", u"Preview Stocks", None))
        self.label_12.setText(QCoreApplication.translate("PreviewStocksW5", u"The Orders :", None))
        self.ChosenKuihW5.setItemText(0, QCoreApplication.translate("PreviewStocksW5", u"All", None))
        self.ChosenKuihW5.setItemText(1, QCoreApplication.translate("PreviewStocksW5", u"Almond_London", None))
        self.ChosenKuihW5.setItemText(2, QCoreApplication.translate("PreviewStocksW5", u"Cookies", None))
        self.ChosenKuihW5.setItemText(3, QCoreApplication.translate("PreviewStocksW5", u"Cornflakes_Crunchy", None))
        self.ChosenKuihW5.setItemText(4, QCoreApplication.translate("PreviewStocksW5", u"Dahlia", None))
        self.ChosenKuihW5.setItemText(5, QCoreApplication.translate("PreviewStocksW5", u"Makmur", None))
        self.ChosenKuihW5.setItemText(6, QCoreApplication.translate("PreviewStocksW5", u"Rainbow", None))
        self.ChosenKuihW5.setItemText(7, QCoreApplication.translate("PreviewStocksW5", u"Red_Pearl", None))
        self.ChosenKuihW5.setItemText(8, QCoreApplication.translate("PreviewStocksW5", u"Semperit", None))
        self.ChosenKuihW5.setItemText(9, QCoreApplication.translate("PreviewStocksW5", u"Suji", None))
        self.ChosenKuihW5.setItemText(10, QCoreApplication.translate("PreviewStocksW5", u"Tart_Nenas", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PreviewStocksW5", u"Kuih Raya", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PreviewStocksW5", u"Quantity", None));
        self.PreviewStocksW5Button.setText(QCoreApplication.translate("PreviewStocksW5", u"Preview Stocks", None))
        self.menulist_kuih_raya.setTitle(QCoreApplication.translate("PreviewStocksW5", u"cookies!", None))
    # retranslateUi

