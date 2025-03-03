from Crypto.Cipher import AES, ChaCha20
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64
import os

def derive_key(user_id):
    print("\n=== Derive Key, Proses hasing untuk Key ===")
    print("User ID:", user_id)
    hashed = hashlib.sha256(user_id.encode()).digest()
    print("Hasil hashing:", hashed)
    aes_key = hashed[:16]  # 16 byte untuk AES
    print(f'Key untuk AES 128: {aes_key}')
    chacha_key = hashed[:32]  # 32 byte untuk ChaCha20
    print(f'Key untuk ChaCha20: {chacha_key}')
    vigenere_key = hashed.hex()[:len(user_id)]  # Panjang sesuai user_id
    print(f'Key untuk Vigenere: {vigenere_key}')
    return aes_key, chacha_key, vigenere_key

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
        
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    final_ciphertext = base64.b64encode(iv + ciphertext).decode()
    
    print(f"\nAES Encryption:\nKey: {key}\nIV: {iv}\nCiphertext: {final_ciphertext}\n")
    return final_ciphertext

def aes_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    
    iv, encrypted = data[:16], data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    final_decrypt = unpad(cipher.decrypt(encrypted), AES.block_size).decode()
    
    print(f"\nAES Decryption:\nKey: {key}\nIV: {iv}\nDecrypted: {final_decrypt}\n")
    return final_decrypt

def vigenere_encrypt(text, key):
    key = (key * (len(text) // len(key) + 1))[:len(text)]  
    ciphertext = ''.join(chr((ord(t) + ord(k)) % 256) for t, k in zip(text, key))
    
    print(f"\nVigenere Encryption:\nKey: {key}\nCiphertext: {ciphertext.encode()}\n")
    return ciphertext

def vigenere_decrypt(text, key):
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    ciphertext = ''.join(chr((ord(t) - ord(k)) % 256) for t, k in zip(text, key))
    
    print(f"\nVigenere Decryption:\nKey: {key}\nDecrypted: {ciphertext}\n")    
    return ciphertext

def chacha20_encrypt(plaintext, key):
    nonce = os.urandom(8)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext.encode())
    final_ciphertext = base64.b64encode(nonce + ciphertext).decode()
    
    print(f"\nChaCha20 Encryption:\nKey: {key}\nNonce: {nonce}\nCiphertext: {final_ciphertext}\n")
    return final_ciphertext

def chacha20_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    nonce, encrypted = data[:8], data[8:]
    cipher = ChaCha20.new(key=key, nonce=nonce)
    final_decrypt = cipher.decrypt(encrypted).decode()
    
    print(f"\nChaCha20 Decryption:\nKey: {key}\nNonce: {nonce}\nDecrypted: {final_decrypt}\n")    
    return final_decrypt

def encrypt_pipeline(plaintext, user_id):
    print("\n=== Encrypt Plaintext ===")
    aes_key, chacha_key, vigenere_key = derive_key(user_id)
    aes_enc = aes_encrypt(plaintext, aes_key)
    vigenere_enc = vigenere_encrypt(aes_enc, vigenere_key)
    chacha_enc = chacha20_encrypt(vigenere_enc, chacha_key)
    return chacha_enc

def decrypt_pipeline(ciphertext, user_id):
    print("\n=== Decrypt Plaintext ===")
    aes_key, chacha_key, vigenere_key = derive_key(user_id)
    chacha_dec = chacha20_decrypt(ciphertext, chacha_key)
    vigenere_dec = vigenere_decrypt(chacha_dec, vigenere_key)
    return aes_decrypt(vigenere_dec, aes_key)

# Contoh penggunaan
user_id = "user12345"
plaintext = "Hello, world!"
enc_text = encrypt_pipeline(plaintext, user_id)
dec_text = decrypt_pipeline(enc_text, user_id)

print("\n=== Hasil Enkripsi dan Dekripsi ===")
print(f"Plaintext: {plaintext}")
print(f"Encrypted: {enc_text}")
print(f"Decrypted: {dec_text}")
