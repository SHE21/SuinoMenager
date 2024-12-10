import uuid
from PyQt5.QtWidgets import (QDialogButtonBox, QLineEdit, QPushButton, QVBoxLayout, QDateEdit, QFormLayout, QDialog, QComboBox)
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt

from data.connection.Connection import Connection
from data.service.CircleService import CircleService
from presentation.listeners.IDialogCallback import IDialogCallback
from utils.data import Strings

class CircleForm(QDialog):
    def __init__(self, id_uuid_suino: str):
        super().__init__()
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.connection = Connection()
        self.circle_service = CircleService(self.connection)
        # Layout
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.circle_input = QComboBox()
        self.circle_input.addItems(Strings.circle_list)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        self.date_start_input = QDateEdit()
        self.date_start_input.setCalendarPopup(True)
        self.date_start_input.setDisplayFormat("yyyy-MM-dd")
        #self.date_start_input.setStyleSheet(Style().FONTE_EDIT_DATE_18PX)
        self.date_start_input.setDate(QDate.currentDate())

        self.observation_input = QLineEdit()

        form_layout.addRow("Ciclo:", self.circle_input)
        form_layout.addRow("Data de inicio:", self.date_start_input)
        form_layout.addRow("Observação:", self.observation_input)

        # Botão de envio
        self.submit_button = QPushButton("Enviar")
        self.submit_button.clicked.connect(lambda: self.save_circle(id_uuid_suino))

        form_layout.addRow(self.submit_button)

        layout.addLayout(form_layout)
        layout.addWidget(button_box)
        self.setLayout(layout)
        self.setFixedSize(820, 720)

    def save_circle(self, id_uuid_suino: str):
        circle_name = self.circle_input.currentText()
        start_date = self.date_start_input.date().toString("yyyy-MM-dd")
        end_date = "0000-00-00"
        observation = self.observation_input.text()
        is_ended = False

        result = self.circle_service.create_circle(
            id_uuid=uuid.uuid4(),
            id_uuid_suino=id_uuid_suino,
            circle_name=circle_name,
            start_date=start_date,
            end_date=end_date,
            observation=observation,
            is_ended=is_ended
        )

        if result is not None:
            print("Ciclo salvo")
        else:
            print("Erro ao salva o ciclo")
        
