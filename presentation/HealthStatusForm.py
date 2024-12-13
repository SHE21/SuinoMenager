from datetime import datetime
import uuid
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
from model.Health import Health
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
        self.is_treatment.setFixedWidth(75)
        self.is_treatment.setStyleSheet(Style().FONTE_COMBO_BOX)
        self.is_treatment.addItems(["Não", "Sim"])
        self.is_treatment.currentTextChanged.connect(self.show_treatment_section)

        self.weight = QLineEdit()
        self.weight.setFixedWidth(75)
        self.weight.setValidator(QDoubleValidator(0.0, 1000.0, 3))
        self.weight.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.medicine_name = QLineEdit()
        self.medicine_name.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.dosage = QLineEdit()
        self.dosage.setFixedWidth(75)
        self.dosage.setValidator(QDoubleValidator(0.0, 1000.0, 3))
        self.dosage.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.diagnosis = QLineEdit()
        self.diagnosis.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.observations = QLineEdit()
        self.observations.setStyleSheet(Style().FONTE_EDIT_18PX)

        self.addRow("Peso (kg):", self.weight)
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
        self.labelForField(self.weight).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.medicine_name).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.dosage).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.diagnosis).setStyleSheet(Style().FONTE_LABEL)
        self.labelForField(self.observations).setStyleSheet(Style().FONTE_LABEL)

    def get_values_fields(self) -> Health:
        medicine_type = self.medicine_type.currentText()
        administration_type = self.administration_type.currentText()
        medicine_name = self.medicine_name.text()
        dosage = float(self.dosage.text())
        weight = float(self.weight.text())
        diagnosis = self.diagnosis.text()
        observations = self.observations.text()
        is_treatment = self.is_treatment.currentText() == "Sim"
        date_start = (
            self.date_start_input.date().toString("yyyy-MM-dd")
            if is_treatment
            else "0000-00-00"
        )
        date_end = (
            self.date_end_input.date().toString("yyyy-MM-dd")
            if is_treatment
            else "0000-00-00"
        )

        return Health(
            id=0,
            id_uuid=uuid.uuid4(),
            id_uuid_suino=self.suino.id_uuid,
            id_uuid_circle=self.circle.id_uuid,
            weight=weight,
            registration_date=datetime.now().strftime("%Y-%m-%d"),
            id_uui_health=uuid.uuid4(),
            medicine_name=medicine_name,
            medicine_type=medicine_type,
            adminitration_type=administration_type,  # corrigir ortografia
            dosage=dosage,
            is_treatment=is_treatment,
            diagnosis=diagnosis,
            date_start=date_start,
            date_end=date_end,
            obervation=observations,  # corrigir ortografia
        )

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
