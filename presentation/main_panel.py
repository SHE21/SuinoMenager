from abc import ABC, abstractmethod
from PyQt5.QtWidgets import (QWidget, QApplication, QSizePolicy, QDesktopWidget, QPushButton, QVBoxLayout, QMainWindow, QToolBar, QAction, QDockWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from presentation.SuinoListWidget import SuinoListWidget
from presentation.SuinoForm import SuinoForm
from presentation.style.style import Style
from utils.calculus import get_taskbar_dimensions

STYLE_DOCK = """QWidget {
            background-color:;
        }"""

class MainPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.setWindowTitle("Cadastro de Suínos")
        self.resize(screen_geometry.width(), screen_geometry.height()-40)

        self.add_suino = None

        # Layouts
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet(STYLE_DOCK)
        layout = QVBoxLayout()
        layout.setSizeConstraint(QVBoxLayout.SetDefaultConstraint)
        layout.setContentsMargins(0, 0, 0, 0)

        self.suino_list_widget = SuinoListWidget(screen_geometry)
        layout.addWidget(self.suino_list_widget)

        self.create_toolbar()
        self.dock_widget()

        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    def create_toolbar(self):
        # Criando a barra de ferramentas
        toolbar = QToolBar("Minha Barra de Ferramentas")
        toolbar.setMovable(True)  # Permite mover a barra de ferramentas
        self.addToolBar(Qt.TopToolBarArea, toolbar)  # Adiciona a barra de ferramentas no topo

        # Ação para mostrar uma mensagem
        show_msg_action = QAction(QIcon(), "Mostrar Mensagem", self)
        show_msg_action.setStatusTip("Exibe uma mensagem de exemplo")
        show_msg_action.triggered.connect(self.show_message)

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
        dock_left.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)  # Áreas permitidas para o dock
        dock_left.setStyleSheet(STYLE_DOCK)

        save_button = QPushButton("Adicionar Suino")
        save_button.setSizePolicy(QSizePolicy.Expanding, 50)
        save_button.setStyleSheet(Style().FONTE_BUTTON_18PX)
        save_button.clicked.connect(self.open_form_add_suino)

        dock_content = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(save_button, alignment=Qt.AlignTop)
        dock_content.setLayout(layout)
            
        dock_left.setWidget(dock_content)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_left)

    def show_message():
        print("teste")

    def open_form_add_suino(self):
        if not self.add_suino or not self.add_suino.isVisible():
            self.add_suino = SuinoForm()
            self.add_suino.exec_()

    def onClose(text: str):
        print(text)
