"""
A simple implementation of a Caesar Cipher.

@author GCCIS Faculty
"""

def is_alphabetic(character):
    """
    Returns True if the character is an uppercase letter of the alphabet.
    """
    code = ord(character)
    return code >= 65 and code <= 90

def encrypt_letter(letter, shift=3):
    """
    Encrypts a single letter by shifting it by the specified number of positions
    forward in the alphabet.

    Returns the encrypted letter or an empty string ('') if the argument is not
    an uppercase letter of the alphabet.
    """
    if is_alphabetic(letter):
        code = ord(letter)
        shifted = code + shift
        encrypted = chr(shifted)
        return encrypted
    else:
        return ''
    
def decrypt_letter(letter, shift=3):
    """
    Dedcrypts a single letter by shifting it by the specified number of 
    positions backward in the alphabet.

    Returns the decrypted letter.
    """
    code = ord(letter)
    shifted = code - shift
    decrypted = chr(shifted)
    if is_alphabetic(decrypted):
        return decrypted
    else:
        return ''
    
def encrypt_message(plaintext, shift=3):
    """
    Encrypts an entire plaintext message by encrypting each individual letter
    with the specified shift.

    Returns the ciphertext.
    """
    ciphertext = ''

    for index in range(len(plaintext)):
        letter = encrypt_letter(plaintext[index], shift)
        ciphertext = ciphertext + letter

    return ciphertext

def decrypt_message(ciphertext, shift=3):
    """
    Decrypts an entire ciphertext message by decrypting each individual letter
    with the specified shift.

    Returns the plaintext.
    """
    plaintext = ''

    for letter in ciphertext:
        letter = decrypt_letter(letter, shift)
        plaintext = plaintext + letter

    return plaintext

def main():
    """
    Prompts the user to enter a message. Each word in the original message is 
    encrypted and printed to standard output.
    """
    message = input("enter a message: ")
    tokens = message.split()
    for token in tokens:
        ciphertext = encrypt_message(token)
        print(ciphertext)

if __name__ == "__main__":
    main()