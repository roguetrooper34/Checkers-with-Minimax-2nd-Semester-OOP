# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'play_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDialog, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)
import images_rc

class Ui_playCheckers(object):
    def setupUi(self, playCheckers):
        if not playCheckers.objectName():
            playCheckers.setObjectName(u"playCheckers")
        playCheckers.setWindowModality(Qt.WindowModal)
        playCheckers.resize(900, 620)
        playCheckers.setMinimumSize(QSize(900, 620))
        playCheckers.setMaximumSize(QSize(900, 621))
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(14)
        playCheckers.setFont(font)
        icon = QIcon()
        icon.addFile(u":/ist_logo/ist_logo.png", QSize(), QIcon.Normal, QIcon.On)
        playCheckers.setWindowIcon(icon)
        playCheckers.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 243, 231, 255), stop:0.5625 rgba(235, 213, 164, 255), stop:0.98 rgba(235, 208, 136, 255), stop:1 rgba(0, 0, 0, 0));")
        self.gridLayoutWidget = QWidget(playCheckers)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 689, 618))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkers28 = QPushButton(self.gridLayoutWidget)
        self.playing_spots = QButtonGroup(playCheckers)
        self.playing_spots.setObjectName(u"playing_spots")
        self.playing_spots.addButton(self.checkers28)
        self.checkers28.setObjectName(u"checkers28")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.checkers28.sizePolicy().hasHeightForWidth())
        self.checkers28.setSizePolicy(sizePolicy)
        self.checkers28.setMinimumSize(QSize(85, 77))
        self.checkers28.setMaximumSize(QSize(85, 70))
        self.checkers28.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers28.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers28, 6, 7, 1, 1)

        self.pushButton_59 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup = QButtonGroup(playCheckers)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setExclusive(False)
        self.buttonGroup.addButton(self.pushButton_59)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_59.sizePolicy().hasHeightForWidth())
        self.pushButton_59.setSizePolicy(sizePolicy)
        self.pushButton_59.setMinimumSize(QSize(85, 77))
        self.pushButton_59.setMaximumSize(QSize(85, 70))
        self.pushButton_59.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_59, 1, 7, 1, 1)

        self.checkers24 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers24)
        self.checkers24.setObjectName(u"checkers24")
        sizePolicy.setHeightForWidth(self.checkers24.sizePolicy().hasHeightForWidth())
        self.checkers24.setSizePolicy(sizePolicy)
        self.checkers24.setMinimumSize(QSize(85, 77))
        self.checkers24.setMaximumSize(QSize(85, 70))
        self.checkers24.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers24.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers24, 5, 6, 1, 1)

        self.checkers6 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers6)
        self.checkers6.setObjectName(u"checkers6")
        sizePolicy.setHeightForWidth(self.checkers6.sizePolicy().hasHeightForWidth())
        self.checkers6.setSizePolicy(sizePolicy)
        self.checkers6.setMinimumSize(QSize(85, 77))
        self.checkers6.setMaximumSize(QSize(85, 70))
        self.checkers6.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers6.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers6, 1, 2, 1, 1)

        self.pushButton_26 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_26)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setMinimumSize(QSize(85, 77))
        self.pushButton_26.setMaximumSize(QSize(85, 70))
        self.pushButton_26.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_26, 2, 6, 1, 1)

        self.pushButton_43 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_43)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy)
        self.pushButton_43.setMinimumSize(QSize(85, 77))
        self.pushButton_43.setMaximumSize(QSize(85, 70))
        self.pushButton_43.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_43, 5, 5, 1, 1)

        self.checkers29 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers29)
        self.checkers29.setObjectName(u"checkers29")
        sizePolicy.setHeightForWidth(self.checkers29.sizePolicy().hasHeightForWidth())
        self.checkers29.setSizePolicy(sizePolicy)
        self.checkers29.setMinimumSize(QSize(85, 77))
        self.checkers29.setMaximumSize(QSize(85, 70))
        self.checkers29.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers29.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers29, 7, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(85, 77))
        self.pushButton_7.setMaximumSize(QSize(85, 70))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_7, 0, 6, 1, 1)

        self.pushButton_14 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_14)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QSize(85, 77))
        self.pushButton_14.setMaximumSize(QSize(85, 70))
        self.pushButton_14.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_14, 1, 1, 1, 1)

        self.pushButton_48 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_48)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy)
        self.pushButton_48.setMinimumSize(QSize(85, 77))
        self.pushButton_48.setMaximumSize(QSize(85, 70))
        self.pushButton_48.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_48, 5, 1, 1, 1)

        self.pushButton_29 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_29)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        self.pushButton_29.setMinimumSize(QSize(85, 77))
        self.pushButton_29.setMaximumSize(QSize(85, 70))
        self.pushButton_29.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_29, 1, 3, 1, 1)

        self.checkers25 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers25)
        self.checkers25.setObjectName(u"checkers25")
        sizePolicy.setHeightForWidth(self.checkers25.sizePolicy().hasHeightForWidth())
        self.checkers25.setSizePolicy(sizePolicy)
        self.checkers25.setMinimumSize(QSize(85, 77))
        self.checkers25.setMaximumSize(QSize(85, 70))
        self.checkers25.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers25.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers25, 6, 1, 1, 1)

        self.checkers32 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers32)
        self.checkers32.setObjectName(u"checkers32")
        sizePolicy.setHeightForWidth(self.checkers32.sizePolicy().hasHeightForWidth())
        self.checkers32.setSizePolicy(sizePolicy)
        self.checkers32.setMinimumSize(QSize(85, 77))
        self.checkers32.setMaximumSize(QSize(85, 70))
        self.checkers32.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers32.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers32, 7, 6, 1, 1)

        self.checkers20 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers20)
        self.checkers20.setObjectName(u"checkers20")
        sizePolicy.setHeightForWidth(self.checkers20.sizePolicy().hasHeightForWidth())
        self.checkers20.setSizePolicy(sizePolicy)
        self.checkers20.setMinimumSize(QSize(85, 77))
        self.checkers20.setMaximumSize(QSize(85, 70))
        self.checkers20.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.checkers20.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers20, 4, 7, 1, 1)

        self.checkers9 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers9)
        self.checkers9.setObjectName(u"checkers9")
        sizePolicy.setHeightForWidth(self.checkers9.sizePolicy().hasHeightForWidth())
        self.checkers9.setSizePolicy(sizePolicy)
        self.checkers9.setMinimumSize(QSize(85, 77))
        self.checkers9.setMaximumSize(QSize(85, 70))
        self.checkers9.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers9.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers9, 2, 1, 1, 1)

        self.checkers23 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers23)
        self.checkers23.setObjectName(u"checkers23")
        sizePolicy.setHeightForWidth(self.checkers23.sizePolicy().hasHeightForWidth())
        self.checkers23.setSizePolicy(sizePolicy)
        self.checkers23.setMinimumSize(QSize(85, 77))
        self.checkers23.setMaximumSize(QSize(85, 70))
        self.checkers23.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers23.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers23, 5, 4, 1, 1)

        self.pushButton_47 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_47)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy)
        self.pushButton_47.setMinimumSize(QSize(85, 77))
        self.pushButton_47.setMaximumSize(QSize(85, 70))
        self.pushButton_47.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_47, 4, 0, 1, 1)

        self.pushButton_63 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_63)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_63.sizePolicy().hasHeightForWidth())
        self.pushButton_63.setSizePolicy(sizePolicy)
        self.pushButton_63.setMinimumSize(QSize(85, 77))
        self.pushButton_63.setMaximumSize(QSize(85, 70))
        self.pushButton_63.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_63, 4, 6, 1, 1)

        self.pushButton_33 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_33)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        self.pushButton_33.setMinimumSize(QSize(85, 77))
        self.pushButton_33.setMaximumSize(QSize(85, 70))
        self.pushButton_33.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_33, 6, 2, 1, 1)

        self.pushButton_61 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_61)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_61.sizePolicy().hasHeightForWidth())
        self.pushButton_61.setSizePolicy(sizePolicy)
        self.pushButton_61.setMinimumSize(QSize(85, 77))
        self.pushButton_61.setMaximumSize(QSize(85, 70))
        self.pushButton_61.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_61, 4, 4, 1, 1)

        self.checkers31 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers31)
        self.checkers31.setObjectName(u"checkers31")
        sizePolicy.setHeightForWidth(self.checkers31.sizePolicy().hasHeightForWidth())
        self.checkers31.setSizePolicy(sizePolicy)
        self.checkers31.setMinimumSize(QSize(85, 77))
        self.checkers31.setMaximumSize(QSize(85, 70))
        self.checkers31.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers31.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers31, 7, 4, 1, 1)

        self.checkers26 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers26)
        self.checkers26.setObjectName(u"checkers26")
        sizePolicy.setHeightForWidth(self.checkers26.sizePolicy().hasHeightForWidth())
        self.checkers26.setSizePolicy(sizePolicy)
        self.checkers26.setMinimumSize(QSize(85, 77))
        self.checkers26.setMaximumSize(QSize(85, 70))
        self.checkers26.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers26.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers26, 6, 3, 1, 1)

        self.checkers14 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers14)
        self.checkers14.setObjectName(u"checkers14")
        sizePolicy.setHeightForWidth(self.checkers14.sizePolicy().hasHeightForWidth())
        self.checkers14.setSizePolicy(sizePolicy)
        self.checkers14.setMinimumSize(QSize(85, 77))
        self.checkers14.setMaximumSize(QSize(85, 70))
        self.checkers14.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.checkers14.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers14, 3, 2, 1, 1)

        self.checkers17 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers17)
        self.checkers17.setObjectName(u"checkers17")
        sizePolicy.setHeightForWidth(self.checkers17.sizePolicy().hasHeightForWidth())
        self.checkers17.setSizePolicy(sizePolicy)
        self.checkers17.setMinimumSize(QSize(85, 77))
        self.checkers17.setMaximumSize(QSize(85, 70))
        self.checkers17.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.checkers17.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers17, 4, 1, 1, 1)

        self.checkers13 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers13)
        self.checkers13.setObjectName(u"checkers13")
        sizePolicy.setHeightForWidth(self.checkers13.sizePolicy().hasHeightForWidth())
        self.checkers13.setSizePolicy(sizePolicy)
        self.checkers13.setMinimumSize(QSize(85, 77))
        self.checkers13.setMaximumSize(QSize(85, 70))
        self.checkers13.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.checkers13.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers13, 3, 0, 1, 1)

        self.checkers19 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers19)
        self.checkers19.setObjectName(u"checkers19")
        sizePolicy.setHeightForWidth(self.checkers19.sizePolicy().hasHeightForWidth())
        self.checkers19.setSizePolicy(sizePolicy)
        self.checkers19.setMinimumSize(QSize(85, 77))
        self.checkers19.setMaximumSize(QSize(85, 70))
        self.checkers19.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.checkers19.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers19, 4, 5, 1, 1)

        self.pushButton_49 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_49)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy)
        self.pushButton_49.setMinimumSize(QSize(85, 77))
        self.pushButton_49.setMaximumSize(QSize(85, 70))
        self.pushButton_49.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_49, 7, 3, 1, 1)

        self.checkers18 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers18)
        self.checkers18.setObjectName(u"checkers18")
        sizePolicy.setHeightForWidth(self.checkers18.sizePolicy().hasHeightForWidth())
        self.checkers18.setSizePolicy(sizePolicy)
        self.checkers18.setMinimumSize(QSize(85, 77))
        self.checkers18.setMaximumSize(QSize(85, 70))
        self.checkers18.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.checkers18.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers18, 4, 3, 1, 1)

        self.checkers7 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers7)
        self.checkers7.setObjectName(u"checkers7")
        sizePolicy.setHeightForWidth(self.checkers7.sizePolicy().hasHeightForWidth())
        self.checkers7.setSizePolicy(sizePolicy)
        self.checkers7.setMinimumSize(QSize(85, 77))
        self.checkers7.setMaximumSize(QSize(85, 70))
        self.checkers7.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers7.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers7, 1, 4, 1, 1)

        self.pushButton_22 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_22)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setMinimumSize(QSize(85, 77))
        self.pushButton_22.setMaximumSize(QSize(85, 70))
        self.pushButton_22.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_22, 3, 7, 1, 1)

        self.checkers1 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers1)
        self.checkers1.setObjectName(u"checkers1")
        sizePolicy.setHeightForWidth(self.checkers1.sizePolicy().hasHeightForWidth())
        self.checkers1.setSizePolicy(sizePolicy)
        self.checkers1.setMinimumSize(QSize(85, 77))
        self.checkers1.setMaximumSize(QSize(85, 70))
        self.checkers1.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers1.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers1, 0, 1, 1, 1)

        self.pushButton_28 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_28)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        self.pushButton_28.setMinimumSize(QSize(85, 77))
        self.pushButton_28.setMaximumSize(QSize(85, 70))
        self.pushButton_28.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_28, 2, 4, 1, 1)

        self.pushButton_41 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_41)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy)
        self.pushButton_41.setMinimumSize(QSize(85, 77))
        self.pushButton_41.setMaximumSize(QSize(85, 70))
        self.pushButton_41.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_41, 5, 3, 1, 1)

        self.pushButton_20 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_20)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setMinimumSize(QSize(85, 77))
        self.pushButton_20.setMaximumSize(QSize(85, 70))
        self.pushButton_20.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_20, 2, 0, 1, 1)

        self.checkers27 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers27)
        self.checkers27.setObjectName(u"checkers27")
        sizePolicy.setHeightForWidth(self.checkers27.sizePolicy().hasHeightForWidth())
        self.checkers27.setSizePolicy(sizePolicy)
        self.checkers27.setMinimumSize(QSize(85, 77))
        self.checkers27.setMaximumSize(QSize(85, 70))
        self.checkers27.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers27.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers27, 6, 5, 1, 1)

        self.pushButton_16 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_16)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QSize(85, 77))
        self.pushButton_16.setMaximumSize(QSize(85, 70))
        self.pushButton_16.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_16, 7, 1, 1, 1)

        self.checkers30 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers30)
        self.checkers30.setObjectName(u"checkers30")
        sizePolicy.setHeightForWidth(self.checkers30.sizePolicy().hasHeightForWidth())
        self.checkers30.setSizePolicy(sizePolicy)
        self.checkers30.setMinimumSize(QSize(85, 77))
        self.checkers30.setMaximumSize(QSize(85, 70))
        self.checkers30.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers30.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers30, 7, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_11)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QSize(85, 77))
        self.pushButton_11.setMaximumSize(QSize(85, 70))
        self.pushButton_11.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_11, 6, 0, 1, 1)

        self.checkers10 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers10)
        self.checkers10.setObjectName(u"checkers10")
        sizePolicy.setHeightForWidth(self.checkers10.sizePolicy().hasHeightForWidth())
        self.checkers10.setSizePolicy(sizePolicy)
        self.checkers10.setMinimumSize(QSize(85, 77))
        self.checkers10.setMaximumSize(QSize(85, 70))
        self.checkers10.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers10.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers10, 2, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(85, 77))
        self.pushButton_3.setMaximumSize(QSize(85, 70))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_23 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_23)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setMinimumSize(QSize(85, 77))
        self.pushButton_23.setMaximumSize(QSize(85, 70))
        self.pushButton_23.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_23, 3, 3, 1, 1)

        self.pushButton_42 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_42)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        self.pushButton_42.setMinimumSize(QSize(85, 77))
        self.pushButton_42.setMaximumSize(QSize(85, 70))
        self.pushButton_42.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_42, 5, 7, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(85, 77))
        self.pushButton_5.setMaximumSize(QSize(85, 70))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)

        self.checkers2 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers2)
        self.checkers2.setObjectName(u"checkers2")
        sizePolicy.setHeightForWidth(self.checkers2.sizePolicy().hasHeightForWidth())
        self.checkers2.setSizePolicy(sizePolicy)
        self.checkers2.setMinimumSize(QSize(85, 77))
        self.checkers2.setMaximumSize(QSize(85, 70))
        self.checkers2.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers2.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers2, 0, 3, 1, 1)

        self.pushButton_51 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_51)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy)
        self.pushButton_51.setMinimumSize(QSize(85, 77))
        self.pushButton_51.setMaximumSize(QSize(85, 70))
        self.pushButton_51.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_51, 2, 2, 1, 1)

        self.checkers21 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers21)
        self.checkers21.setObjectName(u"checkers21")
        sizePolicy.setHeightForWidth(self.checkers21.sizePolicy().hasHeightForWidth())
        self.checkers21.setSizePolicy(sizePolicy)
        self.checkers21.setMinimumSize(QSize(85, 77))
        self.checkers21.setMaximumSize(QSize(85, 70))
        self.checkers21.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers21.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers21, 5, 0, 1, 1)

        self.pushButton_34 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_34)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy)
        self.pushButton_34.setMinimumSize(QSize(85, 77))
        self.pushButton_34.setMaximumSize(QSize(85, 70))
        self.pushButton_34.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_34, 6, 6, 1, 1)

        self.pushButton_54 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_54)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_54.sizePolicy().hasHeightForWidth())
        self.pushButton_54.setSizePolicy(sizePolicy)
        self.pushButton_54.setMinimumSize(QSize(85, 77))
        self.pushButton_54.setMaximumSize(QSize(85, 70))
        self.pushButton_54.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_54, 7, 7, 1, 1)

        self.checkers8 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers8)
        self.checkers8.setObjectName(u"checkers8")
        sizePolicy.setHeightForWidth(self.checkers8.sizePolicy().hasHeightForWidth())
        self.checkers8.setSizePolicy(sizePolicy)
        self.checkers8.setMinimumSize(QSize(85, 77))
        self.checkers8.setMaximumSize(QSize(85, 70))
        self.checkers8.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers8.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers8, 1, 6, 1, 1)

        self.checkers22 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers22)
        self.checkers22.setObjectName(u"checkers22")
        sizePolicy.setHeightForWidth(self.checkers22.sizePolicy().hasHeightForWidth())
        self.checkers22.setSizePolicy(sizePolicy)
        self.checkers22.setMinimumSize(QSize(85, 77))
        self.checkers22.setMaximumSize(QSize(85, 70))
        self.checkers22.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/white-removebg-preview.png);")
        self.checkers22.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers22, 5, 2, 1, 1)

        self.pushButton_24 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_24)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setMinimumSize(QSize(85, 77))
        self.pushButton_24.setMaximumSize(QSize(85, 70))
        self.pushButton_24.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_24, 3, 1, 1, 1)

        self.checkers16 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers16)
        self.checkers16.setObjectName(u"checkers16")
        sizePolicy.setHeightForWidth(self.checkers16.sizePolicy().hasHeightForWidth())
        self.checkers16.setSizePolicy(sizePolicy)
        self.checkers16.setMinimumSize(QSize(85, 77))
        self.checkers16.setMaximumSize(QSize(85, 70))
        self.checkers16.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.checkers16.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers16, 3, 6, 1, 1)

        self.checkers12 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers12)
        self.checkers12.setObjectName(u"checkers12")
        sizePolicy.setHeightForWidth(self.checkers12.sizePolicy().hasHeightForWidth())
        self.checkers12.setSizePolicy(sizePolicy)
        self.checkers12.setMinimumSize(QSize(85, 77))
        self.checkers12.setMaximumSize(QSize(85, 70))
        self.checkers12.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers12.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers12, 2, 7, 1, 1)

        self.pushButton_37 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_37)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy)
        self.pushButton_37.setMinimumSize(QSize(85, 77))
        self.pushButton_37.setMaximumSize(QSize(85, 70))
        self.pushButton_37.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_37, 6, 4, 1, 1)

        self.checkers11 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers11)
        self.checkers11.setObjectName(u"checkers11")
        sizePolicy.setHeightForWidth(self.checkers11.sizePolicy().hasHeightForWidth())
        self.checkers11.setSizePolicy(sizePolicy)
        self.checkers11.setMinimumSize(QSize(85, 77))
        self.checkers11.setMaximumSize(QSize(85, 70))
        self.checkers11.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers11.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers11, 2, 5, 1, 1)

        self.pushButton_19 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_19)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setMinimumSize(QSize(85, 77))
        self.pushButton_19.setMaximumSize(QSize(85, 70))
        self.pushButton_19.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_19, 3, 5, 1, 1)

        self.pushButton_57 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_57)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy)
        self.pushButton_57.setMinimumSize(QSize(85, 77))
        self.pushButton_57.setMaximumSize(QSize(85, 70))
        self.pushButton_57.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_57, 1, 5, 1, 1)

        self.pushButton_53 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_53)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_53.sizePolicy().hasHeightForWidth())
        self.pushButton_53.setSizePolicy(sizePolicy)
        self.pushButton_53.setMinimumSize(QSize(85, 77))
        self.pushButton_53.setMaximumSize(QSize(85, 70))
        self.pushButton_53.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_53, 7, 5, 1, 1)

        self.pushButton_15 = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton_15)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QSize(85, 77))
        self.pushButton_15.setMaximumSize(QSize(85, 70))
        self.pushButton_15.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton_15, 4, 2, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(85, 77))
        self.pushButton.setMaximumSize(QSize(85, 70))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 251, 201);")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.checkers3 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers3)
        self.checkers3.setObjectName(u"checkers3")
        sizePolicy.setHeightForWidth(self.checkers3.sizePolicy().hasHeightForWidth())
        self.checkers3.setSizePolicy(sizePolicy)
        self.checkers3.setMinimumSize(QSize(85, 77))
        self.checkers3.setMaximumSize(QSize(85, 70))
        self.checkers3.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers3.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers3, 0, 5, 1, 1)

        self.checkers4 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers4)
        self.checkers4.setObjectName(u"checkers4")
        sizePolicy.setHeightForWidth(self.checkers4.sizePolicy().hasHeightForWidth())
        self.checkers4.setSizePolicy(sizePolicy)
        self.checkers4.setMinimumSize(QSize(85, 77))
        self.checkers4.setMaximumSize(QSize(85, 70))
        self.checkers4.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers4.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers4, 0, 7, 1, 1)

        self.checkers15 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers15)
        self.checkers15.setObjectName(u"checkers15")
        sizePolicy.setHeightForWidth(self.checkers15.sizePolicy().hasHeightForWidth())
        self.checkers15.setSizePolicy(sizePolicy)
        self.checkers15.setMinimumSize(QSize(85, 77))
        self.checkers15.setMaximumSize(QSize(85, 70))
        self.checkers15.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.checkers15.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers15, 3, 4, 1, 1)

        self.checkers5 = QPushButton(self.gridLayoutWidget)
        self.playing_spots.addButton(self.checkers5)
        self.checkers5.setObjectName(u"checkers5")
        sizePolicy.setHeightForWidth(self.checkers5.sizePolicy().hasHeightForWidth())
        self.checkers5.setSizePolicy(sizePolicy)
        self.checkers5.setMinimumSize(QSize(85, 77))
        self.checkers5.setMaximumSize(QSize(85, 70))
        self.checkers5.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"image: url(:/pieces/images for pieces/black-removebg-preview(1).png);")
        self.checkers5.setAutoDefault(False)

        self.gridLayout.addWidget(self.checkers5, 1, 0, 1, 1)

        self.textHistory = QTextBrowser(playCheckers)
        self.textHistory.setObjectName(u"textHistory")
        self.textHistory.setGeometry(QRect(690, 0, 211, 471))
        self.gridLayoutWidget_2 = QWidget(playCheckers)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(690, 470, 211, 151))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.surrenderButton = QPushButton(self.gridLayoutWidget_2)
        self.surrenderButton.setObjectName(u"surrenderButton")

        self.gridLayout_2.addWidget(self.surrenderButton, 1, 1, 1, 1)

        self.playerTurnLabel = QLabel(self.gridLayoutWidget_2)
        self.playerTurnLabel.setObjectName(u"playerTurnLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.playerTurnLabel.sizePolicy().hasHeightForWidth())
        self.playerTurnLabel.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"MS Reference Sans Serif"])
        font1.setPointSize(22)
        self.playerTurnLabel.setFont(font1)
        self.playerTurnLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.playerTurnLabel, 0, 0, 1, 2)

        self.drawButton = QPushButton(self.gridLayoutWidget_2)
        self.drawButton.setObjectName(u"drawButton")

        self.gridLayout_2.addWidget(self.drawButton, 1, 0, 1, 1)

        self.line = QFrame(playCheckers)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(690, 470, 211, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(playCheckers)

        QMetaObject.connectSlotsByName(playCheckers)
    # setupUi

    def retranslateUi(self, playCheckers):
        playCheckers.setWindowTitle(QCoreApplication.translate("playCheckers", u"Checkers", None))
        self.checkers28.setText("")
        self.pushButton_59.setText("")
        self.checkers24.setText("")
        self.checkers6.setText("")
        self.pushButton_26.setText("")
        self.pushButton_43.setText("")
        self.checkers29.setText("")
        self.pushButton_7.setText("")
        self.pushButton_14.setText("")
        self.pushButton_48.setText("")
        self.pushButton_29.setText("")
        self.checkers25.setText("")
        self.checkers32.setText("")
        self.checkers20.setText("")
        self.checkers9.setText("")
        self.checkers23.setText("")
        self.pushButton_47.setText("")
        self.pushButton_63.setText("")
        self.pushButton_33.setText("")
        self.pushButton_61.setText("")
        self.checkers31.setText("")
        self.checkers26.setText("")
        self.checkers14.setText("")
        self.checkers17.setText("")
        self.checkers13.setText("")
        self.checkers19.setText("")
        self.pushButton_49.setText("")
        self.checkers18.setText("")
        self.checkers7.setText("")
        self.pushButton_22.setText("")
        self.checkers1.setText("")
        self.pushButton_28.setText("")
        self.pushButton_41.setText("")
        self.pushButton_20.setText("")
        self.checkers27.setText("")
        self.pushButton_16.setText("")
        self.checkers30.setText("")
        self.pushButton_11.setText("")
        self.checkers10.setText("")
        self.pushButton_3.setText("")
        self.pushButton_23.setText("")
        self.pushButton_42.setText("")
        self.pushButton_5.setText("")
        self.checkers2.setText("")
        self.pushButton_51.setText("")
        self.checkers21.setText("")
        self.pushButton_34.setText("")
        self.pushButton_54.setText("")
        self.checkers8.setText("")
        self.checkers22.setText("")
        self.pushButton_24.setText("")
        self.checkers16.setText("")
        self.checkers12.setText("")
        self.pushButton_37.setText("")
        self.checkers11.setText("")
        self.pushButton_19.setText("")
        self.pushButton_57.setText("")
        self.pushButton_53.setText("")
        self.pushButton_15.setText("")
        self.pushButton.setText("")
        self.checkers3.setText("")
        self.checkers4.setText("")
        self.checkers15.setText("")
        self.checkers5.setText("")
        self.textHistory.setHtml(QCoreApplication.translate("playCheckers", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">testing 1 2 3<br /><br />testing 4 5 6</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.surrenderButton.setText(QCoreApplication.translate("playCheckers", u"Surrender", None))
        self.playerTurnLabel.setText(QCoreApplication.translate("playCheckers", u"x player turn", None))
        self.drawButton.setText(QCoreApplication.translate("playCheckers", u"Draw?", None))
    # retranslateUi

