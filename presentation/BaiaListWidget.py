from PyQt5.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QApplication,
)

from model.Baia import Baia
from assets.style.style import LIST, STYLE_LABEL_HEALTH


class BaiaListWidget(QListWidget):
    def __init__(self, on_click_item_baia_list):
        self.on_click_item_baia_list = on_click_item_baia_list
        self.baia_list: list[Baia] = []
        super().__init__()
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setFixedSize(1220, 680)
        self.setStyleSheet(LIST)

    def setList(self, baia_list: list[Baia]):
        self.clear()
        self.baia_list = baia_list
        self.init_list()

    def init_list(self):
        for baia in self.baia_list:
            self.addCustomItem(baia)

    def addCustomItem(self, baia: Baia):
        item = QListWidgetItem()
        item_widget = QWidget()
        item_widget.setLayout(self.init_item_list(baia))
        item.setSizeHint(item_widget.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, item_widget)

    def init_item_list(self, baia: Baia) -> QHBoxLayout:
        line_push_button = QPushButton("ver mais")
        line_push_button.clicked.connect(lambda: self.on_click_item_baia_list(baia))
        line_push_button.setFixedSize(100, 30)
        title_text = QLabel(baia.label)
        title_text.setStyleSheet(STYLE_LABEL_HEALTH)

        item_layout = QHBoxLayout()
        item_layout.setContentsMargins(0, 1, 0, 1)
        item_layout.setSpacing(0)
        item_layout.addWidget(title_text)
        item_layout.addWidget(line_push_button)
        return item_layout
