import tempfile
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class aes:
    def __init__(self, key: bytes, iv: bytes):
        self.key = key
        self.iv = iv
        self.enc = AES.new(key, AES.MODE_CBC, iv=iv)
        self.dec = AES.new(key, AES.MODE_CBC, iv=iv)

    def encrypt(self, file_to_encrypt: str):
        with open(file_to_encrypt, 'rb') as to_encrypt, tempfile.TemporaryFile() as encrypted_file:
            encrypted_file.write(self.enc.encrypt(
                pad(to_encrypt.read(), AES.block_size)))
            encrypted_file.seek(0)
            to_encrypt.close()
            with open(file_to_encrypt, 'wb') as to_encrypt:
                to_encrypt.write(encrypted_file.read())

    def decrypt(self, file_to_decrypt: str):
        with open(file_to_decrypt, 'rb') as to_decrypt, tempfile.TemporaryFile() as decrypted_file:
            decrypted_file.write(
                unpad(self.dec.decrypt(to_decrypt.read()), AES.block_size))
            decrypted_file.seek(0)
            to_decrypt.close()
            with open(file_to_decrypt, 'wb') as to_decrypt:
                to_decrypt.write(decrypted_file.read())


# if __name__ == '__main__':
#     key = b'6969696969696969'
#     iv = b'4242424242424242'
#     a = aes(key, iv)
#     # a.encrypt('test.txt')
#     # a.encrypt('temp.sha256')
#     a.decrypt('test.txt')
#     a.decrypt('temp.sha256')
