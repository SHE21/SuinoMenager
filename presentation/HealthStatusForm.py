from datetime import datetime
import uuid
from PyQt5.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
)

from model.Circle import Circle
from model.Health import Health
from model.Suino import Suino
from presentation.UtilsWidget import (
    combo_box_text_input,
    date_input,
    line_edit_numb_input,
    line_edit_text_input,
)
from presentation.style.style import Style
from utils.data import Strings


class HealthStatusForm(QFormLayout):
    def __init__(self, suino: Suino, circle: Circle):
        self.suino = suino
        self.circle = circle
        super().__init__()
        self.medicine_type = combo_box_text_input(Strings.medicine_type_list)
        self.administration_type = combo_box_text_input(
            Strings.administration_type_list
        )
        self.is_treatment = combo_box_text_input(["Não", "Sim"])
        self.is_treatment.currentTextChanged.connect(self.show_treatment_section)

        self.weight = line_edit_numb_input()
        self.medicine_name = line_edit_text_input()
        self.dosage = line_edit_numb_input()
        self.diagnosis = line_edit_text_input()
        self.observations = line_edit_text_input()

        self.addRow("Peso (kg):", self.weight)
        self.addRow("Nome da Medicação:", self.medicine_name)
        self.addRow("Tipo de Medicação:", self.medicine_type)
        self.addRow("Tipo de Adiminstração:", self.administration_type)
        self.addRow("Dosagem (mg):", self.dosage)
        self.addRow("Diagnóstico:", self.diagnosis)
        self.addRow("Observações:", self.observations)
        self.addRow("É tratamento:", self.is_treatment)

        self.set_style_fields()

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
            self.date_start_input = date_input()
            self.date_end_input = date_input()

            self.treatment_section = QHBoxLayout()
            self.treatment_section.addWidget(self.date_start_input)
            self.treatment_section.addWidget(self.date_end_input)
            self.addRow("Período do Tratamento:", self.treatment_section)
            self.labelForField(self.treatment_section).setStyleSheet(
                Style().FONTE_LABEL
            )
        else:
            self.removeRow(self.treatment_section)

    def set_style_fields(self):
        # Iterar sobre as linhas do QFormLayout
        for i in range(self.rowCount()):
            label_item = self.itemAt(i, QFormLayout.LabelRole)
            label_item.widget().setStyleSheet(Style().FONTE_LABEL)
