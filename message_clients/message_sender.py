import redis

class RedisClient():
    def __init__(self):
        super().__init__()
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def send(self, channel, message):
        self.redis.publish(channel, message)

    def handle(self, message):
        print(message)
        pass

if __name__ == '__main__':
    client = RedisClient()
    client.send('channel', b'kutckvluyfkufvliyvliyg;iy')
    