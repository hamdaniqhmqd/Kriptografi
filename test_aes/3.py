# file: aes128_simulator.py

class AES128Simulator:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.key = self.str_to_key(user_id)
        self.iv = self.key_to_iv(self.key)

    # ===== Fungsi Utilitas =====
    def str_to_key(self, user_id: str) -> bytes:
        key = user_id.encode('Windows-1252')
        if len(key) < 16:
            key += b' ' * (16 - len(key))  # padding dengan spasi
        return key[:16]

    def key_to_iv(self, key: bytes) -> bytes:
        return key[:16]  # Ambil 16 byte pertama dari key

    def pad(self, text: bytes) -> bytes:
        padding_len = 16 - len(text) % 16
        return text + bytes([padding_len] * padding_len)

    def unpad(self, padded_text: bytes) -> bytes:
        padding_len = padded_text[-1]
        return padded_text[:-padding_len]

    def xor_bytes(self, a: bytes, b: bytes) -> bytes:
        return bytes(x ^ y for x, y in zip(a, b))

    # ===== Fungsi Enkripsi Blok Sederhana =====
    def simple_encrypt_block(self, block: bytes, key: bytes) -> bytes:
        return self.xor_bytes(block[::-1], key)

    def simple_decrypt_block(self, block: bytes, key: bytes) -> bytes:
        return self.xor_bytes(block, key)[::-1]

    # ===== Simulasi AES-CBC =====
    def encrypt_cbc(self, plaintext: str) -> str:
        plaintext_bytes = self.pad(plaintext.encode('Windows-1252'))
        ciphertext = b''
        prev_block = self.iv
        for i in range(0, len(plaintext_bytes), 16):
            block = plaintext_bytes[i:i+16]
            xored = self.xor_bytes(block, prev_block)
            encrypted = self.simple_encrypt_block(xored, self.key)
            ciphertext += encrypted
            prev_block = encrypted

        return ciphertext.decode('Windows-1252', errors='replace')

    def decrypt_cbc(self, ciphertext_str: str) -> str:
        ciphertext = ciphertext_str.encode('Windows-1252', errors='replace')
        plaintext_bytes = b''
        prev_block = self.iv
        for i in range(0, len(ciphertext), 16):
            block = ciphertext[i:i+16]
            decrypted = self.simple_decrypt_block(block, self.key)
            plain_block = self.xor_bytes(decrypted, prev_block)
            plaintext_bytes += plain_block
            prev_block = block

        return self.unpad(plaintext_bytes).decode('Windows-1252')

# ===== Contoh Penggunaan =====
if __name__ == "__main__":
    user_id = "1955"
    chat_message = "Halo, namaku ahmad, nama kamu siapa?"

    aes = AES128Simulator(user_id)

    print(f"\nKey       = {aes.key}")
    print(f"IV          = {aes.iv}")
    print(f"Pesan Chat  =  {chat_message}")

    ciphertext = aes.encrypt_cbc(chat_message)
    print("\nCiphertext (Windows-1252):")
    print(ciphertext)

    plaintext = aes.decrypt_cbc(ciphertext)
    print("\nDidekripsi kembali:")
    print(plaintext)
