FROM python:3.11

RUN mkdir -p /home/app

COPY ./main.py /home/main.py

# set default dir so that next commands executes in /home/app dir
WORKDIR /home

# will execute npm install in /home/app because of WORKDIR
RUN pip install fastapi

RUN pip install uvicorn

RUN pip install prometheus-fastapi-instrumentator

# no need for /home/app/server.js because of WORKDIR
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["uvicorn", "main:app", "--reload"]
