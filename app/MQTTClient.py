# coding=utf-8
import logging
import random
from Configuration import Configuration
from paho.mqtt import client as mqtt_client

class MQTTClient():
    def __init__(self, configuration: Configuration):
        self.configuration = configuration

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                logging.debug(f"Connected to MQTT-Broker ({self.configuration.mqtt.host}:{self.configuration.mqtt.port})")
                client.publish(f"{self.configuration.mqtt.topic}/availability", payload="online", qos=0, retain=True)
            else:
                logging.error(f"Could not connect to MQTT-Broker. Error-Code {rc}")
        
        client_id = f'led2mqtt-{random.randint(0, 1000)}'
        transport = "websockets" if self.configuration.mqtt.websockets == "true" else "tcp"

        self.client = mqtt_client.Client(client_id, transport=transport, reconnect_on_failure=True)
        self.client.will_set(f"{self.configuration.mqtt.topic}/availability", payload="offline", qos=0, retain=True)
        self.client.on_connect = on_connect
        
        if self.configuration.mqtt.username and self.configuration.mqtt.password:
            self.client.username_pw_set(self.configuration.mqtt.username, self.configuration.mqtt.password)
            logging.debug(f"Set MQTT-Username to {self.configuration.mqtt.username}")

    def connect(self):
        self.client.connect(self.configuration.mqtt.host, int(self.configuration.mqtt.port))

    def publish(self, topic, message):
        result = self.client.publish(topic, message, qos=0, retain=True)
        status = result[0]
        if status != 0:
            logging.error(f"Failed to send MQTT-message to topic {topic}")

    def subscribe(self, topic, on_message):
        self.client.subscribe(topic)
        self.client.on_message = on_message
