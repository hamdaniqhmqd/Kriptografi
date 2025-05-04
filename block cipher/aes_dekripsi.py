from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha256
from binascii import unhexlify

def decrypt_cbc(ciphertext, password):
    hash_bytes = sha256(password.encode()).digest()
    key = hash_bytes[:16]
    iv = ciphertext[:16]
    cipher_text = ciphertext[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(cipher_text)
    return unpad(decrypted, AES.block_size).decode()

if __name__ == "__main__":
    password = "233307092"
    hex_ciphertext = "dfc10b1706d44614427ba587d13ee725fc6c550c4d35bce856619723d73399248dce477e1002415f35993590ab09aead"  # isi dari hasil enkripsi (dalam hex)
    ciphertext = unhexlify(hex_ciphertext)

    plaintext = decrypt_cbc(ciphertext, password)
    print("Teks hasil dekripsi:", plaintext)
