from datetime import date
import sys
from PyQt5.QtWidgets import (
    QApplication
)

from data.connection.Connection import Connection
from data.model.SuinoModel import get_suino_model
from data.service.SuinoService import SuinoService
from presentation.SuinoForm import SuinoForm
from presentation.main_panel import MainPanel

def main():
    app = QApplication(sys.argv)
    main_panel = MainPanel()
    main_panel.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    connection = Connection()
    suino_service = SuinoService(connection)
    
    suino_service.create_suino(
            id_tag="TAG126",
            race="Large White",
            date_birth=date(2023, 5, 15),
            gender="Fêmea",
            origin="Fazenda Primavera",
            destination="Abatedouro São João"
        )
    
    if suino_service is not None:
        print("Suino criado!")
    else:
        print("Erro ao adicionar um registro!")

    suino_by_id_tag = suino_service.get_suino_by_id_tag("TAG126")
    print(suino_by_id_tag)

    connection.close()

