from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import base64

def encrypt_cbc(plain_text, password):
    print("=== ENKRIPSI ===")
    print(f"\nPlaintext asli: {plain_text}")
    print(f"Plaintext (bytes): {plain_text.encode('Windows-1252')}")
    print(f"Panjang Plaintext (bytes): {len(plain_text.encode('Windows-1252'))}")
    print(f"\nPassword: {password}")
    print(f"Password (bytes): {password.encode('Windows-1252')}")
    print(f"Panjang Password (bytes): {len(password.encode('Windows-1252'))}")

    hash_bytes = sha256(password.encode("Windows-1252")).digest()
    key = hash_bytes[:16]
    iv = hash_bytes[16:]
    print(f"\nHash SHA-256: {hash_bytes.decode("Windows-1252")}")
    print(f"Panjang Hash SHA-256: {len(hash_bytes.decode("Windows-1252"))}")
    print(f"\nKey (16 byte): {key.decode("Windows-1252")}")
    print(f"Panjang Key (16 byte): {len(key.decode("Windows-1252"))}")
    print(f"\nIV  (16 byte): {iv.decode("Windows-1252")}")
    print(f"Panjang IV  (16 byte): {len(iv.decode("Windows-1252"))}")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plain_text.encode("Windows-1252"), AES.block_size)
    print(f"\nPlaintext setelah padding: {padded_text}")
    print(f"Panjang Plaintext setelah padding: {len(padded_text)}")

    cipher_text = cipher.encrypt(padded_text)
    print(f"\nCiphertext (bytes): {cipher_text}")
    print(f"Panjang Ciphertext (bytes): {len(cipher_text)}")
    return cipher_text

def decrypt_cbc(ciphertext, password):
    print("\n=== DEKRIPSI ===")

    b64_cipher = base64.b64encode(ciphertext).decode("Windows-1252")

    print(f"\nCiphertext (bytes): {b64_cipher}")
    print(f"Panjang Ciphertext (bytes): {len(b64_cipher)}")
    print(f"\nPassword: {password}")
    print(f"Password (bytes): {password.encode('Windows-1252')}")
    print(f"Panjang Password (bytes): {len(password.encode('Windows-1252'))}")

    hash_bytes = sha256(password.encode("Windows-1252")).digest()
    key = hash_bytes[:16]
    iv = hash_bytes[16:]
    print(f"\nHash SHA-256: {hash_bytes.decode("Windows-1252")}")
    print(f"Panjang Hash SHA-256: {len(hash_bytes.decode("Windows-1252"))}")
    print(f"\nKey (16 byte): {key.decode("Windows-1252")}")
    print(f"Panjang Key (16 byte): {len(key.decode("Windows-1252"))}")
    print(f"\nIV  (16 byte): {iv.decode("Windows-1252")}")
    print(f"Panjang IV  (16 byte): {len(iv.decode("Windows-1252"))}")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    print(f"\nPlaintext setelah dekripsi (masih terpadding): {decrypted}")

    unpadded = unpad(decrypted, AES.block_size)
    print(f"Plaintext setelah unpadding: {unpadded}")
    return unpadded.decode("Windows-1252")

if __name__ == "__main__":
    password = "233307092"
    plaintext = "Ahmad Hamdani"

    # Enkripsi dan ubah ke Base64
    cipher = encrypt_cbc(plaintext, password)
    b64_cipher = base64.b64encode(cipher).decode("Windows-1252")
    print("\nCiphertext (Base64):", b64_cipher)
    print("Panjang Ciphertext (Base64):", len(b64_cipher))

    # Dekripsi dari Base64
    cipher_bytes = base64.b64decode(b64_cipher)
    decrypted_text = decrypt_cbc(cipher_bytes, password)
    print("\nTeks hasil dekripsi:", decrypted_text)
    print("Panjang Teks hasil dekripsi:", len(decrypted_text))
