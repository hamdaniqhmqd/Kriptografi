from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def print_block(title, block):
    print(f"{title}: {binascii.hexlify(block).decode().upper()}")

# Gunakan AES dengan mode CBC yang lebih aman
def aes_encrypt_debug(plaintext, key):
    plaintext = pad(plaintext, AES.block_size)  # Padding sebelum enkripsi
    cipher = AES.new(key, AES.MODE_CBC)  # Mode CBC lebih aman
    iv = cipher.iv  # IV diperlukan untuk dekripsi
    ciphertext = cipher.encrypt(plaintext)

    print("\n==== PROSES ENKRIPSI AES-128 ====")
    print_block("Key", key)
    print_block("IV", iv)
    print_block("Plaintext (Hex)", plaintext)
    print_block("Ciphertext", ciphertext)

    return iv + ciphertext  # Gabungkan IV dan ciphertext

def aes_decrypt_debug(ciphertext, key):
    iv = ciphertext[:AES.block_size]  # Ambil IV dari awal ciphertext
    ciphertext = ciphertext[AES.block_size:]  # Sisanya adalah ciphertext

    cipher = AES.new(key, AES.MODE_CBC, iv)  # Gunakan IV yang sama
    decrypted = cipher.decrypt(ciphertext)

    try:
        plaintext = unpad(decrypted, AES.block_size)  # Hapus padding setelah dekripsi
        print("\n==== PROSES DEKRIPSI AES-128 ====")
        print_block("Key", key)
        print_block("IV", iv)
        print_block("Ciphertext", ciphertext)
        print_block("Decrypted Plaintext (Hex)", plaintext)
        print(f"Decrypted Plaintext: {plaintext.decode(errors='ignore')}")
        return plaintext
    except ValueError:
        print("Error: Padding is incorrect. Data mungkin rusak atau kunci salah.")
        return None

# Key harus 16, 24, atau 32 byte
key = b'233307092'  # 16-byte key untuk AES-128
plaintext = b'Halo, namaku ahmad, nama kamu siapa?, Halo, namaku ahmad, nama kamu siapa?, Halo, namaku ahmad, nama kamu siapa?'  # Bisa kurang dari 16 byte, akan dipad otomatis

ciphertext = aes_encrypt_debug(plaintext, key)
decrypted_plaintext = aes_decrypt_debug(ciphertext, key)
