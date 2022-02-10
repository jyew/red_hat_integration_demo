FROM python:3.7.7-slim
# FROM nemo:latest
# ENV PYTHONUNBUFFERED=1

COPY * /opt/microservices/
COPY requirements.txt /opt/microservices/

COPY requirements.txt requirements.txt

WORKDIR /root

#ENV TRANSFORMERS_CACHE="/root/cache/hf_cache_home" 
ENV HF_HOME="/root/cache/hf_cache_home" 

RUN pip install --upgrade pip \
  && pip install --upgrade pipenv \
  && apt-get clean \
  && apt-get update \
  && apt-get install -y libsndfile1 ffmpeg \
  && apt-get install build-essential -y \
  && apt-get -y install gcc \
  # && apt-get install g++ \
  && pip install --upgrade -r /opt/microservices/requirements.txt

USER 1001

EXPOSE 8080
WORKDIR /opt/microservices/

CMD ["python", "app.py", "8080"]