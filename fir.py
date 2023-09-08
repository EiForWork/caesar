ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
KEY = 19

def caesar_encrypt(plain_text):
    cipher_text = ''  # Corrected variable name
    plain_text = plain_text.upper()
    for c in plain_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET) #26 of lenght
        cipher_text = cipher_text + ALPHABET[index]  # Updated variable name
    return cipher_text  # Return the correct variable

def caesar_decrypt(cipher_text):
    plain_text = ''
    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]
    return plain_text

m = 'odeng'
encrypted = caesar_encrypt(m)
print(encrypted,"This message is has encrypted")
print(caesar_decrypt(encrypted), "Already has Decrypted")
