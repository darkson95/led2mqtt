# LED2MQTT

This application controls a classic dimmable RGB-LED-Strip via the GPIOs with PWM and adds a light entity in Home Assistant via MQTT-Discovery.

## Docker run

### Building the image

```bash
git clone https://github.com/darkson95/led2mqtt
cd led2mqtt
docker build --tag led2mqtt .
```

### Creating the config

```bash
cp .env.example .env
nano .env # edit the .env file with your configuration
```

### Starting the container

```bash
docker run --env-file ./app/.env --privileged --name led2mqtt led2mqtt
```

## Docker Compose
```bash
git clone https://github.com/darkson95/led2mqtt
cd led2mqtt
cp .env.example .env
nano .env # edit the .env file with your configuration
docker compose up -d
```

## Notice

If you don't want to run the container in privileged mode, have a look at this article: [Docker Access to Raspberry Pi GPIO Pins](https://stackoverflow.com/a/48234752/13391690)
