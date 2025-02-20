from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

# Fungsi untuk mencetak blok dalam format heksadesimal
def print_block(title, block):
    print(f"{title}: {binascii.hexlify(block).decode().upper()}")

# Fungsi untuk menjalankan AES dengan debugging
def aes_encrypt_debug(plaintext, key):
    # Pastikan plaintext dipad (AES membutuhkan blok 16 byte)
    plaintext = pad(plaintext, AES.block_size)
    
    # Buat objek AES dalam mode ECB (agar mudah dilihat tiap round)
    cipher = AES.new(key, AES.MODE_ECB)

    # Tampilkan nilai awal
    print("==== PROSES ENKRIPSI AES-128 ====")
    print_block("Plaintext", plaintext)
    print_block("Key", key)

    # Proses enkripsi dengan mencetak tiap round
    block = plaintext
    for round_num in range(11):  # AES-128 memiliki 10 putaran + 1 awal
        block = cipher.encrypt(block)  # Lakukan enkripsi
        print_block(f"After Round {round_num}", block)

    print_block("Ciphertext", block)

# Contoh Key dan Plaintext (16 byte)
key = b'1234567890abcdef'       # 16-byte key untuk AES-128
plaintext = b'Hello, AES 128!!'  # 16-byte plaintext

# Jalankan enkripsi dengan debugging
aes_encrypt_debug(plaintext, key)
