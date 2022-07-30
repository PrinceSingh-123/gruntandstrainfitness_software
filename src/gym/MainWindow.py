# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import gym.resources_rc as resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setStyleSheet(u"QPushButton[text='Add']{\n"
"	border: none;\n"
"	border-radius:5px;\n"
"	padding: 5px 8px;\n"
"	color:white;\n"
"	background-color: rgb(138, 226, 52);\n"
"	font-weight:bold;\n"
"}\n"
"QPushButton[text='Add']:hover{\n"
"	background-color: none;\n"
"	border: 1px solid rgb(138, 226, 52);\n"
"	color: rgb(138, 226, 52);\n"
"}\n"
"QPushButton[text='Update']{\n"
"	border: none;\n"
"	border-radius:5px;\n"
"	padding: 5px 8px;\n"
"	color:white;\n"
"	background-color: rgb(114, 159, 207);\n"
"	font-weight:bold;\n"
"}\n"
"QPushButton[text='Update']:hover{\n"
"	background-color: none;\n"
"	border: 1px solid rgb(114, 159, 207);\n"
"	color: rgb(114, 159, 207);\n"
"}\n"
"QPushButton[text='Cancel']{\n"
"	border: none;\n"
"	border-radius:5px;\n"
"	padding: 5px 8px;\n"
"	color:white;\n"
"	background-color: rgb(239, 41, 41);\n"
"	font-weight:bold;\n"
"}\n"
"QPushButton[text='Cancel']:hover{\n"
"	background-color: none;\n"
"	border: 1px solid rgb(239, 41, 41);\n"
"	color: rgb(239, 41, 41);\n"
"}\n"
"QPushButton[text='Delete']{\n"
""
                        "	border: none;\n"
"	border-radius:5px;\n"
"	padding: 5px 8px;\n"
"	color:white;\n"
"	background-color: rgb(204, 0, 0);\n"
"	font-weight:bold;\n"
"}\n"
"QPushButton[text='Delete']:hover{\n"
"	background-color: none;\n"
"	border: 1px solid rgb(204, 0, 0);\n"
"	color: rgb(204, 0, 0);\n"
"}\n"
"QPushButton[text='Edit']{\n"
"	border: none;\n"
"	border-radius:5px;\n"
"	padding: 5px 8px;\n"
"	color:white;\n"
"	background-color: rgb(52, 101, 164);\n"
"	font-weight:bold;\n"
"}\n"
"QPushButton[text='Edit']:hover{\n"
"	background-color: none;\n"
"	border: 1px solid rgb(52, 101, 164);\n"
"	color: rgb(52, 101, 164);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.option_frame_container = QFrame(self.centralwidget)
        self.option_frame_container.setObjectName(u"option_frame_container")
        self.option_frame_container.setStyleSheet(u"background-color: rgb(37, 37, 37)")
        self.option_frame_container.setFrameShape(QFrame.NoFrame)
        self.option_frame_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.option_frame_container)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.option_frame = QFrame(self.option_frame_container)
        self.option_frame.setObjectName(u"option_frame")
        self.option_frame.setStyleSheet(u"#option_frame QPushButton {\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	font-weight: bold;\n"
"	text-align: left;\n"
"	border: none;\n"
"	padding: 5px 8px;\n"
"}\n"
"#option_frame QPushButton:hover{\n"
"	background-color: rgb(85, 87, 83)\n"
"}")
        self.option_frame.setFrameShape(QFrame.NoFrame)
        self.option_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.option_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.option_frame)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuButton.setStyleSheet(u"background-color: transparent;\n"
"color: #fff;\n"
"")

        self.verticalLayout.addWidget(self.menuButton)

        self.homeButton = QPushButton(self.option_frame)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.homeButton)

        self.userButton = QPushButton(self.option_frame)
        self.userButton.setObjectName(u"userButton")
        self.userButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userButton.setIcon(icon1)
        self.userButton.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.userButton)

        self.attendanceButton = QPushButton(self.option_frame)
        self.attendanceButton.setObjectName(u"attendanceButton")
        self.attendanceButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/calendar-month.png", QSize(), QIcon.Normal, QIcon.Off)
        self.attendanceButton.setIcon(icon2)
        self.attendanceButton.setIconSize(QSize(26, 26))

        self.verticalLayout.addWidget(self.attendanceButton)

        self.expenseButton = QPushButton(self.option_frame)
        self.expenseButton.setObjectName(u"expenseButton")
        self.expenseButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/receipt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expenseButton.setIcon(icon3)
        self.expenseButton.setIconSize(QSize(26, 26))

        self.verticalLayout.addWidget(self.expenseButton)

        self.revenueButton = QPushButton(self.option_frame)
        self.revenueButton.setObjectName(u"revenueButton")
        self.revenueButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/script.png", QSize(), QIcon.Normal, QIcon.Off)
        self.revenueButton.setIcon(icon4)
        self.revenueButton.setIconSize(QSize(26, 26))

        self.verticalLayout.addWidget(self.revenueButton)

        self.staffButton = QPushButton(self.option_frame)
        self.staffButton.setObjectName(u"staffButton")
        self.staffButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/user-business.png", QSize(), QIcon.Normal, QIcon.Off)
        self.staffButton.setIcon(icon5)
        self.staffButton.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.staffButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_21.addWidget(self.option_frame)


        self.horizontalLayout.addWidget(self.option_frame_container)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(13)
        self.stackedWidget.setFont(font)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_26 = QVBoxLayout(self.home_page)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 0, 0, 0)
        self.frame_25 = QFrame(self.home_page)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_25)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(50, 0, 100, 0)
        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy1.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy1)
        self.frame_30.setMinimumSize(QSize(0, 115))
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_18 = QFrame(self.frame_30)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_18)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.num_staffs = QLabel(self.frame_18)
        self.num_staffs.setObjectName(u"num_staffs")
        self.num_staffs.setMinimumSize(QSize(114, 47))
        self.num_staffs.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(18)
        self.num_staffs.setFont(font2)
        self.num_staffs.setStyleSheet(u"background-color: rgb(85, 87, 83);\n"
"color: rgb(243, 243, 243);")
        self.num_staffs.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.num_staffs)


        self.horizontalLayout_20.addWidget(self.frame_18, 0, Qt.AlignBottom)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)

        self.frame_17 = QFrame(self.frame_30)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_17)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label)

        self.num_users = QLabel(self.frame_17)
        self.num_users.setObjectName(u"num_users")
        self.num_users.setMinimumSize(QSize(114, 47))
        self.num_users.setMaximumSize(QSize(16777215, 50))
        self.num_users.setFont(font2)
        self.num_users.setStyleSheet(u"background-color: rgb(85, 87, 83);\n"
"color: rgb(243, 243, 243);")
        self.num_users.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.num_users)


        self.horizontalLayout_20.addWidget(self.frame_17, 0, Qt.AlignBottom)


        self.verticalLayout_39.addWidget(self.frame_30)

        self.frame_19 = QFrame(self.frame_25)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy2)
        self.frame_19.setMaximumSize(QSize(16777215, 400))
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_19)
        self.verticalLayout_38.setSpacing(6)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(9, 9, 9, 65)
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_22)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_6.setFont(font3)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.comboBox = QComboBox(self.frame_22)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 0))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.comboBox)


        self.verticalLayout_38.addWidget(self.frame_22, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.frame_28 = QFrame(self.frame_19)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_28)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_23)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_3)

        self.totalExpense = QLabel(self.frame_23)
        self.totalExpense.setObjectName(u"totalExpense")
        self.totalExpense.setMinimumSize(QSize(114, 0))
        self.totalExpense.setMaximumSize(QSize(16777215, 50))
        self.totalExpense.setFont(font2)
        self.totalExpense.setStyleSheet(u"background-color: rgb(85, 87, 83);\n"
"color: rgb(243, 243, 243);")
        self.totalExpense.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.totalExpense)


        self.horizontalLayout_13.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_28)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.label_4 = QLabel(self.frame_24)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.totalRevenue = QLabel(self.frame_24)
        self.totalRevenue.setObjectName(u"totalRevenue")
        self.totalRevenue.setMinimumSize(QSize(114, 0))
        self.totalRevenue.setMaximumSize(QSize(16777215, 50))
        self.totalRevenue.setFont(font2)
        self.totalRevenue.setStyleSheet(u"background-color: rgb(85, 87, 83);\n"
"color: rgb(243, 243, 243);")
        self.totalRevenue.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.totalRevenue)


        self.horizontalLayout_13.addWidget(self.frame_24)


        self.verticalLayout_38.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_19)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(220, 0))
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_29)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_5)

        self.totalProfit = QLabel(self.frame_29)
        self.totalProfit.setObjectName(u"totalProfit")
        self.totalProfit.setMaximumSize(QSize(16777215, 50))
        self.totalProfit.setFont(font2)
        self.totalProfit.setStyleSheet(u"background-color: rgb(85, 87, 83);\n"
"color: rgb(243, 243, 243);")
        self.totalProfit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.totalProfit)


        self.verticalLayout_38.addWidget(self.frame_29, 0, Qt.AlignHCenter)


        self.verticalLayout_39.addWidget(self.frame_19)


        self.verticalLayout_26.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.home_page)
        self.user_page = QWidget()
        self.user_page.setObjectName(u"user_page")
        self.verticalLayout_3 = QVBoxLayout(self.user_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.user_add_frame = QFrame(self.user_page)
        self.user_add_frame.setObjectName(u"user_add_frame")
        sizePolicy1.setHeightForWidth(self.user_add_frame.sizePolicy().hasHeightForWidth())
        self.user_add_frame.setSizePolicy(sizePolicy1)
        self.user_add_frame.setMaximumSize(QSize(600, 16777215))
        self.user_add_frame.setFrameShape(QFrame.NoFrame)
        self.user_add_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.user_add_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.user_add_title_frame = QFrame(self.user_add_frame)
        self.user_add_title_frame.setObjectName(u"user_add_title_frame")
        sizePolicy1.setHeightForWidth(self.user_add_title_frame.sizePolicy().hasHeightForWidth())
        self.user_add_title_frame.setSizePolicy(sizePolicy1)
        self.user_add_title_frame.setFrameShape(QFrame.NoFrame)
        self.user_add_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.user_add_title_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.user_add_title_frame)
        self.titleLabel.setObjectName(u"titleLabel")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(False)
        font4.setWeight(50)
        self.titleLabel.setFont(font4)
        self.titleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.titleLabel)


        self.verticalLayout_4.addWidget(self.user_add_title_frame)

        self.user_add_main_frame = QFrame(self.user_add_frame)
        self.user_add_main_frame.setObjectName(u"user_add_main_frame")
        sizePolicy2.setHeightForWidth(self.user_add_main_frame.sizePolicy().hasHeightForWidth())
        self.user_add_main_frame.setSizePolicy(sizePolicy2)
        self.user_add_main_frame.setFrameShape(QFrame.NoFrame)
        self.user_add_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.user_add_main_frame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.user_add_label_frame = QFrame(self.user_add_main_frame)
        self.user_add_label_frame.setObjectName(u"user_add_label_frame")
        self.user_add_label_frame.setFrameShape(QFrame.NoFrame)
        self.user_add_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.user_add_label_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.usenameLable = QLabel(self.user_add_label_frame)
        self.usenameLable.setObjectName(u"usenameLable")

        self.verticalLayout_6.addWidget(self.usenameLable)

        self.emailLabel = QLabel(self.user_add_label_frame)
        self.emailLabel.setObjectName(u"emailLabel")

        self.verticalLayout_6.addWidget(self.emailLabel)

        self.nameLable = QLabel(self.user_add_label_frame)
        self.nameLable.setObjectName(u"nameLable")

        self.verticalLayout_6.addWidget(self.nameLable)

        self.membershipTypeLabel = QLabel(self.user_add_label_frame)
        self.membershipTypeLabel.setObjectName(u"membershipTypeLabel")
        self.membershipTypeLabel.setMargin(0)

        self.verticalLayout_6.addWidget(self.membershipTypeLabel)

        self.ageLabel = QLabel(self.user_add_label_frame)
        self.ageLabel.setObjectName(u"ageLabel")
        self.ageLabel.setMargin(0)

        self.verticalLayout_6.addWidget(self.ageLabel)

        self.addressLabel = QLabel(self.user_add_label_frame)
        self.addressLabel.setObjectName(u"addressLabel")

        self.verticalLayout_6.addWidget(self.addressLabel)

        self.bioLabel = QLabel(self.user_add_label_frame)
        self.bioLabel.setObjectName(u"bioLabel")

        self.verticalLayout_6.addWidget(self.bioLabel)

        self.profilePicLabel = QLabel(self.user_add_label_frame)
        self.profilePicLabel.setObjectName(u"profilePicLabel")

        self.verticalLayout_6.addWidget(self.profilePicLabel)


        self.horizontalLayout_5.addWidget(self.user_add_label_frame)

        self.user_add_edit_frame = QFrame(self.user_add_main_frame)
        self.user_add_edit_frame.setObjectName(u"user_add_edit_frame")
        sizePolicy.setHeightForWidth(self.user_add_edit_frame.sizePolicy().hasHeightForWidth())
        self.user_add_edit_frame.setSizePolicy(sizePolicy)
        self.user_add_edit_frame.setFrameShape(QFrame.NoFrame)
        self.user_add_edit_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.user_add_edit_frame)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.usernameLineEdit = QLineEdit(self.user_add_edit_frame)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.verticalLayout_5.addWidget(self.usernameLineEdit)

        self.emailLineEdit = QLineEdit(self.user_add_edit_frame)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.verticalLayout_5.addWidget(self.emailLineEdit)

        self.nameLineEdit = QLineEdit(self.user_add_edit_frame)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.verticalLayout_5.addWidget(self.nameLineEdit)

        self.membershipTypecomboBox = QComboBox(self.user_add_edit_frame)
        self.membershipTypecomboBox.addItem("")
        self.membershipTypecomboBox.addItem("")
        self.membershipTypecomboBox.setObjectName(u"membershipTypecomboBox")
        self.membershipTypecomboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.membershipTypecomboBox)

        self.ageLineEdit = QLineEdit(self.user_add_edit_frame)
        self.ageLineEdit.setObjectName(u"ageLineEdit")

        self.verticalLayout_5.addWidget(self.ageLineEdit)

        self.addressLineEdit = QLineEdit(self.user_add_edit_frame)
        self.addressLineEdit.setObjectName(u"addressLineEdit")

        self.verticalLayout_5.addWidget(self.addressLineEdit)

        self.bioLineEdit = QLineEdit(self.user_add_edit_frame)
        self.bioLineEdit.setObjectName(u"bioLineEdit")

        self.verticalLayout_5.addWidget(self.bioLineEdit)

        self.frame_6 = QFrame(self.user_add_edit_frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.profilePicLineEdit = QLineEdit(self.frame_6)
        self.profilePicLineEdit.setObjectName(u"profilePicLineEdit")
        self.profilePicLineEdit.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.profilePicLineEdit)

        self.selectFileButton = QPushButton(self.frame_6)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectFileButton.setIcon(icon6)

        self.horizontalLayout_6.addWidget(self.selectFileButton)


        self.verticalLayout_5.addWidget(self.frame_6)


        self.horizontalLayout_5.addWidget(self.user_add_edit_frame)


        self.verticalLayout_4.addWidget(self.user_add_main_frame)

        self.user_add_button_frame = QFrame(self.user_add_frame)
        self.user_add_button_frame.setObjectName(u"user_add_button_frame")
        self.user_add_button_frame.setFrameShape(QFrame.NoFrame)
        self.user_add_button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.user_add_button_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.user_add_button_frame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.addButton)

        self.updateButton = QPushButton(self.user_add_button_frame)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateButton.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.updateButton)

        self.horizontalSpacer = QSpacerItem(325, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(self.user_add_button_frame)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout_4.addWidget(self.user_add_button_frame)


        self.verticalLayout_3.addWidget(self.user_add_frame, 0, Qt.AlignTop)

        self.user_list_frame = QFrame(self.user_page)
        self.user_list_frame.setObjectName(u"user_list_frame")
        sizePolicy2.setHeightForWidth(self.user_list_frame.sizePolicy().hasHeightForWidth())
        self.user_list_frame.setSizePolicy(sizePolicy2)
        self.user_list_frame.setFrameShape(QFrame.NoFrame)
        self.user_list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.user_list_frame)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.tableWidget = QTableWidget(self.user_list_frame)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setWordWrap(True)

        self.verticalLayout_31.addWidget(self.tableWidget)


        self.verticalLayout_3.addWidget(self.user_list_frame)

        self.stackedWidget.addWidget(self.user_page)
        self.attendance_page = QWidget()
        self.attendance_page.setObjectName(u"attendance_page")
        self.verticalLayout_14 = QVBoxLayout(self.attendance_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.attendance_add_frame_2 = QFrame(self.attendance_page)
        self.attendance_add_frame_2.setObjectName(u"attendance_add_frame_2")
        sizePolicy1.setHeightForWidth(self.attendance_add_frame_2.sizePolicy().hasHeightForWidth())
        self.attendance_add_frame_2.setSizePolicy(sizePolicy1)
        self.attendance_add_frame_2.setMinimumSize(QSize(300, 0))
        self.attendance_add_frame_2.setMaximumSize(QSize(600, 16777215))
        self.attendance_add_frame_2.setFrameShape(QFrame.NoFrame)
        self.attendance_add_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.attendance_add_frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.attendance_add_title_frame = QFrame(self.attendance_add_frame_2)
        self.attendance_add_title_frame.setObjectName(u"attendance_add_title_frame")
        self.attendance_add_title_frame.setFrameShape(QFrame.NoFrame)
        self.attendance_add_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.attendance_add_title_frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 0, 0, 0)
        self.titleLabel_2 = QLabel(self.attendance_add_title_frame)
        self.titleLabel_2.setObjectName(u"titleLabel_2")
        self.titleLabel_2.setFont(font4)
        self.titleLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.titleLabel_2, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.attendance_add_title_frame, 0, Qt.AlignBottom)

        self.attendance_add_main_frame = QFrame(self.attendance_add_frame_2)
        self.attendance_add_main_frame.setObjectName(u"attendance_add_main_frame")
        sizePolicy1.setHeightForWidth(self.attendance_add_main_frame.sizePolicy().hasHeightForWidth())
        self.attendance_add_main_frame.setSizePolicy(sizePolicy1)
        self.attendance_add_main_frame.setFrameShape(QFrame.NoFrame)
        self.attendance_add_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.attendance_add_main_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.attendance_add_main_left = QFrame(self.attendance_add_main_frame)
        self.attendance_add_main_left.setObjectName(u"attendance_add_main_left")
        self.attendance_add_main_left.setFrameShape(QFrame.NoFrame)
        self.attendance_add_main_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.attendance_add_main_left)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.usenameLable_2 = QLabel(self.attendance_add_main_left)
        self.usenameLable_2.setObjectName(u"usenameLable_2")

        self.verticalLayout_11.addWidget(self.usenameLable_2)

        self.presentLabel = QLabel(self.attendance_add_main_left)
        self.presentLabel.setObjectName(u"presentLabel")

        self.verticalLayout_11.addWidget(self.presentLabel)


        self.horizontalLayout_8.addWidget(self.attendance_add_main_left)

        self.attendance_add_main_right = QFrame(self.attendance_add_main_frame)
        self.attendance_add_main_right.setObjectName(u"attendance_add_main_right")
        sizePolicy.setHeightForWidth(self.attendance_add_main_right.sizePolicy().hasHeightForWidth())
        self.attendance_add_main_right.setSizePolicy(sizePolicy)
        self.attendance_add_main_right.setFrameShape(QFrame.NoFrame)
        self.attendance_add_main_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.attendance_add_main_right)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.usernameComboBox = QComboBox(self.attendance_add_main_right)
        self.usernameComboBox.setObjectName(u"usernameComboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.usernameComboBox.sizePolicy().hasHeightForWidth())
        self.usernameComboBox.setSizePolicy(sizePolicy3)
        self.usernameComboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.usernameComboBox)

        self.presentComboBox = QComboBox(self.attendance_add_main_right)
        self.presentComboBox.addItem("")
        self.presentComboBox.addItem("")
        self.presentComboBox.setObjectName(u"presentComboBox")
        self.presentComboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.presentComboBox)


        self.horizontalLayout_8.addWidget(self.attendance_add_main_right)


        self.verticalLayout_9.addWidget(self.attendance_add_main_frame)

        self.attendance_add_button_frame = QFrame(self.attendance_add_frame_2)
        self.attendance_add_button_frame.setObjectName(u"attendance_add_button_frame")
        self.attendance_add_button_frame.setFrameShape(QFrame.NoFrame)
        self.attendance_add_button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.attendance_add_button_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.addButton_2 = QPushButton(self.attendance_add_button_frame)
        self.addButton_2.setObjectName(u"addButton_2")
        self.addButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_2.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.addButton_2)

        self.updateButton_2 = QPushButton(self.attendance_add_button_frame)
        self.updateButton_2.setObjectName(u"updateButton_2")
        self.updateButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateButton_2.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.updateButton_2)

        self.horizontalSpacer_2 = QSpacerItem(288, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.cancelButton_2 = QPushButton(self.attendance_add_button_frame)
        self.cancelButton_2.setObjectName(u"cancelButton_2")
        self.cancelButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton_2.setIcon(icon9)

        self.horizontalLayout_3.addWidget(self.cancelButton_2)


        self.verticalLayout_9.addWidget(self.attendance_add_button_frame, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.attendance_add_frame_2)

        self.attendance_list_frame_2 = QFrame(self.attendance_page)
        self.attendance_list_frame_2.setObjectName(u"attendance_list_frame_2")
        sizePolicy1.setHeightForWidth(self.attendance_list_frame_2.sizePolicy().hasHeightForWidth())
        self.attendance_list_frame_2.setSizePolicy(sizePolicy1)
        self.attendance_list_frame_2.setFrameShape(QFrame.NoFrame)
        self.attendance_list_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.attendance_list_frame_2)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.attendance_list_frame_2)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 35))
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 0, 0, 0)
        self.radioButton = QRadioButton(self.frame_31)
        self.radioButton.setObjectName(u"radioButton")
        font5 = QFont()
        font5.setPointSize(11)
        self.radioButton.setFont(font5)

        self.horizontalLayout_22.addWidget(self.radioButton)

        self.label_7 = QLabel(self.frame_31)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setPointSize(12)
        self.label_7.setFont(font6)

        self.horizontalLayout_22.addWidget(self.label_7)

        self.dateEdit_2 = QDateEdit(self.frame_31)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        sizePolicy3.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy3)
        self.dateEdit_2.setMinimumSize(QSize(135, 0))
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout_22.addWidget(self.dateEdit_2)


        self.verticalLayout_45.addWidget(self.frame_31, 0, Qt.AlignLeft)

        self.tableWidget_2 = QTableWidget(self.attendance_list_frame_2)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy4)
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_45.addWidget(self.tableWidget_2)


        self.verticalLayout_14.addWidget(self.attendance_list_frame_2)

        self.stackedWidget.addWidget(self.attendance_page)
        self.expense_page = QWidget()
        self.expense_page.setObjectName(u"expense_page")
        self.expense_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_19 = QVBoxLayout(self.expense_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.expense_add_frame_2 = QFrame(self.expense_page)
        self.expense_add_frame_2.setObjectName(u"expense_add_frame_2")
        sizePolicy1.setHeightForWidth(self.expense_add_frame_2.sizePolicy().hasHeightForWidth())
        self.expense_add_frame_2.setSizePolicy(sizePolicy1)
        self.expense_add_frame_2.setMaximumSize(QSize(600, 16777215))
        self.expense_add_frame_2.setFrameShape(QFrame.NoFrame)
        self.expense_add_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.expense_add_frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame = QFrame(self.expense_add_frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.headingLabel = QLabel(self.frame)
        self.headingLabel.setObjectName(u"headingLabel")
        self.headingLabel.setFont(font4)
        self.headingLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.headingLabel, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame)

        self.frame_2 = QFrame(self.expense_add_frame_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setSpacing(14)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 2, 0, 0)
        self.titleLable = QLabel(self.frame_5)
        self.titleLable.setObjectName(u"titleLable")

        self.verticalLayout_17.addWidget(self.titleLable)

        self.purposeLabel = QLabel(self.frame_5)
        self.purposeLabel.setObjectName(u"purposeLabel")

        self.verticalLayout_17.addWidget(self.purposeLabel)

        self.amountLable = QLabel(self.frame_5)
        self.amountLable.setObjectName(u"amountLable")

        self.verticalLayout_17.addWidget(self.amountLable)

        self.descriptionLabel = QLabel(self.frame_5)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setMargin(0)

        self.verticalLayout_17.addWidget(self.descriptionLabel)


        self.horizontalLayout_12.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.titleLineEdit = QLineEdit(self.frame_4)
        self.titleLineEdit.setObjectName(u"titleLineEdit")

        self.verticalLayout_18.addWidget(self.titleLineEdit)

        self.purposeLineEdit = QLineEdit(self.frame_4)
        self.purposeLineEdit.setObjectName(u"purposeLineEdit")

        self.verticalLayout_18.addWidget(self.purposeLineEdit)

        self.amountLineEdit = QLineEdit(self.frame_4)
        self.amountLineEdit.setObjectName(u"amountLineEdit")

        self.verticalLayout_18.addWidget(self.amountLineEdit)

        self.descriptionTextEdit = QTextEdit(self.frame_4)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")

        self.verticalLayout_18.addWidget(self.descriptionTextEdit)


        self.horizontalLayout_12.addWidget(self.frame_4)


        self.verticalLayout_13.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.expense_add_frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.addButton_3 = QPushButton(self.frame_3)
        self.addButton_3.setObjectName(u"addButton_3")
        self.addButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_3.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.addButton_3)

        self.updateButton_3 = QPushButton(self.frame_3)
        self.updateButton_3.setObjectName(u"updateButton_3")
        self.updateButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateButton_3.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.updateButton_3)

        self.horizontalSpacer_3 = QSpacerItem(256, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.cancelButton_3 = QPushButton(self.frame_3)
        self.cancelButton_3.setObjectName(u"cancelButton_3")
        self.cancelButton_3.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.cancelButton_3)


        self.verticalLayout_13.addWidget(self.frame_3)


        self.verticalLayout_19.addWidget(self.expense_add_frame_2)

        self.expense_list_frame_2 = QFrame(self.expense_page)
        self.expense_list_frame_2.setObjectName(u"expense_list_frame_2")
        sizePolicy2.setHeightForWidth(self.expense_list_frame_2.sizePolicy().hasHeightForWidth())
        self.expense_list_frame_2.setSizePolicy(sizePolicy2)
        self.expense_list_frame_2.setFrameShape(QFrame.NoFrame)
        self.expense_list_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.expense_list_frame_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_3 = QTableWidget(self.expense_list_frame_2)
        if (self.tableWidget_3.columnCount() < 8):
            self.tableWidget_3.setColumnCount(8)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFrameShape(QFrame.NoFrame)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(57)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_20.addWidget(self.tableWidget_3)


        self.verticalLayout_19.addWidget(self.expense_list_frame_2)

        self.stackedWidget.addWidget(self.expense_page)
        self.revenue_page = QWidget()
        self.revenue_page.setObjectName(u"revenue_page")
        self.verticalLayout_27 = QVBoxLayout(self.revenue_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.revenue_add_frame_3 = QFrame(self.revenue_page)
        self.revenue_add_frame_3.setObjectName(u"revenue_add_frame_3")
        sizePolicy1.setHeightForWidth(self.revenue_add_frame_3.sizePolicy().hasHeightForWidth())
        self.revenue_add_frame_3.setSizePolicy(sizePolicy1)
        self.revenue_add_frame_3.setMaximumSize(QSize(600, 16777215))
        self.revenue_add_frame_3.setFrameShape(QFrame.NoFrame)
        self.revenue_add_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.revenue_add_frame_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_7 = QFrame(self.revenue_add_frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.headingLabel_2 = QLabel(self.frame_7)
        self.headingLabel_2.setObjectName(u"headingLabel_2")
        self.headingLabel_2.setFont(font4)
        self.headingLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_23.addWidget(self.headingLabel_2, 0, Qt.AlignTop)


        self.verticalLayout_22.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.revenue_add_frame_3)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_9)
        self.verticalLayout_24.setSpacing(14)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 2, 0, 0)
        self.titleLable_2 = QLabel(self.frame_9)
        self.titleLable_2.setObjectName(u"titleLable_2")

        self.verticalLayout_24.addWidget(self.titleLable_2)

        self.purposeLabel_2 = QLabel(self.frame_9)
        self.purposeLabel_2.setObjectName(u"purposeLabel_2")

        self.verticalLayout_24.addWidget(self.purposeLabel_2)

        self.amountLable_2 = QLabel(self.frame_9)
        self.amountLable_2.setObjectName(u"amountLable_2")

        self.verticalLayout_24.addWidget(self.amountLable_2)

        self.descriptionLabel_2 = QLabel(self.frame_9)
        self.descriptionLabel_2.setObjectName(u"descriptionLabel_2")
        self.descriptionLabel_2.setMargin(0)

        self.verticalLayout_24.addWidget(self.descriptionLabel_2)


        self.horizontalLayout_14.addWidget(self.frame_9, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_10)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.titleLineEdit_2 = QLineEdit(self.frame_10)
        self.titleLineEdit_2.setObjectName(u"titleLineEdit_2")

        self.verticalLayout_25.addWidget(self.titleLineEdit_2)

        self.sourceLineEdit_2 = QLineEdit(self.frame_10)
        self.sourceLineEdit_2.setObjectName(u"sourceLineEdit_2")

        self.verticalLayout_25.addWidget(self.sourceLineEdit_2)

        self.amountLineEdit_2 = QLineEdit(self.frame_10)
        self.amountLineEdit_2.setObjectName(u"amountLineEdit_2")

        self.verticalLayout_25.addWidget(self.amountLineEdit_2)

        self.descriptionTextEdit_2 = QTextEdit(self.frame_10)
        self.descriptionTextEdit_2.setObjectName(u"descriptionTextEdit_2")

        self.verticalLayout_25.addWidget(self.descriptionTextEdit_2)


        self.horizontalLayout_14.addWidget(self.frame_10)


        self.verticalLayout_22.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.revenue_add_frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.addButton_4 = QPushButton(self.frame_11)
        self.addButton_4.setObjectName(u"addButton_4")
        self.addButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_4.setIcon(icon7)

        self.horizontalLayout_7.addWidget(self.addButton_4)

        self.updateButton_4 = QPushButton(self.frame_11)
        self.updateButton_4.setObjectName(u"updateButton_4")
        self.updateButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateButton_4.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.updateButton_4)

        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.cancelButton_4 = QPushButton(self.frame_11)
        self.cancelButton_4.setObjectName(u"cancelButton_4")
        self.cancelButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton_4.setIcon(icon9)

        self.horizontalLayout_7.addWidget(self.cancelButton_4)


        self.verticalLayout_22.addWidget(self.frame_11)


        self.verticalLayout_27.addWidget(self.revenue_add_frame_3)

        self.revenue_list_frame_3 = QFrame(self.revenue_page)
        self.revenue_list_frame_3.setObjectName(u"revenue_list_frame_3")
        sizePolicy2.setHeightForWidth(self.revenue_list_frame_3.sizePolicy().hasHeightForWidth())
        self.revenue_list_frame_3.setSizePolicy(sizePolicy2)
        self.revenue_list_frame_3.setFrameShape(QFrame.NoFrame)
        self.revenue_list_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.revenue_list_frame_3)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_4 = QTableWidget(self.revenue_list_frame_3)
        if (self.tableWidget_4.columnCount() < 8):
            self.tableWidget_4.setColumnCount(8)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setFrameShape(QFrame.NoFrame)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_21.addWidget(self.tableWidget_4)


        self.verticalLayout_27.addWidget(self.revenue_list_frame_3)

        self.stackedWidget.addWidget(self.revenue_page)
        self.staff_page = QWidget()
        self.staff_page.setObjectName(u"staff_page")
        self.verticalLayout_34 = QVBoxLayout(self.staff_page)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.staff_list_frame_4 = QFrame(self.staff_page)
        self.staff_list_frame_4.setObjectName(u"staff_list_frame_4")
        sizePolicy1.setHeightForWidth(self.staff_list_frame_4.sizePolicy().hasHeightForWidth())
        self.staff_list_frame_4.setSizePolicy(sizePolicy1)
        self.staff_list_frame_4.setFrameShape(QFrame.NoFrame)
        self.staff_list_frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.staff_list_frame_4)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_12 = QFrame(self.staff_list_frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_12)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.create_page = QWidget()
        self.create_page.setObjectName(u"create_page")
        self.verticalLayout_41 = QVBoxLayout(self.create_page)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.staff_add_frame_4 = QFrame(self.create_page)
        self.staff_add_frame_4.setObjectName(u"staff_add_frame_4")
        sizePolicy1.setHeightForWidth(self.staff_add_frame_4.sizePolicy().hasHeightForWidth())
        self.staff_add_frame_4.setSizePolicy(sizePolicy1)
        self.staff_add_frame_4.setMaximumSize(QSize(600, 16777215))
        self.staff_add_frame_4.setFrameShape(QFrame.NoFrame)
        self.staff_add_frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.staff_add_frame_4)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_13 = QFrame(self.staff_add_frame_4)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy2.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy2)
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_13)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy1.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy1)
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_15)
        self.verticalLayout_36.setSpacing(5)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_21)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.headingLabel_3 = QLabel(self.frame_21)
        self.headingLabel_3.setObjectName(u"headingLabel_3")
        self.headingLabel_3.setFont(font4)
        self.headingLabel_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_37.addWidget(self.headingLabel_3)


        self.verticalLayout_36.addWidget(self.frame_21)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_16)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_26)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.nameLable_2 = QLabel(self.frame_26)
        self.nameLable_2.setObjectName(u"nameLable_2")

        self.verticalLayout_16.addWidget(self.nameLable_2)

        self.positionLabel = QLabel(self.frame_26)
        self.positionLabel.setObjectName(u"positionLabel")

        self.verticalLayout_16.addWidget(self.positionLabel)

        self.salaryLable = QLabel(self.frame_26)
        self.salaryLable.setObjectName(u"salaryLable")

        self.verticalLayout_16.addWidget(self.salaryLable)

        self.dateJoinedLable = QLabel(self.frame_26)
        self.dateJoinedLable.setObjectName(u"dateJoinedLable")

        self.verticalLayout_16.addWidget(self.dateJoinedLable)


        self.horizontalLayout_17.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_16)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_27)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.nameLineEdit_2 = QLineEdit(self.frame_27)
        self.nameLineEdit_2.setObjectName(u"nameLineEdit_2")

        self.verticalLayout_35.addWidget(self.nameLineEdit_2)

        self.positionLineEdit = QLineEdit(self.frame_27)
        self.positionLineEdit.setObjectName(u"positionLineEdit")

        self.verticalLayout_35.addWidget(self.positionLineEdit)

        self.salaryLineEdit = QLineEdit(self.frame_27)
        self.salaryLineEdit.setObjectName(u"salaryLineEdit")

        self.verticalLayout_35.addWidget(self.salaryLineEdit)

        self.dateEdit = QDateEdit(self.frame_27)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout_35.addWidget(self.dateEdit)


        self.horizontalLayout_17.addWidget(self.frame_27)


        self.verticalLayout_36.addWidget(self.frame_16)

        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 10, 0)
        self.addButton_5 = QPushButton(self.frame_20)
        self.addButton_5.setObjectName(u"addButton_5")
        self.addButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton_5.setIcon(icon7)

        self.horizontalLayout_9.addWidget(self.addButton_5)

        self.updateButton_5 = QPushButton(self.frame_20)
        self.updateButton_5.setObjectName(u"updateButton_5")
        self.updateButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateButton_5.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.updateButton_5)

        self.horizontalSpacer_5 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.cancelButton_5 = QPushButton(self.frame_20)
        self.cancelButton_5.setObjectName(u"cancelButton_5")
        self.cancelButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton_5.setIcon(icon9)

        self.horizontalLayout_9.addWidget(self.cancelButton_5)


        self.verticalLayout_36.addWidget(self.frame_20, 0, Qt.AlignBottom)


        self.verticalLayout_32.addWidget(self.frame_15)


        self.verticalLayout_28.addWidget(self.frame_13)


        self.verticalLayout_41.addWidget(self.staff_add_frame_4)

        self.stackedWidget_2.addWidget(self.create_page)
        self.pay_page = QWidget()
        self.pay_page.setObjectName(u"pay_page")
        self.verticalLayout_52 = QVBoxLayout(self.pay_page)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.staff_add_frame_5 = QFrame(self.pay_page)
        self.staff_add_frame_5.setObjectName(u"staff_add_frame_5")
        sizePolicy1.setHeightForWidth(self.staff_add_frame_5.sizePolicy().hasHeightForWidth())
        self.staff_add_frame_5.setSizePolicy(sizePolicy1)
        self.staff_add_frame_5.setMaximumSize(QSize(600, 16777215))
        self.staff_add_frame_5.setFrameShape(QFrame.NoFrame)
        self.staff_add_frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.staff_add_frame_5)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_35 = QFrame(self.staff_add_frame_5)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy1.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy1)
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_35)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_36)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.pay_heading = QLabel(self.frame_36)
        self.pay_heading.setObjectName(u"pay_heading")
        self.pay_heading.setFont(font4)
        self.pay_heading.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_48.addWidget(self.pay_heading)


        self.verticalLayout_47.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy1.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy1)
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_38)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.salaryLable_2 = QLabel(self.frame_38)
        self.salaryLable_2.setObjectName(u"salaryLable_2")

        self.verticalLayout_29.addWidget(self.salaryLable_2)

        self.salaryLable_3 = QLabel(self.frame_38)
        self.salaryLable_3.setObjectName(u"salaryLable_3")

        self.verticalLayout_29.addWidget(self.salaryLable_3)


        self.horizontalLayout_23.addWidget(self.frame_38, 0, Qt.AlignTop)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_39)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.amountEdit = QLineEdit(self.frame_39)
        self.amountEdit.setObjectName(u"amountEdit")

        self.verticalLayout_33.addWidget(self.amountEdit)

        self.descriptionTextEdit_3 = QTextEdit(self.frame_39)
        self.descriptionTextEdit_3.setObjectName(u"descriptionTextEdit_3")

        self.verticalLayout_33.addWidget(self.descriptionTextEdit_3)


        self.horizontalLayout_23.addWidget(self.frame_39)


        self.verticalLayout_47.addWidget(self.frame_37)

        self.frame_40 = QFrame(self.frame_35)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 10, 0)
        self.payButton = QPushButton(self.frame_40)
        self.payButton.setObjectName(u"payButton")
        self.payButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_24.addWidget(self.payButton)

        self.horizontalSpacer_8 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)

        self.payCancelButton = QPushButton(self.frame_40)
        self.payCancelButton.setObjectName(u"payCancelButton")
        self.payCancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.payCancelButton.setIcon(icon9)

        self.horizontalLayout_24.addWidget(self.payCancelButton)


        self.verticalLayout_47.addWidget(self.frame_40, 0, Qt.AlignBottom)


        self.verticalLayout_42.addWidget(self.frame_35)


        self.verticalLayout_52.addWidget(self.staff_add_frame_5)

        self.stackedWidget_2.addWidget(self.pay_page)

        self.verticalLayout_8.addWidget(self.stackedWidget_2)


        self.verticalLayout_30.addWidget(self.frame_12)

        self.tableWidget_5 = QTableWidget(self.staff_list_frame_4)
        if (self.tableWidget_5.columnCount() < 11):
            self.tableWidget_5.setColumnCount(11)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(9, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(10, __qtablewidgetitem41)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        sizePolicy4.setHeightForWidth(self.tableWidget_5.sizePolicy().hasHeightForWidth())
        self.tableWidget_5.setSizePolicy(sizePolicy4)
        self.tableWidget_5.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_5.setFrameShape(QFrame.NoFrame)
        self.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_30.addWidget(self.tableWidget_5)


        self.verticalLayout_34.addWidget(self.staff_list_frame_4)

        self.stackedWidget.addWidget(self.staff_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeButton.setText("")
#if QT_CONFIG(tooltip)
        self.userButton.setToolTip(QCoreApplication.translate("MainWindow", u"User", None))
#endif // QT_CONFIG(tooltip)
        self.userButton.setText("")
#if QT_CONFIG(tooltip)
        self.attendanceButton.setToolTip(QCoreApplication.translate("MainWindow", u"attendance", None))
#endif // QT_CONFIG(tooltip)
        self.attendanceButton.setText("")
#if QT_CONFIG(tooltip)
        self.expenseButton.setToolTip(QCoreApplication.translate("MainWindow", u"Expense", None))
#endif // QT_CONFIG(tooltip)
        self.expenseButton.setText("")
#if QT_CONFIG(tooltip)
        self.revenueButton.setToolTip(QCoreApplication.translate("MainWindow", u"Reveneu", None))
#endif // QT_CONFIG(tooltip)
        self.revenueButton.setText("")
#if QT_CONFIG(tooltip)
        self.staffButton.setToolTip(QCoreApplication.translate("MainWindow", u"Staff", None))
#endif // QT_CONFIG(tooltip)
        self.staffButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total no. of staffs:", None))
        self.num_staffs.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total no. of users:", None))
        self.num_users.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"In:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Last 30 days", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Last 365 days", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Grand Total", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Expenses:", None))
        self.totalExpense.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Revenues:", None))
        self.totalRevenue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total profit:", None))
        self.totalProfit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Enter user details:", None))
        self.usenameLable.setText(QCoreApplication.translate("MainWindow", u"Username*:", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email*:", None))
        self.nameLable.setText(QCoreApplication.translate("MainWindow", u"Name*:", None))
        self.membershipTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Membership Type*:", None))
        self.ageLabel.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.addressLabel.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.bioLabel.setText(QCoreApplication.translate("MainWindow", u"Bio:", None))
        self.profilePicLabel.setText(QCoreApplication.translate("MainWindow", u"Profile Pic:", None))
        self.membershipTypecomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Free", None))
        self.membershipTypecomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Premium", None))

        self.selectFileButton.setText("")
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Membership Type", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Profile Pic", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Bio", None));
        self.titleLabel_2.setText(QCoreApplication.translate("MainWindow", u"Take Today's Attendance:", None))
        self.usenameLable_2.setText(QCoreApplication.translate("MainWindow", u"Username*:", None))
        self.presentLabel.setText(QCoreApplication.translate("MainWindow", u"Present*:", None))
        self.presentComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.presentComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.addButton_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.updateButton_2.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.cancelButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Turn on filter", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Select Date:", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy", None))
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Day", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Present", None));
        self.headingLabel.setText(QCoreApplication.translate("MainWindow", u"Enter expense details:", None))
        self.titleLable.setText(QCoreApplication.translate("MainWindow", u"Title*:", None))
        self.purposeLabel.setText(QCoreApplication.translate("MainWindow", u"Purpose*:", None))
        self.amountLable.setText(QCoreApplication.translate("MainWindow", u"Amount*:", None))
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.addButton_3.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.updateButton_3.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.cancelButton_3.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Purpose", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Added at", None));
        self.headingLabel_2.setText(QCoreApplication.translate("MainWindow", u"Enter revenue details:", None))
        self.titleLable_2.setText(QCoreApplication.translate("MainWindow", u"Title*:", None))
        self.purposeLabel_2.setText(QCoreApplication.translate("MainWindow", u"Source*:", None))
        self.amountLable_2.setText(QCoreApplication.translate("MainWindow", u"Amount*:", None))
        self.descriptionLabel_2.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.addButton_4.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.updateButton_4.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.cancelButton_4.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Source", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Added at", None));
        self.headingLabel_3.setText(QCoreApplication.translate("MainWindow", u"Enter staff details:", None))
        self.nameLable_2.setText(QCoreApplication.translate("MainWindow", u"Name*:", None))
        self.positionLabel.setText(QCoreApplication.translate("MainWindow", u"Position*:", None))
        self.salaryLable.setText(QCoreApplication.translate("MainWindow", u"Salary:", None))
        self.dateJoinedLable.setText(QCoreApplication.translate("MainWindow", u"Date Joined:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.addButton_5.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.updateButton_5.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.cancelButton_5.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pay_heading.setText("")
        self.salaryLable_2.setText(QCoreApplication.translate("MainWindow", u"Amount*:", None))
        self.salaryLable_3.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.payButton.setText(QCoreApplication.translate("MainWindow", u"Pay", None))
        self.payCancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        ___qtablewidgetitem23 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem24 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Date Joined", None));
        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Due Amount", None));
        ___qtablewidgetitem29 = self.tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Paid", None));
        ___qtablewidgetitem30 = self.tableWidget_5.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Generated Date", None));
    # retranslateUi

