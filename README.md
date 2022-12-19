# LED2MQTT

This application controls a classic dimmable RGB-LED-Strip via the GPIOs with Pulse-Width-Modulation and adds a light entity in Home Assistant via MQTT-Discovery.

## Docker run

```bash
# edit the environment variables with your configuration
docker run \
  -d \
  -e "MQTT_HOST=" \ # default: localhost
  -e "MQTT_PORT=" \ # default: 1883
  -e "MQTT_WEBSOCKETS=" \ # default: false, options: true, false
  -e "MQTT_USERNAME=" \ # default: empty
  -e "MQTT_PASSWORD=" \ # default: empty
  -e "MQTT_TOPIC=" \ # default: led2mqtt
  -e "MQTT_DISCOVERY_TOPIC=" \ # default: homeassistant
  -e "HA_DEVICE_NAME=" \ # default: LED Strips
  -e "HA_DEVICE_MANUFACTURER=" \ # default: LED2MQTT
  -e "HA_DEVICE_MODEL=" \ # default: LED Strips
  -e "HA_DEVICE_UNIQUE_ID=" \ # default: LED2MQTT_LEDSTRIPS
  -e "LED_GPIO_RED=" \ # default: 23
  -e "LED_GPIO_GREEN=" \ # default: 24
  -e "LED_GPIO_BLUE=" \ # default: 25
  -e "LOG_LEVEL=" \ # default: INFO, options: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
  --device /dev/gpiomem \
  --name led2mqtt \
  ghcr.io/darkson95/led2mqtt:latest
```

## Docker Compose
```bash
wget https://raw.githubusercontent.com/darkson95/led2mqtt/main/docker-compose.yaml
nano docker-compose.yaml # edit the environment variables with your configuration
docker compose up -d
```

## Notice

If you don't want to run the container in privileged mode, have a look at this article: [Docker Access to Raspberry Pi GPIO Pins](https://stackoverflow.com/a/48234752/13391690)
