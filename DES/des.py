from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

key = b'mysecret'

cipher = DES.new(key, DES.MODE_CBC)

plaintext = b'This is a message'
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
print(binascii.hexlify(ciphertext))
iv = cipher.iv

decrypt_cipher = DES.new(key, DES.MODE_CBC, iv)  # Provide the IV for decryption
original = decrypt_cipher.decrypt(ciphertext)
original = unpad(original, DES.block_size)
print(original.decode())
