from datetime import datetime
import sys
import uuid
from PyQt5.QtWidgets import (
    QApplication
)

from data.connection.Connection import Connection
from data.service.HealthService import HealthService
from presentation.main_panel import MainPanel

def main():
    app = QApplication(sys.argv)
    main_panel = MainPanel()
    main_panel.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    conn = Connection()
    service = HealthService(conn)
    result = service.create_status_health(
        id_uuid = uuid.uuid4(),
        id_uuid_suino = uuid.uuid4(),
        id_uuid_circle = uuid.uuid4(),
        weight = 4.6,
        registration_date = datetime.now().strftime("%Y-%m-%d"),
        id_uui_health = uuid.uuid4(),
        medicine_name = "monoxilina",
        medicine_type = "antibiotico",
        adminitration_type = "intramuscular",
        dosage = 120.0,
        is_treatment = True,
        diagnosis = "verminose",
        date_start = datetime.now().strftime("%Y-%m-%d"),
        date_end = "0000-00-00",
        obervation = "suino em tratamento contra vermisono. não serve para o abate"
    )

    if result:
        print("Health salvo!!")
    else:
        print("Error!")