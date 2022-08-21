# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_player.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import images_rc

class Ui_which_player_dialog(object):
    def setupUi(self, which_player_dialog):
        if not which_player_dialog.objectName():
            which_player_dialog.setObjectName(u"which_player_dialog")
        which_player_dialog.resize(416, 132)
        icon = QIcon()
        icon.addFile(u":/ist_logo/ist_logo.png", QSize(), QIcon.Normal, QIcon.On)
        which_player_dialog.setWindowIcon(icon)
        self.label = QLabel(which_player_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 440, 81))
        self.label.setMinimumSize(QSize(440, 81))
        self.label.setMaximumSize(QSize(440, 81))
        self.label.setStyleSheet(u"font: 14pt \"MS Reference Sans Serif\";")
        self.horizontalLayoutWidget = QWidget(which_player_dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 50, 401, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.player1_button = QPushButton(self.horizontalLayoutWidget)
        self.player1_button.setObjectName(u"player1_button")

        self.horizontalLayout.addWidget(self.player1_button)

        self.horizontalSpacer = QSpacerItem(30, 10, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.player2_button = QPushButton(self.horizontalLayoutWidget)
        self.player2_button.setObjectName(u"player2_button")

        self.horizontalLayout.addWidget(self.player2_button)


        self.retranslateUi(which_player_dialog)

        QMetaObject.connectSlotsByName(which_player_dialog)
    # setupUi

    def retranslateUi(self, which_player_dialog):
        which_player_dialog.setWindowTitle(QCoreApplication.translate("which_player_dialog", u"Who is going to play against the AI?", None))
        self.label.setText(QCoreApplication.translate("which_player_dialog", u"Choose which player is playing against\n"
"the AI", None))
        self.player1_button.setText(QCoreApplication.translate("which_player_dialog", u"Player 1", None))
        self.player2_button.setText(QCoreApplication.translate("which_player_dialog", u"Player 2", None))
    # retranslateUi

