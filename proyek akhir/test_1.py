from Crypto.Cipher import AES, ChaCha20
from Crypto.Util.Padding import pad, unpad
import base64
import os

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)  # Mode CBC
    iv = cipher.iv  # Simpan IV untuk dekripsi nanti
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))  # Padding sebelum enkripsi
    full_ciphertext = base64.b64encode(iv + ciphertext).decode()
    print(f"AES Encryption:\nKey: {key}\nIV: {iv}\nCiphertext: {full_ciphertext}\n")
    return full_ciphertext
    # return base64.b64encode(iv + encrypted_text).decode()
    # iv = os.urandom(16)
    # cipher = AES.new(key, AES.MODE_CBC, iv)
    # ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

def aes_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    iv, encrypted = data[:16], data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size).decode()
    print(f"AES Decryption:\nKey: {key}\nIV: {iv}\nDecrypted: {decrypted}\n")
    return decrypted

def vigenere_encrypt(text, key):
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    encrypted = ''.join(chr((ord(t) + ord(k)) % 256) for t, k in zip(text, key))
    print(f"Vigenere Encryption:\nKey: {key}\nCiphertext: {encrypted.encode()}\n")
    return encrypted

def vigenere_decrypt(text, key):
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    decrypted = ''.join(chr((ord(t) - ord(k)) % 256) for t, k in zip(text, key))
    print(f"Vigenere Decryption:\nKey: {key}\nDecrypted: {decrypted}\n")
    return decrypted

def chacha20_encrypt(plaintext, key):
    nonce = os.urandom(8)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext.encode())
    full_ciphertext = base64.b64encode(nonce + ciphertext).decode()
    print(f"ChaCha20 Encryption:\nKey: {key}\nNonce: {nonce}\nCiphertext: {full_ciphertext}\n")
    return full_ciphertext

def chacha20_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    nonce, encrypted = data[:8], data[8:]
    cipher = ChaCha20.new(key=key, nonce=nonce)
    decrypted = cipher.decrypt(encrypted).decode()
    print(f"ChaCha20 Decryption:\nKey: {key}\nNonce: {nonce}\nDecrypted: {decrypted}\n")
    return decrypted

def encrypt_pipeline(plaintext, aes_key, vigenere_key, chacha_key):
    aes_enc = aes_encrypt(plaintext, aes_key)
    vigenere_enc = vigenere_encrypt(aes_enc, vigenere_key)
    chacha_enc = chacha20_encrypt(vigenere_enc, chacha_key)
    print(f"Final Ciphertext: {chacha_enc}\n")
    return chacha_enc

def decrypt_pipeline(ciphertext, aes_key, vigenere_key, chacha_key):
    chacha_dec = chacha20_decrypt(ciphertext, chacha_key)
    vigenere_dec = vigenere_decrypt(chacha_dec, vigenere_key)
    aes_dec = aes_decrypt(vigenere_dec, aes_key)
    print(f"Final Decrypted: {aes_dec}\n")
    return aes_dec

# Contoh penggunaan
aes_key = b'1234567812345678'
chacha_key = b'12345678123456781234567812345678'
vigenere_key = "secretkey"

plaintext = "Hello, world!"
enc_text = encrypt_pipeline(plaintext, aes_key, vigenere_key, chacha_key)
dec_text = decrypt_pipeline(enc_text, aes_key, vigenere_key, chacha_key)
