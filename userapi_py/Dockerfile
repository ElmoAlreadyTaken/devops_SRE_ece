FROM python:3.9.12

WORKDIR /src
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 3001
CMD [ "python", "./Client.py" ]

