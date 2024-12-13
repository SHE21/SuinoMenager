from datetime import date, datetime
import sys
import uuid
from PyQt5.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QDateEdit,
    QComboBox,
    QDialog,
    QDialogButtonBox,
)
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon

from data.connection.Connection import Connection
from data.service.SuinoService import SuinoService
from presentation.dialogs.Messagens import show_error_message
from presentation.style.style import Style
from utils.data import Strings


class SuinoForm(QDialog):
    dialog_closed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon("src/images/icon_window.png"))
        self.connection = Connection()
        self.suino_service = SuinoService(self.connection)
        self.setWindowTitle("Registrar Suíno")
        self.setFixedWidth(500)
        # Labels e campos de texto

        button_box = QDialogButtonBox()
        button_box.setStyleSheet(Style().BUTTON_DIALOG)
        save_button = QPushButton("Salvar")
        cancel_button = QPushButton("Cancelar")

        save_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        # Adicionar os botões ao QDialogButtonBox
        button_box.addButton(cancel_button, QDialogButtonBox.RejectRole)
        button_box.addButton(save_button, QDialogButtonBox.AcceptRole)

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

        layout.addWidget(button_box)
        self.setLayout(layout)

    @pyqtSlot()
    def accept(self):
        id_tag = self.id_tag_input.text()
        race = self.race_input.currentText()
        date_birth = self.date_birth_input.date().toString("yyyy-MM-dd")
        gender = self.gender_input.currentText()
        origin = self.origin_input.text()
        registration_date = datetime.now().strftime("%Y-%m-%d")

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
                origin=origin,
                registration_date=registration_date,
            )

            print(
                f"id_tag:{id_tag}, "
                f"race:{race}, "
                f"date_birth:{date_birth}, "
                f"gender:{gender}, "
                f"origin:{origin}"
            )

            if result is not None:
                self.dialog_closed.emit(True)
            else:
                print("erro ao alvar no banco de dados")

            super().accept()

        self.connection.close()

    @pyqtSlot()
    def reject(self):
        self.dialog_closed.emit(False)
        super().reject()
