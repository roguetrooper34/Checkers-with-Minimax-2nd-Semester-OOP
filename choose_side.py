# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_side.ui'
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
    QPushButton, QSizePolicy, QWidget)
import images_rc

class Ui_choose_a_side(object):
    def setupUi(self, choose_a_side):
        if not choose_a_side.objectName():
            choose_a_side.setObjectName(u"choose_a_side")
        choose_a_side.setWindowModality(Qt.ApplicationModal)
        choose_a_side.resize(354, 194)
        choose_a_side.setMinimumSize(QSize(354, 194))
        choose_a_side.setMaximumSize(QSize(354, 194))
        icon = QIcon()
        icon.addFile(u":/ist_logo/ist_logo.png", QSize(), QIcon.Normal, QIcon.On)
        choose_a_side.setWindowIcon(icon)
        choose_a_side.setModal(True)
        self.label = QLabel(choose_a_side)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 271, 141))
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.horizontalLayoutWidget = QWidget(choose_a_side)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(180, 110, 160, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.chose_white_button = QPushButton(self.horizontalLayoutWidget)
        self.chose_white_button.setObjectName(u"chose_white_button")

        self.horizontalLayout.addWidget(self.chose_white_button)

        self.chose_black_button = QPushButton(self.horizontalLayoutWidget)
        self.chose_black_button.setObjectName(u"chose_black_button")

        self.horizontalLayout.addWidget(self.chose_black_button)

        self.toss_button = QPushButton(choose_a_side)
        self.toss_button.setObjectName(u"toss_button")
        self.toss_button.setGeometry(QRect(30, 140, 75, 24))

        self.retranslateUi(choose_a_side)

        self.chose_white_button.setDefault(True)


        QMetaObject.connectSlotsByName(choose_a_side)
    # setupUi

    def retranslateUi(self, choose_a_side):
        choose_a_side.setWindowTitle(QCoreApplication.translate("choose_a_side", u"Choose a side", None))
        self.label.setText(QCoreApplication.translate("choose_a_side", u"Choose a side:\n"
"\n"
"White (plays first)\n"
"Black (plays second)", None))
        self.chose_white_button.setText(QCoreApplication.translate("choose_a_side", u"White", None))
        self.chose_black_button.setText(QCoreApplication.translate("choose_a_side", u"Black", None))
        self.toss_button.setText(QCoreApplication.translate("choose_a_side", u"Toss", None))
    # retranslateUi

