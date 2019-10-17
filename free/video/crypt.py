from binascii import b2a_hex
from binascii import a2b_hex
from base64 import b64encode
from Crypto.Cipher import AES


class Crypt():
    def __init__(self, key):
        self._key = key
        self._mode = AES.MODE_CBC

    def encrypt(self, text):
        if len(text) % 16 != 0:
            text = text + (16 - len(text) % 16)*'0'
        cryptor = AES.new(self._key, self._mode, b'0000000000000000')
        cipher_text = b2a_hex(cryptor.encrypt(text))
        return cipher_text.decode('utf-8')

    def decrypt(self, text):
        cryptor = AES.new(self._key, self._mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        plain_text_strtip = plain_text.decode('utf-8').rstrip('0')
        base64_text = b64encode(plain_text_strtip.encode('utf-8'))
        return base64_text.decode('utf-8')
