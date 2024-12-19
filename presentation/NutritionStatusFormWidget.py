from datetime import datetime
import uuid
from PyQt5.QtWidgets import QFormLayout, QComboBox, QLineEdit, QDateEdit

from data.ServiceInterface import ServiceInterface
from data.service.NutritionService import NutritionService
from model.Circle import Circle
from model.Nutrition import Nutrition
from model.Suino import Suino
from utils.UtilsWidget import line_edit_numb_input, line_edit_text_input
from presentation.style.style import Style


class NutritionStatusFormWidget(QFormLayout):
    def __init__(self, suino: Suino, circle: Circle, service: ServiceInterface):
        self.suino = suino
        self.circle = circle
        self.service = service
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

    def get_values_fields(self) -> Nutrition:
        weight = float(self.weight.text())
        daily_feed_intake = float(self.daily_feed_intake.text())
        weight_gain_daily = float(self.weight_gain_daily.text())
        water_intake = float(self.water_intake.text())
        feed_composition = self.feed_composition.text()
        supplementation = self.supplementation.text()

        return Nutrition(
            id=0,
            id_uuid=uuid.uuid4(),
            id_uuid_suino=self.suino.id_uuid,
            id_uuid_circle=self.circle.id_uuid,
            weight=weight,
            registration_date=datetime.now().strftime("%Y-%m-%d"),
            id_uuid_nutrition=uuid.uuid4(),
            daily_feed_intake=daily_feed_intake,
            feed_composition=feed_composition,
            weight_gain_daily=weight_gain_daily,
            water_intake=water_intake,
            supplementation=supplementation,
        )

    def create_nutrition(self, nutrition: Nutrition):
        return self.service.create(nutrition)

    def set_style_fields(self):
        for i in range(self.rowCount()):
            label_item = self.itemAt(i, QFormLayout.LabelRole)
            label_item.widget().setStyleSheet(Style().FONTE_LABEL)
