from datetime import date, datetime
import sys
import uuid
from PyQt5.QtWidgets import QApplication

from data.connection.Connection import Connection
from data.service.InstalationService import InstalationService
from model.Instalation import Instalation
from presentation.MainPanel import MainPanel


def main():
    app = QApplication(sys.argv)
    main_panel = MainPanel()
    main_panel.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
