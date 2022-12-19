# coding=utf-8
import json
import logging
from os import path, environ as env

class Configuration():
    def __init__(self):
        self.mqtt_host = self.getConfigEntry("MQTT_HOST", "localhost")
        self.mqtt_port = self.getConfigEntry("MQTT_PORT", "1883")
        self.mqtt_websockets = self.getConfigEntry("MQTT_WEBSOCKETS", "false")
        self.mqtt_username = self.getConfigEntry("MQTT_USERNAME", "")
        self.mqtt_password = self.getConfigEntry("MQTT_PASSWORD", "")
        self.mqtt_topic = self.getConfigEntry("MQTT_TOPIC", "led2mqtt")
        self.mqtt_discovery_topic = self.getConfigEntry("MQTT_DISCOVERY_TOPIC", "homeassistant")

        self.ha_device_name = self.getConfigEntry("HA_DEVICE_NAME", "LED Strips")
        self.ha_device_manufacturer = self.getConfigEntry("HA_DEVICE_MANUFACTURER", "LED2MQTT")
        self.ha_device_model = self.getConfigEntry("HA_DEVICE_MODEL", "LED Strips")
        self.ha_device_unique_id = self.getConfigEntry("HA_DEVICE_UNIQUE_ID", "LED2MQTT_LEDSTRIPS")

        self.led_gpio_red = self.getConfigEntry("LED_GPIO_RED", "23")
        self.led_gpio_green = self.getConfigEntry("LED_GPIO_GREEN", "24")
        self.led_gpio_blue = self.getConfigEntry("LED_GPIO_BLUE", "25")
        
        self.log_level = self.getConfigEntry("LOG_LEVEL", "INFO")

    def getConfigEntry(self, name, default):
        config = env.get(name)
        return config if config else default

    def getVersion(self):
        basedir = path.abspath(path.dirname(__file__))
        with open(path.join(basedir, 'VERSION')) as f:
            version = f.read()
            return version.strip()

    def print(self):
        logging.debug(f"Configuration mqtt_host: {self.mqtt_host}")
        logging.debug(f"Configuration mqtt_port: {self.mqtt_port}")
        logging.debug(f"Configuration mqtt_websockets: {self.mqtt_websockets}")
        logging.debug(f"Configuration mqtt_username: {self.mqtt_username}")
        logging.debug(f"Configuration mqtt_password: {self.mqtt_password}")
        logging.debug(f"Configuration mqtt_topic: {self.mqtt_topic}")
        logging.debug(f"Configuration mqtt_discovery_topic: {self.mqtt_discovery_topic}")
        logging.debug(f"Configuration ha_device_name: {self.ha_device_name}")
        logging.debug(f"Configuration ha_device_manufacturer: {self.ha_device_manufacturer}")
        logging.debug(f"Configuration ha_device_model: {self.ha_device_model}")
        logging.debug(f"Configuration ha_device_unique_id: {self.ha_device_unique_id}")
        logging.debug(f"Configuration led_gpio_red: {self.led_gpio_red}")
        logging.debug(f"Configuration led_gpio_green: {self.led_gpio_green}")
        logging.debug(f"Configuration led_gpio_blue: {self.led_gpio_blue}")
        logging.debug(f"Configuration log_level: {self.log_level}")
