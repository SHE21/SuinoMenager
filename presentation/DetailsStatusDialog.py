from datetime import datetime
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QPushButton,
    QDialog,
    QHBoxLayout,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from model.Circle import Circle
from model.DailyStatus import DailyStatus
from model.Suino import Suino
from presentation import UtilsWidget


class DetailsStatusDialog(QDialog):
    def __init__(self, daily_status: DailyStatus):
        self.daily_status = daily_status
        super().__init__()
        self.setWindowIcon(QIcon("src/images/icon_window.png"))
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowTitle(f"Detalhes do status")
        self.setLayout(self.init_layout())
        self.setFixedSize(834, 758)

    def init_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()
        self.init_grid(layout=layout)
        return layout

    def init_grid(self, layout: QVBoxLayout):
        grid = QGridLayout()
        grid.addWidget(UtilsWidget.label_title("Peso (kg):"), 0, 0)
        grid.addWidget(UtilsWidget.label_value(str(self.daily_status.weight)), 0, 1)

        grid.addWidget(UtilsWidget.label_title("Data de registro:"), 1, 0)
        grid.addWidget(
            UtilsWidget.label_value(str(self.daily_status.registration_date)), 1, 1
        )
        layout.addLayout(grid)
