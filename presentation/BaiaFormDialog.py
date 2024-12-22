from PyQt5.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QDialog,
    QFormLayout,
    QDialogButtonBox,
    QMessageBox,
)

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot

from assets.strings.Strings import (
    ACTION_TITLE_CANCEL,
    ACTION_TITLE_REGISTER,
    DIALOG_TITLE_REGISTER_BAIA,
    WARNINGS_TITLE_EMPTY_FIELDS,
    WARNINGS_MSN_EMPTY_FIELDS,
    ICON_APP,
)
from assets.style.style import BUTTON_DIALOG
from data.connection.Connection import Connection
from data.service.BaiaService import BaiaService
from model.Instalation import Instalation
from presentation.BaiaFormWidget import BaiaFormWidget
from utils.UtilsWidget import validate_fields


class BaiaFormDialog(QDialog):
    closed_dialog_baia_form = pyqtSignal(bool)

    def __init__(self, instalation: Instalation):
        self.instalation = instalation
        super().__init__()
        self.setWindowIcon(QIcon(ICON_APP))
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowTitle(DIALOG_TITLE_REGISTER_BAIA)
        self.setLayout(self.init_layout())
        self.setFixedSize(834, 758)
        self.connection = Connection()
        self.service = BaiaService(self.connection)

    def init_layout(self) -> QVBoxLayout:
        self.layout_v = QVBoxLayout()
        self.layout_v.addLayout(self.init_instalation_form())
        self.layout_v.addWidget(self.init_dialog_buttons())
        return self.layout_v

    def init_instalation_form(self) -> QFormLayout:
        self.form_layout = BaiaFormWidget(self.instalation)
        return self.form_layout

    def init_dialog_buttons(self) -> QDialogButtonBox:
        button_box = QDialogButtonBox()
        button_box.setStyleSheet(BUTTON_DIALOG)
        save_button = QPushButton(ACTION_TITLE_REGISTER)
        cancel_button = QPushButton(ACTION_TITLE_CANCEL)

        save_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        button_box.addButton(cancel_button, QDialogButtonBox.RejectRole)
        button_box.addButton(save_button, QDialogButtonBox.AcceptRole)
        return button_box

    @pyqtSlot()
    def accept(self):
        get_valid_fields = validate_fields(self.form_layout)
        if len(get_valid_fields) > 0:
            QMessageBox.warning(
                self,
                WARNINGS_TITLE_EMPTY_FIELDS,
                WARNINGS_MSN_EMPTY_FIELDS + "".join(get_valid_fields),
            )
        else:
            baia = self.form_layout.get_values_fields()
            result = self.service.create(baia)
            if result:
                self.closed_dialog_baia_form.emit(True)
            else:
                self.closed_dialog_baia_form.emit(True)

            super().accept()

    @pyqtSlot()
    def reject(self):
        self.closed_dialog_baia_form.emit(False)
        super().reject()
