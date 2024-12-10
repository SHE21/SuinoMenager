from datetime import date
import sys
import uuid
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDateEdit, QComboBox)
from PyQt5.QtCore import QDate

from data.connection.Connection import Connection
from data.service.SuinoService import SuinoService
from presentation.dialogs.Messagens import show_error_message
from presentation.listeners.OnClickListener import OnClickListener
from presentation.style.style import Style
from utils.data import Strings

class SuinoForm(QWidget):
    def __init__(self, on: OnClickListener):
        super().__init__()
        self.connection = Connection()
        self.suino_service = SuinoService(self.connection)
        self.setWindowTitle("Cadastro de Suínos")
    

        self.setFixedWidth(500)
        # Labels e campos de texto

        self.id_tag_label = QLabel("ID Tag:")
        self.id_tag_label.setStyleSheet(Style().FONTE_LABEL)
        self.id_tag_label.setFixedHeight(30)
        self.id_tag_input = QLineEdit()
        self.id_tag_input.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.date_birth_label = QLabel("Data de Nascimento:")
        self.date_birth_label.setStyleSheet(Style().FONTE_LABEL)
        self.date_birth_label.setFixedHeight(30)

        self.date_birth_input = QDateEdit()
        self.date_birth_input.setCalendarPopup(True)  # Habilita o popup de calendário
        self.date_birth_input.setDisplayFormat("yyyy-MM-dd")
        self.date_birth_input.setStyleSheet(Style().FONTE_EDIT_DATE_18PX)
        self.date_birth_input.setDate(QDate.currentDate())

        self.race_label = QLabel("Raça:")
        self.race_label.setStyleSheet(Style().FONTE_LABEL)
        self.race_label.setFixedHeight(30)
        self.race_input = QComboBox()
        self.race_input.addItems(Strings.suino_races)
        self.race_input.setStyleSheet(Style().FONTE_COMBO_BOX)
        
        self.gender_label = QLabel("Gênero:")
        self.gender_label.setStyleSheet(Style().FONTE_LABEL)
        self.gender_label.setFixedHeight(30)
        self.gender_input = QComboBox()
        self.gender_input.setFixedHeight(40)
        self.gender_input.setStyleSheet(Style().FONTE_COMBO_BOX)
        self.gender_input.addItems(["---Selecione um gênero---", "Macho", "Fêmea"])

        self.origin_label = QLabel("Origem:")
        self.origin_label.setStyleSheet(Style().FONTE_LABEL)
        self.origin_label.setFixedHeight(30)
        self.origin_input = QLineEdit()
        self.origin_input.setStyleSheet(Style().FONTE_EDIT_18PX)
        on.onClick("testtestetes")

        # Botão de salvar
        self.save_button = QPushButton("Salvar")
        self.save_button.clicked.connect(self.save_data)
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

        layout.addWidget(self.race_label)
        layout.addWidget(self.race_input)

        layout.addWidget(self.origin_label)
        layout.addWidget(self.origin_input)

        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_data(self):
        id_tag=self.id_tag_input.text()
        race=self.race_input.currentText()
        date_birth=self.date_birth_input.date().toString("yyyy-MM-dd")
        gender=self.gender_input.currentText()
        origin=self.origin_input.text()

        if not id_tag or not race or not gender or not origin:
            show_error_message("Todos os campos precisam ser preenchidos!")
            return
        else:
            result = self.suino_service.create_suino(
                id_tag=id_tag,
                id_uuid=uuid.uuid4(),
                race=race,
                date_birth=date_birth,
                gender=gender,
                origin=origin
            )

            print(f"id_tag:{id_tag}, "
            f"race:{race}, "
            f"date_birth:{date_birth}, "
            f"gender:{gender}, "
            f"origin:{origin}")

            if result is not None:
                self.close()
            else:
                show_error_message("Houve um erro ao salvar!")

        self.connection.close()


