from PyQt5.QtWidgets import QWidget, QVBoxLayout


class RightContent(QWidget):
    def __init__(self):
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setContentsMargins(0, 7, 7, 0)
        super().__init__()
        self.setLayout(self.vertical_layout)

    def addWidget(self, widget: QWidget):
        self.vertical_layout.addWidget(widget)
