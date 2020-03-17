FROM ubuntu:16.04

MAINTAINER keerthi "kr583413@dal.ca"

RUN apt-get update && \
    apt-get install -y python-pip python-dev

COPY ./requirments.txt  /app/requirements.txt
WORKDIR  /app
RUN  pip install -r requirements.txt
COPY . /app

Expose 5000

CMD ["python", "/src/app.py"]