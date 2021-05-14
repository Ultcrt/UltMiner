from PySide2 import QtWidgets
from ultminer.ultminer_ui.main_window import MainWindow


def main():
    app = QtWidgets.QApplication([])
    m = MainWindow()
    m.show()
    app.exec_()
