from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QPushButton,
    QDialog,
    QHBoxLayout,
    QFormLayout,
    QDialogButtonBox,
    QMessageBox,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot

from assets.strings.Strings import (
    ACTION_TITLE_CANCEL,
    ACTION_TITLE_REGISTER,
    DIALOG_TITLE_REGISTER_INSTALATION,
    ICON_APP,
)
from assets.style.style import BUTTON_DIALOG
from data.connection.Connection import Connection
from data.service.InstalationService import InstalationService
from presentation.InstalationFormWidget import InstalationFormWidget
from utils.UtilsWidget import validate_fields


class InstalationFormDialog(QDialog):
    dialog_closed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(ICON_APP))
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowTitle(DIALOG_TITLE_REGISTER_INSTALATION)
        self.setLayout(self.init_layout())
        self.setFixedSize(834, 758)
        self.connection = Connection()
        self.service = InstalationService(self.connection)

    def init_layout(self) -> QVBoxLayout:
        self.layout_v = QVBoxLayout()
        self.layout_v.addLayout(self.init_instalation_form())
        self.layout_v.addWidget(self.init_dialog_buttons())
        return self.layout_v

    def init_instalation_form(self) -> QFormLayout:
        self.instalation_form = InstalationFormWidget()
        return self.instalation_form

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
        get_valid_fields = validate_fields(self.instalation_form)
        if len(get_valid_fields) > 0:
            QMessageBox.warning(
                self,
                "Campos estão vazios",
                "Os seguintes campos estão vazios:\n" + "".join(get_valid_fields),
            )
        else:
            instalation = self.instalation_form.get_values_fields()
            result = self.service.create(instalation)
            if result:
                print("dados salvo!!")
                self.dialog_closed.emit(True)
            else:
                print("Error!")
                self.dialog_closed.emit(True)

            super().accept()

    @pyqtSlot()
    def reject(self):
        self.dialog_closed.emit(False)
        super().reject()
