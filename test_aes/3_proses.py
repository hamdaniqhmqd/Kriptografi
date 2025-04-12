import random

# ===== Fungsi Utilitas =====

def str_to_key(user_id: str) -> bytes:
    key = user_id.encode('utf-8')
    if len(key) < 16:
        key += b' ' * (16 - len(key))  # padding dengan spasi
    return key[:16]  # ambil 16 byte

def pad(text: bytes) -> bytes:
    padding_len = 16 - len(text) % 16
    return text + bytes([padding_len] * padding_len)

def unpad(padded_text: bytes) -> bytes:
    padding_len = padded_text[-1]
    return padded_text[:-padding_len]

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

# Fungsi dummy AES-like block cipher (substitusi sederhana)
def simple_encrypt_block(block: bytes, key: bytes) -> bytes:
    return xor_bytes(block[::-1], key)  # balik + xor

def simple_decrypt_block(block: bytes, key: bytes) -> bytes:
    return xor_bytes(block, key)[::-1]  # xor + balik

# ===== AES-CBC Simulasi =====

def encrypt_cbc(plaintext: str, key: bytes, iv: bytes) -> str:
    plaintext_bytes = pad(plaintext.encode('utf-8'))
    ciphertext = b''
    prev_block = iv
    print("\n=== 🔒 Proses Enkripsi ===")
    for i in range(0, len(plaintext_bytes), 16):
        block = plaintext_bytes[i:i+16]
        print(f"\nBlock plaintext[{i//16}]: {block}")
        xored = xor_bytes(block, prev_block)
        print(f"XOR dengan prev_block/IV : {xored}")
        encrypted = simple_encrypt_block(xored, key)
        print(f"Hasil enkripsi block      : {encrypted}")
        ciphertext += encrypted
        prev_block = encrypted

    return ciphertext.decode('windows-1252', errors='replace')

def decrypt_cbc(ciphertext_str: str, key: bytes, iv: bytes) -> str:
    ciphertext = ciphertext_str.encode('windows-1252', errors='replace')
    plaintext_bytes = b''
    prev_block = iv
    print("\n=== 🔓 Proses Dekripsi ===")
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        print(f"\nBlock ciphertext[{i//16}]: {block}")
        decrypted = simple_decrypt_block(block, key)
        print(f"Hasil decrypt block       : {decrypted}")
        plain_block = xor_bytes(decrypted, prev_block)
        print(f"XOR dengan prev_block/IV  : {plain_block}")
        plaintext_bytes += plain_block
        prev_block = block

    return unpad(plaintext_bytes).decode('utf-8')

# ===== Simulasi Chat =====

def simulate_chat():
    id_user = input("Masukkan ID User (sebagai key): ")
    chat = input("Masukkan Pesan Chat: ")

    key = str_to_key(id_user)
    iv = bytes([random.randint(0, 255) for _ in range(16)])  # IV acak
    print(f"\n🔑 Key        : {key}")
    print(f"🧊 IV (acak)  : {iv}")

    ciphertext = encrypt_cbc(chat, key, iv)
    print("\n🔐 Ciphertext (Windows-1252):")
    print(ciphertext)

    plaintext = decrypt_cbc(ciphertext, key, iv)
    print("\n🟢 Didekripsi kembali:")
    print(plaintext)

simulate_chat()
