import sys
from PyQt5.QtWidgets import (
    QWidget,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QDialog,
    QSizePolicy,
)

from data.connection.Connection import Connection
from data.service.SuinoService import SuinoService
from model.Suino import Suino
from presentation.DetailsWidget import DetailsWidget
from presentation.DialogWidget import DialogWidget
from presentation.style.style import Style


class SuinoListWidget(QWidget):
    def __init__(self, screen_geometry):
        super().__init__()
        self.connection = Connection()
        self.suino_service = SuinoService(self.connection)
        self.list_widget = QListWidget(self)
        self.list_widget.setStyleSheet(Style().LIST)
        self.list_widget.setFixedSize(
            screen_geometry.width() - 180, screen_geometry.height() - 40
        )
        self.details_widget = None
        self.list_widget.show()

    def addItem(self, suino: Suino):
        item = QListWidgetItem()
        item_widget = QWidget()
        line_text = QLabel(f"TAG: {suino.id_tag}")
        line_text.setStyleSheet(Style().FONTE_ITEN_LIST)
        line_push_button = QPushButton("Detalhes")
        line_push_button.clicked.connect(lambda: self.show_details(suino.id_uuid))
        line_push_button.setFixedSize(100, 30)
        item_layout = QHBoxLayout()
        item_layout.addWidget(line_text, 3)
        item_layout.addWidget(line_push_button)
        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())
        self.list_widget.addItem(item)
        self.list_widget.setItemWidget(item, item_widget)

    def load_list(self):
        self.list_widget.clear()
        suino_list = self.suino_service.get_suinos()
        for suino in suino_list:
            self.addItem(suino)

    def show_dialog(self):
        dialog = DialogWidget("Deseja excluir esse registro?")

        # Exibir o diálogo e aguardar a resposta
        if dialog.exec_() == QDialog.Accepted:
            input_text = dialog.get_input_text()
            print(f"Texto inserido: {input_text}")
        else:
            print("Diálogo cancelado")

    def show_details(self, title: str):
        if not self.details_widget or not self.details_widget.isVisible():
            self.details_widget = DetailsWidget(title)
            self.details_widget.exec_()
