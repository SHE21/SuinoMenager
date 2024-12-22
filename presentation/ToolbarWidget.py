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
    DIALOG_TITLE_REGISTER_BAIA,
    MAIN_PANEL_BUTTON_ADD_INSTALATION,
    MAIN_PANEL_BUTTON_ADD_SUINO,
)
from assets.style.style import FONTE_BUTTON_18PX
from model.Instalation import Instalation
from presentation.style.style import Style


class ToolbarWidget(QWidget):
    def __init__(self, title: str, open_dialog_baia_form):
        self.open_dialog_baia_form = open_dialog_baia_form
        self.instalation = None
        super().__init__()
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.addWidget(QLabel(title))
        self.init_buttons()
        self.setLayout(self.layout_horizontal)

    def update(self, instalation: Instalation):
        self.instalation = instalation

    def init_buttons(self):
        create_suino_button = QPushButton(DIALOG_TITLE_REGISTER_BAIA)
        create_suino_button.setSizePolicy(QSizePolicy.Expanding, 50)
        create_suino_button.setFixedWidth(190)
        create_suino_button.setStyleSheet(FONTE_BUTTON_18PX)
        create_suino_button.clicked.connect(
            lambda: self.open_dialog_baia_form(self.instalation)
        )
        self.layout_horizontal.addWidget(create_suino_button)
