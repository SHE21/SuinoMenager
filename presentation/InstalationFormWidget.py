import uuid
from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QMessageBox,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot

from model.Instalation import Instalation
from utils.UtilsWidget import line_edit_numb_input, line_edit_text_input
from presentation.style.style import Style
from utils.Utils import get_datetime


class InstalationFormWidget(QFormLayout):

    def __init__(self):
        super().__init__()
        self.init_fields()

    def init_fields(self):
        self.name_input = line_edit_text_input()
        self.address_input = line_edit_text_input()
        self.geo_location_input = line_edit_text_input()
        self.area_input = line_edit_numb_input()
        self.infra_input = line_edit_text_input()

        self.addRow("Nome:", self.name_input)
        self.addRow("Endereço:", self.address_input)
        self.addRow("Área m2:", self.area_input)
        self.addRow("Localização Geográfica:", self.geo_location_input)
        self.addRow("Infraestrtura Disponível:", self.infra_input)

        self.set_style_fields()

    def get_values_fields(self) -> Instalation:
        name = self.name_input.text()
        address = self.address_input.text()
        geo_location = [
            float(x.strip()) for x in self.geo_location_input.text().split(",")
        ]
        area = float(self.area_input.text())
        infra = self.infra_input.text()
        registration_date = get_datetime()

        return Instalation(
            id=0,
            id_uuid=uuid.uuid4(),
            geo_location=geo_location,
            address=address,
            name=name,
            area=area,
            infra=infra,
            registration_date=registration_date,
        )

    def set_style_fields(self):
        # Iterar sobre as linhas do QFormLayout
        for i in range(self.rowCount()):
            label_item = self.itemAt(i, QFormLayout.LabelRole)
            label_item.widget().setStyleSheet(Style().FONTE_LABEL)
