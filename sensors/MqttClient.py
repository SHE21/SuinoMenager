import paho.mqtt.client as mqtt
from PyQt5.QtCore import QThread, pyqtSignal


class MqttClient(QThread):
    message_received = pyqtSignal(
        str
    )  # Sinal para enviar mensagens para a interface gráfica

    def __init__(self, broker, port, topic):
        super().__init__()
        self.client_id = "baias_"
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client(client_id=self.client_id)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao broker MQTT")
            client.subscribe(self.topic)
        else:
            print(f"Falha na conexão. Código de erro: {rc}")

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        if message == "off":
            self.stop()
        else:
            self.message_received.emit(message)  # Emite o sinal com a mensagem recebida

    def run(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_forever()

    def stop(self):
        self.client.disconnect()
        self.client.loop_stop()
        self.quit()
