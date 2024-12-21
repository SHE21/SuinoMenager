from model.Instalation import Instalation
from utils import UtilsWidget


from PyQt5.QtWidgets import QGridLayout, QWidget, QVBoxLayout


class RightHeader(QWidget):
    def __init__(self):
        self.grid_layout = QGridLayout()
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        super().__init__()
        self.setLayout(self.grid_layout)

    def update(self, instalation: Instalation):
        self.grid_layout.addWidget(UtilsWidget.label_title("Granja:"), 0, 0)
        self.grid_layout.addWidget(UtilsWidget.label_value(instalation.name), 0, 1)
