FROM python:3.11
RUN mkdir /sulusai
WORKDIR /sulusai


ENV PYTHONBUFFERED 1

COPY ./requirements.txt /sulusai/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /sulusai

CMD python manage.py migrate && python manage.py loaddata fixtures/dump.json && python manage.py runserver 0.0.0.0:8000
