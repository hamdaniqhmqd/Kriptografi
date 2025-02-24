from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

# Fungsi untuk mencetak blok dalam format heksadesimal
def print_block(title, block):
    print(f"{title}: {binascii.hexlify(block).decode().upper()}")

# Fungsi untuk menjalankan enkripsi AES dengan debugging
def aes_encrypt_debug(plaintext, key):
    plaintext = pad(plaintext, AES.block_size)  # Pastikan data dipad (AES butuh 16 byte blok)
    cipher = AES.new(key, AES.MODE_ECB)  # Mode ECB untuk debugging
    
    print("\n==== PROSES ENKRIPSI AES-128 ====")
    print(f"Plaintext Sebelum Enkripsi: {plaintext.decode(errors='ignore')}")
    print_block("Plaintext (Hex)", plaintext)
    print_block("Key", key)

    block = plaintext
    for round_num in range(11):  # 10 round utama + 1 awal
        block = cipher.encrypt(block)  # Enkripsi per round
        print_block(f"After Round {round_num}", block)

    print("\n=== Hasil Akhir Enkripsi ===")
    print_block("Ciphertext", block)
    return block  # Return ciphertext untuk proses dekripsi

# Fungsi untuk menjalankan dekripsi AES dengan debugging
def aes_decrypt_debug(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Mode ECB untuk debugging
    
    print("\n==== PROSES DEKRIPSI AES-128 ====")
    print_block("Ciphertext", ciphertext)
    print_block("Key", key)

    block = ciphertext
    for round_num in range(11):  # 10 round utama + 1 awal
        block = cipher.decrypt(block)  # Dekripsi per round
        print_block(f"After Round {round_num}", block)

    plaintext = unpad(block, AES.block_size)  # Hapus padding
    print("\n=== Hasil Akhir Dekripsi ===")
    print_block("Decrypted Plaintext (Hex)", plaintext)
    print(f"Decrypted Plaintext: {plaintext.decode(errors='ignore')}")
    return plaintext

# Contoh Key dan Plaintext (16 byte)
key = b'ahmadhamdani1234'       # 16-byte key untuk AES-128
plaintext = b'Hello, Ahmad'  # 16-byte plaintext

# Jalankan enkripsi
ciphertext = aes_encrypt_debug(plaintext, key)

# Jalankan dekripsi
decrypted_plaintext = aes_decrypt_debug(ciphertext, key)
