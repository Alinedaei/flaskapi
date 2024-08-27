from flask_restful import Resource
from app.redis_client import RedisClient
from app.kafka_client import KafkaClient

redis_client = RedisClient()
kafka_client = KafkaClient()

class MyResource(Resource):
    def get(self):
        # مثال ساده برای دریافت داده‌ها از Redis
        value = redis_client.get_value('mykey')
        return {'value': value}, 200

    def post(self):
        # ارسال داده به Kafka
        kafka_client.send_message('mytopic', 'Hello Kafka!')
        return {'message': 'Message sent to Kafka'}, 201

