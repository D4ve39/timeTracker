# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'time_tracker_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_TimeTracker(object):
    def setupUi(self, TimeTracker):
        if not TimeTracker.objectName():
            TimeTracker.setObjectName(u"TimeTracker")
        TimeTracker.resize(918, 575)
        self.centralwidget = QWidget(TimeTracker)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bt_update_time_entries = QPushButton(self.centralwidget)
        self.bt_update_time_entries.setObjectName(u"bt_update_time_entries")
        self.bt_update_time_entries.setGeometry(QRect(10, 50, 181, 25))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 161, 17))
        TimeTracker.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TimeTracker)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 22))
        TimeTracker.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TimeTracker)
        self.statusbar.setObjectName(u"statusbar")
        TimeTracker.setStatusBar(self.statusbar)

        self.retranslateUi(TimeTracker)

        QMetaObject.connectSlotsByName(TimeTracker)
    # setupUi

    def retranslateUi(self, TimeTracker):
        TimeTracker.setWindowTitle(QCoreApplication.translate("TimeTracker", u"MainWindow", None))
        self.bt_update_time_entries.setText(QCoreApplication.translate("TimeTracker", u"UPDATE TIME ENTRIES", None))
        self.label.setText(QCoreApplication.translate("TimeTracker", u"TIME TRACKER", None))
    # retranslateUi

