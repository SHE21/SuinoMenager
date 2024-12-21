from PyQt5.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QApplication,
    QSizePolicy,
)

from assets.strings.Strings import (
    MAIN_PANEL_BUTTON_ADD_INSTALATION,
    MAIN_PANEL_BUTTON_ADD_SUINO,
)
from presentation.style.style import Style


class ToolbarWidget(QWidget):
    def __init__(self, title: str):
        super().__init__()
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.addWidget(QLabel(title))
        self.setLayout(self.layout_horizontal)

    def addButtons(self, buttons: list[QPushButton]):
        for button in buttons:
            self.layout_horizontal.addWidget(button)
