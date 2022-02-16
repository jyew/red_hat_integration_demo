FROM python:3.7.7-slim

COPY * /opt/microservices/
COPY requirements.txt /opt/microservices/
COPY requirements.txt requirements.txt

ENV TRANSFORMERS_CACHE="/opt/cache/tf_cache_home" 

WORKDIR /opt/microservices/

RUN apt-get clean \
  && apt-get update \
  && apt-get install build-essential -y \
  && apt-get -y install libsndfile1 \
  && apt-get -y install libsndfile1-dev \
  && apt-get -y install ffmpeg \
  && apt-get -y install gcc \
  && apt-get -y install wget unzip && rm -rf /var/cache/apk/* \
  && wget https://jyewbucket.s3.ap-southeast-1.amazonaws.com/model_repository.zip \
  && unzip model_repository.zip -d model_repository \
  && rm model_repository.zip \
  && mkdir -p /opt/cache/tf_cache_home \
  && mkdir -p /opt/cache/nemo_nlp_tmp \
  && pip install --upgrade pip \
  && pip install --upgrade pipenv \
  && pip install --upgrade -r /opt/microservices/requirements.txt \
  && chown 1001:1001 -R /opt/cache \ 
  && chmod -R 777 /opt/cache 

USER 1001

EXPOSE 8000

CMD ["python", "app.py", "8000"]