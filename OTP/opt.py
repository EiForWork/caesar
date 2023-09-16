from random import randint
import matplotlib.pyplot as plt
# we need the alphabet because we convert letters into numberical values to be able to use
# mathematical operation
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

# otp encryp
def encrypt(text,key):
    text = text.upper()
    cipher_text = ''

    for index,char in enumerate(text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index)%len(ALPHABET)]
    return cipher_text


def decrypt(cipher_text,key):
    plain = ''
    for index,char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain += ALPHABET[(char_index - key_index)%len(ALPHABET)]
    return plain

def random_sequence(text):
    random = []

    for i in range(len(text)):
        random.append(randint(0,len(ALPHABET)-1))
    return random

def frequency_analysis(text):
    text = text.upper()
    letter_frequency = {}

    for letter in ALPHABET:
        letter_frequency[letter] = 0

    for letter in text:
        if letter in ALPHABET:
            letter_frequency[letter] += 1
    return letter_frequency        
    
def plot_distribution(letter_frequency):
    plt.bar(letter_frequency.keys(),letter_frequency.values())
    plt.show()

if __name__ == '__main__':
    message = 'You are my only one'
    seq = random_sequence(message)
    print("Original Message: %s" % message.upper())
    cipher_text = encrypt(message,seq)
    print("Encrypted message: %s" % cipher_text)
    decrypted_text = decrypt(cipher_text,seq)
    print("Decrypt message: %s"% decrypted_text)
    plot_distribution(frequency_analysis(cipher_text))