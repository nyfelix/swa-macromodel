FROM python:3.8-alpine

WORKDIR /model

RUN pip install -U pip wheel
# RUN pip install --no-cache-dir git+https://gitlab.com/hsr-iet/smartwaterproject/swconsumption.git@master
# use stable release
#RUN pip install --no-cache-dir git+https://gitlab.com/hsr-phai/phai-contest.git@stable

COPY *.py .
# enviroment variable to use as argument
#ENV level ""

CMD \
#python -c "import phaicontest; print(f'** Contest version: {phaicontest.__version__}')"; \
python /model/skript.py

