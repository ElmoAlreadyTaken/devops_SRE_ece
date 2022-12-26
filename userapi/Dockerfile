FROM python:3.8

WORKDIR /src
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 3000
CMD [ "python", "./WebServer.py" , "./Client.py" ]