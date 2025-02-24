from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def print_block(title, block):
    print(f"{title}: {binascii.hexlify(block).decode().upper()}")
    print_matrix(block)

def print_matrix(block):
    """ Cetak blok dalam format 4x4 matrix """
    matrix = [block[i:i+4] for i in range(0, 16, 4)]
    print("+----+----+----+----+")
    for row in matrix:
        print("| " + " | ".join(f"{binascii.hexlify(bytes([byte])).decode().upper()}" for byte in row) + " |")
    print("+----+----+----+----+")

def aes_encrypt_debug(plaintext, key):
    plaintext = pad(plaintext, AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB)
    
    print("\n==== PROSES ENKRIPSI AES-128 ====")
    print(f"Plaintext Sebelum Enkripsi: {plaintext.decode(errors='ignore')}")
    print_block("Plaintext (Hex)", plaintext)
    print_block("Key", key)

    block = plaintext
    for round_num in range(11):  # 10 round utama + 1 awal
        block = cipher.encrypt(block)  # Enkripsi per round
        print(f"\n--- After Round {round_num} ---")
        print_block(f"Round {round_num} Output", block)

    print("\n=== Hasil Akhir Enkripsi ===")
    print_block("Ciphertext", block)
    return block

def aes_decrypt_debug(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    
    print("\n==== PROSES DEKRIPSI AES-128 ====")
    print_block("Ciphertext", ciphertext)
    print_block("Key", key)

    block = ciphertext
    for round_num in range(11):  # 10 round utama + 1 awal
        block = cipher.decrypt(block)  # Dekripsi per round
        print(f"\n--- After Round {round_num} ---")
        print_block(f"Round {round_num} Output", block)

    plaintext = unpad(block, AES.block_size)
    print("\n=== Hasil Akhir Dekripsi ===")
    print_block("Decrypted Plaintext (Hex)", plaintext)
    print(f"Decrypted Plaintext: {plaintext.decode(errors='ignore')}")
    return plaintext

key = b'ahmadhamdani1234'       # 16-byte key untuk AES-128
plaintext = b'Hello, Ahmad123'  # 16-byte plaintext

ciphertext = aes_encrypt_debug(plaintext, key)
decrypted_plaintext = aes_decrypt_debug(ciphertext, key)
