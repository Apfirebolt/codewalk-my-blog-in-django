FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN mkdir /codewalk
WORKDIR /codewalk

RUN pip install --upgrade pip
COPY requirements.txt /codewalk/
RUN pip install -r requirements.txt

COPY . /codewalk/