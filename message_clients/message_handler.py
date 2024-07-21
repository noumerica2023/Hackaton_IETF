import redis

class RedisClient():
    def __init__(self):
        creds_provider = redis.UsernamePasswordCredentialProvider("default", "ietfietf")
        self.redis = redis.Redis(host='redis-11699.c241.us-east-1-4.ec2.redns.redis-cloud.com', port= 11699, credential_provider = creds_provider)

        self.handler = lambda x: x

    def subscribe(self, channel):
        pubsub = self.redis.pubsub()
        pubsub.subscribe(channel)
        for message in pubsub.listen():
            self.handle(message)

    def send(self, channel, message):
        self.redis.publish(channel, message)

    def handle(self, message):
        self.handler(message)

    def register_handler(self, handler):
        self.handler = handler


if __name__ == '__main__':
    client = RedisClient()
    client.subscribe('channel')