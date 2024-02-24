FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

RUN pip install -r /tmp/requirements.txt
