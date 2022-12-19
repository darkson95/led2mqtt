# LED2MQTT

This application controls a classic dimmable RGB-LED-Strip via the GPIOs with PWM and adds a light entity in Home Assistant via MQTT-Discovery.

## Docker run

```bash
docker run -d \
  -env MQTT_HOST= \ # edit the environment variables with your configuration
  -env MQTT_PORT= \ 
  -env MQTT_WEBSOCKETS= \ 
  -env MQTT_USERNAME= \ 
  -env MQTT_PASSWORD= \ 
  -env MQTT_TOPIC= \ 
  -env MQTT_DISCOVERY_TOPIC= \ 
  -env HA_DEVICE_NAME= \ 
  -env HA_DEVICE_MANUFACTURER= \ 
  -env HA_DEVICE_MODEL= \ 
  -env HA_DEVICE_UNIQUE_ID= \ 
  -env HA_DEVICE_IDENTIFIER= \ 
  -env LED_GPIO_RED= \ 
  -env LED_GPIO_GREEN= \ 
  -env LED_GPIO_BLUE= \ 
  -env LOG_LEVEL=INFO \ 
  --device/dev/gpiomem \
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
