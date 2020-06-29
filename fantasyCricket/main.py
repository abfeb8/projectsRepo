from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# global variable set to store the selected team
currentTeam = set()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 921, 91))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.batCount = QtWidgets.QLabel(self.groupBox)
        self.batCount.setGeometry(QtCore.QRect(130, 40, 47, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.batCount.setFont(font)
        self.batCount.setStyleSheet("color: rgb(0, 170, 255);")
        self.batCount.setObjectName("batCount")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(230, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.bowCount = QtWidgets.QLabel(self.groupBox)
        self.bowCount.setGeometry(QtCore.QRect(340, 40, 31, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.bowCount.setFont(font)
        self.bowCount.setStyleSheet("color: rgb(0, 170, 255);")
        self.bowCount.setObjectName("bowCount")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(430, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.arCount = QtWidgets.QLabel(self.groupBox)
        self.arCount.setGeometry(QtCore.QRect(560, 40, 47, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.arCount.setFont(font)
        self.arCount.setStyleSheet("color: rgb(0, 170, 255);")
        self.arCount.setObjectName("arCount")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(660, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.wkCount = QtWidgets.QLabel(self.groupBox)
        self.wkCount.setGeometry(QtCore.QRect(820, 40, 47, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.wkCount.setFont(font)
        self.wkCount.setStyleSheet("color: rgb(0, 170, 255);")
        self.wkCount.setObjectName("wkCount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 131, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pointsAvailable = QtWidgets.QLabel(self.centralwidget)
        self.pointsAvailable.setGeometry(QtCore.QRect(180, 150, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.pointsAvailable.setFont(font)
        self.pointsAvailable.setStyleSheet("color: rgb(0, 170, 255);")
        self.pointsAvailable.setObjectName("pointsAvailable")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 140, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pointsUsed = QtWidgets.QLabel(self.centralwidget)
        self.pointsUsed.setGeometry(QtCore.QRect(620, 150, 47, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.pointsUsed.setFont(font)
        self.pointsUsed.setStyleSheet("color: rgb(0, 170, 255);")
        self.pointsUsed.setObjectName("pointsUsed")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 180, 401, 451))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioBat = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBat.setGeometry(QtCore.QRect(20, 20, 82, 17))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioBat.setFont(font)
        self.radioBat.setObjectName("radioBat")
        self.radioBow = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBow.setGeometry(QtCore.QRect(110, 20, 82, 17))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioBow.setFont(font)
        self.radioBow.setObjectName("radioBow")
        self.radioAr = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioAr.setGeometry(QtCore.QRect(210, 20, 82, 17))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioAr.setFont(font)
        self.radioAr.setObjectName("radioAr")
        self.radioWk = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioWk.setGeometry(QtCore.QRect(320, 20, 82, 17))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioWk.setFont(font)
        self.radioWk.setObjectName("radioWk")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 70, 361, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playerDiaplay1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay1.setFont(font)
        self.playerDiaplay1.setText("")
        self.playerDiaplay1.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay1.setObjectName("playerDiaplay1")
        self.verticalLayout.addWidget(self.playerDiaplay1)
        self.playerDiaplay2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay2.setFont(font)
        self.playerDiaplay2.setText("")
        self.playerDiaplay2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay2.setObjectName("playerDiaplay2")
        self.verticalLayout.addWidget(self.playerDiaplay2)
        self.playerDiaplay3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay3.setFont(font)
        self.playerDiaplay3.setText("")
        self.playerDiaplay3.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay3.setObjectName("playerDiaplay3")
        self.verticalLayout.addWidget(self.playerDiaplay3)
        self.playerDiaplay4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay4.setFont(font)
        self.playerDiaplay4.setText("")
        self.playerDiaplay4.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay4.setObjectName("playerDiaplay4")
        self.verticalLayout.addWidget(self.playerDiaplay4)
        self.playerDiaplay5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay5.setFont(font)
        self.playerDiaplay5.setText("")
        self.playerDiaplay5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay5.setObjectName("playerDiaplay5")
        self.verticalLayout.addWidget(self.playerDiaplay5)
        self.playerDiaplay6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay6.setFont(font)
        self.playerDiaplay6.setText("")
        self.playerDiaplay6.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay6.setObjectName("playerDiaplay6")
        self.verticalLayout.addWidget(self.playerDiaplay6)
        self.playerDiaplay7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay7.setFont(font)
        self.playerDiaplay7.setText("")
        self.playerDiaplay7.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay7.setObjectName("playerDiaplay7")
        self.verticalLayout.addWidget(self.playerDiaplay7)
        self.playerDiaplay8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay8.setFont(font)
        self.playerDiaplay8.setText("")
        self.playerDiaplay8.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay8.setObjectName("playerDiaplay8")
        self.verticalLayout.addWidget(self.playerDiaplay8)
        self.playerDiaplay9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay9.setFont(font)
        self.playerDiaplay9.setText("")
        self.playerDiaplay9.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay9.setObjectName("playerDiaplay9")
        self.verticalLayout.addWidget(self.playerDiaplay9)
        self.playerDiaplay10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay10.setFont(font)
        self.playerDiaplay10.setText("")
        self.playerDiaplay10.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerDiaplay10.setObjectName("playerDiaplay10")
        self.verticalLayout.addWidget(self.playerDiaplay10)
        self.playerDiaplay11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.playerDiaplay11.setFont(font)
        self.playerDiaplay11.setText("")
        self.playerDiaplay11.setObjectName("playerDiaplay11")
        self.verticalLayout.addWidget(self.playerDiaplay11)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(490, 180, 411, 451))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.selectedTeamName = QtWidgets.QLabel(self.groupBox_3)
        self.selectedTeamName.setGeometry(QtCore.QRect(140, 0, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.selectedTeamName.setFont(font)
        self.selectedTeamName.setStyleSheet("color: rgb(0, 170, 255);")
        self.selectedTeamName.setObjectName("selectedTeamName")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 371, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.teamDisplay1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay1.setFont(font)
        self.teamDisplay1.setText("")
        self.teamDisplay1.setObjectName("teamDisplay1")
        self.verticalLayout_2.addWidget(self.teamDisplay1)
        self.teamDisplay2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay2.setFont(font)
        self.teamDisplay2.setText("")
        self.teamDisplay2.setObjectName("teamDisplay2")
        self.verticalLayout_2.addWidget(self.teamDisplay2)
        self.teamDisplay3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay3.setFont(font)
        self.teamDisplay3.setText("")
        self.teamDisplay3.setObjectName("teamDisplay3")
        self.verticalLayout_2.addWidget(self.teamDisplay3)
        self.teamDisplay4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay4.setFont(font)
        self.teamDisplay4.setText("")
        self.teamDisplay4.setObjectName("teamDisplay4")
        self.verticalLayout_2.addWidget(self.teamDisplay4)
        self.teamDisplay5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay5.setFont(font)
        self.teamDisplay5.setText("")
        self.teamDisplay5.setObjectName("teamDisplay5")
        self.verticalLayout_2.addWidget(self.teamDisplay5)
        self.teamDisplay6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay6.setFont(font)
        self.teamDisplay6.setText("")
        self.teamDisplay6.setObjectName("teamDisplay6")
        self.verticalLayout_2.addWidget(self.teamDisplay6)
        self.teamDisplay7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay7.setFont(font)
        self.teamDisplay7.setText("")
        self.teamDisplay7.setObjectName("teamDisplay7")
        self.verticalLayout_2.addWidget(self.teamDisplay7)
        self.teamDisplay8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay8.setFont(font)
        self.teamDisplay8.setText("")
        self.teamDisplay8.setObjectName("teamDisplay8")
        self.verticalLayout_2.addWidget(self.teamDisplay8)
        self.teamDisplay9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay9.setFont(font)
        self.teamDisplay9.setText("")
        self.teamDisplay9.setObjectName("teamDisplay9")
        self.verticalLayout_2.addWidget(self.teamDisplay9)
        self.teamDisplay10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay10.setFont(font)
        self.teamDisplay10.setText("")
        self.teamDisplay10.setObjectName("teamDisplay10")
        self.verticalLayout_2.addWidget(self.teamDisplay10)
        self.teamDisplay11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.teamDisplay11.setFont(font)
        self.teamDisplay11.setText("")
        self.teamDisplay11.setObjectName("teamDisplay11")
        self.verticalLayout_2.addWidget(self.teamDisplay11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 21))
        self.menubar.setStyleSheet("background-color: rgb(115, 115, 115);\n"
                                   "color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionNew_Team.setFont(font)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# ****************************************************************************************
        # creating event to check if the 'NEW Team' option has been selected
        self.actionNew_Team.triggered.connect(lambda: self.clickedNewTeam())

        # creating event to check if any of the radio button has been pressed
        self.radioBat.clicked.connect(lambda: self.radioClick('BAT'))
        self.radioBow.clicked.connect(lambda: self.radioClick('BWL'))
        self.radioAr.clicked.connect(lambda: self.radioClick('AR'))
        self.radioWk.clicked.connect(lambda: self.radioClick('WK'))

        # creating event to select player from the playerDisplay
        self.playerDiaplay1.mousePressEvent = self.displayLable1Clicked
        self.playerDiaplay2.mousePressEvent = self.displayLable2Clicked
        self.playerDiaplay3.mousePressEvent = self.displayLable3Clicked
        self.playerDiaplay4.mousePressEvent = self.displayLable4Clicked
        self.playerDiaplay5.mousePressEvent = self.displayLable5Clicked
        self.playerDiaplay6.mousePressEvent = self.displayLable6Clicked
        self.playerDiaplay7.mousePressEvent = self.displayLable7Clicked
        self.playerDiaplay8.mousePressEvent = self.displayLable8Clicked
        self.playerDiaplay9.mousePressEvent = self.displayLable9Clicked
        self.playerDiaplay10.mousePressEvent = self.displayLable10Clicked
        self.playerDiaplay11.mousePressEvent = self.displayLable11Clicked

# ****************************************************************************************
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Your Selection"))
        self.label.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.batCount.setText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "Bowler(BOW)"))
        self.bowCount.setText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.arCount.setText(_translate("MainWindow", "##"))
        self.label_7.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.wkCount.setText(_translate("MainWindow", "##"))
        self.label_2.setText(_translate("MainWindow", "Points Available"))
        self.pointsAvailable.setText(_translate("MainWindow", "####"))
        self.label_6.setText(_translate("MainWindow", "Points Used"))
        self.pointsUsed.setText(_translate("MainWindow", "####"))
        self.radioBat.setText(_translate("MainWindow", "BAT"))
        self.radioBow.setText(_translate("MainWindow", "BOW"))
        self.radioAr.setText(_translate("MainWindow", "AR"))
        self.radioWk.setText(_translate("MainWindow", "WK"))
        self.label_4.setText(_translate("MainWindow", "Team Name"))
        self.selectedTeamName.setText(
            _translate("MainWindow", "Displayed Here"))
        self.menuManage_Teams.setTitle(
            _translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(
            _translate("MainWindow", "Evaluate Team"))

# ****************************************************************************************

    def clickedNewTeam(self):  # function to perform when new team option is selected
        # it will clear the previous list if present
        for i in range(1, 12):
            lable = getattr(self, 'playerDiaplay{}'.format(i))
            lable2 = getattr(self, 'teamDisplay{}'.format(i))
            lable.setText("")
            lable2.setText("")
        # seting all the value to there default values
        self.batCount.setText('0')
        self.bowCount.setText('0')
        self.arCount.setText('0')
        self.wkCount.setText('0')
        self.pointsAvailable.setText('1000')
        self.pointsUsed.setText('0')

    def radioClick(self, catogry):  # function to perform clicked on any of the radio button
        # it will clear the previous list if present
        for i in range(1, 12):
            lable = getattr(self, 'playerDiaplay{}'.format(i))
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            lable.setText("")
        # getting the players from our data base of the seleted catogeery
        c.execute("""
                  select player from stats
                  where ctg = :ctg
                  """, {'ctg': catogry})
        # set the lables on the UI to the players name
        k = 1
        for i in c.fetchall():
            lable = getattr(self, 'playerDiaplay{}'.format(k))
            lable.setText(str(i[0]))
            k += 1

    def displayLable1Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('1'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable2Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('2'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable3Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('3'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable4Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('4'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable5Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('5'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable6Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('6'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable7Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('7'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable8Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('8'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable9Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('9'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable10Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('10'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    def displayLable11Clicked(self, text):
        global currentTeam
        lable = getattr(self, 'playerDiaplay{}'.format('11'))
        if (lable.styleSheet()) == 'color: rgb(0, 170, 255);':
            lable.setStyleSheet("color: rgb(0, 0, 0);")
            currentTeam.remove(lable.text())
        else:
            lable.setStyleSheet("color: rgb(0, 170, 255);")
            currentTeam.add(lable.text())
        self.teamDisplay()

    # function to show current selected players in the team display menu
    def teamDisplay(self):
        global currentTeam
        k = 1
        currentTeam = list(currentTeam)
        for i in range(11):
            lable = getattr(self, 'teamDisplay{}'.format(str(k)))
            try:
                lable.setText(currentTeam[i])
            except Exception:
                lable.setText('')
            k += 1
        currentTeam = set(currentTeam)


# ****************************************************************************************
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
