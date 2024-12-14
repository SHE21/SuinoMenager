import paho.mqtt.client as mqtt
import time
import paho.mqtt.client as mqtt


# mosquitto_pub -h localhost -p 1884 -t "baia/entenvironment/temperature" -m "26.7"
# mosquitto_sub -h localhost -p 1884 -t "baia/entenvironment/temperature"
class ReceiverData:
    def __init__(self, on_message):
        # Configuração do Broker MQTT
        self.on_message = on_message
        self.broker = "localhost"  # Endereço do broker
        self.port = 1884  # Porta do broker
        self.topic = "baia/entenvironment/temperature"  # Tópico para publicar o evento
        self.client_id = "gerenciador_granja"

    # Função de callback chamada quando o cliente se conectar ao broker
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conectado com sucesso ao Broker MQTT")
            # Inscreve no tópico onde os sensores estão publicando dados
            client.subscribe(self.topic)  # Altere o tópico conforme sua configuração
        else:
            print(f"Falha na conexão. Código de erro: {rc}")

    # Função de callback chamada quando uma nova mensagem é recebida
    """""
    def on_message(self, client, userdata, msg):
        # Exibe a mensagem recebida no console
        message = msg.payload.decode()

        if message == "off":
            print("desligado")
            self.client.disconnect()
            self.client.loop_stop()
        else:
            print(message)
    """ ""

    def receiver(self):
        # Criação do cliente MQTT
        self.client = mqtt.Client(client_id=self.client_id)

        # Definindo os callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Conectar ao broker MQTT
        self.client.connect(self.broker, self.port, 60)

        # Iniciar o loop MQTT para aguardar e processar as mensagens
        self.client.loop_forever()  # Isso mantém o cliente rodando e esperando por mensagens


# if __name__ == "__main__":
# ReceiverData().receiver()
