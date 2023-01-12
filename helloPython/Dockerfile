FROM python:3

WORKDIR /app
COPY python2.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./python2.py" ]
