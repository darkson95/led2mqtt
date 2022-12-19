# coding=utf-8
import json
import logging

from Configuration import Configuration
from gpiozero.pins.rpigpio import RPiGPIOFactory
from gpiozero import RGBLED

class LED():
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
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
            if red > 255 or red < 0 or green > 255 or green < 0 or blue > 255 or blue < 0:
                logging.warn(f"Each RGB color component must be between 0 and 255")
                return

            if brightness > 255 or brightness < 0:
                logging.warn(f"Brightness component must be between 0 and 255")
                return

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
        return f"{self.configuration.mqtt.topic}/light/{self.configuration.ha_device.unique_id}/light/config"

    def get_discovery_message(self):
        message = {
            "schema": "json",
            "availability": [
                { "topic": f"{self.configuration.mqtt.topic}/availability" }
            ],
            "device": {
                "identifiers": [
                    self.configuration.ha_device.unique_id
                ],
                "manufacturer": self.configuration.ha_device.manufacturer,
                "model": self.configuration.ha_device.model,
                "name": self.configuration.ha_device.name,
                "sw_version": "LED2MQTT"
            },
            "name": self.configuration.ha_device.name,
            "unique_id": self.configuration.ha_device.unique_id,
            "command_topic": f"{self.configuration.mqtt.topic}/set",
            "json_attributes_topic": self.configuration.mqtt.topic,
            "state_topic": self.configuration.mqtt.topic,
            "brightness_state_topic": self.configuration.mqtt.topic,
            "brightness_value_template ": "{{ value_json.brightness }}",
            "brightness": True,
            "color_mode": True,
            "supported_color_modes": [ "rgb" ]
        }

        return json.dumps(message)
