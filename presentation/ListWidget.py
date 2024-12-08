import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDialog, QLineEdit, QDialogButtonBox

from model.Suino import Suino
from presentation.DetailsWidget import DetailsWidget
from presentation.DialogWidget import DialogWidget
from presentation.style.style import Style

class ListWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Criar a QListWidget
        self.list_widget = QListWidget(self)
        self.list_widget.setStyleSheet(Style().LIST)
        self.list_widget.setFixedSize(1890, 820)

        self.details_widget = None

        # Adicionar itens à lista com widgets personalizados
        for i in range(5):  # Vamos adicionar 5 itens para exemplificar
            self.addItem(f"{i}")

        self.list_widget.show()

    def addItem(self, suino: Suino):
        item = QListWidgetItem()
        item_widget = QWidget()
        line_text = QLabel(f"Suino {id}")
        line_push_button = QPushButton("suino.id_tag")
        line_push_button.clicked.connect(lambda:self.show_details(id))
        line_push_button.setFixedSize(100, 50)
        item_layout = QHBoxLayout()
        item_layout.addWidget(line_text)
        item_layout.addWidget(line_push_button)
        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())
        self.list_widget.addItem(item)
        self.list_widget.setItemWidget(item, item_widget)

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
            self.details_widget.show()

