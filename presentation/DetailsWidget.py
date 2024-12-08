from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from presentation.style.style import Style

class DetailsWidget(QWidget):
    def __init__(self, title: str):
        super().__init__()
        self.setWindowTitle("Detalhes de Suínos")
        layout = QVBoxLayout()

        self.gender_label = QLabel(title)
        self.gender_label.setStyleSheet(Style().FONTE_LABEL)
        self.gender_label.setFixedHeight(30)
        layout.addWidget(self.gender_label)
    
        self.setLayout(layout)
        self.setFixedSize(720, 720)