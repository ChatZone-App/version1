from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import resourcesLogin_rc


class Ui_MainWindowLI(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1197, 950)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(8)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"* {\n"
                                         "	\n"
                                         "}\n"
                                         "\n"
                                         "#centralwidget{\n"
                                         "	background-color: #15202B;\n"
                                         "\n"
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
                                         "#name {\n"
                                         "	color: #fff;\n"
                                         "	letter-spacing: 4px;\n"
                                         "}\n"
                                         "#projectDesc {\n"
                                         "	color: #fff;\n"
                                         "	letter-spacing: 9.5px\n"
                                         "}\n"
                                         "#welcomeMessage {\n"
                                         "	color: #fff;\n"
                                         "	letter-spacing: 1.5px;\n"
                                         "	margin-top: 80px;\n"
                                         "	margin-bottom: 130px;\n"
                                         "}\n"
                                         "#userNameInput, #passInput {\n"
                                         "	background-color: transparent;\n"
                                         "	border: none;	\n"
                                         "	border-bottom: 2px solid #fff;\n"
                                         "	padding-top: 20px;\n"
                                         "	padding-bottom: 5px;\n"
                                         "	color: #fff;\n"
                                         "	letter-spacing: 1.5px\n"
                                         "}\n"
                                         "#userNameLabel, #passLabel {\n"
                                         "	color: #fff;\n"
                                         "	letter-spacing: 1.3px\n"
                                         "}\n"
                                         "#toUserFromUse"
                                         "rNameFrame, #toUserFromPassFrame {\n"
                                         "	color: #006AFF;\n"
                                         "	margin-top: 5px;\n"
                                         "	letter-spacing: 1.5px;\n"
                                         "	margin-bottom: 40px;\n"
                                         "}\n"
                                         "#signInButton {\n"
                                         "	background-color: #006AFF;\n"
                                         "	letter-spacing: 2px;\n"
                                         "	padding: 8px 0;\n"
                                         "	color: #fff;\n"
                                         "	border-radius: 5px;\n"
                                         "	margin: 20px 0 35px\n"
                                         "}\n"
                                         "#forgetPass {\n"
                                         "	color: #fff;\n"
                                         "	letter-spacing: 2px;\n"
                                         "	border: none\n"
                                         "}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.centralwidget)
        self.titleBar.setObjectName(u"titleBar")
        font1 = QFont()
        font1.setPointSize(3)
        self.titleBar.setFont(font1)
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.backBouttonFrame = QFrame(self.titleBar)
        self.backBouttonFrame.setObjectName(u"backBouttonFrame")
        self.backBouttonFrame.setFrameShape(QFrame.StyledPanel)
        self.backBouttonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.backBouttonFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.leftBtn = QPushButton(self.backBouttonFrame)
        self.leftBtn.setObjectName(u"leftBtn")
        self.leftBtn.setMaximumSize(QSize(19, 30))
        self.leftBtn.setStyleSheet(u"border: none;\n"
                                   "")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/left.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.leftBtn.setIcon(icon)
        self.leftBtn.setIconSize(QSize(25, 25))
        self.leftBtn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.leftBtn)

        self.horizontalLayout.addWidget(
            self.backBouttonFrame, 0, Qt.AlignLeft | Qt.AlignTop)

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
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.appName.setFont(font2)
        self.appName.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.appName, 0, Qt.AlignHCenter)

        self.horizontalLayout.addWidget(
            self.mainWindowTitle, 0, Qt.AlignHCenter)

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
        self.mainBody.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.mainBody)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.body = QFrame(self.mainBody)
        self.body.setObjectName(u"body")
        sizePolicy1.setHeightForWidth(
            self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy1)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.body)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(80, 60, 80, 50)
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.appNameAndLoge = QFrame(self.frame)
        self.appNameAndLoge.setObjectName(u"appNameAndLoge")
        self.appNameAndLoge.setFrameShape(QFrame.StyledPanel)
        self.appNameAndLoge.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.appNameAndLoge)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 3)
        self.logo = QLabel(self.appNameAndLoge)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(50, 50))
        font3 = QFont()
        font3.setPointSize(5)
        self.logo.setFont(font3)
        self.logo.setPixmap(QPixmap(u":/Icons/Icons/telegram.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo, 0, Qt.AlignBottom)

        self.name = QLabel(self.appNameAndLoge)
        self.name.setObjectName(u"name")
        font4 = QFont()
        font4.setFamily(u"Microsoft YaHei")
        font4.setPointSize(26)
        font4.setBold(False)
        font4.setWeight(50)
        self.name.setFont(font4)

        self.horizontalLayout_3.addWidget(self.name, 0, Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.appNameAndLoge)

        self.projectDesc = QLabel(self.frame)
        self.projectDesc.setObjectName(u"projectDesc")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.projectDesc.sizePolicy().hasHeightForWidth())
        self.projectDesc.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamily(u"Trebuchet MS")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.projectDesc.setFont(font5)

        self.verticalLayout_5.addWidget(self.projectDesc, 0, Qt.AlignRight)

        self.welcomeMessage = QLabel(self.frame)
        self.welcomeMessage.setObjectName(u"welcomeMessage")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.welcomeMessage.sizePolicy().hasHeightForWidth())
        self.welcomeMessage.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setFamily(u"Verdana")
        font6.setPointSize(14)
        self.welcomeMessage.setFont(font6)

        self.verticalLayout_5.addWidget(
            self.welcomeMessage, 0, Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.signInFrame = QFrame(self.body)
        self.signInFrame.setObjectName(u"signInFrame")
        sizePolicy1.setHeightForWidth(
            self.signInFrame.sizePolicy().hasHeightForWidth())
        self.signInFrame.setSizePolicy(sizePolicy1)
        self.signInFrame.setMinimumSize(QSize(400, 0))
        self.signInFrame.setFrameShape(QFrame.StyledPanel)
        self.signInFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.signInFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.userNameFrame = QFrame(self.signInFrame)
        self.userNameFrame.setObjectName(u"userNameFrame")
        self.userNameFrame.setFrameShape(QFrame.StyledPanel)
        self.userNameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.userNameFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.userNameLabel = QLabel(self.userNameFrame)
        self.userNameLabel.setObjectName(u"userNameLabel")
        font7 = QFont()
        font7.setFamily(u"Trebuchet MS")
        font7.setPointSize(10)
        self.userNameLabel.setFont(font7)

        self.verticalLayout_7.addWidget(self.userNameLabel)

        self.userNameInput = QLineEdit(self.userNameFrame)
        self.userNameInput.setObjectName(u"userNameInput")
        self.userNameInput.setMinimumSize(QSize(0, 0))
        self.userNameInput.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamily(u"8514oem")
        font8.setBold(False)
        font8.setWeight(50)
        self.userNameInput.setFont(font8)
        self.userNameInput.setStyleSheet(u"font-size: 10px;\n"
                                         "letter-spacing: 1.5px")

        self.verticalLayout_7.addWidget(self.userNameInput)

        self.toUserFromUserNameFrame = QLabel(self.userNameFrame)
        self.toUserFromUserNameFrame.setObjectName(u"toUserFromUserNameFrame")
        font9 = QFont()
        font9.setFamily(u"Trebuchet MS")
        font9.setPointSize(9)
        self.toUserFromUserNameFrame.setFont(font9)

        self.verticalLayout_7.addWidget(self.toUserFromUserNameFrame)

        self.verticalLayout_6.addWidget(self.userNameFrame)

        self.passFrame = QFrame(self.signInFrame)
        self.passFrame.setObjectName(u"passFrame")
        self.passFrame.setFrameShape(QFrame.StyledPanel)
        self.passFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.passFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.passLabel = QLabel(self.passFrame)
        self.passLabel.setObjectName(u"passLabel")
        self.passLabel.setFont(font7)

        self.verticalLayout_8.addWidget(self.passLabel)

        self.passInput = QLineEdit(self.passFrame)
        self.passInput.setEchoMode(QLineEdit.Password)
        self.passInput.setObjectName(u"passInput")
        font10 = QFont()
        font10.setFamily(u"8514oem")
        font10.setPointSize(8)
        self.passInput.setFont(font10)

        self.verticalLayout_8.addWidget(self.passInput)

        self.toUserFromPassFrame = QLabel(self.passFrame)
        self.toUserFromPassFrame.setObjectName(u"toUserFromPassFrame")
        self.toUserFromPassFrame.setFont(font9)

        self.verticalLayout_8.addWidget(self.toUserFromPassFrame)

        self.verticalLayout_6.addWidget(self.passFrame)

        self.signInButton = QPushButton(self.signInFrame)
        self.signInButton.setObjectName(u"signInButton")
        font11 = QFont()
        font11.setFamily(u"Trebuchet MS")
        font11.setPointSize(14)
        self.signInButton.setFont(font11)
        self.signInButton.setFlat(False)
        self.signInButton.shortcut = QShortcut(QKeySequence("Return"), self.signInButton)

        self.verticalLayout_6.addWidget(self.signInButton)

        self.forgetPass = QPushButton(self.signInFrame)
        self.forgetPass.setObjectName(u"forgetPass")
        self.forgetPass.setFont(font9)
        self.forgetPass.setFlat(False)

        self.verticalLayout_6.addWidget(self.forgetPass)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_4.addWidget(self.signInFrame, 0, Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.body)

        self.size_grip = QFrame(self.mainBody)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(
            self.size_grip, 0, Qt.AlignRight | Qt.AlignBottom)

        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.leftBtn.setText("")
        self.appName.setToolTip(QCoreApplication.translate(
            "MainWindow", u"App Name", None))
        self.appName.setText(QCoreApplication.translate(
            "MainWindow", u"chatZone", None))
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
        self.logo.setText("")
        self.name.setText(QCoreApplication.translate(
            "MainWindow", u"chatZone", None))
        self.projectDesc.setText(QCoreApplication.translate(
            "MainWindow", u"college project", None))
        self.welcomeMessage.setText(QCoreApplication.translate(
            "MainWindow", u"Welcome Back!", None))
        self.userNameLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Phone Number", None))
        self.toUserFromUserNameFrame.setText("")
        self.passLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Password", None))
        self.toUserFromPassFrame.setText("")
        self.signInButton.setText(
            QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.forgetPass.setText(QCoreApplication.translate(
            "MainWindow", u"Forget My Password", None))
