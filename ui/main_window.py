# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ultminer.ultminer_ui.main_window import GraphCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(965, 545)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.input_frame = QFrame(self.centralwidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.input_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pool_widget = QWidget(self.input_frame)
        self.pool_widget.setObjectName(u"pool_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.pool_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pool_label = QLabel(self.pool_widget)
        self.pool_label.setObjectName(u"pool_label")

        self.horizontalLayout_4.addWidget(self.pool_label)

        self.pool_edit = QLineEdit(self.pool_widget)
        self.pool_edit.setObjectName(u"pool_edit")

        self.horizontalLayout_4.addWidget(self.pool_edit)


        self.horizontalLayout.addWidget(self.pool_widget)

        self.wallet_widget = QWidget(self.input_frame)
        self.wallet_widget.setObjectName(u"wallet_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.wallet_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.wallet_label = QLabel(self.wallet_widget)
        self.wallet_label.setObjectName(u"wallet_label")

        self.horizontalLayout_5.addWidget(self.wallet_label)

        self.wallet_edit = QLineEdit(self.wallet_widget)
        self.wallet_edit.setObjectName(u"wallet_edit")
        self.wallet_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.wallet_edit.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.wallet_edit)


        self.horizontalLayout.addWidget(self.wallet_widget)

        self.miner_widget = QWidget(self.input_frame)
        self.miner_widget.setObjectName(u"miner_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.miner_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.miner_name_label = QLabel(self.miner_widget)
        self.miner_name_label.setObjectName(u"miner_name_label")

        self.horizontalLayout_2.addWidget(self.miner_name_label)

        self.miner_edit = QLineEdit(self.miner_widget)
        self.miner_edit.setObjectName(u"miner_edit")

        self.horizontalLayout_2.addWidget(self.miner_edit)


        self.horizontalLayout.addWidget(self.miner_widget)

        self.start_button = QPushButton(self.input_frame)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout.addWidget(self.start_button)


        self.verticalLayout_3.addWidget(self.input_frame)

        self.functional_tab_widget = QTabWidget(self.centralwidget)
        self.functional_tab_widget.setObjectName(u"functional_tab_widget")
        self.graph_tab = QWidget()
        self.graph_tab.setObjectName(u"graph_tab")
        self.verticalLayout = QVBoxLayout(self.graph_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graph_combo_widget = QWidget(self.graph_tab)
        self.graph_combo_widget.setObjectName(u"graph_combo_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.graph_combo_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.graph_combo = QComboBox(self.graph_combo_widget)
        self.graph_combo.setObjectName(u"graph_combo")
        self.graph_combo.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.graph_combo)

        self.graph_combo_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.graph_combo_spacer)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)

        self.verticalLayout.addWidget(self.graph_combo_widget)

        self.graph_canvas = GraphCanvas(self.graph_tab)
        self.graph_canvas.setObjectName(u"graph_canvas")

        self.verticalLayout.addWidget(self.graph_canvas)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 15)
        self.functional_tab_widget.addTab(self.graph_tab, "")
        self.log_tab = QWidget()
        self.log_tab.setObjectName(u"log_tab")
        self.verticalLayout_2 = QVBoxLayout(self.log_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.log_browser = QTextBrowser(self.log_tab)
        self.log_browser.setObjectName(u"log_browser")
        self.log_browser.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.verticalLayout_2.addWidget(self.log_browser)

        self.functional_tab_widget.addTab(self.log_tab, "")

        self.verticalLayout_3.addWidget(self.functional_tab_widget)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.functional_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pool_label.setText(QCoreApplication.translate("MainWindow", u"\u77ff\u6c60\u5730\u5740\uff1a", None))
        self.wallet_label.setText(QCoreApplication.translate("MainWindow", u"\u94b1\u5305\u5730\u5740\uff1a", None))
        self.miner_name_label.setText(QCoreApplication.translate("MainWindow", u"\u77ff\u5de5\u540d\uff1a", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.functional_tab_widget.setTabText(self.functional_tab_widget.indexOf(self.graph_tab), QCoreApplication.translate("MainWindow", u"\u56fe\u8868", None))
        self.log_browser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI';\"><br /></p></body></html>", None))
        self.functional_tab_widget.setTabText(self.functional_tab_widget.indexOf(self.log_tab), QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
    # retranslateUi

