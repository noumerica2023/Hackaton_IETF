from message_clients.message_handler import RedisClient
from encrypts.kyber_encrypt import KyberEncrypt
from encrypts.aes_encrypt import AESEncrypt
from kyber import Kyber512

class SecureReceive:
    def __init__(self, channel):
        self.redis = RedisClient()

        self.pk, self.sk = Kyber512.keygen()
        print (self.pk)

        def handle_message_receipt(data):

            data = data['data']
            if data == 1:
                return

            # split the data into challenge, ciphertext, nonce, tag
            challenge, ciphertext, nonce, tag = data.split(b' ||| ')

            # generate AES key using challenge and shared key pair
            share_key = KyberEncrypt().decrypt(self.sk, challenge)

            # decrypt data using AES key
            decrypted_data = AESEncrypt().decrypt(nonce, tag, ciphertext, share_key)
            print(decrypted_data)


        self.redis.register_handler(handle_message_receipt)
        self.redis.subscribe(channel)


if __name__ == '__main__':
    SecureReceive('channel')
