import redis

class RedisClient():
    def __init__(self):
        super().__init__()
        self.redis = redis.Redis(host='localhost', port=6379)

    def subscribe(self, channel):
        pubsub = self.redis.pubsub()
        pubsub.subscribe(channel)
        for message in pubsub.listen():
            self.handle(message)

    def send(self, channel, message):
        self.redis.publish(channel, message)

    def handle(self, message):
        print(message)
        

if __name__ == '__main__':
    client = RedisClient()
    client.subscribe('channel')