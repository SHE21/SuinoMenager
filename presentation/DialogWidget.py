import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDialog, QLineEdit, QDialogButtonBox

class DialogWidget(QDialog):
    def __init__(self, title: str):
        super().__init__()

        self.setWindowTitle(title)

        # Layout do diálogo
        layout = QVBoxLayout()

        # Campo de entrada (QLineEdit)
        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText("Digite algo aqui")
        layout.addWidget(self.input_text)

        # Botões OK e Cancelar
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(self.button_box)

        # Conectar os botões aos métodos
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        # Definir o layout do diálogo
        self.setLayout(layout)

    def get_input_text(self):
        return self.input_text.text()

