FROM python:3.8-alpine

RUN apk add --no-cache git

WORKDIR /model

RUN pip install -U pip wheel
#RUN pip install --no-cache-dir git+https://gitlab.com/hsr-iet/smartwaterproject/swconsumption.git@master

WORKDIR /webservice

RUN pip install Flask
COPY *.py .
ENV FLASK_APP=service.py
# enviroment variable to use as argument
#ENV level ""



EXPOSE 5000

CMD flask run