FROM python:3.9-alpine

#BOTS
COPY bots/reply/ /bots/reply/
COPY bots/utils/ /bots/utils/
COPY bots/config.py /bots/
#ML
COPY ml/    /ml/

#RUN ENVIROMENT
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

#COMMANDS
WORKDIR /bots
CMD ["python3", "reply/reply.py"]