from PyQt5.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QApplication,
)

from model.Instalation import Instalation
from presentation.style.style import Style
from abc import ABC, abstractmethod


class OnClickListener(ABC):
    @abstractmethod
    def on_click_listener(instalation: Instalation):
        pass


class InstalationListWidget(QListWidget):
    def __init__(self, instalation_list: list[Instalation], open_dialog_details):
        self.instalation_list = instalation_list
        self.open_dialog_details = open_dialog_details
        super().__init__()
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setFixedSize(screen_geometry.width() - 180, screen_geometry.height() - 40)
        self.setStyleSheet(Style().LIST)
        self.init_list()
        self.show()

    def init_list(self):
        for instalation in self.instalation_list:
            self.addCustomItem(instalation)

    def addCustomItem(self, instalation: Instalation):
        item = QListWidgetItem()
        item_widget = QWidget()
        item_widget.setLayout(self.init_item_list(instalation))
        item.setSizeHint(item_widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, item_widget)

    def init_item_list(self, instalation: Instalation) -> QHBoxLayout:
        line_push_button = QPushButton("ver mais")
        line_push_button.clicked.connect(lambda: self.open_dialog_details(instalation))
        line_push_button.setFixedSize(100, 30)
        title_text = QLabel(instalation.name)
        title_text.setStyleSheet(Style().STYLE_LABEL_HEALTH)

        item_layout = QHBoxLayout()
        item_layout.setContentsMargins(0, 1, 0, 1)
        item_layout.setSpacing(0)
        item_layout.addWidget(title_text)
        item_layout.addWidget(line_push_button)
        return item_layout
