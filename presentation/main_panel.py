from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QPushButton, QVBoxLayout, QMessageBox, QComboBox)

from presentation.ListWidget import ListWidget
from presentation.SuinoForm import SuinoForm
from presentation.listeners.OnClickListener import OnClickListener
from presentation.style.style import Style

class MainPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Suínos")
        self.initUI()

    def initUI(self):

        # Botão de salvar
        self.save_button = QPushButton("Adicionar Suino")
        self.save_button.setFixedSize(200, 50)
        self.save_button.setStyleSheet(Style().FONTE_BUTTON_18PX)
        self.save_button.clicked.connect(self.open_form_add_suino)

        self.add_suino = None

        # Layouts
        layout = QVBoxLayout()
        layout.addWidget(self.save_button)

        self.list = ListWidget()
        layout.addWidget(self.list)
        self.setLayout(layout)

        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(screen_geometry)



        self.setMinimumSize(400, 300)  # Tamanho mínimo
        self.setMaximumSize(1920, 1080)  # Tamanho máximo (ajuste conforme necessário)

    def open_form_add_suino(self):
        if not self.add_suino or not self.add_suino.isVisible():
            self.add_suino = SuinoForm(self.fall_back())
            self.add_suino.show()

    def fall_back(self)-> OnClickListener:
        return OnClickListener().onClick