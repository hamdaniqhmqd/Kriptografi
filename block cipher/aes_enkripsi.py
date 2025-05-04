from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256

def encrypt_cbc(plain_text, password):
    hash_bytes = sha256(password.encode()).digest()
    key = hash_bytes[:16]
    iv = hash_bytes[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plain_text.encode(), AES.block_size)
    cipher_text = cipher.encrypt(padded_text)
    return iv + cipher_text  # tanpa menyisipkan iv

if __name__ == "__main__":
    password = "233307092"
    plaintext = "Ini adalah pesan rahasia."
    cipher = encrypt_cbc(plaintext, password)
    print("Ciphertext (hex):", cipher.hex())
