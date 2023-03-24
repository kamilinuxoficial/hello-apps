FROM python:3

WORKDIR /app
COPY python2.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./python2.py" ]


#Para ejecutar el hello python hay que descomentar el codigo de abajo y comentar el de arriba
#FROM python:3
#WORKDIR /app
#COPY helloPython.py .
#CMD [ "python", "./helloPython.py" ]