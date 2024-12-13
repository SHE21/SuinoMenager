from datetime import datetime
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QPushButton,
    QDialog,
    QHBoxLayout,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from model.Circle import Circle
from model.Suino import Suino
from presentation import UtilsWidget
from presentation.DailyStatusListWidget import DailyStatusListWidget
from presentation.style.style import Style
from utils.calculus import calculate_days


class DetailsDailyStatusDialog(QDialog):
    def __init__(self, suino: Suino, circle: Circle):
        super().__init__()
        self.suino = suino
        self.circle = circle
        self.setWindowIcon(QIcon("src/images/icon_window.png"))
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowTitle(f"Ciclo - {circle.circle_name}")
        self.setLayout(self.init_layout())
        self.setFixedSize(834, 758)

    def init_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()
        self.init_grid(layout=layout)
        self.init_toobar(layout=layout)
        self.init_list(layout=layout)
        return layout

    def init_list(self, layout: QVBoxLayout):
        self.daily_status_list_widget = DailyStatusListWidget(self.circle.id_uuid)
        layout.addWidget(self.daily_status_list_widget)

    def init_grid(self, layout: QVBoxLayout):
        grid = QGridLayout()
        grid.addWidget(UtilsWidget.label_title("Suino:"), 0, 0)
        grid.addWidget(UtilsWidget.label_value(self.suino.id_tag), 0, 1)

        grid.addWidget(UtilsWidget.label_title("Ciclo:"), 1, 0)
        grid.addWidget(UtilsWidget.label_value(self.circle.circle_name), 1, 1)

        grid.addWidget(UtilsWidget.label_title("Data de inicio:"), 2, 0)
        date_now = datetime.now()
        data_birth_string = f"{str(self.circle.start_date)} ({calculate_days(str(self.circle.start_date), date_now.strftime("%Y-%m-%d"))} dias)"
        grid.addWidget(UtilsWidget.label_value(data_birth_string), 2, 1)
        layout.addLayout(grid)

    def init_toobar(self, layout: QVBoxLayout):
        tool_bar = QHBoxLayout()
        tool_bar.setContentsMargins(0, 8, 0, 0)
        title_label = QLabel("Monitoramento diário")
        title_label.setAlignment(Qt.AlignVCenter)
        title_label.setStyleSheet(Style().STYLE_TOOLBAR_TITLE_1)
        title_label.setFixedHeight(40)
        btn_add_status_health = QPushButton("Registrar Status Médico")
        btn_add_status_health.setStyleSheet(Style().STYLE_TOOLBAR_BUTTON)
        btn_add_status_health.setFixedHeight(40)
        btn_add_status_nutrition = QPushButton("Registrar Status Alimentar")
        btn_add_status_nutrition.setStyleSheet(Style().STYLE_TOOLBAR_BUTTON)
        btn_add_status_nutrition.setFixedHeight(40)
        tool_bar.addWidget(title_label)
        tool_bar.addWidget(btn_add_status_health)
        tool_bar.addWidget(btn_add_status_nutrition)
        layout.addLayout(tool_bar)
