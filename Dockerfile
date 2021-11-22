FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-dev python3-pip build-essential
RUN mkdir -p /opt/webapp/
ADD requirements.txt /tmp/
ADD webapp.py /opt/webapp
RUN pip install -r /tmp/requirements.txt
WORKDIR /opt/webapp
CMD ["python3", "webapp.py"]
