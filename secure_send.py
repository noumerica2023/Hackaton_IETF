from message_clients.message_sender import RedisClient
from encrypts.kyber_encrypt import KyberEncrypt
from encrypts.aes_encrypt import AESEncrypt
from kyber import Kyber512

class SecureSend:
    def __init__(self, key):
        self.public_key = key
    
    def send(self, data):
         # generating AES key using Kyber challenge, shared key pair. 
        challenge, share_key = KyberEncrypt().generate_challenge_key_pair(self.public_key)

        # use share_key to encypt data
        nonce, tag, ciphertext = AESEncrypt().encrypt(data, share_key)

        # send encrypted data and AES Key to receiver
        RedisClient().send('channel', challenge)
        RedisClient().send('channel', ciphertext)
        RedisClient().send('channel', nonce)
        RedisClient().send('channel', tag)


if __name__ == '__main__':
    pk, sk = Kyber512.keygen()
    print(sk)
    SecureSend(pk).send(b'Hello World')
