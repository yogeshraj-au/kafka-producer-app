from kafka import KafkaProducer
import time
import psutil
import json
import logging

logging.basicConfig(level=logging.DEBUG)

bootstrap_servers = 'kafka:9092'
topic_name = 'logs'

def collect_metrics():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    metrics = {
        'cpu_percent': cpu_percent,
        'memory_percent': memory_percent,
        'disk_usage': disk_usage
    }
    return metrics

def send_metrics(producer):
    metrics = collect_metrics()
    message = json.dumps(metrics).encode()
    producer.send(topic_name, value=message)
    producer.flush()

if __name__ == '__main__':
    # Kafka producer configuration
    config = {'bootstrap_servers': bootstrap_servers}

    # Create Kafka producer
    producer = KafkaProducer(**config)

    try:
        while True:
            send_metrics(producer)
            time.sleep(10)  # Sleep for 10 seconds before sending the next metrics

    except KeyboardInterrupt:
        pass

    finally:
        producer.flush()
        producer.close()
