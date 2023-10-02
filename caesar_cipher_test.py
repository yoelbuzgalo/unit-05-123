from caesar_cipher import *

def test_encrypt_letter():
    # setup
    plaintext = "A"
    shift = 3
    expected = "D"

    # invoke
    actual = encrypt_letter(plaintext, shift)

    # analyze
    assert expected == actual


def test_encrypt_message():
    # setup
    plaintext = "HELLO"
    expected = "KHOOR"

    # invoke
    actual = encrypt_message(plaintext)

    # analyze
    assert expected == actual


def test_decrypt_message():
    # setup
    plaintext = "ROOHK"
    expected = "OLLEH"

    # invoke
    actual = decrypt_message(plaintext)

    # analyze
    assert expected == actual