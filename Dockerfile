FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt --allow-all-external
ADD . /code/
