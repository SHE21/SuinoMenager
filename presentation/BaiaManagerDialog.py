from datetime import datetime
from PyQt5.QtWidgets import (
    QDialogButtonBox,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QDateEdit,
    QFormLayout,
    QMainWindow,
    QHBoxLayout,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
)
from PyQt5.QtCore import QDate, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon

from assets.strings.Strings import (
    DIALOG_TITLE_MANAGER_BAIA,
    MAIN_PANEL_BUTTON_ADD_SUINO,
    ICON_APP,
    MAIN_PANEL_BUTTON_ADD_CIRCLE,
)
from assets.style.style import FONTE_BUTTON_18PX
from data.connection.Connection import Connection
from data.service.CircleService import CircleService
from data.service.SuinoService import SuinoService
from model.Baia import Baia
from model.Circle import Circle
from model.Suino import Suino
from presentation.SuinoFormDialog import SuinoFormDialog
from presentation.SuinoListWidget import SuinoListWidget
from utils import UtilsWidget
from utils.Utils import calculate_days


class BaiaManagerDialog(QMainWindow):
    def __init__(self, baia: Baia, open_click_register_circle):
        self.baia = baia
        self.open_click_register_circle = open_click_register_circle
        super().__init__()
        self.setWindowTitle(f"{DIALOG_TITLE_MANAGER_BAIA} - {baia.label}")
        self.setWindowIcon(QIcon(ICON_APP))
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setFixedSize(934, 858)
        self.setContentsMargins(7, 7, 7, 0)
        self.connection = Connection()
        self.circle_service = CircleService(self.connection)
        circle_result_service = self.circle_service.get_circles_by_uuid_baia(baia=baia)
        self.circle: Circle = (
            circle_result_service[0] if circle_result_service else None
        )
        self.suino_service = SuinoService(self.connection)

        self.init_layout_center()

    def init_layout_center(self):
        self.central_widget = QWidget(self)
        self.layout_center = QVBoxLayout()
        self.layout_center.setSizeConstraint(QVBoxLayout.SetDefaultConstraint)
        self.layout_center.setContentsMargins(0, 0, 0, 7)
        self.layout_center.addWidget(self.init_grid())
        self.layout_center.addWidget(self.init_toolbar())
        self.layout_center.addWidget(self.init_list())
        self.load_list_suino()
        self.central_widget.setLayout(self.layout_center)
        self.setCentralWidget(self.central_widget)

    def init_grid(self) -> QWidget:
        widget = QWidget()
        grid = QGridLayout()
        grid.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(UtilsWidget.label_title("Baia:"), 0, 0)
        grid.addWidget(UtilsWidget.label_value(self.baia.label), 0, 1)

        grid.addWidget(UtilsWidget.label_title("Dimensões:"), 1, 0)
        grid.addWidget(
            UtilsWidget.label_value(
                f"{self.baia.dimen_with}m x {self.baia.dimen_height}m ({self.baia.dimen_with * self.baia.dimen_height}m²)"
            ),
            1,
            1,
        )
        grid.addWidget(UtilsWidget.label_title("Tipo de ocupação:"), 2, 0)
        grid.addWidget(UtilsWidget.label_value(self.baia.type_occupation), 2, 1)
        grid.addWidget(UtilsWidget.label_title("Status:"), 2, 0)
        status = "Ativa" if self.baia.status else "Desativada"
        grid.addWidget(UtilsWidget.label_value(status), 2, 1)
        if self.circle is not None:
            grid.addWidget(UtilsWidget.label_title("Ciclo atual:"), 3, 0)
            grid.addWidget(UtilsWidget.label_value(self.circle.circle_name), 3, 1)
            grid.addWidget(UtilsWidget.label_title("Data de inicio:"), 4, 0)
            date_now = datetime.now()
            data_birth_string = f"{str(self.circle.start_date)} ({calculate_days(str(self.circle.start_date), date_now.strftime("%Y-%m-%d"))} dias)"
            grid.addWidget(UtilsWidget.label_value(data_birth_string), 4, 1)

        widget.setLayout(grid)
        return widget

    def init_toolbar(self) -> QWidget:
        widget = QWidget()
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.setAlignment(Qt.AlignRight)
        create_circle_button = QPushButton(MAIN_PANEL_BUTTON_ADD_CIRCLE)
        create_circle_button.setSizePolicy(QSizePolicy.Expanding, 50)
        create_circle_button.setFixedWidth(190)
        create_circle_button.setStyleSheet(FONTE_BUTTON_18PX)
        create_circle_button.clicked.connect(
            lambda: self.open_click_register_circle(self.baia)
        )
        self.layout_horizontal.addWidget(create_circle_button)

        create_suino_button = QPushButton(MAIN_PANEL_BUTTON_ADD_SUINO)
        create_suino_button.setSizePolicy(QSizePolicy.Expanding, 50)
        create_suino_button.setFixedWidth(190)
        create_suino_button.setStyleSheet(FONTE_BUTTON_18PX)
        create_suino_button.clicked.connect(lambda: self.open_click_register_suino())
        self.layout_horizontal.addWidget(create_suino_button)
        widget.setLayout(self.layout_horizontal)
        return widget

    def init_list(self) -> SuinoListWidget:
        self.suino_list_widget = SuinoListWidget(self.teste)
        return self.suino_list_widget

    def load_list_suino(self):
        suino_list = self.suino_service.get_suino_by_uuid(self.circle)
        self.suino_list_widget.setList(suino_list)

    @pyqtSlot()
    def open_click_register_suino(self):
        dialog = SuinoFormDialog(self.circle)
        dialog.dialog_closed.connect(self.on_dialog_closed)
        dialog.exec_()

    @pyqtSlot(bool)
    def on_dialog_closed(self, result):
        if result:
            self.load_list_suino()
        else:
            print(f"{result}")

    def teste(self, suino: Suino):
        print(f"{suino}")
