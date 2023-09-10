ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()

    cipher_text = ''
    key_index = 0

    for character in plain_text:
        if character in ALPHABET:
            index = (ALPHABET.find(character) + ALPHABET.find(key[key_index])) % len(ALPHABET)
            cipher_text = cipher_text + ALPHABET[index]
            key_index = (key_index + 1) % len(key)
        else:
            # If the character is not in the alphabet, leave it unchanged
            cipher_text = cipher_text + character

    return cipher_text

def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    plain_text = ''
    key_index = 0

    for character in cipher_text:
        if character in ALPHABET:
            index = (ALPHABET.find(character) - ALPHABET.find(key[key_index])) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
            key_index = (key_index + 1) % len(key)
        else:
            # If the character is not in the alphabet, leave it unchanged
            plain_text = plain_text + character

    return plain_text

if __name__ == '__main__':
    text = 'CRYPTOGRAPHY IS EZ'
    key = 'ILOVEYOU'
    encrypted_text = vigenere_encrypt(text, key)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)
