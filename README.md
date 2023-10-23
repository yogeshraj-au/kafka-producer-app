# kafka-producer-app

This repo contains a python script which will send the host metrics such as cpu, memory and disk usage every 10s to a kafka topic. 

[Docker image repo](https://hub.docker.com/repository/docker/imageimpressario/kafka-host-metrics)

Use the below command to run the app:

```
docker run --name kafka-host-metrics imageimpressario/kafka-host-metrics
```
