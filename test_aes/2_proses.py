import os

# S-box AES standar
s_box = [
    # ... (disingkat untuk ruang, sama seperti sebelumnya, gunakan lengkap 256 elemen)
]

# Fungsi XOR untuk dua blok
def xor_blocks(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

# Padding PKCS#7
def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# SubBytes (menggunakan S-Box)
def sub_bytes(state):
    return bytes([s_box[b] for b in state])

# AddRoundKey (XOR dengan kunci)
def add_round_key(state, key):
    return xor_blocks(state, key)

# Key Schedule dummy (kunci tetap)
def expand_key(key):
    return [key] * 11  # Tidak aman, hanya untuk simulasi

# Fungsi enkripsi blok tunggal (disederhanakan)
def encrypt_block(block, key):
    state = add_round_key(block, key)
    for _ in range(9):  # 9 putaran
        state = sub_bytes(state)
        state = add_round_key(state, key)
    state = sub_bytes(state)
    state = add_round_key(state, key)
    return state

# Fungsi dekripsi blok tunggal (simulasi)
def decrypt_block(block, key):
    # Ini bukan dekripsi AES sungguhan, hanya simulasi untuk matching hasil
    state = add_round_key(block, key)
    for _ in range(9):
        state = sub_bytes(state)
        state = add_round_key(state, key)
    state = sub_bytes(state)
    state = add_round_key(state, key)
    return state

# Enkripsi CBC mode
def aes_encrypt_cbc(plaintext, key, iv):
    plaintext = pad(plaintext)
    ciphertext = b''
    prev = iv
    for i in range(0, len(plaintext), 16):
        block = xor_blocks(plaintext[i:i+16], prev)
        enc = encrypt_block(block, key)
        ciphertext += enc
        prev = enc
    return ciphertext

# Dekripsi CBC mode
def aes_decrypt_cbc(ciphertext, key, iv):
    plaintext = b''
    prev = iv
    for i in range(0, len(ciphertext), 16):
        enc_block = ciphertext[i:i+16]
        dec_block = decrypt_block(enc_block, key)
        block = xor_blocks(dec_block, prev)
        plaintext += block
        prev = enc_block
    return unpad(plaintext)

# Generate 16-byte key dari ID user
def generate_key_from_id(id_user):
    key = id_user.encode()
    if len(key) >= 16:
        return key[:16]
    return key.ljust(16, b'\x00')

# Fungsi utama simulasi chat
def chat_simulasi():
    print("=== Simulasi Chat AES-128 CBC ===")
    id_user = input("Masukkan ID User: ")
    pesan = input("Masukkan Pesan Chat: ")
    
    key = generate_key_from_id(id_user)
    iv = os.urandom(16)  # IV acak

    ciphertext = aes_encrypt_cbc(pesan.encode(), key, iv)
    print("\n[ENCRYPTED]")
    print("Key        :", key.hex())
    print("IV         :", iv.hex())
    print("Ciphertext :", ciphertext.hex())

    decrypted = aes_decrypt_cbc(ciphertext, key, iv)
    print("\n[DECRYPTED]")
    print("Plaintext  :", decrypted.decode())

# Jalankan
chat_simulasi()
