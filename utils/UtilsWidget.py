from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QLineEdit, QComboBox, QDateEdit, QFormLayout
from PyQt5.QtGui import QDoubleValidator

from presentation.style.style import Style


def date_input() -> QDateEdit:
    date_edit_unput = QDateEdit()
    date_edit_unput.setStyleSheet(Style().FONTE_EDIT_DATE_18PX)
    date_edit_unput.setBaseSize(100, 30)
    date_edit_unput.setCalendarPopup(True)
    date_edit_unput.setDisplayFormat("yyyy-MM-dd")
    date_edit_unput.setDate(QDate.currentDate())
    return date_edit_unput


def combo_box_text_input(values: list[str]) -> QComboBox:
    combo_box = QComboBox()
    combo_box.setFixedWidth(200)
    combo_box.setStyleSheet(Style().FONTE_COMBO_BOX)
    combo_box.addItems(values)
    return combo_box


def line_edit_text_input() -> QLineEdit:
    line_text = QLineEdit()
    line_text.setStyleSheet(Style().FONTE_EDIT_18PX)
    return line_text


def line_edit_numb_input() -> QLineEdit:
    line_edit = QLineEdit()
    line_edit.setStyleSheet(Style().FONTE_EDIT_18PX)
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


def validate_fields(form_layout: QFormLayout) -> list[str]:
    errors = []
    # Itera sobre todos os widgets do QFormLayout
    for i in range(form_layout.rowCount()):
        widget = form_layout.itemAt(i, 1).widget()
        if isinstance(widget, QComboBox) and not widget.currentText().strip():
            errors.append(f"{form_layout.itemAt(i, 0).widget().currentText()}\n")

        elif isinstance(widget, QLineEdit) and not widget.text().strip():
            errors.append(f"{form_layout.itemAt(i, 0).widget().text()}\n")

        elif isinstance(widget, QDateEdit) and not widget.date().strip():
            errors.append(f"{form_layout.itemAt(i, 0).widget().date()}\n")

    return errors
