FROM python:3.8-alpine

RUN apk add --no-cache git

WORKDIR /model

COPY model-mockup/*.py .
#RUN pip install -U pip wheel
#RUN pip install --no-cache-dir git+https://gitlab.com/hsr-iet/smartwaterproject/swconsumption.git@master

WORKDIR /webservice
COPY *.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["service.py"]