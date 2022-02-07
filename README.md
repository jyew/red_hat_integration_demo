# Red Hat Integration Suite Demo with Twitter and Nvidia Triton Sentiment Model

Pre-requisite: You must have an OpenShift Container Platform with sufficient administrative rights to install operators, create projects and configure workloads. The following demo is based on Openshift 4.8.

Red Hat Integration is a comprehensive set of integration and messaging technologies to connect applications and data across hybrid infrastructures. 

It is an agile, distributed, containerized and API-centric solution. 

It provides service composition and orchestration, application connectivity and data transformation, real-time message streaming, change data capture, and API management—all combined with a cloud-native platform and toolchain to support the full spectrum of modern application development.

This repo is with reference to https://github.com/ksingh7/twitter_streaming_app_on_openshift_OCS with some updated codes and modification. 

## Instruction

### Deploy Kafka / AMQ Streams Messaging Service 

1. Install AMQ Streams Operator

Under **Administrator** view, click Operators -> OperatorHub -> Red Hat Integration - AMQ Streams -> Install

Next, select installation mode to be on a specific namespace and create new namespace called "amq-streams". It will take roughly a min to finish installation.

When it is done, click "View Operator". You should see a page which you can manage your Kafka usage.

2. Create a Kafka cluster

Inside the operator, click "Create kafka". For simplicity, you can keep all default configuration the same. Let's name it as "my-cluster". 

3. Create a Kafka topic

Inside the operator, click "Kafka topic" -> "Create kafkaTopic". Name the topic as "tweets".

### Deploy a MongoDB service on openshift





### Deploy Triton Sentiment Inference Service



### Deploy Python Backend Flask API service




### Deploy Frontend Service


### 3scale to protect API


### (Optional) Deploy Fuse Online




