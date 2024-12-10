import enum


class Style():
    def __init__(self):
        self.FONTE_EDIT_18PX = """QLineEdit {
            font-size: 18px;
            border: 2px solid gray;
            border-radius: 5px;
            padding: 5px;
        }"""

        self.FONTE_EDIT_DATE_18PX = """QDateEdit {
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
           font-size: 18px;
            border: 2px solid gray;
            border-radius: 5px;
            padding: 5px;
        }"""
        self.LIST = """QListWidget {
            background-color:#dedede;
        }"""

        self.LIST_BUTTON = """QPushButton {
            background-color:;
        }"""

        self.BUTTON_DIALOG = """
            QDialogButtonBox QPushButton {
                font-size: 16px;    /* Tamanho de fonte */
                padding: 10px 20px; /* Espaçamento interno */
                min-width: 150px;   /* Largura mínima do botão */
            }
        """