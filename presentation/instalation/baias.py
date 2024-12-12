import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QPushButton,
)
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPen, QColor, QBrush, QFont
from rules import instalation


class GranjaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Granja - Baia de Porcos")
        self.setGeometry(100, 100, 600, 400)

        # Criação da cena gráfica
        self.scene = QGraphicsScene()

        # Dimensões iniciais da baia
        self.largura = 320  # 3m em pixels (ajustado para visualização)
        self.altura = 320  # 3m em pixels (ajustado para visualização)
        corredor = instalation.get("corredor")
        space_between = instalation.get("space")
        inicial_position = instalation.get("inicial_position")
        # Criar a baia (retângulo)
        for side_index, sides in enumerate(instalation.get("sides")):
            if side_index == 0:
                for baia_index, side in enumerate(sides):
                    if baia_index == 0:
                        self.scene.addRect(
                            inicial_position,
                            inicial_position,
                            self.largura,
                            self.altura,
                            QPen(QColor(0, 0, 0)),
                            QBrush(QColor(200, 200, 255)),
                        )
                        self.scene.addRect(
                            inicial_position,
                            inicial_position,
                            30,
                            30,
                            QPen(QColor(0, 0, 0)),
                            QBrush(QColor(200, 200, 255)),
                        )
                    else:
                        inicial_position += space_between
                        self.baia2 = self.scene.addRect(
                            (self.largura * baia_index) + inicial_position,
                            50,
                            self.largura,
                            self.altura,
                            QPen(QColor(0, 0, 0)),
                            QBrush(QColor(200, 200, 255)),
                        )
                        self.baia2 = self.scene.addRect(
                            (self.largura * baia_index) + inicial_position,
                            50,
                            30,
                            30,
                            QPen(QColor(0, 0, 0)),
                            QBrush(QColor(200, 200, 255)),
                        )
                        print(str(inicial_position))

        """"
        self.baia = self.scene.addRect(inicial_position, 50, self.largura, self.altura, QPen(QColor(0, 0, 0)), QBrush(QColor(200, 200, 255)))
        self.baia2 = self.scene.addRect((self.largura * 1) + 65, 50, self.largura, self.altura, QPen(QColor(0, 0, 0)), QBrush(QColor(200, 200, 255)))
        self.baia3 = self.scene.addRect((self.largura * 2) + 80, 50, self.largura, self.altura, QPen(QColor(0, 0, 0)), QBrush(QColor(200, 200, 255)))
        self.baia4 = self.scene.addRect((self.largura * 3) + 95, 50, self.largura, self.altura, QPen(QColor(0, 0, 0)), QBrush(QColor(200, 200, 255)))

        self.baia5 = self.scene.addRect(50, self.altura + corredor, self.largura, self.altura, QPen(QColor(0, 0, 0)), QBrush(QColor(200, 200, 255)))
        self.baia6 = self.scene.addRect((self.largura * 1) + 65, self.altura + corredor, self.largura, self.altura, QPen(QColor(0, 0, 0)), QBrush(QColor(200, 200, 255)))
        self.baia7 = self.scene.addRect((self.largura * 2) + 80, self.altura + corredor, self.largura, self.altura, QPen(QColor(0, 0, 0)), QBrush(QColor(200, 200, 255)))
        self.baia8 = self.scene.addRect((self.largura * 3) + 95, self.altura + corredor, self.largura, self.altura, QPen(QColor(0, 0, 0)), QBrush(QColor(200, 200, 255)))

        self.canto = self.scene.addRect(50, 50, 30, 30, QPen(QColor(0, 0, 0)), QBrush(QColor(200, 200, 255)))
        """

        # Adicionar o texto com as dimensões da baia
        self.texto = QGraphicsTextItem("1")
        self.texto.setFont(QFont("Arial", 12))
        dimens = 44
        self.texto.setPos(
            dimens + dimens / 2 - self.texto.boundingRect().width() / 2,
            dimens + dimens / 2 - self.texto.boundingRect().height() / 2,
        )

        # Adicionar à cena
        self.scene.addItem(self.texto)

        # Criação da visualização para mostrar a cena
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        # Adicionar botão para alterar as dimensões e a cor da baia
        self.botao = QPushButton("Alterar Baia", self)
        self.botao.setGeometry(50, 350, 150, 30)
        self.botao.clicked.connect(self.alterar_baia)

    def alterar_baia(self):
        # Alterar as dimensões da baia
        self.largura = 400  # Nova largura
        self.altura = 250  # Nova altura

        # Atualizar a baia com as novas dimensões
        self.baia.setRect(50, 50, self.largura, self.altura)

        # Atualizar o texto para refletir as novas dimensões
        self.texto.setPlainText(f"{self.largura / 100}m x {self.altura / 100}m")
        self.texto.setPos(
            50 + self.largura / 2 - self.texto.boundingRect().width() / 2,
            50 + self.altura / 2 - self.texto.boundingRect().height() / 2,
        )

        # Alterar a cor da baia
        self.baia.setBrush(QBrush(QColor(150, 255, 150)))  # Cor nova para a baia


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GranjaWindow()
    window.show()
    sys.exit(app.exec_())
