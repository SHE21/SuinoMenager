from PyQt5.QtWidgets import (
    QListWidget,
)

from model.Instalation import Instalation


class InstalationListWidget(QListWidget):
    def __init__(self, instalation_list: list[Instalation]):
        self.instalation_list = instalation_list
        super().__init__()
