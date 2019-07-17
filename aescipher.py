import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

from Crypto.Cipher import AES
import base64
import sys
import os

KEY = 'f64d844827e34eeebb81bce153290305'

def pad(byte_array):
    BLOCK_SIZE = 16
    pad_len = BLOCK_SIZE - len(byte_array) % BLOCK_SIZE
    return byte_array + (bytes([pad_len]) * pad_len)

def unpad(byte_array):
    last_byte = byte_array[-1]
    return byte_array[0:-last_byte]

def encrypt(message):
    """
    Input String, return base64 encoded encrypted String
    """

    byte_array = message.encode("UTF-8")

    padded = pad(byte_array)

    iv = os.urandom(AES.block_size)
    cipher = AES.new( KEY.encode("UTF-8"), AES.MODE_CBC, iv )
    encrypted = cipher.encrypt(padded)

    return base64.b64encode(iv+encrypted).decode("UTF-8")

def decrypt(message):
    """
    Input encrypted bytes, return decrypted bytes, using iv and KEY
    """

    byte_array = base64.b64decode(message)

    iv = byte_array[0:16]
    messagebytes = byte_array[16:]
    cipher = AES.new(KEY.encode("UTF-8"), AES.MODE_CBC, iv )
    decrypted_padded = cipher.decrypt(messagebytes)
    decrypted = unpad(decrypted_padded)

    return decrypted.decode("UTF-8");

if __name__== "__main__":
    v = 'vinicius'
    v1 = encrypt(v)
    v2 = encrypt(v)
    print(v1)
    print(v2)
    print(decrypt(v1))
    print(decrypt(v2))
