from PyQt5.QtWidgets import (
    QLineEdit,
    QDateEdit,
    QComboBox,
    QFormLayout,
    QHBoxLayout,
)
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QDoubleValidator

from model.Circle import Circle
from model.Suino import Suino
from presentation.style.style import Style
from utils.data import Strings


class HealthStatusForm(QFormLayout):
    def __init__(self, suino: Suino, circle: Circle):
        self.suino = suino
        self.circle = circle
        super().__init__()
        self.medicine_type = QComboBox()
        self.medicine_type.setFixedWidth(200)
        self.medicine_type.setStyleSheet(Style().FONTE_COMBO_BOX)
        self.medicine_type.addItems(Strings.medicine_type_list)

        self.administration_type = QComboBox()
        self.administration_type.setFixedWidth(200)
        self.administration_type.setStyleSheet(Style().FONTE_COMBO_BOX)
        self.administration_type.addItems(Strings.administration_type_list)

        self.is_treatment = QComboBox()
        self.is_treatment.setFixedWidth(65)
        self.is_treatment.setStyleSheet(Style().FONTE_COMBO_BOX)
        self.is_treatment.addItems(["Não", "Sim"])
        self.is_treatment.currentTextChanged.connect(self.show_treatment_section)

        self.wight = QLineEdit()
        self.wight.setFixedWidth(65)
        self.wight.setValidator(QDoubleValidator(0.0, 1000.0, 3))
        self.wight.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.medicine_name = QLineEdit()
        self.medicine_name.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.dosage = QLineEdit()
        self.dosage.setFixedWidth(65)
        self.dosage.setValidator(QDoubleValidator(0.0, 1000.0, 3))
        self.dosage.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.diagnosis = QLineEdit()
        self.diagnosis.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.observations = QLineEdit()
        self.observations.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.addRow("Peso (kg):", self.wight)
        self.addRow("Nome da Medicação:", self.medicine_name)
        self.addRow("Tipo de Medicação:", self.medicine_type)
        self.addRow("Tipo de Adiminstração:", self.administration_type)
        self.addRow("Dosagem (mg):", self.dosage)
        self.addRow("Diagnóstico:", self.diagnosis)
        self.addRow("Observações:", self.observations)
        self.addRow("É tratamento:", self.is_treatment)

        self.labelForField(self.medicine_type).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.administration_type).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.is_treatment).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.wight).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.medicine_name).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.dosage).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.diagnosis).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.observations).setStyleSheet(Style().FONTE_LABEL)

    def show_treatment_section(self):
        if self.is_treatment.currentText() == "Sim":
            self.date_start_input = self.get_date_edit()
            self.date_end_input = self.get_date_edit()

            self.treatment_section = QHBoxLayout()
            self.treatment_section.addWidget(self.date_start_input)
            self.treatment_section.addWidget(self.date_end_input)
            self.addRow("Período do Tratamento:", self.treatment_section)
            self.labelForField(self.treatment_section).setStyleSheet(
                Style().FONTE_LABEL
            )
        else:
            self.removeRow(self.treatment_section)

    def get_date_edit(self) -> QDateEdit:
        date_edit_unput = QDateEdit()
        date_edit_unput.setStyleSheet(Style().FONTE_EDIT_DATE_18PX)
        date_edit_unput.setBaseSize(100, 30)
        date_edit_unput.setCalendarPopup(True)
        date_edit_unput.setDisplayFormat("yyyy-MM-dd")
        date_edit_unput.setDate(QDate.currentDate())
        return date_edit_unput
