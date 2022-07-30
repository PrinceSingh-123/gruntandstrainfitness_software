from PySide2.QtWidgets import (
    QApplication, QFileDialog, QTableWidgetItem, QDialog, QHeaderView,
    QLabel, QPushButton, QVBoxLayout, QMainWindow
)
from PySide2.QtGui import QPixmap, QIcon, QCursor, QPalette, QColor
from PySide2.QtUiTools import loadUiType
from PySide2.QtCore import QDate, QPersistentModelIndex, Qt
from datetime import datetime, timedelta 
import sqlite3
import sys

# custome modules
from gym.MainWindow import Ui_MainWindow
import gym.resources_rc as resources_rc
import gym.user as user
import gym.attendance as atn
import gym.expense as exp
import gym.revenue as rvn
import gym.staff as stf
from gym.utils import check_email
from pathlib import Path

app = QApplication(sys.argv)

# code for connecting sqlite database
resources_folder = Path(__file__).joinpath("../resources").resolve()
db_filepath = resources_folder.joinpath("paradox.db")

# making the connection with database...
con = sqlite3.connect(db_filepath)

choice = {
    0: 'No',
    1: 'Yes'
}
paid = {
    0: 'No',
    1: 'Yes',
    2: 'Partially'
}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # setting the initial window title
        self.setWindowTitle("GruntAndStrainFitness")

        self.toggle_menu = True
        self.menuButton.clicked.connect(self.handle_toggle_menu)

        # connecting butttons to their slots
        self.homeButton.clicked.connect(self.connect_page)
        self.userButton.clicked.connect(self.connect_page)
        self.attendanceButton.clicked.connect(self.connect_page)
        self.expenseButton.clicked.connect(self.connect_page)
        self.revenueButton.clicked.connect(self.connect_page)
        self.staffButton.clicked.connect(self.connect_page)

        # Adding actual values in Home page
        self.total_users()
        self.total_staffs()
        self.total_expense()
        self.total_revenue()
        self.total_profit()

        # selection in total in days
        self.comboBox.currentIndexChanged.connect(self.days_changed)

        # setting up the calender widget
        self.dateEdit.setMaximumDate(QDate.currentDate())
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_2.setMaximumDate(QDate.currentDate())
        self.dateEdit_2.setDate(QDate.currentDate())
        self.dateEdit_2.hide()
        self.label_7.hide()
        self.radioButton.clicked.connect(self.handle_radio_button)
        self.dateEdit_2.dateChanged.connect(self.filter_date)

        # file selection pop up
        self.selectFileButton.clicked.connect(self.open_photo)

        # connecting to adding slots 
        self.addButton.clicked.connect(self.add_user)
        self.addButton_2.clicked.connect(self.add_attendance)
        self.addButton_3.clicked.connect(self.add_expense)
        self.addButton_4.clicked.connect(self.add_revenue)
        self.addButton_5.clicked.connect(self.add_staff)

        # connecting to canceling update slots
        self.cancelButton.clicked.connect(self.cancel_user_update)
        self.cancelButton_2.clicked.connect(self.cancel_attendance_update)
        self.cancelButton_3.clicked.connect(self.cancel_expense_update)
        self.cancelButton_4.clicked.connect(self.cancel_revenue_update)
        self.cancelButton_5.clicked.connect(self.cancel_staff_update)

        #resizing column header of membership type
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        #removing automatic indexing in table
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_5.verticalHeader().setVisible(False)

        # connecting payCancelButton  
        self.payCancelButton.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.create_page))

        # hiding update buttuns initially
        self.update_cancel_hide()

        #adding exixting users in table
        users = user.list_detail(con)
        if users:
            for usr in users:
                self.add_new_user(usr)         

        #adding existing attendance records in table
        attendances = atn.list_(con)
        if attendances:
            for attendance in attendances:
                self.add_new_attendance(attendance)

        #adding existing expense records in table
        expenses = exp.list_(con)
        if expenses:
            for expense in expenses:
                self.add_new_expense(expense)

        #adding existing revenue records in table
        revenues = rvn.list_(con)
        if revenues:
            for revenue in revenues:
                self.add_new_revenue(revenue)

        #adding existing revenue records in table
        staffs = stf.list_(con)
        if staffs:
            for staff in staffs:
                self.add_new_staff(staff)

    def filter_date(self):
        day = self.dateEdit_2.date().toString('yyyy-MM-dd')
        rowPosition = self.tableWidget_2.rowCount()
        for i in reversed(range(rowPosition)):
            self.tableWidget_2.removeRow(i)
        attendances = atn.list_in_date(con,day)
        if attendances:
            for attendance in attendances:
                self.add_new_attendance(attendance)

    def handle_radio_button(self):
        if self.radioButton.isChecked():
            self.dateEdit_2.show()
            self.label_7.show()
            rowPosition = self.tableWidget_2.rowCount()
            for i in reversed(range(rowPosition)):
                self.tableWidget_2.removeRow(i)
            day = self.dateEdit_2.date().toString('yyyy-MM-dd')
            attendances = atn.list_in_date(con,day)
            if attendances:
                for attendance in attendances:
                    self.add_new_attendance(attendance)
        else:
            self.dateEdit_2.hide()
            self.label_7.hide()
            rowPosition = self.tableWidget_2.rowCount()
            for i in reversed(range(rowPosition)):
                self.tableWidget_2.removeRow(i)
            attendances = atn.list_(con)
            if attendances:
                for attendance in attendances:
                    self.add_new_attendance(attendance)

    # function that connects the page to the button and change window title accordingly
    def connect_page(self):
        btn = self.sender().objectName()
        if btn == "homeButton":
            self.stackedWidget.setCurrentWidget(self.home_page)
            self.setWindowTitle('Office Management System - Home')
            self.total_users()
            self.total_staffs()
            self.total_expense()
            self.total_revenue()
            self.total_profit()
        if btn == "userButton":
            self.stackedWidget.setCurrentWidget(self.user_page)
            self.setWindowTitle('Office Management System - User')
        elif btn == "attendanceButton":
            self.stackedWidget.setCurrentWidget(self.attendance_page)
            self.usernameComboBox.clear()
            usernames = user.list_username(con)
            if usernames:
                for username in usernames:
                    self.usernameComboBox.addItem(username[0])
            self.setWindowTitle('Office Management System - Attendance')
        elif btn == "expenseButton":
            self.stackedWidget.setCurrentWidget(self.expense_page)
            self.setWindowTitle('Office Management System - Expense')
        elif btn == "revenueButton":
            self.stackedWidget.setCurrentWidget(self.revenue_page)
            self.setWindowTitle('Office Management System - Revenue')
        elif btn == "staffButton":
            self.stackedWidget.setCurrentWidget(self.staff_page)
            self.setWindowTitle('Office Management System - Staff')
    
    def open_photo(self):
        fileName = QFileDialog.getOpenFileName(self,app.tr("Open Image"), "/home/jeevan/Pictures", app.tr("Image Files (*.png *.jpg *.bmp)"))
        self.profilePicLineEdit.setText(fileName[0])

    def handle_toggle_menu(self):
        if not self.toggle_menu:
            self.homeButton.setText('')
            self.userButton.setText('')
            self.attendanceButton.setText('')
            self.expenseButton.setText('')
            self.revenueButton.setText('')
            self.staffButton.setText('')
            self.toggle_menu = True
        else:
            self.homeButton.setText('Home')
            self.userButton.setText('User')
            self.attendanceButton.setText('Attendance')
            self.expenseButton.setText('Expanse')
            self.revenueButton.setText('Revenue')
            self.staffButton.setText('Staff')
            self.toggle_menu = False

    def days_changed(self):
        self.total_expense()
        self.total_revenue()
        self.total_profit()
    
    def update_cancel_hide(self):
        self.updateButton.hide()
        self.updateButton_2.hide()
        self.updateButton_3.hide()
        self.updateButton_4.hide()
        self.updateButton_5.hide()
        self.cancelButton.hide()
        self.cancelButton_2.hide()
        self.cancelButton_3.hide()
        self.cancelButton_4.hide()
        self.cancelButton_5.hide()

    def cancel_user_update(self):
        self.clear_user_field()
        self.updateButton.hide()
        self.cancelButton.hide()
        self.addButton.show()

    def cancel_attendance_update(self):
        self.clear_attendance_fields()
        self.updateButton_2.hide()
        self.cancelButton_2.hide()
        self.addButton_2.show()

    def cancel_expense_update(self):
        self.clear_expense_fields()
        self.updateButton_3.hide()
        self.cancelButton_3.hide()
        self.addButton_3.show()

    def cancel_revenue_update(self):
        self.clear_revenue_fields()
        self.updateButton_4.hide()
        self.cancelButton_4.hide()
        self.addButton_4.show()

    def cancel_staff_update(self):
        self.clear_staff_fields()
        self.updateButton_5.hide()
        self.cancelButton_5.hide()
        self.addButton_5.show()

    def add_user(self):
        usr = {}
        usr['username'] = self.usernameLineEdit.text()
        usr['email'] = self.emailLineEdit.text()
        usr['membership_type'] = self.membershipTypecomboBox.currentText()
        usr['name'] = self.nameLineEdit.text()
        age = self.ageLineEdit.text()
        if age:
            usr['age'] = age
        address = self.addressLineEdit.text()
        if address:
            usr['address'] = address
        bio = self.bioLineEdit.text()
        if bio:
            usr['bio'] = bio
        profile_pic = self.profilePicLineEdit.text()
        if profile_pic:
            usr['profile_pic'] = profile_pic
        try:
            newUser = user.create(con, usr)
            self.add_new_user(newUser)
            self.clear_user_field()
        except Exception as e:
            print(e)

    def add_attendance(self):
        attendance = {}
        attendance['user'] = self.usernameComboBox.currentText()
        attendance['present'] = self.presentComboBox.currentIndex()
        newAttendance = atn.create(con,attendance)
        self.add_new_attendance(newAttendance)
        self.clear_attendance_fields()

    def add_expense(self):
        expanse = {}
        title = self.titleLineEdit.text()
        if title:
            expanse['title'] = title
        else:
            print('Title required')
        purpose = self.purposeLineEdit.text()
        if purpose:
            expanse['purpose'] = purpose
        else:
            print('Purpose required')
        amount = self.amountLineEdit.text()
        if amount:
            expanse['amount'] = amount
        else:
            print('Amount required')
        description = self.descriptionTextEdit.toPlainText()
        if description:
            expanse['description'] = description
        newExpense = exp.create(con,expanse)
        self.add_new_expense(newExpense)
        self.clear_expense_fields()

    def add_revenue(self):
        revenue = {}
        title = self.titleLineEdit_2.text()
        if title:
            revenue['title'] = title
        else:
            print('Title required')
        source = self.sourceLineEdit_2.text()
        if source:
            revenue['source'] = source
        else:
            print('Source required')
        amount = self.amountLineEdit_2.text()
        if amount:
            revenue['amount'] = amount
        else:
            print('Amount required')
        description = self.descriptionTextEdit_2.toPlainText()
        if description:
            revenue['description'] = description
        newRevenue = rvn.create(con,revenue)
        self.add_new_revenue(newRevenue)
        self.clear_revenue_fields()

    def add_staff(self):
        staff = {}
        name = self.nameLineEdit_2.text()
        if name:
            staff['name'] = name
        else:
            print('Name required')
        position = self.positionLineEdit.text()
        if position:
            staff['position']= position
        else:
            print('Position required')
        salary = self.salaryLineEdit.text()
        if salary:
            staff['salary'] = salary
        else:
            print('Salary required')
        date_joined = self.dateEdit.date().toString('yyyy-MM-dd')
        if date_joined:
            staff['date_joined'] = date_joined
        try:
            newStaff = stf.create(con,staff)
            self.add_new_staff(newStaff)
            self.clear_staff_fields()
        except Exception as e:
            print(str(e))

    # adding value to the table widget cell
    def create_table_widget(self,rowPosition,columnPosition,text,tableName, type=None):
        if type == "image":
            if text:
                viewbtn=QPushButton(getattr(self,tableName))
                viewbtn.setText('View')
                viewbtn.setCursor(QCursor(Qt.PointingHandCursor))
                index = QPersistentModelIndex(getattr(self,tableName).model().index(rowPosition, columnPosition))
                getattr(self,tableName).setCellWidget(rowPosition,columnPosition,viewbtn)
                viewbtn.clicked.connect(
                    lambda *args,index=index, data=text: self.view_pic(index,data))
        elif text:
            qtablewidgetitem = QTableWidgetItem()
            getattr(self,tableName).setItem(rowPosition,columnPosition,qtablewidgetitem)
            qtablewidgetitem=getattr(self,tableName).item(rowPosition,columnPosition)
            qtablewidgetitem.setText(str(text))

    # function for viewing image in dialog box
    def view_pic(self,index,data):
        model = self.tableWidget.model()
        username = model.data(model.index(index.row(), 0))
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Viewing {username} profile pic")
        curQImage = QPixmap()
        curQImage.loadFromData(data) 
        lbl = QLabel()
        lbl.setPixmap(curQImage)
        layout = QVBoxLayout()
        layout.addWidget(lbl)
        dialog.setLayout(layout)
        size = layout.geometry()
        dialog.setFixedSize(size.size())
        dialog.show()

    def add_pay_btn(self, rowPosition, columnPosition, qtablewidget):
        paybtn=QPushButton(qtablewidget)
        paybtn.setText('Pay')
        paybtn.setCursor(QCursor(Qt.PointingHandCursor))
        qtablewidget.setCellWidget(rowPosition,columnPosition-3,paybtn)
        index = QPersistentModelIndex(
            qtablewidget.model().index(rowPosition, columnPosition-3))
        paybtn.clicked.connect(
            lambda *args,qtablewidget=qtablewidget,index=index: self.edit_pay(index,qtablewidget))

    def edit_pay(self,index,qtablewidget):
        model = qtablewidget.model()
        id = model.data(model.index(index.row(), 0))
        payDetail = stf.req_pay(con,id)
        self.stackedWidget_2.setCurrentWidget(self.pay_page)
        self.pay_heading.setText(f"Paying {payDetail[1]}({payDetail[0]}) and Due Amount is {payDetail[2]}")
        self.payButton.clicked.connect(lambda index=index,id=id,due_amount=payDetail[2]: self.pay_staff(index,id,due_amount))

    def pay_staff(self,index,id,due_amount):
        staff = {}
        expense = {}
        amount = self.amountEdit.text()
        if not amount or amount == '0':
            print("Enter some amount")
        else:
            amount = float(amount)
            if amount > due_amount:
                print("Amount should be less than or equal to due amount")
            else:
                newDueAmount = due_amount-amount
                staff['due_amount'] = newDueAmount
                if newDueAmount == 0:
                    staff['paid'] = 1
                else:
                    staff['paid'] = 2
                try:
                    updated_staff = stf.update(con,id,staff)
                    if updated_staff:
                        expense['title'] = f"pay salary to {updated_staff[1]}"
                        expense['purpose'] = "salary paid"
                        expense['amount'] = amount
                        description = self.descriptionTextEdit_3.toPlainText()
                        if description:
                            expense['description'] = description
                        newExpense = exp.create(con,expense)
                        self.add_new_expense(newExpense)
                        self.descriptionTextEdit_3.setText('')
                        if index.isValid():
                            self.tableWidget_5.removeRow(index.row())
                            self.add_new_staff(updated_staff)
                            self.amountEdit.setText('')
                            self.stackedWidget_2.setCurrentWidget(self.create_page)
                except Exception as e:
                    print(str(e))

    #function that add delete button on row
    def add_edit_btn(self, rowPosition, columnPosition, qtablewidget):
        edtbtn=QPushButton(qtablewidget)
        edtbtn.setText('Edit')
        icon = QIcon(':/icons/icons/book.png')
        edtbtn.setIcon(icon)
        edtbtn.setCursor(QCursor(Qt.PointingHandCursor))
        qtablewidget.setCellWidget(rowPosition,columnPosition-2,edtbtn)
        index = QPersistentModelIndex(
            qtablewidget.model().index(rowPosition, columnPosition-1))
        edtbtn.clicked.connect(
            lambda *args,qtablewidget=qtablewidget,index=index: self.edit_row(index,qtablewidget))

    def edit_row(self, index, qtablewidget):
        model = qtablewidget.model()
        if qtablewidget == self.tableWidget:
            username = model.data(model.index(index.row(), 0))
            self.fill_user_form(username)
            self.updateButton.clicked.connect(lambda *args,index=index: self.update_user(index))
        elif qtablewidget == self.tableWidget_2:
            username = model.data(model.index(index.row(), 0))
            day = model.data(model.index(index.row(), 1))
            self.fill_attendance_form(username,day)
            self.updateButton_2.clicked.connect(lambda *args,index=index,day=day: self.update_attendance(index, day))
        elif qtablewidget == self.tableWidget_3:
            id = model.data(model.index(index.row(), 0))
            self.fill_expense_form(id)
            self.updateButton_3.clicked.connect(lambda *args,index=index,id=id: self.update_expense(index,id))
        elif qtablewidget == self.tableWidget_4:
            id = model.data(model.index(index.row(), 0))
            self.fill_revenue_form(id)
            self.updateButton_4.clicked.connect(lambda *args,index=index,id=id: self.update_revenue(index,id))
        elif qtablewidget == self.tableWidget_5:
            id = model.data(model.index(index.row(), 0))
            self.fill_staff_form(id)
            self.updateButton_5.clicked.connect(lambda *args,index=index,id=id: self.update_staff(index,id))
        
    def fill_user_form(self, username):
        self.addButton.hide()
        self.updateButton.show()
        self.cancelButton.show()
        self.usernameLineEdit.setReadOnly(True)
        usr = user.single_detail(con, username)
        self.usernameLineEdit.setText(usr[0])
        self.emailLineEdit.setText(usr[1])
        self.membershipTypecomboBox.setCurrentText(usr[3])
        self.nameLineEdit.setText(usr[2])
        if usr[4]:
            self.ageLineEdit.setText(str(usr[4]))
        if usr[5]:
            self.addressLineEdit.setText(usr[5])
        if usr[7]:
            self.bioLineEdit.setText(usr[7])

    def fill_attendance_form(self,username,day):
        self.addButton_2.hide()
        self.updateButton_2.show()
        self.cancelButton_2.show()
        attendance = atn.detail(con,username,day)
        self.usernameComboBox.activated.connect(lambda *args,username=username: self.on_combo_change(username=username))
        self.usernameComboBox.setCurrentText(username)
        self.presentComboBox.setCurrentIndex(attendance[2])

    def fill_expense_form(self,id):
        self.addButton_3.hide()
        self.updateButton_3.show()
        self.cancelButton_3.show()
        expense = exp.detail(con,id)
        self.titleLineEdit.setText(expense[1])
        self.purposeLineEdit.setText(expense[2])
        self.amountLineEdit.setText(str(expense[3]))
        if expense[4]:
            self.descriptionTextEdit.setText(expense[4])

    def fill_revenue_form(self,id):
        self.addButton_4.hide()
        self.updateButton_4.show()
        self.cancelButton_4.show()
        revenue = rvn.detail(con,id)
        self.titleLineEdit_2.setText(revenue[1])
        self.sourceLineEdit_2.setText(revenue[2])
        self.amountLineEdit_2.setText(str(revenue[3]))
        if revenue[4]:
            self.descriptionTextEdit_2.setText(revenue[4])

    def fill_staff_form(self,id):
        self.addButton_5.hide()
        self.updateButton_5.show()
        self.cancelButton_5.show()
        staff = stf.detail(con,id)
        self.nameLineEdit_2.setText(staff[1])
        self.positionLineEdit.setText(staff[2])
        self.salaryLineEdit.setText(str(staff[3]))
        self.dateEdit.setDate(QDate.fromString(staff[4], 'yyyy-MM-dd'))

    def on_combo_change(self, username):
        self.usernameComboBox.setCurrentText(username)

    def add_new_user(self, newUser):
        rowPosition=self.tableWidget.rowCount()
        columnPosition=self.tableWidget.columnCount()
        self.tableWidget.insertRow(rowPosition)
        for index,val in enumerate(newUser):
            if index == 6:
                self.create_table_widget(rowPosition, index, val, 'tableWidget', 'image')
            else:
                self.create_table_widget(rowPosition, index, val, 'tableWidget')
        self.add_edit_btn(rowPosition, columnPosition, self.tableWidget)
        self.add_delete_btn(rowPosition, columnPosition, self.tableWidget)

    def add_new_attendance(self,newAttendance):
        rowPosition=self.tableWidget_2.rowCount()
        columnPosition=self.tableWidget_2.columnCount()
        self.tableWidget_2.insertRow(rowPosition)
        for index, val in enumerate(newAttendance):
            if index == 2:
                self.create_table_widget(rowPosition, index, choice[val], 'tableWidget_2')
            else:
                self.create_table_widget(rowPosition, index, val, 'tableWidget_2')
        self.add_edit_btn(rowPosition, columnPosition, self.tableWidget_2)
        self.add_delete_btn(rowPosition, columnPosition, self.tableWidget_2)

    def add_new_expense(self,expense):
        rowPosition=self.tableWidget_3.rowCount()
        columnPosition = self.tableWidget_3.columnCount()
        self.tableWidget_3.insertRow(rowPosition)
        for index, val in enumerate(expense):
            self.create_table_widget(rowPosition, index, val, 'tableWidget_3')
        # adding edit btn
        self.add_edit_btn(rowPosition,columnPosition,self.tableWidget_3)
        # adding delete btn
        self.add_delete_btn(rowPosition,columnPosition,self.tableWidget_3)

    def add_new_revenue(self,revenue):
        rowPosition=self.tableWidget_4.rowCount()
        columnPosition = self.tableWidget_4.columnCount()
        self.tableWidget_4.insertRow(rowPosition)
        for index, val in enumerate(revenue):
            self.create_table_widget(rowPosition, index, val, 'tableWidget_4')
        # adding edit btn
        self.add_edit_btn(rowPosition,columnPosition,self.tableWidget_4)
        # adding delete btn
        self.add_delete_btn(rowPosition,columnPosition,self.tableWidget_4)

    def add_new_staff(self,staff):
        rowPosition=self.tableWidget_5.rowCount()
        columnPosition = self.tableWidget_5.columnCount()
        self.tableWidget_5.insertRow(rowPosition)
        if staff[7]:
            days_dif = (datetime.now().date()-datetime.strptime(staff[7],'%Y-%m-%d').date()).days
            if days_dif >= 30:
                amount = (staff[3]*(days_dif//30))+(staff[5] or 0)
                day = (datetime.strptime(staff[7],'%Y-%m-%d')+timedelta(days=30*(days_dif//30))).date().strftime('%Y-%m-%d')
                staff = stf.generate_due(con,staff[0],amount,day)        
        else:
            days_dif = (datetime.now().date()-datetime.strptime(staff[4],'%Y-%m-%d').date()).days
            if days_dif >= 30:
                amount = (staff[3]*(days_dif//30))+(staff[5] or 0)
                day = (datetime.strptime(staff[4],'%Y-%m-%d')+timedelta(days=30*(days_dif//30))).date().strftime('%Y-%m-%d')
                staff = stf.generate_due(con,staff[0],amount,day)
        for index, val in enumerate(staff):
            if index == 6:
                self.create_table_widget(rowPosition, index, paid[val], 'tableWidget_5')
            else:
                self.create_table_widget(rowPosition, index, val, 'tableWidget_5')
        if staff[5]:
            self.add_pay_btn(rowPosition,columnPosition,self.tableWidget_5)
        # adding edit btn
        self.add_edit_btn(rowPosition,columnPosition,self.tableWidget_5)
        # adding delete btn
        self.add_delete_btn(rowPosition,columnPosition,self.tableWidget_5)

    # functions for clearing fields in successful addition 
    def clear_user_field(self):
        self.usernameLineEdit.clear()
        self.emailLineEdit.clear()
        self.membershipTypecomboBox.setCurrentIndex(0)
        self.nameLineEdit.clear()
        self.ageLineEdit.clear()
        self.addressLineEdit.clear()
        self.bioLineEdit.clear()
        self.profilePicLineEdit.clear()

    def clear_attendance_fields(self):
        self.usernameComboBox.setCurrentIndex(0)
        self.presentComboBox.setCurrentIndex(0)

    def clear_expense_fields(self):
        self.titleLineEdit.setText('')
        self.purposeLineEdit.setText('')
        self.amountLineEdit.setText('')
        self.descriptionTextEdit.setText('')

    def clear_revenue_fields(self):
        self.titleLineEdit_2.setText('')
        self.sourceLineEdit_2.setText('')
        self.amountLineEdit_2.setText('')
        self.descriptionTextEdit_2.setText('')

    def clear_staff_fields(self):
        self.nameLineEdit_2.setText('')
        self.positionLineEdit.setText('')
        self.salaryLineEdit.setText('')
        self.dateEdit.setDate(QDate.currentDate())

    def update_user(self, index):
        usr = {}
        username = self.usernameLineEdit.text()
        usr['email'] = self.emailLineEdit.text()
        usr['membership_type'] = self.membershipTypecomboBox.currentText()
        usr['name'] = self.nameLineEdit.text()
        age = self.ageLineEdit.text()
        if age:
            usr['age'] = age
        address = self.addressLineEdit.text()
        if address:
            usr['address'] = address
        bio = self.bioLineEdit.text()
        if bio:
            usr['bio'] = bio
        profile_pic = self.profilePicLineEdit.text()
        if profile_pic:
            usr['profile_pic'] = profile_pic
        try:
            updated_user = user.update(con, username, usr)
            if updated_user and index.isValid():
                self.tableWidget.removeRow(index.row())
                self.add_new_user(updated_user)
                self.clear_user_field()
                self.updateButton.hide()
                self.cancelButton.hide()
                self.addButton.show()
                self.usernameLineEdit.setReadOnly(False)
        except Exception as e:
            print(str(e))

    def update_attendance(self,index,day):
        username = self.usernameComboBox.currentText()
        present = self.presentComboBox.currentIndex()
        try:
            updated_attendance = atn.update(con,username,day,present)
            if updated_attendance and index.isValid():
                self.tableWidget_2.removeRow(index.row())
                self.add_new_attendance(updated_attendance)
                self.clear_attendance_fields()
                self.updateButton_2.hide()
                self.cancelButton_2.hide()
                self.addButton_2.show()
                self.usernameComboBox.activated.disconnect()
        except Exception as e:
            print(str(e))

    def update_expense(self,index, id):
        expanse = {}
        title = self.titleLineEdit.text()
        if title:
            expanse['title'] = title
        else:
            print('Title required')
        purpose = self.purposeLineEdit.text()
        if purpose:
            expanse['purpose'] = purpose
        else:
            print('Purpose required')
        amount = self.amountLineEdit.text()
        if amount:
            expanse['amount'] = amount
        else:
            print('Amount required')
        expanse['description'] = self.descriptionTextEdit.toPlainText()
        try:
            updated_expense = exp.update(con,id,expanse)
            if updated_expense and index.isValid():
                self.tableWidget_3.removeRow(index.row())
                self.add_new_expense(updated_expense)
                self.clear_expense_fields()
                self.updateButton_3.hide()
                self.cancelButton_3.hide()
                self.addButton_3.show()
        except Exception as e:
            print(str(e))

    def update_revenue(self,index, id):
        revenue = {}
        title = self.titleLineEdit_2.text()
        if title:
            revenue['title'] = title
        else:
            print('Title required')
        source = self.sourceLineEdit_2.text()
        if source:
            revenue['source'] = source
        else:
            print('Source required')
        amount = self.amountLineEdit_2.text()
        if amount:
            revenue['amount'] = amount
        else:
            print('Amount required')
        revenue['description'] = self.descriptionTextEdit_2.toPlainText()
        try:
            updated_revenue = rvn.update(con,id,revenue)
            if updated_revenue and index.isValid():
                self.tableWidget_4.removeRow(index.row())
                self.add_new_revenue(updated_revenue)
                self.clear_revenue_fields()
                self.updateButton_4.hide()
                self.cancelButton_4.hide()
                self.addButton_4.show()
        except Exception as e:
            print(str(e))

    def update_staff(self,index,id):
        staff = {}
        name = self.nameLineEdit_2.text()
        if name:
            staff['name'] = name
        else:
            print('Name required')
        position = self.positionLineEdit.text()
        if position:
            staff['position']= position
        else:
            print('Position required')
        salary = self.salaryLineEdit.text()
        if salary:
            staff['salary'] = salary
        else:
            print('Salary required')
        staff['date_joined'] = self.dateEdit.date().toString('yyyy-MM-dd')
        try:
            updated_staff = stf.update(con,id,staff)
            if updated_staff and index.isValid():
                self.tableWidget_5.removeRow(index.row())
                self.add_new_staff(updated_staff)
                self.clear_staff_fields()
                self.updateButton_5.hide()
                self.cancelButton_5.hide()
                self.addButton_5.show()
        except Exception as e:
            print(str(e))

    #function that add delete button on row
    def add_delete_btn(self, rowPosition, columnPosition, qtablewidget):
        dltbtn=QPushButton(qtablewidget)
        dltbtn.setText('Delete')
        icon = QIcon(':/icons/icons/bin.png')
        dltbtn.setIcon(icon)
        dltbtn.setCursor(QCursor(Qt.PointingHandCursor))
        qtablewidget.setCellWidget(rowPosition,columnPosition-1,dltbtn)
        index = QPersistentModelIndex(
            qtablewidget.model().index(rowPosition, columnPosition-1))
        dltbtn.clicked.connect(
            lambda *args,qtablewidget=qtablewidget,index=index: self.delete_row(index,qtablewidget))
    
    def delete_row(self, index, qtablewidget):
        model = qtablewidget.model()
        if qtablewidget == self.tableWidget:
            username = model.data(model.index(index.row(), 0))
            deleted = user.delete(con, username)
        elif qtablewidget == self.tableWidget_2:
            username = model.data(model.index(index.row(), 0))
            day = model.data(model.index(index.row(), 1))
            deleted = atn.delete(con,username,day)
        elif qtablewidget == self.tableWidget_3:
            id = model.data(model.index(index.row(), 0))
            deleted = exp.delete(con,id)
        elif qtablewidget == self.tableWidget_4:
            id = model.data(model.index(index.row(), 0))
            deleted = rvn.delete(con,id)
        elif qtablewidget == self.tableWidget_5:
            id = model.data(model.index(index.row(), 0))
            deleted = stf.delete(con,id)
        if index.isValid() and deleted:
            qtablewidget.removeRow(index.row())

    def total_users(self):
        total = user.list_username(con) or 0
        if total:
            self.num_users.setText(str(len(total)))

    def total_staffs(self):
        total = stf.list_(con) or 0
        if total:
            self.num_staffs.setText(str(len(total)))

    def total_expense(self):
        text = self.comboBox.currentText()
        if text == "Grand Total":
            total = exp.total(con) or 0
        elif text == "Last 30 days":
            total = exp.total_in_days(con,30) or 0
        elif text == "Last 365 days":
            total = exp.total_in_days(con,365) or 0
        if total:
            self.totalExpense.setText(str(total))

    def total_revenue(self):
        text = self.comboBox.currentText()
        if text == "Grand Total":
            total = rvn.total(con) or 0
        elif text == "Last 30 days":
            total = rvn.total_in_days(con,30) or 0
        elif text == "Last 365 days":
            total = rvn.total_in_days(con,365) or 0
        if total:
            self.totalRevenue.setText(str(total))

    def total_profit(self):
        text = self.comboBox.currentText()
        if text == "Grand Total":
            total_exp = exp.total(con) or 0
            total_rvn = rvn.total(con) or 0
        elif text == "Last 30 days":
            total_exp = exp.total_in_days(con,30) or 0
            total_rvn = rvn.total_in_days(con,30) or 0
        elif text == "Last 365 days":
            total_exp = exp.total_in_days(con,365) or 0
            total_rvn = rvn.total_in_days(con,365) or 0
        if total_exp or total_rvn:
            total_pft = total_rvn - total_exp
            if total_pft < 0:
                self.label_5.setText('Total Lose:')
                total_pft = abs(total_pft)
            else:
                self.label_5.setText('Total Profit:')
            self.totalProfit.setText(str(total_pft))

# appliying dark theme to the app
darkPalette = QPalette()
darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
darkPalette.setColor(QPalette.WindowText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor
(127, 127, 127))
darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
darkPalette.setColor(QPalette.ToolTipText, Qt.white)
darkPalette.setColor(QPalette.Text, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(127,
127, 127))
darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
darkPalette.setColor(QPalette.ButtonText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor
(127, 127, 127))
darkPalette.setColor(QPalette.BrightText, Qt.red)
darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80,
80, 80))
darkPalette.setColor(QPalette.HighlightedText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
QColor(127, 127, 127))  
app.setPalette(darkPalette)
app.setStyle('Fusion')


def main():
    window = MainWindow()
    window.show()
    app.exec_()