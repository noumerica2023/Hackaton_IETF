from Crypto.Cipher import AES
from kyber import Kyber512


class KyberEncrypt:
    def generate_challenge_key_pair(self, public_key):
        return Kyber512.enc(public_key)
    
    def decrypt(self, private_key, ciphertext):
        return Kyber512.dec(ciphertext, private_key)

    def generate_keypair(self):
        return Kyber512.generate_keypair()
