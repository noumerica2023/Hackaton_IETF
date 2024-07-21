from Crypto.Cipher import AES
from kyber import Kyber512

class AESEncrypt:
    def encrypt(self, data, key):
        cipher = AES.new(key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return cipher.nonce, tag, ciphertext

    def decrypt(self, nonce, tag, ciphertext, key):
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_data
