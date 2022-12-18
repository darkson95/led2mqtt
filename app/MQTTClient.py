# coding=utf-8
import logging
import random
from paho.mqtt import client as mqtt_client

class MQTTClient():
    def __init__(self, env):
        self.env = env

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                logging.debug("Connected to MQTT-Broker")
                client.publish(env.get("MQTT_TOPIC") + "/availability", payload="online", qos=0, retain=True)
            else:
                logging.error(f"Could not connect to MQTT-Broker. Error-Code {rc}")
        
        self.client = mqtt_client.Client(f'rgb_pwm_mqtt-{random.randint(0, 1000)}', transport=env.get("MQTT_TRANSPORT"), reconnect_on_failure=True)
        self.client.username_pw_set(env.get("MQTT_USERNAME"), env.get("MQTT_PASSWORD"))
        self.client.on_connect = on_connect
        self.client.will_set(env.get("MQTT_TOPIC") + "/availability", payload="offline", qos=0, retain=True)

    def connect(self):
        self.client.connect(self.env.get("MQTT_HOST"), int(self.env.get("MQTT_PORT")))

    def publish(self, topic, message):
        result = self.client.publish(topic, message, qos=0, retain=True)
        status = result[0]
        if status != 0:
            logging.error(f"Failed to send MQTT-message to topic {topic}")

    def subscribe(self, topic, on_message):
        self.client.subscribe(topic)
        self.client.on_message = on_message
