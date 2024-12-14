import paho.mqtt.client as mqtt
import time

# mosquitto_pub -h localhost -p 1884 -t "baia/entenvironment/temperature" -m "26.7"
# mosquitto_sub -h localhost -p 1884 -t "baia/entenvironment/temperature"

# Configuração do Broker MQTT
broker = "localhost"  # Endereço do broker
port = 1884  # Porta do broker
topic = "baia/entenvironment/temperature"  # Tópico para publicar o evento
client_id = "gerenciador_granja"


# Função para conectar ao broker MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(topic)
        print("Conectado com sucesso ao Broker MQTT")
    else:
        print("Falha na conexão. Código de erro:", rc)


def publicar_temperatura(temperatura):
    # Conectar ao Broker MQTT
    client = mqtt.Client(client_id=client_id)
    client.on_connect = on_connect

    client.connect(broker, port, 60)  # Conecta ao broker
    client.loop_start()  # Inicia o loop de comunicação

    # Publicar a temperatura no tópico específico
    message = temperatura
    client.publish(topic, message)  # Publica a mensagem

    print(f"Evento publicado: {message}")

    time.sleep(1)  # Aguarda o envio da mensagem
    client.loop_stop()  # Para o loop após o envio


if __name__ == "__main__":
    # Exemplo de uso da função para publicar um evento
    temperatura = 25.5  # Exemplo de temperatura
    publicar_temperatura(temperatura)
