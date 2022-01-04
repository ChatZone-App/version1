import resourcesLogin_rc
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindowWelcome(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1197, 950)
        self.centralwidget = QWidget(MainWindow)
        font = QFont()
        font.setPointSize(8)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("* {\n"
                                         "    \n"
                                         "}\n"
                                         "\n"
                                         "#centralwidget{\n"
                                         "    background-color: #15202B;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "#titleBar {\n"
                                         "    background-color: #242526;\n"
                                         "}\n"
                                         "\n"
                                         "#close, #restore, #minimize {\n"
                                         "    border-radius: 7px\n"
                                         "}\n"
                                         "#close {\n"
                                         "    background-color: red;\n"
                                         "}\n"
                                         "#restore {\n"
                                         "    background-color: yellow;\n"
                                         "}\n"
                                         "#minimize {\n"
                                         "    background-color: green;\n"
                                         "}\n"
                                         "\n"
                                         "#appName {\n"
                                         "    letter-spacing: 1.5px;\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "\n"
                                         "#name {\n"
                                         "    color: #fff;\n"
                                         "    letter-spacing: 4px;\n"
                                         "}\n"
                                         "#projectDesc {\n"
                                         "    color: #fff;\n"
                                         "    letter-spacing: 9.5px\n"
                                         "}\n"
                                         "#welcomeMessage {\n"
                                         "    color: #fff;\n"
                                         "    letter-spacing: 1.5px;\n"
                                         "    margin-top: 80px;\n"
                                         "    margin-bottom: 130px;\n"
                                         "}\n"
                                         "#userNameInput, #passInput {\n"
                                         "    background-color: transparent;\n"
                                         "    border: none;    \n"
                                         "    border-bottom: 2px solid #fff;\n"
                                         "    padding-top: 20px;\n"
                                         "    padding-bottom: 5px;\n"
                                         "    color: #fff;\n"
                                         "    letter-spacing: 1.5px\n"
                                         "}\n"
                                         "#userNameLabel, #passLabel {\n"
                                         "    color: #fff;\n"
                                         "    letter-spacing: 1.3px\n"
                                         "}\n"
                                         "#toUserFromUserNameFrame, #toUserFromPassFrame {\n"
                                         "    color: #006AFF;\n"
                                         "    margin-top: 5px;\n"
                                         "    letter-spacing: 1.5px;\n"
                                         "    margin-bottom: 40px;\n"
                                         "}\n"
                                         "#signInButton {\n"
                                         "    background-color: #006AFF;\n"
                                         "    letter-spacing: 2px;\n"
                                         "    padding: 8px 0;\n"
                                         "    color: #fff;\n"
                                         "    border-radius: 5px;\n"
                                         "    margin: 20px 0 35px\n"
                                         "}\n"
                                         "#forgetPass {\n"
                                         "    color: #fff;\n"
                                         "    letter-spacing: 2px;\n"
                                         "    border: none\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBar = QFrame(self.centralwidget)
        font = QFont()
        font.setPointSize(3)
        self.titleBar.setFont(font)
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.titleBar.setObjectName("titleBar")
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backBouttonFrame = QFrame(self.titleBar)
        self.backBouttonFrame.setFrameShape(QFrame.StyledPanel)
        self.backBouttonFrame.setFrameShadow(QFrame.Raised)
        self.backBouttonFrame.setObjectName("backBouttonFrame")
        self.horizontalLayout_4 = QHBoxLayout(self.backBouttonFrame)
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout.addWidget(self.backBouttonFrame, 0, Qt.AlignLeft | Qt.AlignTop)
        self.mainWindowTitle = QFrame(self.titleBar)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWindowTitle.sizePolicy().hasHeightForWidth())
        self.mainWindowTitle.setSizePolicy(sizePolicy)
        self.mainWindowTitle.setFrameShape(QFrame.StyledPanel)
        self.mainWindowTitle.setFrameShadow(QFrame.Raised)
        self.mainWindowTitle.setObjectName("mainWindowTitle")
        self.verticalLayout_2 = QVBoxLayout(self.mainWindowTitle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.appName = QLabel(self.mainWindowTitle)
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.appName.setFont(font)
        self.appName.setStyleSheet("")
        self.appName.setObjectName("appName")
        self.verticalLayout_2.addWidget(self.appName, 0, Qt.AlignHCenter)
        self.horizontalLayout.addWidget(
            self.mainWindowTitle, 0, Qt.AlignHCenter)
        self.controls = QFrame(self.titleBar)
        self.controls.setFrameShape(QFrame.StyledPanel)
        self.controls.setFrameShadow(QFrame.Raised)
        self.controls.setObjectName("controls")
        self.horizontalLayout_2 = QHBoxLayout(self.controls)
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimize = QPushButton(self.controls)
        self.minimize.setMinimumSize(QSize(14, 14))
        self.minimize.setMaximumSize(QSize(14, 14))
        self.minimize.setText("")
        self.minimize.setObjectName("minimize")
        self.horizontalLayout_2.addWidget(self.minimize)
        self.restore = QPushButton(self.controls)
        self.restore.setMinimumSize(QSize(14, 14))
        self.restore.setMaximumSize(QSize(14, 14))
        self.restore.setText("")
        self.restore.setObjectName("restore")
        self.horizontalLayout_2.addWidget(self.restore)
        self.close = QPushButton(self.controls)
        self.close.setMinimumSize(QSize(14, 14))
        self.close.setMaximumSize(QSize(14, 14))
        self.close.setText("")
        self.close.setIconSize(QSize(20, 20))
        self.close.setObjectName("close")
        self.horizontalLayout_2.addWidget(self.close)
        self.horizontalLayout.addWidget(self.controls, 0, Qt.AlignRight)
        self.verticalLayout.addWidget(self.titleBar, 0, Qt.AlignTop)
        self.mainBody = QWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        self.mainBody.setFont(font)
        self.mainBody.setToolTip("")
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout_3 = QVBoxLayout(self.mainBody)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.body = QFrame(self.mainBody)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.body.setObjectName("body")
        self.verticalLayout_4 = QVBoxLayout(self.body)
        self.verticalLayout_4.setContentsMargins(80, 60, 80, 50)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QFrame(self.body)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.appNameAndLoge = QFrame(self.frame)
        self.appNameAndLoge.setFrameShape(QFrame.StyledPanel)
        self.appNameAndLoge.setFrameShadow(QFrame.Raised)
        self.appNameAndLoge.setObjectName("appNameAndLoge")
        self.horizontalLayout_3 = QHBoxLayout(self.appNameAndLoge)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 3)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QLabel(self.appNameAndLoge)
        self.logo.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(5)
        self.logo.setFont(font)
        self.logo.setText("")
        self.logo.setPixmap(QPixmap(":/Icons/Icons/telegram.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo, 0, Qt.AlignBottom)
        self.name = QLabel(self.appNameAndLoge)
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.horizontalLayout_3.addWidget(self.name, 0, Qt.AlignVCenter)
        self.verticalLayout_5.addWidget(self.appNameAndLoge)
        self.projectDesc = QLabel(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.projectDesc.sizePolicy().hasHeightForWidth())
        self.projectDesc.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.projectDesc.setFont(font)
        self.projectDesc.setObjectName("projectDesc")
        self.verticalLayout_5.addWidget(self.projectDesc, 0, Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frame, 0, Qt.AlignHCenter)
        self.frame_2 = QFrame(self.body)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(400, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.CreateaccB = QPushButton(self.frame_2)
        self.CreateaccB.setGeometry(QRect(250, 385, 551, 51))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        self.CreateaccB.setFont(font)
        self.CreateaccB.setStyleSheet("background-color: #006aff;\n"
                                      "color: white;\n"
                                      "border-radius: 7px;")
        self.CreateaccB.setObjectName("CreateaccB")
        self.loginB = QPushButton(self.frame_2)
        self.loginB.setGeometry(QRect(250, 265, 551, 51))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        self.loginB.setFont(font)
        self.loginB.setStyleSheet("background-color: #006aff;\n"
                                  "color: white;\n"
                                  "border-radius: 7px;")
        self.loginB.setObjectName("loginB")
        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.body)
        self.size_grip = QFrame(self.mainBody)
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.verticalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight | Qt.AlignBottom)
        self.verticalLayout.addWidget(self.mainBody)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appName.setToolTip(_translate("MainWindow", "App Name"))
        self.appName.setText(_translate("MainWindow", "chatZone"))
        self.minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.restore.setToolTip(_translate("MainWindow", "Restore"))
        self.close.setToolTip(_translate("MainWindow", "Close"))
        self.name.setText(_translate("MainWindow", "chatZone"))
        self.projectDesc.setText(_translate("MainWindow", "college project"))
        self.CreateaccB.setText(_translate("MainWindow", "Sign Up"))
        self.loginB.setText(_translate("MainWindow", "Sign In"))
