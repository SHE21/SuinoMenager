from PyQt5.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QDateEdit,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
)
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon

from model.Circle import Circle
from model.Suino import Suino
from presentation.style.style import Style


class DailyStatusForm(QDialog):
    dialog_closed = pyqtSignal(bool)

    def __init__(self, suino: Suino, circle: Circle, type_status_form: str):
        self.suino = suino
        self.circle = circle
        super().__init__()
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon("src/images/icon_window.png"))
        self.setWindowTitle("Registrar Status Diário do Suíno")
        self.setFixedSize(820, 720)

        layout = QVBoxLayout()
        self.init_dialog_buttons(layout)
        if type_status_form == "health_form":
            layout.addLayout(self.init_form_health())
        elif type_status_form == "nutrition_form":
            layout.addLayout(self.init_form_nutrition())

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
        form_layout = QFormLayout()
        return form_layout

    def init_form_nutrition(self):
        form_layout = QFormLayout()
        return form_layout
