# LED2MQTT

This application controls a classic dimmable RGB-LED-Strip via the GPIOs with PWM and adds a light entity in Home Assistant via MQTT-Discovery.

## Docker run

```bash
docker run \
  -d \
  -e "MQTT_HOST=" \ # edit the environment variables with your configuration
  -e "MQTT_PORT=" \ 
  -e "MQTT_WEBSOCKETS=" \ 
  -e "MQTT_USERNAME=" \ 
  -e "MQTT_PASSWORD=" \ 
  -e "MQTT_TOPIC=" \ 
  -e "MQTT_DISCOVERY_TOPIC=" \ 
  -e "HA_DEVICE_NAME=" \ 
  -e "HA_DEVICE_MANUFACTURER=" \ 
  -e "HA_DEVICE_MODEL=" \ 
  -e "HA_DEVICE_UNIQUE_ID=" \ 
  -e "HA_DEVICE_IDENTIFIER=" \ 
  -e "LED_GPIO_RED=" \ 
  -e "LED_GPIO_GREEN=" \ 
  -e "LED_GPIO_BLUE=" \ 
  -e "LOG_LEVEL=INFO" \ 
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
