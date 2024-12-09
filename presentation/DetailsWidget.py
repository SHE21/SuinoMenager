from datetime import datetime
import uuid
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton, QDialog
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


from data.connection.Connection import Connection
from data.service.CircleService import CircleService
from data.service.SuinoService import SuinoService
from presentation.CircleForm import CircleForm
from presentation.CircleListWidget import CircleListWdiget
from utils.calculus import calculate_days

STYLE_GRID ="""QGridLayout {
            background-color:red;
        }"""

STYLE_BUTTON ="""QPushButton {
            font-size: 18px;
        }"""

STYLE_LABEL_TITLE ="""QLabel {
            height: 10px;
            font-size: 18px;
            background-color:#dedede;
            padding:3px;
        }"""

STYLE_LABEL_VALUE ="""QLabel {
            height: 10px;
            font-size: 18px;
            background-color:#dedede;
            font-weight: bold;
            padding:3px;
        }"""

class DetailsWidget(QDialog):
    def __init__(self, uuid: int):
        super().__init__()
        self.connection = Connection()
        self.suino_service = SuinoService(self.connection)
        suino = self.suino_service.get_suino_by_uuid(uuid)
        self.circle_form = None
        self.setWindowTitle("Detalhes de Suínos")
        layout = QVBoxLayout()

        btn_add_circle = QPushButton("Adicionar ciclo")
        btn_add_circle.clicked.connect(lambda:self.open_circle_form(suino.id_uuid))
        btn_add_circle.setStyleSheet(STYLE_BUTTON)
        btn_add_circle.setFixedSize(140, 50)

        grid = QGridLayout()

        # Adicionando widgets ao layout
        grid.addWidget(self.label_title("ID TAG:"), 0, 0)
        grid.addWidget(self.label_value(suino.id_tag), 0, 1)

        grid.addWidget(self.label_title("Data de Nascimento:"), 1, 0)
        date_now = datetime.now()
        data_birth_string = f"{str(suino.date_birth)} ({calculate_days(str(suino.date_birth), date_now.strftime("%Y-%m-%d"))} dias)"
        grid.addWidget(self.label_value(data_birth_string), 1, 1)

        grid.addWidget(self.label_title("Genero:"), 2, 0)
        grid.addWidget(self.label_value(suino.gender), 2, 1)

        grid.addWidget(self.label_title("Raça:"), 3, 0)
        grid.addWidget(self.label_value(suino.race), 3, 1)

        grid.addWidget(self.label_title("Origem:"), 4, 0)
        grid.addWidget(self.label_value(suino.origini), 4, 1)

        layout.addLayout(grid)
        layout.addWidget(btn_add_circle)

        circle_list_widget = CircleListWdiget(id_uuid=suino.id_uuid)
        if len(circle_list_widget.get_circle_list()) == 5:
            btn_add_circle.setEnabled(False)
        else:
            btn_add_circle.setEnabled(True)

        box_layout = QVBoxLayout()
        box_layout.addWidget(circle_list_widget)
        layout.addLayout(box_layout)
        self.setLayout(layout)
        self.setFixedSize(820, 720)

    def open_circle_form(self, id_uuid_suino: str):
        if not self.circle_form or not self.circle_form.isVisible():
            self.circle_form = CircleForm(id_uuid_suino)
            self.circle_form.exec_()

    def label_title(self, text: str) -> QLabel:
        label = QLabel(text=text)
        label.setStyleSheet(STYLE_LABEL_TITLE)
        label.setFixedSize(180, 30)
        return label
    
    def label_value(self, text: str) -> QLabel:
        label = QLabel(text=text)
        label.setStyleSheet(STYLE_LABEL_VALUE)
        label.setFixedHeight(30)
        return label
