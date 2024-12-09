from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


from data.connection.Connection import Connection
from data.service.SuinoService import SuinoService

STYLE_GRID ="""QGridLayout {
            background-color:red;
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

class DetailsWidget(QWidget):
    def __init__(self, uuid: int):
        super().__init__()
        self.connection = Connection()
        self.suino_service = SuinoService(self.connection)
        suino = self.suino_service.get_suino_by_uuid(uuid)
        self.setWindowTitle("Detalhes de Suínos")
        layout = QVBoxLayout()

        grid = QGridLayout()

        # Adicionando widgets ao layout
        grid.addWidget(self.label_title("ID TAG:"), 0, 0)
        grid.addWidget(self.label_value(suino.id_tag), 0, 1)

        grid.addWidget(self.label_title("Data de Nascimento:"), 1, 0)
        grid.addWidget(self.label_value(str(suino.date_birth)), 1, 1)

        grid.addWidget(self.label_title("Genero:"), 2, 0)
        grid.addWidget(self.label_value(suino.gender), 2, 1)

        grid.addWidget(self.label_title("Raça:"), 3, 0)
        grid.addWidget(self.label_value(suino.race), 3, 1)

        grid.addWidget(self.label_title("Origem:"), 4, 0)
        grid.addWidget(self.label_value(suino.origini), 4, 1)

        layout.addLayout(grid)
        self.setLayout(layout)
        self.setFixedSize(720, 720)

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
