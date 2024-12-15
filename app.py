import sys
from PyQt5.QtWidgets import QApplication

from data.connection.Connection import Connection
from data.service.DailyStatusService import DailyStatusService
from model.Health import Health
from model.Nutrition import Nutrition
from presentation.MainPanel import MainPanel
from presentation.instalation.GranjaWindow import GranjaWindow


def main():
    app = QApplication(sys.argv)
    main_panel = MainPanel()
    main_panel.show()
    sys.exit(app.exec_())


def planta():
    app = QApplication(sys.argv)
    window = GranjaWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
