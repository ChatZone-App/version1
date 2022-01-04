from PySide2.QtCore import (
    QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1367, 950)
        MainWindow.setStyleSheet(u"* {\n"
                                 "	\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#centralwidget{\n"
                                 "	background-color: #15202B;\n"
                                 "}\n"
                                 "\n"
                                 "#titleBar {\n"
                                 "	background-color: #242526;\n"
                                 "}\n"
                                 "\n"
                                 "#close, #restore, #minimize {\n"
                                 "	border-radius: 7px\n"
                                 "}\n"
                                 "#close {\n"
                                 "	background-color: red;\n"
                                 "}\n"
                                 "#restore {\n"
                                 "	background-color: yellow;\n"
                                 "}\n"
                                 "#minimize {\n"
                                 "	background-color: green;\n"
                                 "}\n"
                                 "\n"
                                 "#appName {\n"
                                 "	letter-spacing: 1.5px;\n"
                                 "	color: white;\n"
                                 "}\n"
                                 "\n"
                                 "#sideBar{\n"
                                 "	background-color: #192734;\n"
                                 "}\n"
                                 "#profile{\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "#chatTitle {\n"
                                 "	color: #fff;\n"
                                 "	margin-bottom: 30px\n"
                                 "}\n"
                                 "#search {\n"
                                 "	border: none;\n"
                                 "	border-bottom: 2px solid #404040;\n"
                                 "}\n"
                                 "#searchLineEdit {\n"
                                 "	background-color: transparent;\n"
                                 "	color: #fff\n"
                                 "}\n"
                                 "\n"
                                 "#chatScrollArea {\n"
                                 "	background-color: rgb(21, 32, 43);\n"
                                 "	border: none;\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "#chat-widget {\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "/*  HANDLE BAR VERTICAL */\n"
                                 "QScro"
                                 "llBar::handle:vertical {	\n"
                                 "	background-color: rgb(80, 80, 122);\n"
                                 "	min-height: 30px;\n"
                                 "	border-radius: 7px;\n"
                                 "}\n"
                                 "QScrollBar::handle:vertical:hover{	\n"
                                 "	background-color: rgb(255, 0, 127);\n"
                                 "}\n"
                                 "QScrollBar::handle:vertical:pressed {	\n"
                                 "	background-color: rgb(185, 0, 92);\n"
                                 "}\n"
                                 "\n"
                                 "/* BTN TOP - SCROLLBAR */\n"
                                 "QScrollBar::sub-line:vertical {\n"
                                 "	border: none;\n"
                                 "	background-color: rgb(59, 59, 90);\n"
                                 "	height: 15px;\n"
                                 "	border-top-left-radius: 7px;\n"
                                 "	border-top-right-radius: 7px;\n"
                                 "	subcontrol-position: top;\n"
                                 "	subcontrol-origin: margin;\n"
                                 "}\n"
                                 "QScrollBar::sub-line:vertical:hover {	\n"
                                 "	background-color: rgb(255, 0, 127);\n"
                                 "}\n"
                                 "QScrollBar::sub-line:vertical:pressed {	\n"
                                 "	background-color: rgb(185, 0, 92);\n"
                                 "}\n"
                                 "\n"
                                 "/* BTN BOTTOM - SCROLLBAR */\n"
                                 "QScrollBar::add-line:vertical {\n"
                                 "	border: none;\n"
                                 "	background-color: rgb(59, 59, 90);\n"
                                 "	height: 15px;\n"
                                 "	border-bottom-left-radius: 7px;\n"
                                 "	border-bottom-right-radius: 7px;\n"
                                 "	subcontrol-position: bottom;"
                                 "\n"
                                 "	subcontrol-origin: margin;\n"
                                 "}\n"
                                 "QScrollBar::add-line:vertical:hover {	\n"
                                 "	background-color: rgb(255, 0, 127);\n"
                                 "}\n"
                                 "QScrollBar::add-line:vertical:pressed {	\n"
                                 "	background-color: rgb(185, 0, 92);\n"
                                 "}\n"
                                 "\n"
                                 "/* RESET ARROW */\n"
                                 "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                 "	background: none;\n"
                                 "}\n"
                                 "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                 "	background: none;\n"
                                 "}\n"
                                 "\n"
                                 "#userNameAndState {border: none;}\n"
                                 "#userName {color: #fff;}\n"
                                 "#state{color: #eee;}\n"
                                 "\n"
                                 "#messageInput {\n"
                                 "	margin: 5px 0;\n"
                                 "	color: #fff;\n"
                                 "	letter-spacing: 1.3px\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.centralwidget)
        self.titleBar.setObjectName(u"titleBar")
        font = QFont()
        font.setPointSize(3)
        self.titleBar.setFont(font)
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.mainWindowTitle = QFrame(self.titleBar)
        self.mainWindowTitle.setObjectName(u"mainWindowTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainWindowTitle.sizePolicy().hasHeightForWidth())
        self.mainWindowTitle.setSizePolicy(sizePolicy)
        self.mainWindowTitle.setFrameShape(QFrame.StyledPanel)
        self.mainWindowTitle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainWindowTitle)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.appName = QLabel(self.mainWindowTitle)
        self.appName.setObjectName(u"appName")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.appName.setFont(font1)
        self.appName.setStyleSheet(u"")
        self.verticalLayout_2.addWidget(self.appName, 0, Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.mainWindowTitle)
        self.controls = QFrame(self.titleBar)
        self.controls.setObjectName(u"controls")
        self.controls.setFrameShape(QFrame.StyledPanel)
        self.controls.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.controls)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.minimize = QPushButton(self.controls)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(14, 14))
        self.minimize.setMaximumSize(QSize(14, 14))
        self.horizontalLayout_2.addWidget(self.minimize)
        self.restore = QPushButton(self.controls)
        self.restore.setObjectName(u"restore")
        self.restore.setMinimumSize(QSize(14, 14))
        self.restore.setMaximumSize(QSize(14, 14))
        self.horizontalLayout_2.addWidget(self.restore)
        self.close = QPushButton(self.controls)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(14, 14))
        self.close.setMaximumSize(QSize(14, 14))
        self.close.setIconSize(QSize(20, 20))
        self.horizontalLayout_2.addWidget(self.close)
        self.horizontalLayout.addWidget(self.controls, 0, Qt.AlignRight)
        self.verticalLayout.addWidget(self.titleBar, 0, Qt.AlignTop)
        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(8)
        self.mainBody.setFont(font2)
        self.horizontalLayout_3 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sideBar = QFrame(self.mainBody)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setMinimumSize(QSize(70, 0))
        self.sideBar.setMaximumSize(QSize(70, 16777215))
        self.sideBar.setFrameShape(QFrame.StyledPanel)
        self.sideBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.sideBar)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 20, 0, 35)
        self.appIcon = QLabel(self.sideBar)
        self.appIcon.setObjectName(u"appIcon")
        self.appIcon.setMinimumSize(QSize(40, 40))
        self.appIcon.setMaximumSize(QSize(40, 40))
        self.appIcon.setPixmap(QPixmap(u":/appIcon/telegram.png"))
        self.appIcon.setScaledContents(True)
        self.verticalLayout_4.addWidget(
            self.appIcon, 0, Qt.AlignHCenter | Qt.AlignTop)
        self.Features = QFrame(self.sideBar)
        self.Features.setObjectName(u"Features")
        self.Features.setFrameShape(QFrame.StyledPanel)
        self.Features.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Features)
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 25)
        self.Profile = QPushButton(self.Features)
        self.Profile.setObjectName(u"Profile")
        icon = QIcon()
        icon.addFile(u":/appIcon/home-icon-silhouette.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.Profile.setIcon(icon)
        self.Profile.setIconSize(QSize(30, 30))
        self.Profile.setFlat(True)

        self.verticalLayout_5.addWidget(self.Profile)

        self.messages = QPushButton(self.Features)
        self.messages.setObjectName(u"messages")
        self.messages.setMinimumSize(QSize(0, 0))
        icon1 = QIcon()
        icon1.addFile(u":/appIcon/chat-2-512.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.messages.setIcon(icon1)
        self.messages.setIconSize(QSize(30, 30))
        self.messages.setFlat(True)

        self.verticalLayout_5.addWidget(self.messages)

        self.contacts = QPushButton(self.Features)
        self.contacts.setObjectName(u"contacts")
        icon2 = QIcon()
        icon2.addFile(u":/appIcon/contacts-512.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.contacts.setIcon(icon2)
        self.contacts.setIconSize(QSize(30, 30))
        self.contacts.setFlat(True)

        self.verticalLayout_5.addWidget(self.contacts)

        self.settings = QPushButton(self.Features)
        self.settings.setObjectName(u"settings")
        icon3 = QIcon()
        icon3.addFile(u":/appIcon/settings (2).png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon3)
        self.settings.setIconSize(QSize(30, 30))
        self.settings.setFlat(True)

        self.verticalLayout_5.addWidget(self.settings)

        self.mode = QPushButton(self.Features)
        self.mode.setObjectName(u"mode")
        icon4 = QIcon()
        icon4.addFile(u":/appIcon/night-mode (4).png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.mode.setIcon(icon4)
        self.mode.setIconSize(QSize(30, 30))
        self.mode.setFlat(True)

        self.verticalLayout_5.addWidget(self.mode)

        self.verticalLayout_4.addWidget(self.Features)

        self.Ref_out = QFrame(self.sideBar)
        self.Ref_out.setObjectName(u"Ref_out")
        self.Ref_out.setFrameShape(QFrame.StyledPanel)
        self.Ref_out.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Ref_out)
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.refresh = QPushButton(self.Ref_out)
        self.refresh.setObjectName(u"refresh")
        icon5 = QIcon()
        icon5.addFile(u":/appIcon/refresh-512.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.refresh.setIcon(icon5)
        self.refresh.setIconSize(QSize(30, 30))
        self.refresh.setFlat(True)

        self.verticalLayout_6.addWidget(self.refresh)

        self.logout = QPushButton(self.Ref_out)
        self.logout.setObjectName(u"logout")
        icon6 = QIcon()
        icon6.addFile(u":/appIcon/logout-512.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon6)
        self.logout.setIconSize(QSize(30, 30))
        self.logout.setFlat(True)

        self.verticalLayout_6.addWidget(self.logout)

        self.verticalLayout_4.addWidget(self.Ref_out, 0, Qt.AlignBottom)

        self.horizontalLayout_3.addWidget(self.sideBar)

        self.Body = QFrame(self.mainBody)
        self.Body.setObjectName(u"Body")
        font3 = QFont()
        font3.setPointSize(1)
        self.Body.setFont(font3)
        self.Body.setFrameShape(QFrame.StyledPanel)
        self.Body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Body)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chatBody = QFrame(self.Body)
        self.chatBody.setObjectName(u"chatBody")
        sizePolicy1.setHeightForWidth(
            self.chatBody.sizePolicy().hasHeightForWidth())
        self.chatBody.setSizePolicy(sizePolicy1)
        self.chatBody.setMaximumSize(QSize(16777215, 16777215))
        self.chatBody.setFrameShape(QFrame.StyledPanel)
        self.chatBody.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.chatBody)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, 20, 0, 0)
        self.conversations = QFrame(self.chatBody)
        self.conversations.setObjectName(u"conversations")
        self.conversations.setMinimumSize(QSize(500, 0))
        self.conversations.setMaximumSize(QSize(600, 16777215))
        self.conversations.setFrameShape(QFrame.StyledPanel)
        self.conversations.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7 = QVBoxLayout(self.conversations)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.chatTitle = QLabel(self.conversations)
        self.chatTitle.setObjectName(u"chatTitle")
        self.font4 = font4 = QFont()
        font4.setFamily(u"Trebuchet MS")
        font4.setPointSize(21)
        font4.setBold(True)
        font4.setWeight(75)
        self.chatTitle.setFont(font4)
        self.chatTitle.setStyleSheet(u"color: #fff\n"
                                     "\n"
                                     "")

        self.verticalLayout_7.addWidget(self.chatTitle)

        self.search = QFrame(self.conversations)
        self.search.setObjectName(u"search")
        self.search.setMaximumSize(QSize(440, 16777215))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift")
        self.search.setFont(font5)
        self.search.setFrameShape(QFrame.StyledPanel)
        self.search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.search)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 10)
        self.searchbtn = QPushButton(self.search)
        self.searchbtn.setObjectName(u"searchbtn")
        icon7 = QIcon()
        icon7.addFile(u":/appIcon/search.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.searchbtn.setIcon(icon7)
        self.searchbtn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.searchbtn)

        self.searchLineEdit = QLineEdit(self.search)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        font6 = QFont()
        font6.setFamily(u"Bahnschrift")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setWeight(50)
        self.searchLineEdit.setFont(font6)
        self.searchLineEdit.setFrame(False)

        self.horizontalLayout_5.addWidget(self.searchLineEdit)

        self.verticalLayout_7.addWidget(self.search, 0, Qt.AlignTop)

        self.chatScrollArea = QScrollArea(self.conversations)
        self.chatScrollArea.setObjectName(u"chatScrollArea")
        self.chatScrollArea.setStyleSheet(u"background-color: rgb(21, 32, 43);\n"
                                          "margin-top: 30px\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "")
        self.chatScrollArea.setFrameShape(QFrame.NoFrame)
        self.chatScrollArea.setFrameShadow(QFrame.Plain)
        self.chatScrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -166, 477, 894))

        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.chatScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.NoResultsMessage = QLabel(self.conversations)
        self.NoResultsMessage.setGeometry(QRect(200, 750, 600, 200))
        self.NoResultsMessage.setObjectName(f"NoResultsMessage")
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.NoResultsMessage.setFont(font)
        self.NoResultsMessage.setStyleSheet(
            u"background-color: transparent;color: white;padding: 7px;")
        self.verticalLayout_7.addWidget(self.NoResultsMessage)

        self.verticalLayout_7.addWidget(self.chatScrollArea)

        self.horizontalLayout_4.addWidget(self.conversations, 0, Qt.AlignLeft)
        self.theChat_0 = QFrame(self.chatBody)
        self.theChat_0.setObjectName(u"theChat_0")
        # self.theChat_0.setStyleSheet(u"background-color: #fff"
        #                              "\n"
        #                              "")
        sizePolicy.setHeightForWidth(
            self.theChat_0.sizePolicy().hasHeightForWidth())
        self.theChat_0.setSizePolicy(sizePolicy)
        self.theChat_0.setMinimumSize(QSize(688, 0))
        self.theChat_0.setFrameShape(QFrame.StyledPanel)
        self.theChat_0.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.chatBody)

        self.size_grip = QFrame(self.Body)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.size_grip)

        self.horizontalLayout_3.addWidget(self.Body)

        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.appName.setToolTip(QCoreApplication.translate(
            "MainWindow", u"App Name", None))
        self.appName.setText(QCoreApplication.translate(
            "MainWindow", u"Chat Zone", None))
        self.minimize.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Minimize", None))
        self.minimize.setText("")
        self.restore.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Restore", None))
        self.restore.setText("")
        self.close.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close", None))
        self.close.setText("")
        self.mainBody.setToolTip("")
        self.appIcon.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Chat Zone", None))
        self.appIcon.setText("")
        self.Profile.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Profile", None))
        self.Profile.setText("")
        self.messages.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Messages", None))
        self.messages.setText("")
        self.contacts.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Contacts", None))
        self.contacts.setText("")
        self.settings.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Settings", None))
        self.settings.setText("")
        self.mode.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Light Mode", None))
        self.mode.setText("")
        self.refresh.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Refresh", None))
        self.refresh.setText("")
        self.logout.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Logout", None))
        self.logout.setText("")
        self.chatTitle.setText(
            QCoreApplication.translate("MainWindow", u"Chat", None))
        self.searchbtn.setText("")
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Search or start new chat ....", None))
        self.NoResultsMessage.setText("")
