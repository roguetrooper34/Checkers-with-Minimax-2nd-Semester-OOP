# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 620)
        MainWindow.setMinimumSize(QSize(900, 620))
        MainWindow.setMaximumSize(QSize(900, 620))
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/ist_logo/ist_logo.png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 160, 431, 331))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.playAIButton = QPushButton(self.verticalLayoutWidget)
        self.playAIButton.setObjectName(u"playAIButton")
        self.playAIButton.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.playAIButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.playAIButton)

        self.playHumanButton = QPushButton(self.verticalLayoutWidget)
        self.playHumanButton.setObjectName(u"playHumanButton")
        self.playHumanButton.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout.addWidget(self.playHumanButton)

        self.historyButton = QPushButton(self.verticalLayoutWidget)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout.addWidget(self.historyButton)

        self.quitButton = QPushButton(self.verticalLayoutWidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout.addWidget(self.quitButton)

        self.aboutButton = QPushButton(self.centralwidget)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setGeometry(QRect(704, 542, 141, 41))
        self.aboutButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(669, 50, 201, 191))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ai_score_label = QLabel(self.gridLayoutWidget)
        self.ai_score_label.setObjectName(u"ai_score_label")

        self.gridLayout.addWidget(self.ai_score_label, 4, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.player2_score_label = QLabel(self.gridLayoutWidget)
        self.player2_score_label.setObjectName(u"player2_score_label")

        self.gridLayout.addWidget(self.player2_score_label, 3, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.player1_score_label = QLabel(self.gridLayoutWidget)
        self.player1_score_label.setObjectName(u"player1_score_label")

        self.gridLayout.addWidget(self.player1_score_label, 2, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"MS Reference Sans Serif"])
        font1.setPointSize(14)
        font1.setUnderline(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 80, 331, 71))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(48)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 80, 111, 81))
        self.label_6.setPixmap(QPixmap(u":/ist_logo/ist_logo.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 901, 621))
        self.label_7.setPixmap(QPixmap(u":/main_menu_background/1036609-sports-symmetry-chess-shape-recreation-games-indoor-games-and-sports-board-game-tabletop-game-chessboard-english-draughts.jpg"))
        self.label_7.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_7.raise_()
        self.verticalLayoutWidget.raise_()
        self.aboutButton.raise_()
        self.gridLayoutWidget.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
#if QT_CONFIG(shortcut)
        self.label_7.setBuddy(self.label_7)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.close)

        self.playAIButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Checkers", None))
        self.playAIButton.setText(QCoreApplication.translate("MainWindow", u"Play vs AI", None))
        self.playHumanButton.setText(QCoreApplication.translate("MainWindow", u"Play vs Human", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"Recent Games", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.aboutButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.ai_score_label.setText(QCoreApplication.translate("MainWindow", u"0-0-0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"AI:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Player 1:", None))
        self.player2_score_label.setText(QCoreApplication.translate("MainWindow", u"0-0-0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Player 2:", None))
        self.player1_score_label.setText(QCoreApplication.translate("MainWindow", u"0-0-0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Checkers", None))
        self.label_6.setText("")
        self.label_7.setText("")
    # retranslateUi

