import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox)

from model.Suino import Suino

class SuinoForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Suínos")
        self.initUI()
    
    def initUI(self):
        # Labels e campos de texto

        self.id_tag_label = QLabel("ID Tag:")
        self.id_tag_input = QLineEdit()

        self.date_birth_label = QLabel("Data de Nascimento:")
        self.date_birth_input = QLineEdit()

        self.gender_label = QLabel("Gênero:")
        self.gender_input = QComboBox()
        self.gender_input.addItems(["Macho", "Fêmea"])

        # Botão de salvar
        self.save_button = QPushButton("Salvar")
        self.save_button.clicked.connect(self.save_data)

        # Layouts
        layout = QVBoxLayout()

        layout.addWidget(self.id_tag_label)
        layout.addWidget(self.id_tag_input)

        layout.addWidget(self.date_birth_label)
        layout.addWidget(self.date_birth_input)

        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_input)

        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_data(self):
        # Captura dos dados
        try:
            suino = Suino(
                id=0,
                id_tag=self.id_tag_input.text(),
                date_birth=self.date_birth_input.text(),
                gender=self.gender_input.currentText()
            )

            QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")

            print(f"ID Tag: {suino.id_tag}")
            print(f"Data de Nascimento: {suino.date_birth}")
            print(f"Gênero: {suino.gender}")

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos.")
