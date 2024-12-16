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
from model.Health import Health
from model.Nutrition import Nutrition
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
        self.layout = QVBoxLayout()
        self.init_grid()
        return self.layout

    def init_grid(self):
        if isinstance(self.daily_status, Health):
            self.init_status_health()

        elif isinstance(self.daily_status, Nutrition):
            self.init_status_nutrition()

    def init_status_health(self):
        grid = QGridLayout()
        grid.addWidget(UtilsWidget.label_title("Peso (kg):"), 0, 0)
        grid.addWidget(UtilsWidget.label_value(str(self.daily_status.weight)), 0, 1)

        grid.addWidget(UtilsWidget.label_title("Data de registro:"), 1, 0)
        grid.addWidget(
            UtilsWidget.label_value(str(self.daily_status.registration_date)), 1, 1
        )
        grid.addWidget(UtilsWidget.label_title("Nome da medicação:"), 2, 0)
        grid.addWidget(
            UtilsWidget.label_value(str(self.daily_status.medicine_name)), 2, 1
        )
        grid.addWidget(UtilsWidget.label_title("Tipo de medicação:"), 3, 0)
        grid.addWidget(
            UtilsWidget.label_value(str(self.daily_status.medicine_type)), 3, 1
        )
        grid.addWidget(UtilsWidget.label_title("Tipo adiministração:"), 4, 0)
        grid.addWidget(
            UtilsWidget.label_value(str(self.daily_status.adminitration_type)), 4, 1
        )
        grid.addWidget(UtilsWidget.label_title("Dose:"), 5, 0)
        grid.addWidget(UtilsWidget.label_value(str(self.daily_status.dosage)), 5, 1)
        grid.addWidget(UtilsWidget.label_title("É tratamento:"), 6, 0)
        is_treatment_result = self.daily_status.is_treatment
        if is_treatment_result:
            is_treatment_value = "SIM"
            grid.addWidget(UtilsWidget.label_title("Período de tratamento:"), 7, 0)
            grid.addWidget(
                UtilsWidget.label_value(
                    f"{str(self.daily_status.date_start)} a {str(self.daily_status.date_end)}"
                ),
                7,
                1,
            )
        else:
            is_treatment_value = "NÃO"
        grid.addWidget(UtilsWidget.label_value(is_treatment_value), 6, 1)

        grid.addWidget(UtilsWidget.label_title("Diagnóstico:"), 8, 0)
        grid.addWidget(UtilsWidget.label_value(str(self.daily_status.diagnosis)), 8, 1)

        grid.addWidget(UtilsWidget.label_title("Observações:"), 9, 0)
        grid.addWidget(UtilsWidget.label_value(str(self.daily_status.obervation)), 9, 1)
        self.layout.addLayout(grid)

    def init_status_nutrition(self):
        grid = QGridLayout()
        grid.addWidget(UtilsWidget.label_title("Peso (kg):"), 0, 0)
        grid.addWidget(UtilsWidget.label_value(str(self.daily_status.weight)), 0, 1)

        grid.addWidget(UtilsWidget.label_title("Data de registro:"), 1, 0)
        grid.addWidget(
            UtilsWidget.label_value(str(self.daily_status.registration_date)), 1, 1
        )
        grid.addWidget(UtilsWidget.label_title("Consumo diário:"), 2, 0)
        grid.addWidget(
            UtilsWidget.label_value(
                f"{str(self.daily_status.daily_feed_intake)} kg/dia"
            ),
            2,
            1,
        )
        grid.addWidget(UtilsWidget.label_title("Ganho diário de peso:"), 3, 0)
        grid.addWidget(
            UtilsWidget.label_value(
                f"{str(self.daily_status.weight_gain_daily)} kg/dia"
            ),
            3,
            1,
        )
        grid.addWidget(UtilsWidget.label_title("Consumo de água:"), 4, 0)
        grid.addWidget(
            UtilsWidget.label_value(f"{str(self.daily_status.water_intake)} ml/dia"),
            4,
            1,
        )
        grid.addWidget(UtilsWidget.label_title("Suplementação:"), 5, 0)
        grid.addWidget(
            UtilsWidget.label_value(f"{str(self.daily_status.supplementation)}"),
            5,
            1,
        )
        self.layout.addLayout(grid)
