from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QDoubleValidator

from presentation.style.style import Style


def line_edit_text_input() -> QLineEdit:
    line_text = QLineEdit()
    line_text.setStyleSheet(Style().FONTE_EDIT_18PX)
    return line_text


def line_edit_numb_input() -> QLineEdit:
    line_edit = QLineEdit()
    line_edit.setFixedWidth(75)
    line_edit.setValidator(QDoubleValidator(0.0, 1000.0, 3))
    return line_edit


def label_title(text: str) -> QLabel:
    label = QLabel(text=text)
    label.setStyleSheet(Style().STYLE_LABEL_TITLE)
    label.setFixedSize(180, 30)
    return label


def label_value(text: str) -> QLabel:
    label = QLabel(text=text)
    label.setStyleSheet(Style().STYLE_LABEL_VALUE)
    label.setFixedHeight(30)
    return label
