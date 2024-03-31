
import sqlite3
import sys
import pandas as pd

from tkinter.messagebox import showerror, showinfo
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QTableWidgetItem
from list_kuih_raya_ui import Ui_MainWindow
from new_customer_ui import Ui_NewOrderW2
from update_order_ui import Ui_UpdateOrderW3
from preview_order_ui import Ui_PreviewOrderW4
from preview_stocks_ui import Ui_PreviewStocksW5

con = sqlite3.Connection("kuih_details.db")
cur = con.cursor()
table = """CREATE TABLE IF NOT EXISTS kuihraya2024(
        Customer varchar(20) NOT NULL,
        Phone varchar(20),
        Almond_London int,
        Cookies int,
        Cornflakes_Crunchy int,
        Dahlia int,
        Makmur int,
        Rainbow int,
        Red_Pearl int,
        Semperit int,
        Suji int,
        Tart_Nenas int,
        Total float,
        Deposit float,
        Balance float,
        UNIQUE (Customer)
);"""
cur.execute(table)
con.commit()

#kuihraya24 = ['semperit', 'tart nenas', 'makmur', 'cookies', 'cornflakes crunchy', 'red pearl', 'almond london', 'dahlia', 'rainbow', 'suji']

class MainWindow(QMainWindow): # list kuih raya
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionnew_order.triggered.connect(newWindow2)
        self.ui.actionupdate_order.triggered.connect(newWindow3)
        self.ui.actionpreview_order.triggered.connect(newWindow4)
        self.ui.actionpreview_stocks.triggered.connect(newWindow5)

class Window2(QMainWindow): #new order
    def __init__(self):
        super(Window2, self).__init__()
        self.ui2 = Ui_NewOrderW2()
        self.ui2.setupUi(self)
        self.ui2.actionlist_kuih_raya.triggered.connect(newWindow1)
        self.ui2.actionupdate_order.triggered.connect(newWindow3)
        self.ui2.actionpreview_order.triggered.connect(newWindow4)
        self.ui2.actionpreview_stocks.triggered.connect(newWindow5)
        self.ui2.AddNewOrderButton.clicked.connect(self.insert_data)
    
    def insert_data(self):
        self.customer = self.ui2.CustomerNameInputW2.text()
        self.phone = self.ui2.PhoneInput.text()
        self.kuih1 = self.ui2.W2Kuih01.currentText()
        self.quantitykuih1 = self.ui2.w2Qkuih01.value()
        self.kuih2 = self.ui2.W2Kuih02.currentText()
        self.quantitykuih2 = self.ui2.w2Qkuih02.value()
        self.kuih3 = self.ui2.W2Kuih03.currentText()
        self.quantitykuih3 = self.ui2.w2Qkuih03.value()
        self.kuih4 = self.ui2.W2Kuih04.currentText()
        self.quantitykuih4 = self.ui2.w2Qkuih04.value()
        self.kuih5 = self.ui2.W2Kuih05.currentText()
        self.quantitykuih5 = self.ui2.w2Qkuih05.value()
        #self.deposit = self.ui2.DepositW2.text()
        if self.ui2.DepositW2.text() == "":
            self.deposit = 0
        else:
            self.deposit = self.ui2.DepositW2.text()

        #kuihraya24 = ['Almond_London', 'Cookies', 'Cornflakes_Crunchy', 'Dahlia', 'Makmur', 'Rainbow', 'Red_Pearl', 'Semperit', 'Suji', 'Tart_Nenas']
        list_kuih = {self.kuih1:self.quantitykuih1, self.kuih2:self.quantitykuih2, self.kuih3:self.quantitykuih3, self.kuih4:self.quantitykuih4, self.kuih5:self.quantitykuih5}
        # dictionary tak boleh ada duplicate
        
        if self.customer == "":
            showerror("Adding Order Failed","Please Insert Your Customer's Name")
        else:
            cur.execute('INSERT INTO kuihraya2024 (customer,phone) VALUES (?,?)', (self.customer, self.phone))
            con.commit()
            totalprice = 0
            for i in list_kuih:
                if i == 'Almond_London':
                    quantity = list_kuih[i]
                    price = 39
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Almond_London = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                elif i == 'Cookies':
                    quantity = list_kuih[i]
                    price = 40
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Cookies = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                elif i == 'Cornflakes_Crunchy':
                    quantity = list_kuih[i]
                    price = 31
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Cornflakes_Crunchy = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                elif i == 'Dahlia':
                    quantity = list_kuih[i]
                    price = 33
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Dahlia = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                elif i == 'Makmur':
                    quantity = list_kuih[i]
                    price = 30
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Makmur = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                elif i == 'Rainbow':
                    quantity = list_kuih[i]
                    price = 35
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Rainbow = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                elif i == 'Red_Pearl':
                    quantity = list_kuih[i]
                    price = 31
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Red_Pearl = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                elif i == 'Semperit':
                    quantity = list_kuih[i]
                    price = 32
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Semperit = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                elif i == 'Suji':
                    quantity = list_kuih[i]
                    price = 30
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Suji = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                elif i == 'Tart_Nenas':
                    quantity = list_kuih[i]
                    price = 35
                    price_quantity = price*quantity
                    cur.execute('UPDATE kuihraya2024 SET Tart_Nenas = (?) WHERE Customer = (?)', (quantity, self.customer))
                    con.commit()
                else:
                    price_quantity = 0
                totalprice = totalprice + price_quantity
            showinfo("Adding Order Successful", "Successfully Insert New Order for New Customer")
            self.balance = totalprice - float(self.deposit)
            cur.execute('UPDATE kuihraya2024 SET Total = (?), Deposit = (?), Balance = (?) WHERE Customer = (?)', (totalprice, self.deposit, self.balance, self.customer))
            con.commit()
            self.ui2.TotalW2.setText('RM' + str(totalprice))
            self.ui2.BalanceW2.setText('RM' + str(self.balance))


class Window3(QMainWindow): #update order
    def __init__(self):
        super(Window3, self).__init__()
        self.ui3 = Ui_UpdateOrderW3()
        self.ui3.setupUi(self)
        self.ui3.actionlist_kuih_raya.triggered.connect(newWindow1)
        self.ui3.actionnew_order.triggered.connect(newWindow2)
        self.ui3.actionpreview_order.triggered.connect(newWindow4)
        self.ui3.actionpreview_stocks.triggered.connect(newWindow5)
        self.ui3.AddUpdateOrderButton.clicked.connect(self.check)

    def check(self):
        self.customer = self.ui3.CustomerNameInputW3.text()
        cur.execute("SELECT * FROM kuihraya2024 WHERE Customer =?", (self.customer,)) # this parameter need to be in tuple
        a = cur.fetchall()
        if a == []:
            showerror("Update Order Failed","Customer's Name Do Not Exist in Database")
        else:
            self.addkuih1 = self.ui3.W3Kuih01.currentText()
            self.addquantitykuih1 = self.ui3.w3Qkuih01.value()
            self.addkuih2 = self.ui3.W3Kuih02.currentText()
            self.addquantitykuih2 = self.ui3.w3Qkuih02.value()
            self.addkuih3 = self.ui3.W3Kuih03.currentText()
            self.addquantitykuih3 = self.ui3.w3Qkuih03.value()
            self.addkuih4 = self.ui3.W3Kuih04.currentText()
            self.addquantitykuih4 = self.ui3.w3Qkuih04.value()
            self.addkuih5 = self.ui3.W3Kuih05.currentText()
            self.addquantitykuih5 = self.ui3.w3Qkuih05.value()
            #self.adddeposit = self.ui3.W3AddOnDepo.text()

            if self.ui3.W3AddOnDepo.text() == "":
                self.adddeposit = 0
            else:
                self.adddeposit = self.ui3.W3AddOnDepo.text()

            list_addkuih = {self.addkuih1:self.addquantitykuih1, self.addkuih2:self.addquantitykuih2, self.addkuih3:self.addquantitykuih3, self.addkuih4:self.addquantitykuih4, self.addkuih5:self.addquantitykuih5}
            total = a[0][12]
            depo = a[0][13]
            #balance = a[0][14]
            for i in list_addkuih:
                total_addon = 0
                addprice = 0
                if i == 'Almond_London':
                    quantity = list_addkuih[i]
                    addprice = 39
                    newaddprice = addprice*quantity
                    if a[0][2] == None:
                        cur.execute('UPDATE kuihraya2024 SET Almond_London = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][2]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Almond_London = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                elif i == 'Cookies':
                    quantity = list_addkuih[i]
                    addprice = 40
                    newaddprice = addprice*quantity
                    if a[0][3] == None:
                        cur.execute('UPDATE kuihraya2024 SET Cookies = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][3]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Cookies = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                elif i == 'Cornflakes_Crunchy':
                    quantity = list_addkuih[i]
                    addprice = 31
                    newaddprice = addprice*quantity
                    if a[0][4] == None:
                        cur.execute('UPDATE kuihraya2024 SET Cornflakes_Crunchy = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][4]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Cornflakes_Crunchy = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                elif i == 'Dahlia':
                    quantity = list_addkuih[i]
                    addprice = 33
                    newaddprice = addprice*quantity
                    if a[0][5] == None:
                        cur.execute('UPDATE kuihraya2024 SET Dahlia = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][5]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Dahlia = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                elif i == 'Makmur':
                    quantity = list_addkuih[i]
                    addprice = 30
                    newaddprice = addprice*quantity
                    if a[0][6] == None:
                        cur.execute('UPDATE kuihraya2024 SET Makmur = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][6]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Makmur = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                elif i == 'Rainbow':
                    quantity = list_addkuih[i]
                    addprice = 35
                    newaddprice = addprice*quantity
                    if a[0][7] == None:
                        cur.execute('UPDATE kuihraya2024 SET Rainbow = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][7]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Rainbow = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                elif i == 'Red_Pearl':
                    quantity = list_addkuih[i]
                    addprice = 31
                    newaddprice = addprice*quantity
                    if a[0][8] == None:
                        cur.execute('UPDATE kuihraya2024 SET Red_Pearl = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][8]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Red_Pearl = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                elif i == 'Semperit':
                    quantity = list_addkuih[i]
                    addprice = 32
                    newaddprice = addprice*quantity
                    if a[0][9] == None:
                        cur.execute('UPDATE kuihraya2024 SET Semperit = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][9]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Semperit = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                elif i == 'Suji':
                    quantity = list_addkuih[i]
                    addprice = 30
                    newaddprice = addprice*quantity
                    if a[0][10] == None:
                        cur.execute('UPDATE kuihraya2024 SET Suji = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][10]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Suji = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                elif i == 'Tart_Nenas':
                    quantity = list_addkuih[i]
                    addprice = 35
                    newaddprice = addprice*quantity
                    if a[0][11] == None:
                        cur.execute('UPDATE kuihraya2024 SET Tart_Nenas = (?) WHERE Customer = (?)', (quantity, self.customer))
                        con.commit()
                    else:
                        new_quantity = int(a[0][11]) + quantity
                        cur.execute('UPDATE kuihraya2024 SET Tart_Nenas = (?) WHERE Customer = (?)', (new_quantity, self.customer))
                        con.commit()
                total_addon = total_addon + newaddprice
            new_total = total + total_addon
            new_depo = depo + float(self.adddeposit)
            new_balance = new_total - new_depo
            cur.execute('UPDATE kuihraya2024 SET Total = (?), Deposit = (?), Balance = (?) WHERE Customer = (?)', (new_total, new_depo, new_balance, self.customer))
            con.commit()
            self.ui3.W3TotalAddOn.setText('RM' + str(total_addon))
            self.ui3.W3Total.setText('RM' + str(new_total))
            self.ui3.W3CurDepo.setText('RM' + str(depo))
            self.ui3.W3Balance.setText('RM' + str(new_balance))

class Window4(QMainWindow): #Preview Customer's Order
    def __init__(self):
        super(Window4, self).__init__()
        self.ui4 = Ui_PreviewOrderW4()
        self.ui4.setupUi(self)
        self.ui4.actionlist_kuih_raya.triggered.connect(newWindow1)
        self.ui4.actionnew_order.triggered.connect(newWindow2)
        self.ui4.actionupdate_order.triggered.connect(newWindow3)
        self.ui4.actionpreview_stocks.triggered.connect(newWindow5)
        self.ui4.PreviewOrderW4Button.clicked.connect(self.previewW4)
        self.ui4.tableWidget.setColumnWidth(0,160)
        self.ui4.tableWidget.setColumnWidth(1,160)

    def previewW4(self):
        self.customer = self.ui4.CustomerNameInputW4.text()
        cur.execute("SELECT * FROM kuihraya2024 WHERE Customer =?", (self.customer,)) # this parameter need to be in tuple
        a = cur.fetchall()
        if a == []:
            showerror("Preview Order Failed","Customer's Name Do Not Exist in Database")
        else:
            df = pd.read_sql_query("SELECT * FROM kuihraya2024 WHERE Customer =?",con, params=(self.customer,))
            df1 = df.dropna(axis=1)
            column_name = list(df1.columns)
            kuih_order = column_name[2:-3]
            order_list = []
            for i in kuih_order:
                new = {'kuih raya': i, 'quantity': df1.loc[0,i]}
                order_list.append(new)
            row = 0
            self.ui4.tableWidget.setRowCount(len(order_list))
            for kuih in order_list:
                self.ui4.tableWidget.setItem(row, 0, QTableWidgetItem(kuih['kuih raya']))
                self.ui4.tableWidget.setItem(row, 1, QTableWidgetItem(str(kuih['quantity'])))
                row = row + 1
            self.ui4.TotalW4.setText('RM' + str(df1.loc[0,'Total']))
            self.ui4.DepoW4.setText('RM' + str(df1.loc[0,'Deposit']))
            self.ui4.BalanceW4.setText('RM' + str(df1.loc[0,'Balance']))

class Window5(QMainWindow): #Preview Stock's Order
    def __init__(self):
        super(Window5, self).__init__()
        self.ui5 = Ui_PreviewStocksW5()
        self.ui5.setupUi(self)
        self.ui5.actionlist_kuih_raya.triggered.connect(newWindow1)
        self.ui5.actionnew_order.triggered.connect(newWindow2)
        self.ui5.actionupdate_order.triggered.connect(newWindow3)
        self.ui5.actionpreview_order.triggered.connect(newWindow4)
        self.ui5.PreviewStocksW5Button.clicked.connect(self.previewW5)
        self.ui5.tableWidget.setColumnWidth(0,160)
        self.ui5.tableWidget.setColumnWidth(1,160)

    def previewW5(self):
        self.chosen_kuih = self.ui5.ChosenKuihW5.currentText()
        df2 = pd.read_sql_query("SELECT * FROM kuihraya2024",con)
        if self.chosen_kuih == 'All':
            kuihraya24 = ('Almond_London', 'Cookies', 'Cornflakes_Crunchy', 'Dahlia', 'Makmur', 'Rainbow', 'Red_Pearl', 'Semperit', 'Suji', 'Tart_Nenas')
            #df2 = pd.read_sql_query("SELECT COALESCE(SUM(%s + %s + %s + %s + %s + %s+ %s + %s+ %s+ %s),0) FROM kuihraya2024"%(kuihraya24),con)
            all_orderlist = []
            jumlah = 0
            for i in kuihraya24:
                dfquantity_eachkuih = pd.read_sql_query("SELECT COALESCE(SUM(%s),0) AS Total FROM kuihraya2024" %(i),con)
                new = {'kuih raya': i, 'quantity': dfquantity_eachkuih.loc[0, 'Total']}
                all_orderlist.append(new)
                jumlah = jumlah + dfquantity_eachkuih.loc[0, 'Total']
            self.ui5.tableWidget.setRowCount(len(all_orderlist)+1)
            list_total_kuih = {'kuih raya': 'All', 'quantity': jumlah}
            self.ui5.tableWidget.setItem(0, 0, QTableWidgetItem(list_total_kuih['kuih raya']))
            self.ui5.tableWidget.setItem(0, 1, QTableWidgetItem(str(list_total_kuih['quantity'])))
            row = 1
            for kuih in all_orderlist:
                self.ui5.tableWidget.setItem(row, 0, QTableWidgetItem(kuih['kuih raya']))
                self.ui5.tableWidget.setItem(row, 1, QTableWidgetItem(str(kuih['quantity'])))
                row = row + 1
        else:
            dfquantity_eachkuih = pd.read_sql_query("SELECT COALESCE(SUM(%s),0) AS Total FROM kuihraya2024" %(self.chosen_kuih),con)
            display = {'kuih raya': self.chosen_kuih, 'quantity': dfquantity_eachkuih.loc[0,'Total']}
            self.ui5.tableWidget.setRowCount(len(display))
            self.ui5.tableWidget.setItem(0, 0, QTableWidgetItem(display['kuih raya']))
            self.ui5.tableWidget.setItem(0, 1, QTableWidgetItem(str(display['quantity'])))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    def newWindow1(self): 
        window = MainWindow()
        widget.addWidget(window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def newWindow2(self, ):
        window2 = Window2()
        widget.addWidget(window2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def newWindow3(self):
        window3 = Window3()
        widget.addWidget(window3)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def newWindow4(self):
        window4 = Window4()
        widget.addWidget(window4)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def newWindow5(self):
        window5 = Window5()
        widget.addWidget(window5)
        widget.setCurrentIndex(widget.currentIndex()+1)

    window = MainWindow()
    widget = QStackedWidget()
    widget.addWidget(window)
    widget.setFixedHeight(551)
    widget.setFixedWidth(400)
    widget.show()

    sys.exit(app.exec())