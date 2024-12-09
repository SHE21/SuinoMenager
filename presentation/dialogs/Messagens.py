from PyQt5.QtWidgets import QMessageBox

def show_error_message(message: str):
        # Exibe uma caixa de mensagem de erro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")
        msg.setText(message)
        msg.exec_()

def show_success_message(message: str):
        # Exibe uma caixa de mensagem de erro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Suino Registrado")
        msg.setText(message)
        msg.exec_()