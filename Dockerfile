FROM ubuntu16.04

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y

COPY requirments.txt requirments.txt
COPY flaskapp /opt/

RUN pip3 install -r requirments.txt
WORKDIR /opt/

Expose 5000

CMD["gunicorn3", "-b", "0.0.0.0:5000" ,"app:app","--worker=5"]