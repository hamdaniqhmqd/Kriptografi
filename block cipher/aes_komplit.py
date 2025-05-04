from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import base64

def encrypt_cbc(plain_text, password):

    hash_bytes = sha256(password.encode("Windows-1252")).digest()
    key = hash_bytes[:16]
    iv = hash_bytes[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plain_text.encode("Windows-1252"), AES.block_size)

    cipher_text = cipher.encrypt(padded_text)
    return cipher_text

def decrypted_cbc(ciphertext, password):

    hash_bytes = sha256(password.encode("Windows-1252")).digest()
    key = hash_bytes[:16]
    iv = hash_bytes[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)

    unpadded = unpad(decrypted, AES.block_size)
    return unpadded.decode("Windows-1252")

if __name__ == "__main__":
    password = "233307092"
    plaintext = "Ahmad Hamdani"
    print("Key :", password)
    print("Plaintext :", plaintext)

    cipher = encrypt_cbc(plaintext, password)
    b64_cipher = base64.b64encode(cipher).decode("Windows-1252")
    print("Ciphertext :", b64_cipher)
    cipher_bytes = base64.b64decode(b64_cipher)
    decrypted_text = decrypted_cbc(cipher_bytes, password)
    print("Teks hasil dekripsi:", decrypted_text)
