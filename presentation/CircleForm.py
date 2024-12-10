from datetime import datetime
import uuid
from PyQt5.QtWidgets import (QDialogButtonBox, QLineEdit, QPushButton, QVBoxLayout, QDateEdit, QFormLayout, QDialog, QComboBox)
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QFont

from data.connection.Connection import Connection
from data.service.CircleService import CircleService
from presentation.listeners.IDialogCallback import IDialogCallback
from presentation.style.style import Style
from utils.data import Strings

class CircleForm(QDialog):
    dialog_closed = pyqtSignal(bool)

    def __init__(self, id_uuid_suino: str):
        super().__init__()
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.connection = Connection()
        self.circle_service = CircleService(self.connection)
        # Layout
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.circle_input = QComboBox()
        self.circle_input.setStyleSheet(Style().FONTE_COMBO_BOX)
        self.circle_input.addItems(Strings.circle_list)

        button_box = QDialogButtonBox()
        button_box.setStyleSheet(Style().BUTTON_DIALOG)
        save_button = QPushButton("Salvar")
        cancel_button = QPushButton("Cancelar")
 
        save_button.clicked.connect(lambda: self.accept(id_uuid_suino))
        cancel_button.clicked.connect(self.reject)

        # Adicionar os botões ao QDialogButtonBox
        button_box.addButton(cancel_button, QDialogButtonBox.RejectRole)
        button_box.addButton(save_button, QDialogButtonBox.AcceptRole)

        self.date_start_input = QDateEdit()
        self.date_start_input.setStyleSheet(Style().FONTE_EDIT_DATE_18PX)
        self.date_start_input.setCalendarPopup(True)
        self.date_start_input.setDisplayFormat("yyyy-MM-dd")
        self.date_start_input.setDate(QDate.currentDate())


        self.observation_input = QLineEdit()
        self.observation_input.setStyleSheet(Style().FONTE_EDIT_18PX)

        form_layout.addRow("Ciclo:", self.circle_input)
        form_layout.addRow("Data de inicio:", self.date_start_input)
        form_layout.addRow("Observação:", self.observation_input)

        label_circle_input = form_layout.labelForField(self.circle_input)
        label_circle_input.setStyleSheet(Style().FONTE_LABEL)

        label_date_start_input = form_layout.labelForField(self.date_start_input)
        label_date_start_input.setStyleSheet(Style().FONTE_LABEL)

        label_observation_input = form_layout.labelForField(self.observation_input)
        label_observation_input.setStyleSheet(Style().FONTE_LABEL)

        layout.addLayout(form_layout)
        layout.addWidget(button_box)
        self.setLayout(layout)
        self.setFixedSize(820, 720)

    @pyqtSlot()
    def accept(self, id_uuid_suino: str):
        circle_name = self.circle_input.currentText()
        start_date = self.date_start_input.date().toString("yyyy-MM-dd")
        end_date = "0000-00-00"
        observation = self.observation_input.text()
        is_ended = False
        registration_date=datetime.now().strftime("%Y-%m-%d")

        result = self.circle_service.create_circle(
            id_uuid=uuid.uuid4(),
            id_uuid_suino=id_uuid_suino,
            circle_name=circle_name,
            start_date=start_date,
            end_date=end_date,
            observation=observation,
            is_ended=is_ended,
            registration_date=registration_date
        )

        if result is not None:
           self.dialog_closed.emit(True)
        else:
            print("Erro ao salva o ciclo")

        super().accept()

    @pyqtSlot()
    def reject(self):
        self.dialog_closed.emit(False)
        super().reject()
    
        
