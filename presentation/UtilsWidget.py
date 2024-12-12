from PyQt5.QtWidgets import (
    QLabel,
)

from presentation.style.style import Style


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
