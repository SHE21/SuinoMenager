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
from presentation.style.style import Style


class DailyStatusListWidget(QWidget):
    def __init__(self, id_uuid: str):
        self.id_uuid = id_uuid
        super().__init__()
        self.connection = Connection()
        self.daily_status_service = DailyStatusService(self.connection)

        self.daily_status_list = QListWidget(self)
        self.daily_status_list.setStyleSheet(Style().LIST)
        self.daily_status_list.setFixedSize(794, 290)
        self.daily_status_list.show()
        self.load_list()

    def addStatusItem(self, daily_status: DailyStatus):
        item = QListWidgetItem()
        item_widget = QWidget()
        line_text = QLabel(f"{daily_status.registration_date}")
        line_text.setStyleSheet(Style().FONTE_ITEN_LIST_1)
        line_push_button = QPushButton("Detalhes")
        # line_push_button.clicked.connect(
        # lambda: self.show_details_daily_status(circle.id_uuid)
        # )
        line_push_button.setFixedSize(100, 30)
        item_layout = QHBoxLayout()
        item_layout.addWidget(line_text)
        item_layout.addWidget(line_push_button)
        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())
        self.daily_status_list.addItem(item)
        self.daily_status_list.setItemWidget(item, item_widget)

    def load_list(self):
        self.daily_status_list.clear()
        daily_status_result = self.daily_status_service.get_daily_status(self.id_uuid)
        for daily_status in daily_status_result:
            self.addStatusItem(daily_status)
