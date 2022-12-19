# coding=utf-8
import json
import logging

from Configuration import Configuration
from LED import LED
from MQTTClient import MQTTClient

class LED2MQTT():
    def __init__(self):
        self.configuration = Configuration()
        self.led = LED(self.configuration)
        self.mqtt_client = MQTTClient(self.configuration)
        
        log_level = self.configuration.log_level
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError("Invalid log level: {log_level}")

        logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s - %(message)s')

    def run(self):
        logging.info(f"=-=-=-=-=-=-=-=-=-=-=-=-=")
        logging.info(f"LED2MQTT - Version {self.configuration.getVersion()}")
        logging.info(f"=-=-=-=-=-=-=-=-=-=-=-=-=")

        self.mqtt_client.connect()
        self.mqtt_client.subscribe(f"{self.configuration.mqtt_topic}/set", self.on_message)

        discovery_topic = self.led.get_discovery_topic()
        discovery_message = self.led.get_discovery_message()
        self.mqtt_client.publish(discovery_topic, discovery_message)
        logging.info("Send Discovery-Message: %s", discovery_message)

        self.led.init_rgb(self.configuration.led_gpio_red, self.configuration.led_gpio_green, self.configuration.led_gpio_blue)
        
        state_message = self.led.get_state_message()
        self.mqtt_client.publish(self.configuration.mqtt_topic, state_message)

        self.mqtt_client.client.loop_forever()

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode("utf-8"))

        logging.info(f"Command-Message received: {str(payload)}")

        if "state" in payload:
            power = payload["state"] == "ON"
            red = None if "color" not in payload or "r" not in payload["color"] else int(payload["color"]["r"])
            green = None if "color" not in payload or "g" not in payload["color"] else int(payload["color"]["g"])
            blue = None if "color" not in payload or "b" not in payload["color"] else int(payload["color"]["b"])
            brightness = None if "brightness" not in payload else int(payload["brightness"])

            self.led.update_rgb(power, brightness, red, green, blue)

        state_message = self.led.get_state_message()
        self.mqtt_client.publish(self.configuration.mqtt_topic, state_message)


if __name__ == '__main__':
    led2mqtt = LED2MQTT()
    led2mqtt.run()
