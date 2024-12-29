import sys
from PyQt5.QtWidgets import (
    QWidget,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QLabel,
    QHBoxLayout,
)

from model.Suino import Suino
from presentation.style.style import Style


class SuinoListWidget(QListWidget):
    def __init__(self, open_dialog_details):
        self.suino_list: list[Suino] = []
        self.open_dialog_details = open_dialog_details
        super().__init__()
        self.setFixedSize(920, 580)
        self.setStyleSheet(Style().LIST)

    def addCustomItem(self, suino: Suino):
        item = QListWidgetItem()
        item_widget = QWidget()
        line_text = QLabel(f"TAG: {suino.id_tag}")
        line_text.setStyleSheet(Style().FONTE_ITEN_LIST)
        line_push_button = QPushButton("Detalhes")
        line_push_button.clicked.connect(lambda: self.open_dialog_details(suino))
        line_push_button.setFixedSize(100, 30)
        item_layout = QHBoxLayout()
        item_layout.addWidget(line_text, 3)
        item_layout.addWidget(line_push_button)
        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, item_widget)

    def setList(self, suino_list: list[Suino]):
        self.clear()
        self.suino_list = suino_list
        self.init_list()

    def init_list(self):
        for suino in self.suino_list:
            self.addCustomItem(suino)

    """def show_details(self, title: str):
        if not self.details_widget or not self.details_widget.isVisible():
            self.details_widget = DetailsSuinoDialog(title)
            self.details_widget.exec_()"""
