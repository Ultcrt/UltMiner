# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from collections import deque
from time import sleep, time_ns, strftime, localtime

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import signal
from platform import system

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

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


from scipy.interpolate import make_interp_spline
import json
import os
from subprocess import Popen, PIPE, call, STARTUPINFO, STARTF_USESHOWWINDOW, STDOUT
from ultminer.ultminer_ctrl.nb_kernel import NBKernel
from threading import Thread
import matplotlib.ticker as mticker


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        icon_path = "assets" + os.sep + "UltMiner.ico"

        self.setWindowTitle("UltMiner")
        self.setWindowIcon(QIcon(icon_path))

        self.kernel = NBKernel()

        self.log_thread = None

        # Tray initialize
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(QIcon(icon_path))
        self.tray_menu = QMenu(self)
        self.tray_menu.addAction(
            QAction(
                "主界面",
                self,
                triggered=self.showNormal
            )
        )
        self.tray_menu.addSeparator()
        self.tray_menu.addAction(
            QAction(
                "退出",
                self,
                triggered=self.close
            )
        )
        self.tray.setContextMenu(self.tray_menu)
        self.tray.activated.connect(self.tray_activated_slot)
        self.tray.show()

        self.cfg_path = "cfg" + os.sep + "config.json"

        if not os.path.exists("cfg"):
            os.mkdir("cfg")

        if os.path.exists(self.cfg_path):
            with open(self.cfg_path, "r", encoding='utf-8') as config_file:
                config = json.load(config_file)
                if "pool_url" in config.keys():
                    self.pool_edit.setText(config["pool_url"])
                if "wallet_address" in config.keys():
                    self.wallet_edit.setText(config["wallet_address"])
                if "miner_name" in config.keys():
                    self.miner_edit.setText(config["miner_name"])

        self.start_button.clicked.connect(self.start_slot)
        self.graph_combo.currentIndexChanged.connect(self.graph_combo_change_slot)

    def start_slot(self):
        pool_url = self.pool_edit.text()
        wallet_address = self.wallet_edit.text()
        miner_name = self.miner_edit.text()

        if pool_url == "" or wallet_address == "" or miner_name == "":
            QMessageBox.warning(self, "警告", "输入参数不能为空！")
            return

        config = {
            "pool_url": pool_url,
            "wallet_address": wallet_address,
            "miner_name": miner_name
        }

        if not self.kernel.install_check():
            self.kernel.install_kernel()

        with open(self.cfg_path, "w", encoding='utf-8') as config_file:
            json.dump(config, config_file, indent=4)

        self.graph_canvas.init_with_data_properties(self.kernel.get_drawable_properties())
        self.graph_combo.addItems(self.kernel.get_drawable_properties().keys())
        self.graph_combo.setEnabled(True)
        # Make graph show at start
        self.graph_combo_change_slot()

        cmd = self.kernel.get_command(pool_url, wallet_address, miner_name)

        # nbminer outputs are always stderr
        self.log_thread = MiningCtrlThread(cmd, self.kernel)
        self.log_thread.log_update_signal.connect(self.log_update_slot)
        self.log_thread.graph_update_signal.connect(self.graph_update_slot)

        self.log_thread.start()

        self.start_button.setEnabled(False)

    def graph_combo_change_slot(self):
        self.graph_canvas.draw_data(self.graph_combo.currentIndex(), self.graph_combo.currentText())

    def graph_update_slot(self, new_data):
        self.graph_canvas.append(new_data)
        self.graph_canvas.draw_data(self.graph_combo.currentIndex(), self.graph_combo.currentText())

    def log_update_slot(self, new_line):
        if "ERROR" in new_line:
            style_line = '<span style=\" color: red;\">%s</span>' % new_line
        else:
            style_line = '<span style=\" color: white;\">%s</span>' % new_line
        self.log_browser.append(style_line)
        self.log_browser.moveCursor(QTextCursor.End)

    def tray_activated_slot(self, event):
        if event == QSystemTrayIcon.DoubleClick:
            self.showNormal()

    def closeEvent(self, event: QCloseEvent):
        self.tray.hide()
        if self.log_thread is not None:
            self.log_thread.stop()
            # Wait for mining process to be killed
            self.log_thread.wait()
        event.accept()

    def changeEvent(self, event):
        if self.isMinimized():
            self.hide()
        event.accept()

    def hideEvent(self, event):
        self.tray.show()
        event.accept()

    def showEvent(self, event):
        self.tray.hide()
        event.accept()


class MiningCtrlThread(QThread):
    log_update_signal = Signal(str)
    graph_update_signal = Signal(dict)

    def __init__(self, cmd, kernel):
        super().__init__()

        self.os_type = system()

        if self.os_type == "Windows":
            start_info = STARTUPINFO()
            start_info.dwFlags |= STARTF_USESHOWWINDOW
            self.mining_process = Popen(
                cmd, universal_newlines=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE, startupinfo=start_info
            )
        else:
            self.mining_process = Popen(
                cmd, universal_newlines=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE
            )
        self.kernel = kernel

        self.keep_running = True

    def stop(self):
        self.keep_running = False
        # Different approach to kill all mining process based on OS
        if self.os_type == "Linux":
            os.killpg(self.mining_process.pid, signal.SIGKILL)
        elif self.os_type == "Windows":
            call(['taskkill', '/F', '/T', '/PID', str(self.mining_process.pid)], stdout=PIPE, stderr=STDOUT, stdin=PIPE)

    def run(self):
        while self.keep_running:
            # Log update
            new_line = self.mining_process.stdout.readline()
            self.log_update_signal.emit(new_line)
            # Graph update
            new_data = self.kernel.get_new_drawable_data(new_line)
            if new_data is not None:
                self.graph_update_signal.emit(new_data)


class GraphCanvas(FigureCanvasQTAgg):
    def __init__(self, parent):
        self.max_data_len = 30
        self.color_list = [
            'red',
            'orange',
            'yellow',
            'green',
            'cyan',
            'blue',
            'purple',
            'black'
        ]
        # Initialize matplotlib figure
        self.init_size = (parent.width(), parent.height())
        self.fig = Figure(self.init_size)
        self.fig.set_facecolor("white")
        self.ax = self.fig.add_subplot(111)
        self.axis_init()

        # Initialize matplotlib figure canvas
        super().__init__(self.fig)
        self.setParent(parent)
        self.setGeometry(0, 0, parent.width(), parent.height())
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.data_properties = None

        self.legacy_data = {}

        self.legacy_xticklabels = {}

    def init_with_data_properties(self, data_properties):
        self.data_properties = data_properties
        for key, _ in data_properties.items():
            self.legacy_data[key] = deque([0.0], maxlen=self.max_data_len)
            self.legacy_xticklabels[key] = deque([strftime("%H:%M:%S", localtime())], maxlen=self.max_data_len)

    def append(self, new_data):
        for key, val in new_data.items():
            if key in self.legacy_data:
                self.legacy_data[key].append(val)
                self.legacy_xticklabels[key].append(strftime("%H:%M:%S", localtime()))
            else:
                self.legacy_data[key] = deque([0.0], maxlen=self.max_data_len)
                self.legacy_xticklabels[key] = deque(
                    [strftime("%Y.%m.%d %H:%M:%S", localtime())],
                    maxlen=self.max_data_len
                )

    def draw_data(self, combo_id, key):
        self.ax.cla()

        self.axis_init()

        # Fill up legacy_xticklabels
        filled_xticklabels = self.legacy_xticklabels[key].copy()
        if len(self.legacy_xticklabels[key]) < self.max_data_len:
            filled_xticklabels.extend(["" for _ in range(self.max_data_len - len(self.legacy_xticklabels[key]))])
        self.ax.set_xticklabels(filled_xticklabels, rotation=300)

        if self.data_properties[key].get("range") is not None:
            self.ax.set_ylim(self.data_properties[key]["range"])

        if self.data_properties[key].get("unit") is not None:
            unit = self.data_properties[key]["unit"]
        else:
            unit = ""

        self.ax.get_yaxis().set_major_formatter(
            mticker.FormatStrFormatter('%.1f {unit}'.format(unit=unit))
        )

        # make_interp_spline can only draw more than 4 points.
        # Add (-3, 0), (-2, 0), (-1, 0) into graph to make sure there are always at least 4 points in graph
        data_selected = self.legacy_data[key].copy()
        data_extended = [0.0, 0.0, 0.0]
        data_extended.extend(data_selected)

        x = np.array(range(-3, len(data_selected)))
        y = np.array(data_extended)

        # for cur_x, cur_y in zip(x, y):
        #     if cur_x >= 0 and cur_y >= 0:
        #         self.ax.text(cur_x, cur_y, cur_y)

        self.ax.scatter(x, y, color=self.color_list[int(combo_id % len(self.color_list))])
        self.ax.plot(x, y, color=self.color_list[int(combo_id % len(self.color_list))])

        # B-Spline is not very good in this case
        # smoothed_x = np.linspace(x.min(), x.max(), 1000)
        # smoothed_y = make_interp_spline(x, y)(smoothed_x)
        # self.ax.plot(smoothed_x, smoothed_y, color=self.color_list[int(combo_id % len(self.color_list))])

        self.draw()

    def axis_init(self):
        self.ax.tick_params(axis="x", bottom=True, top=False, labelbottom=True, labeltop=False)
        self.ax.set_xlim((0, self.max_data_len-1))
        self.ax.set_xticks([idx for idx in range(self.max_data_len)])
        self.ax.set_xticklabels([])

        self.ax.tick_params(axis="y", left=True, right=False, labelleft=True, labelright=False)
        self.ax.set_yticklabels([])
