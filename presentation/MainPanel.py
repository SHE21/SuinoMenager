from abc import ABC, abstractmethod
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QSizePolicy,
    QDesktopWidget,
    QPushButton,
    QVBoxLayout,
    QMainWindow,
    QToolBar,
    QAction,
    QDockWidget,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from data.connection.Connection import Connection
from data.service.InstalationService import InstalationService
from model.Instalation import Instalation
from presentation.InstalationDialogForm import InstalationFormDialog
from presentation.InstalationListWidget import InstalationListWidget, OnClickListener
from presentation.SuinoListWidget import SuinoListWidget
from presentation.SuinoForm import SuinoForm
from presentation.instalation.GranjaWindow import GranjaWindow
from presentation.listeners import IDialogCallback
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
        self.setWindowIcon(QIcon("src/images/icon_window.png"))
        self.setWindowTitle("Suino Gerenciador")
        self.resize(screen_geometry.width(), screen_geometry.height() - 40)

        self.add_suino = None

        # Layouts
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet(STYLE_DOCK)
        layout = QVBoxLayout()
        layout.setSizeConstraint(QVBoxLayout.SetDefaultConstraint)
        layout.setContentsMargins(0, 0, 0, 0)

        instalation_service = InstalationService(self.connection)
        instalation_list_result = instalation_service.get_instalation_list()
        instalation_list_widget = InstalationListWidget(
            instalation_list_result, self.open_dialog_details
        )
        layout.addWidget(instalation_list_widget)

        self.create_toolbar()
        self.dock_widget()

        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    def create_toolbar(self):
        # Criando a barra de ferramentas
        toolbar = QToolBar("Minha Barra de Ferramentas")
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

    def dock_widget(self):
        dock_left = QDockWidget()
        dock_left.setFeatures(QDockWidget.NoDockWidgetFeatures)
        dock_left.setAllowedAreas(
            Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea
        )  # Áreas permitidas para o dock
        dock_left.setStyleSheet(STYLE_DOCK)

        create_suino_button = QPushButton("Adicionar Suino")
        create_suino_button.setSizePolicy(QSizePolicy.Expanding, 50)
        create_suino_button.setStyleSheet(Style().FONTE_BUTTON_18PX)
        create_suino_button.clicked.connect(self.open_form_add_suino)

        create_instalation_btn = QPushButton("Instalações")
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

    @pyqtSlot()
    def open_instalation_form(self):
        instalation_dialog = InstalationFormDialog()
        instalation_dialog.dialog_closed.connect(self.on_dialog_closed)
        instalation_dialog.exec_()

    @pyqtSlot()
    def open_form_add_suino(self):
        self.add_suino = SuinoForm()
        self.add_suino.dialog_closed.connect(self.on_dialog_closed)
        self.add_suino.exec_()

    @pyqtSlot(bool)
    def on_dialog_closed(self, result):
        if result:
            self.suino_list_widget.load_list()
            print("O diálogo foi fechado e os dados foram salvos.")
        else:
            print("O diálogo foi fechado com Cancelar.")
