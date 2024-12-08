import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox)

from model.Suino import Suino
from presentation.style.style import Style

class SuinoForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Suínos")
    

        self.setFixedWidth(500)
        # Labels e campos de texto

        self.id_tag_label = QLabel("ID Tag:")
        self.id_tag_label.setStyleSheet(Style().FONTE_LABEL)
        self.id_tag_label.setFixedHeight(30)
        self.id_tag_input = QLineEdit()
        self.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.date_birth_label = QLabel("Data de Nascimento:")
        self.date_birth_label.setStyleSheet(Style().FONTE_LABEL)
        self.date_birth_label.setFixedHeight(30)
        self.date_birth_input = QLineEdit()
        self.date_birth_input.setPlaceholderText("dd/mm/yyyy")
        self.date_birth_input.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.gender_label = QLabel("Gênero:")
        self.gender_label.setStyleSheet(Style().FONTE_LABEL)
        self.gender_label.setFixedHeight(30)
        self.gender_input = QComboBox()
        self.gender_input.setFixedHeight(40)
        self.gender_input.setStyleSheet(Style().FONTE_COMBO_BOX)
        self.gender_input.addItems(["Macho", "Fêmea"])

        # Botão de salvar
        self.save_button = QPushButton("Salvar")
        self.save_button.size = 14
        self.save_button.setStyleSheet(Style().FONTE_BUTTON_18PX)

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

