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

    """
    connect = Connection()
    service = InstalationService(connect)
    resutl = service.get_instalation_list()
    for inst in resutl:
        print(inst.name)
    instalation = Instalation(
        id=0,
        id_uuid=uuid.uuid4(),
        geo_location=[-2.09009, -3.0980],
        address="Luis domingues",
        name="granja do leste",
        area=20.0,
        infra="gralpão de ração, beanheiro para os funcionarios",
        registration_date=datetime.now().strftime("%Y-%m-%d"),
    )

    result = service.create(instalation)

    if result:
        print("Salvo")
    else:
        print("error")
    """
