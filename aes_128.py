from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Fungsi enkripsi
def encrypt_AES(text, key):
    cipher = AES.new(key, AES.MODE_CBC)  # Mode CBC
    iv = cipher.iv  # Simpan IV untuk dekripsi nanti
    encrypted_text = cipher.encrypt(pad(text.encode(), AES.block_size))  # Padding sebelum enkripsi
    return base64.b64encode(iv + encrypted_text).decode()

# Fungsi dekripsi
def decrypt_AES(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)  # Decode dari base64
    iv = encrypted_text[:AES.block_size]  # Ambil IV dari awal blok
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode()

# Pilih salah satu key sesuai dengan varian AES
key_128 = b'1234567890abcdef'       # 16 byte untuk AES-128
key_192 = b'1234567890abcdef12345678'  # 24 byte untuk AES-192
key_256 = b'1234567890abcdef1234567890abcdef'  # 32 byte untuk AES-256

# Pesan yang akan dienkripsi
plain_text = "Data sangat rahasia!"

# Uji dengan AES-128
encrypted_128 = encrypt_AES(plain_text, key_128)
decrypted_128 = decrypt_AES(encrypted_128, key_128)
print(f"AES-128 Enkripsi: {encrypted_128}")
print(f"AES-128 Dekripsi: {decrypted_128}")

# Uji dengan AES-192
encrypted_192 = encrypt_AES(plain_text, key_192)
decrypted_192 = decrypt_AES(encrypted_192, key_192)
print(f"AES-192 Enkripsi: {encrypted_192}")
print(f"AES-192 Dekripsi: {decrypted_192}")

# Uji dengan AES-256
encrypted_256 = encrypt_AES(plain_text, key_256)
decrypted_256 = decrypt_AES(encrypted_256, key_256)
print(f"AES-256 Enkripsi: {encrypted_256}")
print(f"AES-256 Dekripsi: {decrypted_256}")
