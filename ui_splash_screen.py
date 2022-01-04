from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 346)
        SplashScreen.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
                                            "	border-radius:150px;\n"
                                            "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
                                            "\n"
                                            "}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
                                      "	\n"
                                      "border-radius:150px;\n"
                                      "background-color: rgba(77, 77, 127,120);\n"
                                      "\n"
                                      "\n"
                                      "}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
                                     "   border-radius:135px;\n"
                                     "	background-color: rgb(77, 77, 127);\n"
                                     "\n"
                                     "}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 50, 191, 161))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color:none;\n"
                                      "color:#ffffff;")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelPercontage = QLabel(self.widget)
        self.labelPercontage.setObjectName(u"labelPercontage")
        font1 = QFont()
        font1.setFamily(u"Tempus Sans ITC")
        font1.setPointSize(68)
        self.labelPercontage.setFont(font1)
        self.labelPercontage.setStyleSheet(u"background-color:none;\n"
                                           "color:#ffffff;")
        self.labelPercontage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercontage, 1, 0, 1, 1)

        self.labelLoadingInfo = QLabel(self.widget)
        self.labelLoadingInfo.setObjectName(u"labelLoadingInfo")
        self.labelLoadingInfo.setMinimumSize(QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.labelLoadingInfo.setFont(font2)
        self.labelLoadingInfo.setStyleSheet(u"QLabel{\n"
                                            "background-color: rgb(93, 93, 154);\n"
                                            "border-radius:10px;\n"
                                            "color:#ffffff;\n"
                                            "margin-left:40px;\n"
                                            "margin-right:40px;\n"
                                            "}")
        self.labelLoadingInfo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoadingInfo, 2, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate(
            "SplashScreen", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate(
            "SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600; color:#8787ca;\">CHAT</span>ZONE</p></body></html>", None))
        self.labelPercontage.setText(QCoreApplication.translate(
            "SplashScreen", u"<p><span style=\" font-size:48pt;\">0</span><span style=\" font-size:48pt; vertical-align:super;\">%</span></p>", None))
        self.labelLoadingInfo.setText(QCoreApplication.translate(
            "SplashScreen", u"loading...", None))
