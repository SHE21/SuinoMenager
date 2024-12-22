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
        self.grid_layout.addWidget(UtilsWidget.label_title("Endereço:"), 1, 0)
        self.grid_layout.addWidget(UtilsWidget.label_value(instalation.address), 1, 1)
        self.grid_layout.addWidget(UtilsWidget.label_title("Área:"), 2, 0)
        self.grid_layout.addWidget(UtilsWidget.label_value(str(instalation.area)), 2, 1)
        self.grid_layout.addWidget(UtilsWidget.label_title("Ainfra. Disponível:"), 3, 0)
        self.grid_layout.addWidget(UtilsWidget.label_value(instalation.infra), 3, 1)
