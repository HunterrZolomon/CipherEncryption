import math,pyperclip


def reverse_encrypt(message):
    translated = ''
    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    return translated

def reverse_decrypt(message):
    return message[::-1]

key = 'abcdefghijklmnopqrstuvwxyz'
def caesar_encrypt(text):
    s = 4
    result = ''
    for l in text.lower():
        try:
            i = (key.index(l) + s) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

def caesar_decrypt(text):
    s = 4
    result = ''
    for l in text :
        try:
            i = (key.index(l) - s) % 26
            result += key[i]
        except ValueError :
            result += l
    return result

def rot_encrypt(text) :
    s = 13
    result = ''
    for l in text.lower():
        try:
            i = (key.index(l) + s) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()


def rot_decrypt(text):
    s = 13
    result = ''
    for l in text :
        try:
            i = (key.index(l) - s) % 26
            result += key[i]
        except ValueError :
            result += l
    return result

def transposition_encrypt(message):
    key = 6
    ciphertext = [''] * key
    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext) #Cipher text

def transposition_decrypt(message):
    key = 6
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = ['']* numOfColumns
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0 
            row += 1 
    return ''.join(plaintext)

#file_name = input("Enter filename for encryption : ")
#file_name = "test.txt"
#f = open(file_name, "r")
#print("1.Reverse Cipher Encryption")
#print("2.Caesar Cipher Excryption")
#print("3.ROT13 Algorithm")
#print("4.Transposition Cipher Encryption")
#choice = input("\nEnter the choice of encryption: ")

#message = f.readline()


#r_encrypt = reverse_encrypt(message)
#print("Reverse Cipher: ",r_encrypt)
#print("Decrypt Rev Cipher : ",reverse_decrypt(r_encrypt))


#s = 4
#c_encrypt = caesar_encrypt(message,s)
#print("\nCaesar Cipher : ",c_encrypt)
#print("Decrypt caesar : ",caesar_decrypt(c_encrypt,s))
#print(f.readline())

#ROT13 is just Caesar where shift = 13
#rot = 13
#rot_encrypt = caesar_encrypt(message,rot)
#print("\nROT13 Cipher : ",rot_encrypt)
#print("Decrypt ROT13 : ",caesar_decrypt(rot_encrypt,rot))

#t_encrypt = transposition_encrypt(message)
#print("\nTransposition Cipher : ",t_encrypt)
#print("Decrypt Transposition : ",transposition_decrypt(t_encrypt))

#f.close()
