from abc import ABC, abstractmethod
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QSizePolicy,
    QPushButton,
    QVBoxLayout,
    QMainWindow,
    QToolBar,
    QAction,
    QDockWidget,
    QHBoxLayout,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from assets.strings.Strings import (
    ICON_APP,
    MAIN_PANEL_TITLE,
    MAIN_PANEL_TOOLBAR_TITLE,
    MAIN_PANEL_BUTTON_ADD_SUINO,
    MAIN_PANEL_BUTTON_ADD_INSTALATION,
)
from config import TYPE_USER
from data.connection.Connection import Connection
from data.service.InstalationService import InstalationService
from model.Instalation import Instalation
from presentation.InstalationFormDialog import InstalationFormDialog
from presentation.InstalationListWidget import InstalationListWidget
from presentation.SuinoListWidget import SuinoListWidget
from presentation.SuinoFormDialog import SuinoFormDialog
from presentation.style.style import Style
from utils.Utils import get_taskbar_dimensions
from PyQt5.QtCore import pyqtSignal, pyqtSlot

STYLE_DOCK = """QWidget {
            background-color:;
        }"""


class MainPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connection = Connection()
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setWindowIcon(QIcon(ICON_APP))
        self.setWindowTitle(MAIN_PANEL_TITLE)
        self.resize(screen_geometry.width() - 100, screen_geometry.height() - 200)

        self.add_suino = None

        # Layouts
        self.init_layout_center()
        self.init_layout_button()

        self.init_config_center()
        self.init_toolbar()

    def init_layout_center(self):
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet(STYLE_DOCK)
        self.layout_center = QHBoxLayout()
        self.layout_center.setSizeConstraint(QVBoxLayout.SetDefaultConstraint)
        self.layout_center.setContentsMargins(0, 0, 0, 0)
        self.central_widget.setLayout(self.layout_center)
        self.setCentralWidget(self.central_widget)

    def init_layout_button(self):
        button_widget = QWidget(self)
        button_widget.setFixedWidth(190)
        self.layout_section_button = QVBoxLayout()
        self.layout_section_button.setContentsMargins(7, 7, 0, 0)
        self.layout_section_button.setAlignment(Qt.AlignTop | Qt.AlignVCenter)
        self.layout_section_button.setSizeConstraint(QVBoxLayout.SetDefaultConstraint)
        button_widget.setLayout(self.layout_section_button)
        self.layout_center.addWidget(button_widget)

    def init_content_layout_button(self):
        create_instalation_btn = QPushButton(MAIN_PANEL_BUTTON_ADD_INSTALATION)
        create_instalation_btn.setSizePolicy(QSizePolicy.Expanding, 50)
        create_instalation_btn.setStyleSheet(Style().FONTE_BUTTON_18PX)
        create_instalation_btn.clicked.connect(self.open_instalation_form)
        self.layout_section_button.addWidget(create_instalation_btn)

    def init_config_center(self):
        if TYPE_USER == "manager":
            self.init_content_layout_button()
            self.init_content_layout_left()
            self.init_content_layout_right()

    def init_content_layout_right(self):
        # mudar conteudo para lista
        btn = QPushButton("teste")
        btn.setBaseSize(200, 40)
        self.layout_center.addWidget(btn)

    def init_content_layout_left(self):
        self.instalation_service = InstalationService(self.connection)
        instalation_list_result = self.instalation_service.get_instalation_list()
        self.instalation_list_widget = InstalationListWidget(self.open_dialog_details)
        self.instalation_list_widget.setList(instalation_list_result)
        self.layout_center.addWidget(self.instalation_list_widget)

    def init_toolbar(self):
        # Criando a barra de ferramentas
        toolbar = QToolBar(MAIN_PANEL_TOOLBAR_TITLE)
        toolbar.setMovable(True)  # Permite mover a barra de ferramentas
        self.addToolBar(
            Qt.TopToolBarArea, toolbar
        )  # Adiciona a barra de ferramentas no topo

        # Ação para mostrar uma mensagem
        show_msg_action = QAction(QIcon(), "Mostrar Mensagem", self)
        show_msg_action.setStatusTip("Exibe uma mensagem de exemplo")
        # show_msg_action.triggered.connect(self.show_message)

        # Ação para fechar a aplicação
        exit_action = QAction(QIcon(), "Sair", self)
        exit_action.setStatusTip("Fecha a aplicação")
        exit_action.triggered.connect(self.close)

        # Adicionando as ações à barra de ferramentas
        toolbar.addAction(show_msg_action)
        toolbar.addAction(exit_action)

    def init_dock(self):
        dock_left = QDockWidget()
        dock_left.setFeatures(QDockWidget.NoDockWidgetFeatures)
        dock_left.setAllowedAreas(
            Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea
        )  # Áreas permitidas para o dock
        dock_left.setStyleSheet(STYLE_DOCK)

        create_suino_button = QPushButton(MAIN_PANEL_BUTTON_ADD_SUINO)
        create_suino_button.setSizePolicy(QSizePolicy.Expanding, 50)
        create_suino_button.setStyleSheet(Style().FONTE_BUTTON_18PX)
        create_suino_button.clicked.connect(self.open_form_add_suino)

        create_instalation_btn = QPushButton(MAIN_PANEL_BUTTON_ADD_INSTALATION)
        create_instalation_btn.setSizePolicy(QSizePolicy.Expanding, 50)
        create_instalation_btn.setStyleSheet(Style().FONTE_BUTTON_18PX)
        create_instalation_btn.clicked.connect(self.open_instalation_form)

        dock_content = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(create_suino_button, alignment=Qt.AlignTop)
        layout.addWidget(create_instalation_btn, alignment=Qt.AlignTop)
        dock_content.setLayout(layout)

        dock_left.setWidget(dock_content)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_left)

    def open_dialog_details(self, instalation: Instalation):
        print(f"{instalation.name}")

    def open_instalation_form(self):
        instalation_dialog = InstalationFormDialog()
        instalation_dialog.dialog_closed.connect(self.on_dialog_closed)
        instalation_dialog.exec_()

    @pyqtSlot()
    def open_form_add_suino(self):
        self.add_suino = SuinoFormDialog()
        self.add_suino.dialog_closed.connect(self.on_dialog_closed)
        self.add_suino.exec_()

    @pyqtSlot(bool)
    def on_dialog_closed(self, result):
        if result:
            instalation_list_result = self.instalation_service.get_instalation_list()
            self.instalation_list_widget.setList(instalation_list_result)
            print("O diálogo foi fechado e os dados foram salvos.")
        else:
            print("O diálogo foi fechado com Cancelar.")
