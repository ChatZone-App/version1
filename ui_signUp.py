from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import resourcesSignUp_rc


class Ui_MainWindowSU(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1197, 950)  # 1148, 944
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
                                         "#firstNameInput, #lastNameInput,\n"
                                         "#userNameInput, #phoneInput, #pinInput,\n"
                                         "#confPassInput, #passInput{\n"
                                         "	background-color: transparent;\n"
                                         "	border: none;	\n"
                                         "	border-bottom: 2px solid #fff;\n"
                                         "	padding-top: 20px;\n"
                                         "	padding-bottom: 5px;\n"
                                         "	color: #fff;\n"
                                         "	letter-spacing: 1.5px\n"
                                         "}\n"
                                         "#firstNameLabel, #"
                                         "lastNameLabel,\n"
                                         "#userNameLabel, #phoneLabel , #pinLabel,\n"
                                         "#passLabel, #confPassLabel  {\n"
                                         "	color: #fff;\n"
                                         "	letter-spacing: 1.3px\n"
                                         "}\n"
                                         "#toUserFromFirstNameFrame, #toUserFromLastNameFrame, \n"
                                         "#toUserFromUserNameFrame, #toUserFromPhoneFrame ,\n"
                                         "#toUserFromPinFrame, #toUserFromPassFrame, #toUserFromConfPassFrame {\n"
                                         "	color: #006AFF;\n"
                                         "	margin-top: 5px;\n"
                                         "	letter-spacing: 1.5px;\n"
                                         "	margin-bottom: 25px;\n"
                                         "}\n"
                                         "#signUpButton {\n"
                                         "	background-color: #006AFF;\n"
                                         "	letter-spacing: 2px;\n"
                                         "	padding: 8px 0;\n"
                                         "	color: #fff;\n"
                                         "	border-radius: 5px;\n"
                                         "	margin: 30px 0\n"
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
        icon.addFile(u":/icons/Icons/left.png",
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
        self.verticalLayout_4.setContentsMargins(80, 50, 80, 50)
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 60)
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
        self.logo.setPixmap(QPixmap(u":/icons/Icons/telegram.png"))
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

        self.verticalLayout_4.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.signUpFreame = QFrame(self.body)
        self.signUpFreame.setObjectName(u"signUpFreame")
        sizePolicy1.setHeightForWidth(
            self.signUpFreame.sizePolicy().hasHeightForWidth())
        self.signUpFreame.setSizePolicy(sizePolicy1)
        self.signUpFreame.setFrameShape(QFrame.StyledPanel)
        self.signUpFreame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.signUpFreame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.firstAndLastName = QFrame(self.signUpFreame)
        self.firstAndLastName.setObjectName(u"firstAndLastName")
        self.firstAndLastName.setFrameShape(QFrame.StyledPanel)
        self.firstAndLastName.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.firstAndLastName)
        self.horizontalLayout_5.setSpacing(40)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.firstName = QFrame(self.firstAndLastName)
        self.firstName.setObjectName(u"firstName")
        self.firstName.setFrameShape(QFrame.StyledPanel)
        self.firstName.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.firstName)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.firstNameFrame = QFrame(self.firstName)
        self.firstNameFrame.setObjectName(u"firstNameFrame")
        self.firstNameFrame.setMinimumSize(QSize(300, 0))
        self.firstNameFrame.setFrameShape(QFrame.StyledPanel)
        self.firstNameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.firstNameFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.firstNameLabel = QLabel(self.firstNameFrame)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        font6 = QFont()
        font6.setFamily(u"Trebuchet MS")
        font6.setPointSize(10)
        self.firstNameLabel.setFont(font6)

        self.verticalLayout_7.addWidget(self.firstNameLabel)

        self.firstNameInput = QLineEdit(self.firstNameFrame)
        self.firstNameInput.setObjectName(u"firstNameInput")
        self.firstNameInput.setMinimumSize(QSize(0, 0))
        self.firstNameInput.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamily(u"8514oem")
        font7.setBold(False)
        font7.setWeight(50)
        self.firstNameInput.setFont(font7)
        self.firstNameInput.setStyleSheet(u"font-size: 10px;\n"
                                          "letter-spacing: 1.5px")

        self.verticalLayout_7.addWidget(self.firstNameInput)

        self.toUserFromFirstNameFrame = QLabel(self.firstNameFrame)
        self.toUserFromFirstNameFrame.setObjectName(
            u"toUserFromFirstNameFrame")
        font8 = QFont()
        font8.setFamily(u"Trebuchet MS")
        font8.setPointSize(9)
        self.toUserFromFirstNameFrame.setFont(font8)

        self.verticalLayout_7.addWidget(self.toUserFromFirstNameFrame)

        self.verticalLayout_8.addWidget(self.firstNameFrame, 0, Qt.AlignRight)

        self.horizontalLayout_5.addWidget(self.firstName, 0, Qt.AlignTop)

        self.lastName = QFrame(self.firstAndLastName)
        self.lastName.setObjectName(u"lastName")
        self.lastName.setFrameShape(QFrame.StyledPanel)
        self.lastName.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.lastName)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lastNameFrame = QFrame(self.lastName)
        self.lastNameFrame.setObjectName(u"lastNameFrame")
        self.lastNameFrame.setMinimumSize(QSize(300, 0))
        self.lastNameFrame.setFrameShape(QFrame.StyledPanel)
        self.lastNameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.lastNameFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lastNameLabel = QLabel(self.lastNameFrame)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setFont(font6)

        self.verticalLayout_12.addWidget(self.lastNameLabel)

        self.lastNameInput = QLineEdit(self.lastNameFrame)
        self.lastNameInput.setObjectName(u"lastNameInput")
        self.lastNameInput.setMinimumSize(QSize(0, 0))
        self.lastNameInput.setMaximumSize(QSize(16777215, 16777215))
        self.lastNameInput.setFont(font7)
        self.lastNameInput.setStyleSheet(u"font-size: 10px;\n"
                                         "letter-spacing: 1.5px")

        self.verticalLayout_12.addWidget(self.lastNameInput)

        self.toUserFromLastNameFrame = QLabel(self.lastNameFrame)
        self.toUserFromLastNameFrame.setObjectName(u"toUserFromLastNameFrame")
        self.toUserFromLastNameFrame.setFont(font8)

        self.verticalLayout_12.addWidget(self.toUserFromLastNameFrame)

        self.verticalLayout_13.addWidget(
            self.lastNameFrame, 0, Qt.AlignLeft | Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.lastName, 0, Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.firstAndLastName)

        self.userName = QFrame(self.signUpFreame)
        self.userName.setObjectName(u"userName")
        sizePolicy1.setHeightForWidth(
            self.userName.sizePolicy().hasHeightForWidth())
        self.userName.setSizePolicy(sizePolicy1)
        self.userName.setMinimumSize(QSize(0, 0))
        self.userName.setFrameShape(QFrame.StyledPanel)
        self.userName.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.userName)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.userNameFrame = QFrame(self.userName)
        self.userNameFrame.setObjectName(u"userNameFrame")
        self.userNameFrame.setMinimumSize(QSize(640, 0))
        self.userNameFrame.setFrameShape(QFrame.StyledPanel)
        self.userNameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.userNameFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.userNameLabel = QLabel(self.userNameFrame)
        self.userNameLabel.setObjectName(u"userNameLabel")
        self.userNameLabel.setFont(font6)

        self.verticalLayout_9.addWidget(self.userNameLabel)

        self.userNameInput = QLineEdit(self.userNameFrame)
        self.userNameInput.setObjectName(u"userNameInput")
        self.userNameInput.setMinimumSize(QSize(0, 0))
        self.userNameInput.setMaximumSize(QSize(16777215, 16777215))
        self.userNameInput.setFont(font7)
        self.userNameInput.setStyleSheet(u"font-size: 10px;\n"
                                         "letter-spacing: 1.5px")

        self.verticalLayout_9.addWidget(self.userNameInput)

        self.toUserFromUserNameFrame = QLabel(self.userNameFrame)
        self.toUserFromUserNameFrame.setObjectName(u"toUserFromUserNameFrame")
        self.toUserFromUserNameFrame.setFont(font8)

        self.verticalLayout_9.addWidget(self.toUserFromUserNameFrame)

        self.verticalLayout_10.addWidget(
            self.userNameFrame, 0, Qt.AlignHCenter)

        self.verticalLayout_6.addWidget(self.userName, 0, Qt.AlignTop)

        self.phoneAndPin = QFrame(self.signUpFreame)
        self.phoneAndPin.setObjectName(u"phoneAndPin")
        sizePolicy1.setHeightForWidth(
            self.phoneAndPin.sizePolicy().hasHeightForWidth())
        self.phoneAndPin.setSizePolicy(sizePolicy1)
        self.phoneAndPin.setFrameShape(QFrame.StyledPanel)
        self.phoneAndPin.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.phoneAndPin)
        self.horizontalLayout_6.setSpacing(40)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.phoneNumber = QFrame(self.phoneAndPin)
        self.phoneNumber.setObjectName(u"phoneNumber")
        self.phoneNumber.setFrameShape(QFrame.StyledPanel)
        self.phoneNumber.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.phoneNumber)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.phoneFrame = QFrame(self.phoneNumber)
        self.phoneFrame.setObjectName(u"phoneFrame")
        self.phoneFrame.setMinimumSize(QSize(300, 0))
        self.phoneFrame.setFrameShape(QFrame.StyledPanel)
        self.phoneFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.phoneFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.phoneLabel = QLabel(self.phoneFrame)
        self.phoneLabel.setObjectName(u"phoneLabel")
        self.phoneLabel.setFont(font6)

        self.verticalLayout_14.addWidget(self.phoneLabel)

        self.phoneInput = QLineEdit(self.phoneFrame)
        self.phoneInput.setObjectName(u"phoneInput")
        self.phoneInput.setMinimumSize(QSize(0, 0))
        self.phoneInput.setMaximumSize(QSize(16777215, 16777215))
        self.phoneInput.setFont(font7)
        self.phoneInput.setStyleSheet(u"font-size: 10px;\n"
                                      "letter-spacing: 1.5px")

        self.verticalLayout_14.addWidget(self.phoneInput)

        self.toUserFromPhoneFrame = QLabel(self.phoneFrame)
        self.toUserFromPhoneFrame.setObjectName(u"toUserFromPhoneFrame")
        self.toUserFromPhoneFrame.setFont(font8)

        self.verticalLayout_14.addWidget(self.toUserFromPhoneFrame)

        self.verticalLayout_11.addWidget(self.phoneFrame, 0, Qt.AlignRight)

        self.horizontalLayout_6.addWidget(self.phoneNumber)

        self.pin = QFrame(self.phoneAndPin)
        self.pin.setObjectName(u"pin")
        self.pin.setFrameShape(QFrame.StyledPanel)
        self.pin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pin)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pinFrame = QFrame(self.pin)
        self.pinFrame.setObjectName(u"pinFrame")
        self.pinFrame.setMinimumSize(QSize(300, 0))
        self.pinFrame.setFrameShape(QFrame.StyledPanel)
        self.pinFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.pinFrame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pinLabel = QLabel(self.pinFrame)
        self.pinLabel.setObjectName(u"pinLabel")
        self.pinLabel.setFont(font6)

        self.verticalLayout_16.addWidget(self.pinLabel)

        self.pinInput = QLineEdit(self.pinFrame)
        self.pinInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.pinInput.setObjectName(u"pinInput")
        self.pinInput.setMinimumSize(QSize(0, 0))
        self.pinInput.setMaximumSize(QSize(16777215, 16777215))
        self.pinInput.setFont(font7)
        self.pinInput.setStyleSheet(u"font-size: 10px;\n"
                                    "letter-spacing: 1.5px")

        self.verticalLayout_16.addWidget(self.pinInput)

        self.toUserFromPinFrame = QLabel(self.pinFrame)
        self.toUserFromPinFrame.setObjectName(u"toUserFromPinFrame")
        self.toUserFromPinFrame.setFont(font8)

        self.verticalLayout_16.addWidget(self.toUserFromPinFrame)

        self.verticalLayout_15.addWidget(self.pinFrame, 0, Qt.AlignLeft)

        self.horizontalLayout_6.addWidget(self.pin)

        self.verticalLayout_6.addWidget(self.phoneAndPin, 0, Qt.AlignTop)

        self.passAndConfirmation = QFrame(self.signUpFreame)
        self.passAndConfirmation.setObjectName(u"passAndConfirmation")
        self.passAndConfirmation.setFrameShape(QFrame.StyledPanel)
        self.passAndConfirmation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.passAndConfirmation)
        self.horizontalLayout_7.setSpacing(40)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.password = QFrame(self.passAndConfirmation)
        self.password.setObjectName(u"password")
        sizePolicy1.setHeightForWidth(
            self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy1)
        self.password.setFrameShape(QFrame.StyledPanel)
        self.password.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.password)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.passFrame = QFrame(self.password)
        self.passFrame.setObjectName(u"passFrame")
        self.passFrame.setMinimumSize(QSize(300, 0))
        self.passFrame.setFrameShape(QFrame.StyledPanel)
        self.passFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.passFrame)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.passLabel = QLabel(self.passFrame)
        self.passLabel.setObjectName(u"passLabel")
        self.passLabel.setFont(font6)

        self.verticalLayout_18.addWidget(self.passLabel)

        self.passInput = QLineEdit(self.passFrame)
        self.passInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.passInput.setObjectName(u"passInput")
        self.passInput.setMinimumSize(QSize(0, 0))
        self.passInput.setMaximumSize(QSize(16777215, 16777215))
        self.passInput.setFont(font7)
        self.passInput.setStyleSheet(u"font-size: 10px;\n"
                                     "letter-spacing: 1.5px")

        self.verticalLayout_18.addWidget(self.passInput)

        self.toUserFromPassFrame = QLabel(self.passFrame)
        self.toUserFromPassFrame.setObjectName(u"toUserFromPassFrame")
        self.toUserFromPassFrame.setFont(font8)

        self.verticalLayout_18.addWidget(self.toUserFromPassFrame)

        self.verticalLayout_17.addWidget(
            self.passFrame, 0, Qt.AlignRight | Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.password)

        self.confPass = QFrame(self.passAndConfirmation)
        self.confPass.setObjectName(u"confPass")
        self.confPass.setFrameShape(QFrame.StyledPanel)
        self.confPass.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.confPass)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.confPassFrame = QFrame(self.confPass)
        self.confPassFrame.setObjectName(u"confPassFrame")
        self.confPassFrame.setMinimumSize(QSize(300, 0))
        self.confPassFrame.setFrameShape(QFrame.StyledPanel)
        self.confPassFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.confPassFrame)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.confPassLabel = QLabel(self.confPassFrame)
        self.confPassLabel.setObjectName(u"confPassLabel")
        self.confPassLabel.setFont(font6)

        self.verticalLayout_20.addWidget(self.confPassLabel)

        self.confPassInput = QLineEdit(self.confPassFrame)
        # self.password_text=QtGui.QLineEdit()
        self.confPassInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.confPassInput.setObjectName(u"confPassInput")
        self.confPassInput.setMinimumSize(QSize(0, 0))
        self.confPassInput.setMaximumSize(QSize(16777215, 16777215))
        self.confPassInput.setFont(font7)
        self.confPassInput.setStyleSheet(u"font-size: 10px;\n"
                                         "letter-spacing: 1.5px")

        self.verticalLayout_20.addWidget(self.confPassInput)

        self.toUserFromConfPassFrame = QLabel(self.confPassFrame)
        self.toUserFromConfPassFrame.setObjectName(u"toUserFromConfPassFrame")
        self.toUserFromConfPassFrame.setFont(font8)

        self.verticalLayout_20.addWidget(self.toUserFromConfPassFrame)

        self.verticalLayout_19.addWidget(
            self.confPassFrame, 0, Qt.AlignLeft | Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.confPass)

        self.verticalLayout_6.addWidget(
            self.passAndConfirmation, 0, Qt.AlignTop)

        self.signUpButton = QPushButton(self.signUpFreame)
        self.signUpButton.setObjectName(u"signUpButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.signUpButton.sizePolicy().hasHeightForWidth())
        self.signUpButton.setSizePolicy(sizePolicy3)
        self.signUpButton.setMinimumSize(QSize(640, 0))
        self.signUpButton.setMaximumSize(QSize(640, 16777215))
        font9 = QFont()
        font9.setFamily(u"Trebuchet MS")
        font9.setPointSize(14)
        self.signUpButton.setFont(font9)
        self.signUpButton.setFlat(False)
        self.signUpButton.shortcut = QShortcut(QKeySequence("Return"), self.signUpButton)


        self.verticalLayout_6.addWidget(
            self.signUpButton, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.signUpFreame)

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
        self.firstNameLabel.setText(QCoreApplication.translate(
            "MainWindow", u"First Name", None))
        self.toUserFromFirstNameFrame.setText("")
        self.lastNameLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Last Name", None))
        self.toUserFromLastNameFrame.setText("")
        self.userNameLabel.setText(QCoreApplication.translate(
            "MainWindow", u"User Name", None))
        self.toUserFromUserNameFrame.setText("")
        self.phoneLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Phone Number", None))
        self.toUserFromPhoneFrame.setText("")
        self.pinLabel.setText(
            QCoreApplication.translate("MainWindow", u"PIN", None))
        self.toUserFromPinFrame.setText("")
        self.passLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Password", None))
        self.toUserFromPassFrame.setText("")
        self.confPassLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Confirm Password", None))
        self.toUserFromConfPassFrame.setText("")
        self.signUpButton.setText(
            QCoreApplication.translate("MainWindow", u"Sign Up", None))
