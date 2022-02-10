FROM python:3.7.7-slim

# ENV PYTHONUNBUFFERED=1

COPY * /opt/microservices/
COPY requirements.txt /opt/microservices/

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
  && pip install --upgrade pipenv \
  && apt-get clean \
  && apt-get update \
  && pip install --upgrade -r /opt/microservices/requirements.txt

USER 1001

EXPOSE 8080
WORKDIR /opt/microservices/

CMD ["python", "app.py", "8080"]