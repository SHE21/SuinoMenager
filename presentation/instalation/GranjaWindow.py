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
from PyQt5.QtWidgets import QToolTip, QApplication, QPushButton, QWidget
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPen, QColor, QBrush, QFont
from presentation.instalation.BaiaRect import BaiaRect
from sensors.MqttClient import MqttClient
from sensors.ReceiverData import ReceiverData

# mosquitto_sub -h localhost -p 1883 -t "teste/topico"


class GranjaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Granja - Baia de Porcos")
        self.setGeometry(100, 100, 00, 400)

        # Criação da cena gráfica
        self.scene = QGraphicsScene()

        self.largura = 320  # Largura da baia
        self.altura = 320  # Altura da baia
        num_filas = 2  # Número de filas
        num_baias_por_fila = 5  # Número de baias por fila
        espacamento_horizontal = 15  # Espaço entre baias na horizontal
        espacamento_vertical = 15  # Espaço entre baias na vertical
        corredor = 100

        self.criar_baias(
            num_filas,
            num_baias_por_fila,
            self.largura,
            self.altura,
            espacamento_horizontal,
            espacamento_vertical,
            corredor,
        )

        # Criação da visualização para mostrar a cena
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        """""
        self.broker = "localhost"  # Endereço do broker
        self.port = 1884  # Porta do broker
        self.topic = "baia/entenvironment/temperature"  # Tópico para publicar o evento
        self.client_id = "gerenciador_granja"

        self.mqtt_thread = MqttClient(
            broker=self.broker, port=self.port, topic=self.topic
        )
        self.mqtt_thread.message_received.connect(self.display_message)
        self.mqtt_thread.start()
        """

    def criar_baias(
        self,
        num_filas,
        num_baias_por_fila,
        largura,
        altura,
        espacamento_horizontal,
        espacamento_vertical,
        corredor,
    ):
        self.baias = {}
        # Loop para criar baias em cada fila
        for i in range(num_filas):
            for j in range(num_baias_por_fila):
                # Calcular posição horizontal e vertical da baia
                x = (j * largura) + (j * espacamento_horizontal) + 50
                y = (i * altura) + (i * espacamento_vertical) + (i * corredor) + 50

                key = f"baia_{i}_{j}"
                # Adicionar a baia à cena
                self.baias[key] = BaiaRect(x, y, largura, altura)
                self.scene.addItem(self.baias[key])
                self.add_label(x, y, str(j))

    def add_label(self, x, y, text):
        self.scene.addRect(
            x,
            y,
            36,
            36,
            QPen(QColor(0, 0, 0)),
            QBrush(QColor(200, 200, 255)),
        )
        self.texto = QGraphicsTextItem(text)
        self.texto.setFont(QFont("Arial", 12))
        self.texto.setPos(x + 8, y + 2)
        self.scene.addItem(self.texto)

    def display_message(self, message):
        # Atualiza o label com a mensagem recebida
        print(f"RECEBIDAO: {message}")

    def close_application(self):
        # Encerra a thread MQTT e fecha a aplicação
        # self.mqtt_thread.stop()
        self.close()
