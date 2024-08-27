from kafka import KafkaProducer

class KafkaClient:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

    def send_message(self, topic, value):
        self.producer.send(topic, value.encode('utf-8'))

