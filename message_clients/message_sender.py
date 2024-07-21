import redis

class RedisClient():
    def __init__(self):
        creds_provider = redis.UsernamePasswordCredentialProvider("default", "ietfietf")
        self.redis = redis.Redis(host='redis-11699.c241.us-east-1-4.ec2.redns.redis-cloud.com', port= 11699, credential_provider = creds_provider)

    def send(self, channel, message):
        self.redis.publish(channel, message)

    def handle(self, message):
        print(message)
        pass

if __name__ == '__main__':
    client = RedisClient()
    client.send('channel', b'kutckvluyfkufvliyvliyg;iy')
    