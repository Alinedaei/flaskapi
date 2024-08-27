import redis

class RedisClient:
    def __init__(self):
        self.client = redis.Redis(host='redis', port=6379, db=0)

    def get_value(self, key):
        return self.client.get(key)

    def set_value(self, key, value):
        self.client.set(key, value)

