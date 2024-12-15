from PyQt5.QtWidgets import (
    QLineEdit,
    QDateEdit,
    QComboBox,
    QFormLayout,
    QHBoxLayout,
)
from PyQt5.QtGui import QDoubleValidator

from model.Circle import Circle
from model.Suino import Suino
from presentation.UtilsWidget import line_edit_numb_input, line_edit_text_input
from presentation.style.style import Style


class NutritionStatusForm(QFormLayout):
    def __init__(self, suino: Suino, circle: Circle):
        self.suino = suino
        self.circle = circle
        super().__init__()

        self.weight = line_edit_numb_input()
        self.daily_feed_intake = line_edit_numb_input()
        self.weight_gain_daily = line_edit_numb_input()
        self.water_intake = line_edit_numb_input()
        self.feed_composition = line_edit_text_input()
        self.supplementation = line_edit_text_input()

        self.addRow("Peso (kg):", self.weight)
        self.addRow("Consumo de ração (kg/dia):", self.daily_feed_intake)
        self.addRow("Ganho de peso (kg/dia):", self.weight_gain_daily)
        self.addRow("Consumo de água (ml/dia):", self.water_intake)
        self.addRow("Composição da ração:", self.feed_composition)
        self.addRow("Suplementação:", self.supplementation)

        self.set_style_fields()

    def set_style_fields(self):
        # Iterar sobre as linhas do QFormLayout
        for i in range(self.rowCount()):
            label_item = self.itemAt(i, QFormLayout.LabelRole)
            label_item.widget().setStyleSheet(Style().FONTE_LABEL)
            field_item = self.itemAt(i, QFormLayout.FieldRole)
            field_item.widget().setStyleSheet(Style().FONTE_EDIT_18PX)
