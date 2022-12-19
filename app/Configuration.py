# coding=utf-8
import logging
from os import path, environ as env

class Configuration():
    def __init__(self):
        self.mqtt_host = self.getConfigEntry("MQTT_PORT", "localhost")
        self.mqtt_port = self.getConfigEntry("MQTT_PORT", "1883")
        self.mqtt_websockets = self.getConfigEntry("MQTT_WEBSOCKETS", "true")
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
        logging.debug(f"Got config-entry from env: {name} = {config} (default: {default})")

        return config if config else default

    def getVersion(self):
        basedir = path.abspath(path.dirname(__file__))
        with open(path.join(basedir, 'VERSION')) as f:
            version = f.read()
            return version
