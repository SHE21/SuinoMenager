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

from data.connection.Connection import Connection
from data.service.InstalationService import InstalationService
from presentation.InstalationLayoutForm import InstalationLayoutForm
from presentation.UtilsWidget import validate_fields
from presentation.style.style import Style


class InstalationFormDialog(QDialog):
    dialog_closed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("src/images/icon_window.png"))
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setWindowTitle(f"Registrar Instalação")
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
        self.instalation_form = InstalationLayoutForm()
        return self.instalation_form

    def init_dialog_buttons(self) -> QDialogButtonBox:
        button_box = QDialogButtonBox()
        button_box.setStyleSheet(Style().BUTTON_DIALOG)
        save_button = QPushButton("Registrar")
        cancel_button = QPushButton("Cancelar")

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
