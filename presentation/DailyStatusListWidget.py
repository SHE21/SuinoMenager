from PyQt5.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
)

from data.connection.Connection import Connection
from data.service.DailyStatusService import DailyStatusService
from model.DailyStatus import DailyStatus
from model.Health import Health
from model.Nutrition import Nutrition
from presentation.style.style import Style


class DailyStatusListWidget(QWidget):
    def __init__(self, id_uuid: str):
        self.id_uuid = id_uuid
        super().__init__()
        self.connection = Connection()
        self.daily_status_service = DailyStatusService(self.connection)
        self.daily_status_list = QListWidget(self)
        self.daily_status_list.setStyleSheet(Style().LIST)
        self.daily_status_list.setFixedSize(808, 565)
        self.daily_status_list.show()
        self.load_list()

    def addStatusItem(self, daily_status: DailyStatus):
        item = QListWidgetItem()
        item_widget = QWidget()
        item_widget.setLayout(self.init_item_daily_status(daily_status))
        item.setSizeHint(item_widget.sizeHint())
        self.daily_status_list.addItem(item)
        self.daily_status_list.setItemWidget(item, item_widget)

    def load_list(self):
        self.daily_status_list.clear()
        daily_status_result = self.daily_status_service.get_daily_status(self.id_uuid)
        for daily_status in daily_status_result:
            self.addStatusItem(daily_status)

    def init_item_daily_status(self, daily_status: DailyStatus) -> QHBoxLayout:
        line_push_button = QPushButton("ver mais")
        # line_push_button.clicked.connect(
        # lambda: self.show_details_daily_status(circle.id_uuid)
        # )
        line_push_button.setFixedSize(100, 30)

        item_layout = QHBoxLayout()
        item_layout.setContentsMargins(0, 1, 0, 1)
        item_layout.setSpacing(0)
        self.get_type_status(daily_status, item_layout)
        item_layout.addWidget(line_push_button)

        return item_layout

    def get_type_status(self, daily_status: DailyStatus, layout: QHBoxLayout):

        if isinstance(daily_status, Health):
            title_text = QLabel(
                f"Saúde-> Diagnóstico: {daily_status.diagnosis} | Adminstração: {daily_status.adminitration_type} | Dose:{daily_status.dosage} | {daily_status.registration_date}"
            )
            title_text.setStyleSheet(Style().STYLE_LABEL_HEALTH)
            layout.addWidget(title_text)

        elif isinstance(daily_status, Nutrition):
            title_text = QLabel(
                f"Nutrição-> Peso:{daily_status.weight}kg | Consumo de Ração:{daily_status.daily_feed_intake}kg/dia | Ganho de Peso:{daily_status.weight_gain_daily}kg/dia | {daily_status.registration_date}"
            )
            title_text.setStyleSheet(Style().STYLE_LABEL_NUTRITION)
            layout.addWidget(title_text)
