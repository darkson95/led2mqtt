# coding=utf-8

class Configuration():
    def __init__(self, env):
        self.mqtt.host = self.getConfigEntry(env, "MQTT_PORT", "localhost")
        self.mqtt.port = self.getConfigEntry(env, "MQTT_PORT", "1883")
        self.mqtt.websockets = self.getConfigEntry(env, "MQTT_WEBSOCKETS", "true")
        self.mqtt.username = self.getConfigEntry(env, "MQTT_USERNAME", "")
        self.mqtt.password = self.getConfigEntry(env, "MQTT_PASSWORD", "")
        self.mqtt.topic = self.getConfigEntry(env, "MQTT_TOPIC", "led2mqtt")
        self.mqtt.discovery_topic = self.getConfigEntry(env, "MQTT_DISCOVERY_TOPIC", "homeassistant")
        
        self.ha_device.name = self.getConfigEntry(env, "HA_DEVICE_NAME", "LED Strips")
        self.ha_device.manufacturer = self.getConfigEntry(env, "HA_DEVICE_MANUFACTURER", "LED2MQTT")
        self.ha_device.model = self.getConfigEntry(env, "HA_DEVICE_MODEL", "LED Strips")
        self.ha_device.unique_id = self.getConfigEntry(env, "HA_DEVICE_UNIQUE_ID", "LED2MQTT_LEDSTRIPS")
        
        self.led_gpio.red = self.getConfigEntry(env, "LED_GPIO_RED", "23")
        self.led_gpio.green = self.getConfigEntry(env, "LED_GPIO_GREEN", "24")
        self.led_gpio.blue = self.getConfigEntry(env, "LED_GPIO_BLUE", "25")
        
        self.log_level = self.getConfigEntry(env, "LOG_LEVEL", "INFO")

    def getConfigEntry(self, env, name, default):
        config = env.get(name)
        return config if config else default

    def getVersion(self):
        with open('VERSION') as f:
            version = f.read()
            return version
