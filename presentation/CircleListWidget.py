from PyQt5.QtWidgets import  QListWidget, QListWidgetItem, QWidget, QLabel, QPushButton, QHBoxLayout

from data.connection.Connection import Connection
from data.service.CircleService import CircleService
from model.Circle import Circle
from presentation.style.style import Style

class CircleListWdiget(QWidget):
    def __init__(self, id_uuid: str):
        super().__init__()
        self.connection = Connection()
        self.cricle_service = CircleService(self.connection)

        self.circle_list = QListWidget(self)
        self.circle_list.setStyleSheet(Style().LIST)
        self.circle_list.setFixedSize(794, 290)

        self.circle_list_result = self.cricle_service.get_circles_by_uuid_suino(id_uuid)

        for circle in self.circle_list_result:
            print(circle.circle_name)
            self.addItem(circle)

        self.circle_list.show()

    def addItem(self, circle: Circle):
        item = QListWidgetItem()
        item_widget = QWidget()
        line_text = QLabel(f"{circle.circle_name}")
        line_push_button = QPushButton("Detalhes")
        #line_push_button.clicked.connect(lambda:self.show_details(suino.id_uuid))
        line_push_button.setFixedSize(100, 30)
        item_layout = QHBoxLayout()
        item_layout.addWidget(line_text)
        item_layout.addWidget(line_push_button)
        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())
        self.circle_list.addItem(item)
        self.circle_list.setItemWidget(item, item_widget)

    def get_circle_list(self):
        return self.circle_list_result