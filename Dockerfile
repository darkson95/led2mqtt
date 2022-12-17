FROM python:3

WORKDIR /usr/local/app
COPY app ./
RUN pip install -r requirements.txt

CMD [ "python", "-u", "." ]
