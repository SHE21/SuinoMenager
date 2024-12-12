import enum


class Style:
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
        self.FONTE_ITEN_LIST = """QLabel {
            font-size: 16px;
            font-weight:bold;
            border-radius: 5px;
            padding: 5px;
        }"""
        self.FONTE_ITEN_LIST_1 = """QLabel {
            font-size: 14px;
            font-weight:bold;
            padding: 8px;
        }"""
        self.STYLE_LABEL_HEALTH = """QLabel {
            font-size: 14px;
            font-weight:bold;
            background-color:#DEDEDE;
            padding: 8px;
            border-left: 6px solid #1E90FF;
        }"""
        self.STYLE_LABEL_NUTRITION = """QLabel {
            font-size: 14px;
            font-weight:bold;
            background-color:#DEDEDE;
            padding: 8px;
            border-left: 6px solid #3CB371;
        }"""

        self.STYLE_GRID = """QGridLayout {
                    background-color:red;
                }"""

        self.STYLE_BUTTON = """QPushButton {
                    font-size: 18px;
                }"""

        self.STYLE_LABEL_TITLE = """QLabel {
                    height: 10px;
                    font-size: 18px;
                    background-color:#dedede;
                    padding:3px;
                }"""

        self.STYLE_LABEL_VALUE = """QLabel {
                    height: 10px;
                    font-size: 18px;
                    background-color:#dedede;
                    font-weight: bold;
                    padding:3px;
                }"""
