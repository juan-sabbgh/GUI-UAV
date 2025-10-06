import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QApplication
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget,
    QLabel, QSizePolicy
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from diseño_ventana import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.btn_2_tablero.setChecked(True)

    def _on_checked_buttons(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) + self.ui.full_menu_widget.findChildren(QPushButton)
        for btn in btn_list:
            if index in [3, 4]:
                btn.setAutoExcluaive(False)
                btn.setAutoChecjed(False)
            else:
                btn.setAutoExcluaive(False)

    # Funciones para cambiar de páginas
    def on_btn_1_tablero_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_btn_2_tablero_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_btn_1_diagnosticar_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_btn_2_diagnosticar_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_btn_1_estadisticos_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_btn_2_estadisticos_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Cargando hoja de estilos e íconos
    with open("./style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    # ejecutando ventana
    window = MainWindow()
    window.show()

    # Cierre
    sys.exit(app.exec())




