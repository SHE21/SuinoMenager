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


if __name__ == "__main__":
    # main()
    app = QApplication(sys.argv)
    window = GranjaWindow()
    window.show()
    sys.exit(app.exec_())

    """""
    conn = Connection()
    service = NutritionService(conn)
    result = service.create_status_nutrition(
        id_uuid = uuid.uuid4(),
        id_uuid_suino = uuid.uuid4(),
        id_uuid_circle = uuid.uuid4(),
        weight = 4.6,
        registration_date = datetime.now().strftime("%Y-%m-%d"),
        id_uuid_nutrition=uuid.uuid4(),
        daily_feed_intake=4.6,
        feed_composition="feed_composition",
        weight_gain_daily=1.4,
        water_intake=1.4,
        supplementation="supplementation"
    )
    """
