# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import images_rc
import images_rc

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        if not aboutDialog.objectName():
            aboutDialog.setObjectName(u"aboutDialog")
        aboutDialog.resize(531, 331)
        aboutDialog.setMinimumSize(QSize(531, 331))
        aboutDialog.setMaximumSize(QSize(531, 331))
        icon = QIcon()
        icon.addFile(u":/ist_logo/ist_logo.png", QSize(), QIcon.Normal, QIcon.On)
        aboutDialog.setWindowIcon(icon)
        self.label_6 = QLabel(aboutDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 111, 81))
        self.label_6.setPixmap(QPixmap(u":/ist_logo/ist_logo.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(aboutDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 531, 331))
        self.label_7.setMinimumSize(QSize(531, 331))
        self.label_7.setMaximumSize(QSize(531, 331))
        self.label_7.setPixmap(QPixmap(u":/main_menu_background/1036609-sports-symmetry-chess-shape-recreation-games-indoor-games-and-sports-board-game-tabletop-game-chessboard-english-draughts.jpg"))
        self.label_7.setScaledContents(True)
        self.closeAboutButton = QPushButton(aboutDialog)
        self.closeAboutButton.setObjectName(u"closeAboutButton")
        self.closeAboutButton.setGeometry(QRect(400, 270, 91, 41))
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(14)
        self.closeAboutButton.setFont(font)
        self.label = QLabel(aboutDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 404, 240))
        self.label.setFont(font)
        self.label_7.raise_()
        self.label_6.raise_()
        self.closeAboutButton.raise_()
        self.label.raise_()

        self.retranslateUi(aboutDialog)
        self.closeAboutButton.clicked.connect(aboutDialog.close)

        self.closeAboutButton.setDefault(True)


        QMetaObject.connectSlotsByName(aboutDialog)
    # setupUi

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QCoreApplication.translate("aboutDialog", u"About", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.closeAboutButton.setText(QCoreApplication.translate("aboutDialog", u"Ok", None))
        self.label.setText(QCoreApplication.translate("aboutDialog", u"Checkers, written in Python 3.10 and \n"
"Pyside6, it's a demo project made to \n"
"demonstrate knowledge of OOP and\n"
"fundamentals of programming for CS-02A\n"
"class of 2021 IST\n"
"\n"
"Credits:\n"
"Siraj Ahmed (group leader),\n"
"Waleed Malik,\n"
"Shahab Ahmed", None))
    # retranslateUi

