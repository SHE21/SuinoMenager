from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy

from assets.strings.Strings import DIALOG_TITLE_REGISTER_BAIA
from assets.style.style import FONTE_BUTTON_18PX
from data.connection.Connection import Connection
from data.service.BaiaService import BaiaService
from model.Instalation import Instalation
from presentation.BaiaListWidget import BaiaListWidget
from presentation.RightHeader import RightHeader
from presentation.ToolbarWidget import ToolbarWidget


class RightContent(QWidget):
    def __init__(self, on_click_item_baia_list, open_dialog_baia_form):
        self.on_click_item_baia_list = on_click_item_baia_list
        self.open_dialog_baia_form = open_dialog_baia_form
        self.instalation = None
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setContentsMargins(0, 7, 7, 0)
        super().__init__()
        self.init_content_header()
        self.init_toolbar_buttons()
        self.init_baia_list()
        self.setLayout(self.vertical_layout)

    def updated_content(self, instalation: Instalation):
        self.instalation = instalation
        self.instalation_content_header.update(self.instalation)
        self.toolbar_widget.update(self.instalation)
        self.load_baia_list()

    def addWidget(self, widget: QWidget):
        self.vertical_layout.addWidget(widget)

    def init_content_header(self):
        self.instalation_content_header = RightHeader()
        self.vertical_layout.addWidget(self.instalation_content_header)

    def init_toolbar_buttons(self):
        self.toolbar_widget = ToolbarWidget("", self.open_dialog_baia_form)
        self.vertical_layout.addWidget(self.toolbar_widget)

    def init_baia_list(self):
        self.baia_list = BaiaListWidget(self.on_click_item_baia_list)
        self.vertical_layout.addWidget(self.baia_list)

    def load_baia_list(self):
        connection = Connection()
        service = BaiaService(connection)
        baia_list = service.get_baias_by_instalation(self.instalation)
        self.baia_list.setList(baia_list)
