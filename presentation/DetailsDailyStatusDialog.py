from datetime import datetime
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QPushButton,
    QDialog,
)
from PyQt5.QtCore import Qt

from model.Circle import Circle
from presentation.DailyStatusListWidget import DailyStatusListWidget
from presentation.style.style import Style
from utils.calculus import calculate_days


class DetailsDailyStatusDialog(QDialog):
    def __init__(self, circle: Circle):
        super().__init__()
        self.circle = circle
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowTitle(f"Ciclo - {circle.circle_name}")
        self.setLayout(self.init_layout())
        self.setFixedSize(820, 558)

    def init_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()
        self.init_grid(layout=layout)
        self.ini_list(layout=layout)
        return layout

    def ini_list(self, layout: QVBoxLayout):
        self.daily_status_list_widget = DailyStatusListWidget(self.circle.id_uuid)
        layout.addWidget(self.daily_status_list_widget)

    def init_grid(self, layout: QVBoxLayout):
        grid = QGridLayout()
        grid.addWidget(self.label_title("Ciclo:"), 0, 0)
        grid.addWidget(self.label_value(self.circle.circle_name), 0, 1)

        grid.addWidget(self.label_title("Data de inicio:"), 1, 0)
        date_now = datetime.now()
        data_birth_string = f"{str(self.circle.start_date)} ({calculate_days(str(self.circle.start_date), date_now.strftime("%Y-%m-%d"))} dias)"
        grid.addWidget(self.label_value(data_birth_string), 1, 1)
        layout.addLayout(grid)

    def label_title(self, text: str) -> QLabel:
        label = QLabel(text=text)
        label.setStyleSheet(Style().STYLE_LABEL_TITLE)
        label.setFixedSize(180, 30)
        return label

    def label_value(self, text: str) -> QLabel:
        label = QLabel(text=text)
        label.setStyleSheet(Style().STYLE_LABEL_VALUE)
        label.setFixedHeight(30)
        return label
