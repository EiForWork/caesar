ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!'

def crack_caesar(cipher_text):
    for key in range(len(ALPHABET)):   # Take lenght of alphabet
        plain_text=''
        #make a simple Decrypt

        for c in cipher_text:     
            index = ALPHABET.find(c) # TAKE INDEX POSITION FROM ALPHABET
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]

        print('The %s key is: %s'%(key,plain_text))   #Key from the first LOOP

if __name__ == '__main__':
    encrypt = "ASDGNXSQGMSFT"
    crack_caesar(encrypt)