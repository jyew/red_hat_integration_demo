FROM python:3.7.7-slim

COPY * /opt/microservices/
COPY requirements.txt /opt/microservices/
COPY requirements.txt requirements.txt

RUN mkdir -p /opt/cache/tf_cache_home
RUN mkdir -p /opt/cache/nemo_nlp_tmp

ENV TRANSFORMERS_CACHE="/opt/cache/tf_cache_home" 

RUN pip install --upgrade pip \
  && pip install --upgrade pipenv \
  && apt-get clean \
  && apt-get update \
  && apt-get install -y libsndfile1 ffmpeg \
  && apt-get install build-essential -y \
  && apt-get -y install gcc \
  && pip install --upgrade -r /opt/microservices/requirements.txt

USER 1001

EXPOSE 8000
WORKDIR /opt/microservices/

CMD ["python", "app.py", "8000"]