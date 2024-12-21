from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QPushButton,
    QDialog,
    QHBoxLayout,
    QWidget,
)

from model.Instalation import Instalation
from utils import UtilsWidget


class InstalationContentHeader(QWidget):
    def __init__(self):
        self.grid_layout = QGridLayout()
        super().__init__()
        self.setLayout(self.grid_layout)

    def update(self, instalation: Instalation):
        self.grid_layout.addWidget(UtilsWidget.label_title("Granja:"), 0, 0)
        self.grid_layout.addWidget(UtilsWidget.label_value(instalation.name), 0, 1)
