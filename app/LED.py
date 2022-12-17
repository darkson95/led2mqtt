# coding=utf-8
import json
import logging

from gpiozero.pins.rpigpio import RPiGPIOFactory
from gpiozero import RGBLED

class LED():
    def __init__(self, env):
        self.env = env
        self.pin_factory = RPiGPIOFactory()
        self.led = None

        self.power = False
        self.brightness = 255
        self.red = 255
        self.green = 255
        self.blue = 255

    def init_rgb(self, red_pin, grn_pin, blu_pin):
        try:
            self.deinit_rgb()
            self.led = RGBLED(red=red_pin, green=grn_pin, blue=blu_pin, active_high=True, pin_factory=self.pin_factory)
            logging.debug(f"LEDs initialized with pin factory: {str(self.led.pin_factory)}")
        except:
            logging.error("Error occurred while initializing LEDs")

    def update_rgb(self, power, brightness, red, green, blue):
        if(self.led is not None):
            self.power = power

            if brightness != None:
                self.brightness = brightness
            if red != None:
                self.red = red
            if green != None:
                self.green = green
            if blue != None:
                self.blue = blue

            red = (self.red / 255) * (self.brightness / 255) if self.power else 0
            green = (self.green / 255) * (self.brightness / 255) if self.power else 0
            blue = (self.blue / 255) * (self.brightness / 255) if self.power else 0

            logging.debug(f"Set LED to rgb({red:.2f}, {green:.2f}, {blue:.2f})")
            self.led.color = (red, green, blue)
        else:
            logging.error("Error occurred while updating RGB state")

    def deinit_rgb(self):
        try:
            if(self.led is not None):
                self.led.close()
                self.led = None
                logging.debug("LEDs deinitialized")
        except:
            logging.error("Error occurred while deinitializing LEDs")

    def get_state_message(self):
        message = {
            "brightness": self.brightness,
            "color": {
                "r": self.red,
                "g": self.green,
                "b": self.blue,
            },
            "color_mode": "rgb",
            "state": "ON" if self.power else "OFF"
        }

        logging.info(f"State Message: {str(message)}")

        return json.dumps(message)

    def get_discovery_topic(self):
        return self.env.get("MQTT_DISCOVERY_TOPIC") + "/light/" + self.env.get("HA_DEVICE_UNIQUE_ID") + "/light/config"

    def get_discovery_message(self):
        message = {
            "schema": "json",
            "availability": [
                { "topic": self.env.get("MQTT_TOPIC") + "/availability" }
            ],
            "device": {
                "identifiers": [
                    self.env.get("HA_DEVICE_UNIQUE_ID")
                ],
                "manufacturer": self.env.get("HA_DEVICE_MANUFACTURER"),
                "model": self.env.get("HA_DEVICE_MODEL"),
                "name": self.env.get("HA_DEVICE_NAME"),
                "sw_version": "LED2MQTT"
            },
            "name": self.env.get("HA_DEVICE_NAME"),
            "unique_id": self.env.get("HA_DEVICE_UNIQUE_ID"),
            "command_topic": self.env.get("MQTT_TOPIC") + "/set",
            "json_attributes_topic": self.env.get("MQTT_TOPIC"),
            "state_topic": self.env.get("MQTT_TOPIC"),
            "brightness_state_topic": self.env.get("MQTT_TOPIC"),
            "brightness_value_template ": "{{ value_json.brightness }}",
            "brightness": True,
            "color_mode": True,
            "supported_color_modes": [ "rgb" ]
        }

        return json.dumps(message)
