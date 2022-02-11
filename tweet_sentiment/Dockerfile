FROM python:3.7.7-slim

COPY * /opt/microservices/
COPY requirements.txt /opt/microservices/
COPY requirements.txt requirements.txt

# RUN mkdir -p /opt/cache/tf_cache_home
# RUN mkdir -p /opt/cache/nemo_nlp_tmp

ENV TRANSFORMERS_CACHE="/opt/cache/tf_cache_home" 

# RUN curl <file_download_url> -O <copy_directory> \
# && unzip <copy_directory>/<filename>.zip -d <copy_directory> \
# && rm <copy_directory>/<filename>.zip
WORKDIR /opt/microservices/

RUN wget https://jyewbucket.s3.ap-southeast-1.amazonaws.com/model_repository.zip \
  && unzip model_repository.zip -d model_repository \
  && rm model_repository.zip \
  && mkdir -p /opt/cache/tf_cache_home \
  && mkdir -p /opt/cache/nemo_nlp_tmp \
  && pip install --upgrade pip \
  && pip install --upgrade pipenv \
  && apt-get clean \
  && apt-get update \
  && apt-get install -y libsndfile1 ffmpeg \
  && apt-get install build-essential -y \
  && apt-get -y install gcc \
  && pip install --upgrade -r /opt/microservices/requirements.txt

USER 1001

EXPOSE 8000

CMD ["python", "app.py", "8000"]