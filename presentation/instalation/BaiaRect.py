from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtGui import QCursor, QPen, QColor, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QToolTip, QApplication, QPushButton

from presentation.SuinoForm import SuinoForm


# Subclasse personalizada de QGraphicsRectItem
class BaiaRect(QGraphicsRectItem):
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        self.setPen(QPen(QColor(0, 0, 0)))
        self.setBrush(QBrush(QColor(200, 200, 255)))
        self.setAcceptHoverEvents(True)  # Habilita eventos de hover

    # Evento quando o mouse entra no retângulo
    def hoverEnterEvent(self, event):
        self.setBrush(QBrush(QColor(176, 196, 222)))
        self.setCursor(QCursor(Qt.PointingHandCursor))  # Muda para mãozinha
        super().hoverEnterEvent(event)

    # Evento quando o mouse sai do retângulo
    def hoverLeaveEvent(self, event):
        self.setBrush(QBrush(QColor(200, 200, 255)))
        self.setCursor(QCursor(Qt.ArrowCursor))  # Volta para o cursor padrão
        super().hoverLeaveEvent(event)

    def mousePressEvent(self, event):
        if (
            event.button() == Qt.LeftButton
        ):  # Verifica se é um clique com o botão esquerdo
            print(
                f"Baia clicada em: {self.rect().x()}, {self.rect().y()}"
            )  # Exemplo de ação ao clicar
            self.setBrush(QBrush(QColor(220, 20, 60)))
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        # Obtém as coordenadas do mouse dentro do item (não da cena)
        pos = event.pos()  # Posição do mouse dentro do retângulo
        print(f"Mouse movendo sobre a baia: ({pos.x()}, {pos.y()})")
        super().mouseMoveEvent(event)

    def show_tooltip(self, text):
        self.setToolTip(text)
