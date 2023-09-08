ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher_text = 'UHUURBLFR'  # Replace this with your encrypted message
#Hard way to decrypt

def caesar_decrypt(cipher_text, key):
    plain_text = ''
    for c in cipher_text:
        index = ALPHABET.find(c)
        if index != -1:  # Check if the character is in the alphabet
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
        else:
            plain_text = plain_text + c  # Preserve non-alphabet characters

    return plain_text

# Brute-force decryption loop
for key in range(len(ALPHABET)):
    decrypted_text = caesar_decrypt(cipher_text, key)
    print(f"Key {key}: {decrypted_text}")
