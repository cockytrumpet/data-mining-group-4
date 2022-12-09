FROM python:3.11-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
COPY python-docker/ /python-docker/
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "waitress-serve", "app:app" ]

