import enum


class Style():
    def __init__(self):
        self.FONTE_EDIT_18PX = """QLineEdit {
            font-size: 18px;
            border: 2px solid gray;
            border-radius: 5px;
            padding: 5px;
        }"""

        self.FONTE_BUTTON_18PX = """QPushButton {
            font-size: 18px;
            padding: 8px;
        }"""

        self.FONTE_LABEL = """QLabel {
            height: 10px;
            font-size: 18px;
        }"""

        self.FONTE_COMBO_BOX = """QComboBox {
            height: 10px;
            font-size: 18px;
        }"""
        self.LIST = """QListWidget {
            background-color:;
        }"""

        self.LIST_BUTTON = """QPushButton {
            background-color:;
        }"""