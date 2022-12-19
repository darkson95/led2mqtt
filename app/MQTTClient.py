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
                logging.info(f"Connected to MQTT-Broker ({self.get_url()})")
                client.publish(f"{self.configuration.mqtt_topic}/availability", payload="online", qos=0, retain=True)
            else:
                logging.error(f"Could not connect to MQTT-Broker. Error-Code {rc}")
        
        client_id = f'led2mqtt-{random.randint(0, 1000)}'
        transport = "websockets" if self.configuration.mqtt_websockets == "true" else "tcp"

        self.client = mqtt_client.Client(client_id, transport=transport, reconnect_on_failure=True)
        self.client.will_set(f"{self.configuration.mqtt_topic}/availability", payload="offline", qos=0, retain=True)
        self.client.on_connect = on_connect
        
        if self.configuration.mqtt_username and self.configuration.mqtt_password:
            self.client.username_pw_set(self.configuration.mqtt_username, self.configuration.mqtt_password)
            logging.debug(f"Set MQTT-Username to {self.configuration.mqtt_username}")

    def get_url(self):
        protocol = "ws" if self.configuration.mqtt_websockets == "true" else "mqtt"
        return f"{protocol}://{self.configuration.mqtt_host}:{self.configuration.mqtt_port}"

    def connect(self):
        logging.debug(f"Try to connect to MQTT-Broker ({self.get_url()})")
        self.client.connect(self.configuration.mqtt_host, int(self.configuration.mqtt_port))

    def publish(self, topic, message):
        logging.debug(f"MQTT-Publish to {topic}: {message}")
        result = self.client.publish(topic, message, qos=0, retain=True)
        status = result[0]
        if status != 0:
            logging.error(f"Failed to send MQTT-message to topic {topic}")

    def subscribe(self, topic, on_message):
        logging.debug(f"MQTT-Subscribe to {topic}")
        self.client.subscribe(topic)
        self.client.on_message = on_message
