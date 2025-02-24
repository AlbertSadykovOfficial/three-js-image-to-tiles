FROM python:3.12.9-alpine3.21
WORKDIR /app
COPY app/requirements/requirements.txt requirements.txt
RUN pip install -r requirements.txt