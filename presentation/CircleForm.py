from datetime import datetime
import uuid
from PyQt5.QtWidgets import (
    QDialogButtonBox,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QDateEdit,
    QFormLayout,
    QDialog,
    QComboBox,
)
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon

from data.connection.Connection import Connection
from data.service.CircleService import CircleService
from model.Baia import Baia
from model.Circle import Circle
from model.Circle import get_list_circle_name
from presentation.listeners.IDialogCallback import IDialogCallback
from presentation.style.style import Style
from utils.Utils import filter_circle_list
from assets.strings import Strings


class CircleForm(QDialog):
    signal_register_circle = pyqtSignal(Circle)

    def __init__(self, baia: Baia, circle_list: list[Circle]):
        super().__init__()
        self.setWindowTitle("Registrar Ciclo")
        self.setWindowIcon(QIcon("src/images/icon_window.png"))
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.connection = Connection()
        self.circle_service = CircleService(self.connection)
        # Layout
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.circle_input = QComboBox()
        self.circle_input.addItem("-- selecione um ciclo --", 0)
        self.circle_input.setStyleSheet(Style().FONTE_COMBO_BOX)

        """control_list = get_list_circle_name(circle_list)
        original_list = Strings.circle_list_combo

        option_circle_name_list = filter_circle_list(
            original_list,
            control_list,
        )"""
        self.circle_input.addItems(circle_list)

        button_box = QDialogButtonBox()
        button_box.setStyleSheet(Style().BUTTON_DIALOG)
        save_button = QPushButton("Salvar")
        cancel_button = QPushButton("Cancelar")

        save_button.clicked.connect(lambda: self.accept(baia))
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
    def accept(self, baia: Baia):
        circle_name = self.circle_input.currentText()
        start_date = self.date_start_input.date().toString("yyyy-MM-dd")
        end_date = "0000-00-00"
        observation = self.observation_input.text()
        is_ended = False
        registration_date = datetime.now().strftime("%Y-%m-%d")
        id_uuid = uuid.uuid4()

        result = self.circle_service.create_circle(
            id_uuid=id_uuid,
            id_uuid_baia=baia.id_uuid,
            circle_name=circle_name,
            start_date=start_date,
            end_date=end_date,
            observation=observation,
            is_ended=is_ended,
            registration_date=registration_date,
        )

        if result:
            circle = Circle(
                result,
                id_uuid=id_uuid,
                id_uuid_baia=baia.id_uuid,
                circle_name=circle_name,
                start_date=start_date,
                end_date=end_date,
                observation=observation,
                daily_status=None,
                is_ended=is_ended,
                registration_date=registration_date,
            )
        else:
            circle = None

        if result is not None:
            self.signal_register_circle.emit(circle)
        else:
            print("Erro ao salva o ciclo")

        super().accept()

    @pyqtSlot()
    def reject(self):
        self.signal_register_circle.emit(
            Circle(None, None, None, None, None, None, None, None, None, None)
        )
        super().reject()
