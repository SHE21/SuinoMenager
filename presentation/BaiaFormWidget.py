from datetime import datetime
import uuid
from PyQt5.QtWidgets import (
    QFormLayout,
)
from assets.strings import Strings
from assets.style.style import FONTE_LABEL
from model.Baia import Baia
from utils.Utils import get_datetime
from utils.UtilsWidget import (
    combo_box_text_input,
    line_edit_numb_input,
    line_edit_text_input,
)

from model.Instalation import Instalation


class BaiaFormWidget(QFormLayout):
    def __init__(self, instalation: Instalation):
        self.instalation = instalation
        super().__init__()

        self.label_field = line_edit_text_input()
        self.dimen_with_field = line_edit_numb_input()
        self.dimen_height_field = line_edit_numb_input()
        self.type_occupation_field = combo_box_text_input(Strings.baia_type_list)
        self.status_field = combo_box_text_input(Strings.baia_status_list)

        self.addRow("Identificação:", self.label_field)
        self.addRow("Largura:", self.dimen_with_field)
        self.addRow("Comprimento:", self.dimen_height_field)
        self.addRow("Tipo:", self.type_occupation_field)
        self.addRow("Status:", self.status_field)

        self.set_style_fields()

    def get_values_fields(self) -> Baia:
        label = self.label_field.text()
        dimen_with = float(self.dimen_with_field.text())
        dimen_height = float(self.dimen_height_field.text())
        type_occupation = self.type_occupation_field.currentText()
        status = self.status_field.currentText() == "Ativada"

        return Baia(
            id=0,
            id_uuid=uuid.uuid4(),
            id_uuid_instalation=self.instalation.id_uuid,
            label=label,
            dimen_with=dimen_with,
            dimen_height=dimen_height,
            type_occupation=type_occupation,
            status=status,
            registration_date=get_datetime(),
        )

    def set_style_fields(self):
        # Iterar sobre as linhas do QFormLayout
        for i in range(self.rowCount()):
            label_item = self.itemAt(i, QFormLayout.LabelRole)
            label_item.widget().setStyleSheet(FONTE_LABEL)
