FROM python:3
LABEL org.opencontainers.image.source="https://github.com/darkson95/led2mqtt"

WORKDIR /usr/local/app
COPY app ./
RUN pip install -r requirements.txt

CMD [ "python", "-u", "." ]
