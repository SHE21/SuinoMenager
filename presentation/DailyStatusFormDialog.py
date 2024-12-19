from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QMessageBox,
)
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon

from data.connection.Connection import Connection
from data.service.NutritionService import NutritionService
from data.service.HealthService import HealthService
from model.Circle import Circle
from model.Suino import Suino
from presentation.HealthStatusFormWidget import HealthStatusFormWidget
from presentation.NutritionStatusFormWidget import NutritionStatusFormWidget
from utils.UtilsWidget import validate_fields
from presentation.style.style import Style


class DailyStatusFormDialog(QDialog):
    dialog_closed = pyqtSignal(bool)

    def __init__(self, suino: Suino, circle: Circle, type_status_form: str):
        self.suino = suino
        self.circle = circle
        self.connection = Connection()
        super().__init__()
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon("src/images/icon_window.png"))
        self.setWindowTitle("Registrar Status Diário do Suíno")
        self.setFixedSize(834, 758)

        layout = QVBoxLayout()
        if type_status_form == "health_form":
            layout.addLayout(self.init_form_health())
        elif type_status_form == "nutrition_form":
            layout.addLayout(self.init_form_nutrition())

        self.init_dialog_buttons(layout)
        self.setLayout(layout)

    def init_dialog_buttons(self, layout: QVBoxLayout):
        button_box = QDialogButtonBox()
        button_box.setStyleSheet(Style().BUTTON_DIALOG)
        save_button = QPushButton("Registrar")
        cancel_button = QPushButton("Cancelar")

        save_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        button_box.addButton(cancel_button, QDialogButtonBox.RejectRole)
        button_box.addButton(save_button, QDialogButtonBox.AcceptRole)
        layout.addWidget(button_box)

    def init_form_health(self) -> QFormLayout:
        self.form_layout = HealthStatusFormWidget(self.suino, self.circle)
        return self.form_layout

    def init_form_nutrition(self):
        self.form_layout = NutritionStatusFormWidget(
            self.suino, self.circle, NutritionService(connection=self.connection)
        )
        return self.form_layout

    def create_health(self):
        get_valid_fields = validate_fields(self.form_layout)
        if len(get_valid_fields) > 0:
            QMessageBox.warning(
                self,
                "Campos estão vazios",
                "Os seguintes campos estão vazios:\n" + "".join(get_valid_fields),
            )

        else:
            health = self.form_layout.get_values_fields()
            service = HealthService(self.connection)
            result = service.create_status_health(
                id_uuid=health.id_uuid,
                id_uuid_suino=health.id_uuid_suino,
                id_uuid_circle=health.id_uuid_circle,
                weight=health.weight,
                registration_date=health.registration_date,
                id_uui_health=health.id_uui_health,
                medicine_name=health.medicine_name,
                medicine_type=health.medicine_type,
                adminitration_type=health.adminitration_type,
                dosage=health.dosage,
                is_treatment=health.is_treatment,
                diagnosis=health.diagnosis,
                date_start=health.date_start,
                date_end=health.date_end,
                obervation=health.obervation,
            )

            if result:
                print("dados salvo!!")
                self.dialog_closed.emit(True)
            else:
                print("Error!")
                self.dialog_closed.emit(True)

            super().accept()

    def create_nutrition(self):
        get_valid_fields = validate_fields(self.form_layout)
        if len(get_valid_fields) > 0:
            QMessageBox.warning(
                self,
                "Campos estão vazios",
                "Os seguintes campos estão vazios:\n" + "".join(get_valid_fields),
            )
        else:
            nutrition = self.form_layout.get_values_fields()
            result = self.form_layout.create_nutrition(nutrition)
            if result:
                print("dados salvo!!")
                self.dialog_closed.emit(True)
            else:
                print("Error!")
                self.dialog_closed.emit(True)

            super().accept()

    @pyqtSlot()
    def accept(self):
        if isinstance(self.form_layout, HealthStatusFormWidget):
            self.create_health()

        elif isinstance(self.form_layout, NutritionStatusFormWidget):
            self.create_nutrition()

    @pyqtSlot()
    def reject(self):
        self.dialog_closed.emit(False)
        super().reject()
