def text_to_binary(text):
    """Mengonversi teks ke biner ASCII 8-bit"""
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    """Mengonversi biner ASCII 8-bit ke teks"""
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def xor_binary(bin1, bin2):
    """Operasi XOR antara dua string biner"""
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(bin1, bin2))

def lfsr(seed, taps, length):
    """Membangkitkan keystream menggunakan LFSR"""
    reg = seed[:]
    keystream = []
    
    for _ in range(length):
        new_bit = 0
        for t in taps:
            new_bit ^= reg[t]  # XOR sesuai posisi tap
        keystream.append(reg[-1])  # Simpan bit terakhir sebagai output
        reg = [new_bit] + reg[:-1]  # Shift register
    
    return keystream

def generate_seed_from_text(key):
    """Mengubah key teks menjadi seed biner (8-bit tiap karakter)"""
    binary_key = text_to_binary(key)
    return [int(bit) for bit in binary_key]  # Konversi ke list integer (0/1)

def stream_cipher(plaintext, seed_text):
    """Enkripsi dan dekripsi menggunakan stream cipher dengan LFSR"""
    binary_plaintext = text_to_binary(plaintext)
    seed = generate_seed_from_text(seed_text)  # Ubah key teks menjadi seed LFSR
    taps = [len(seed) - 1, len(seed) - 3, len(seed) - 4, len(seed) - 6]  # Posisi tap
    
    keystream = lfsr(seed, taps, len(binary_plaintext))  # Hasil keystream
    binary_ciphertext = xor_binary(binary_plaintext, ''.join(map(str, keystream)))  # XOR
    
    return binary_ciphertext

# Contoh penggunaan
plaintext = "ahmad hamdani"
seed_text = "amad"  # Key untuk LFSR

print(f"Plaintext: {plaintext}")
print(f"Seed Key: {seed_text}")

# Enkripsi
ciphertext = stream_cipher(plaintext, seed_text)
print(f"Ciphertext (biner): {ciphertext}")

# Dekripsi (XOR dengan keystream yang sama)
decrypted_text = binary_to_text(stream_cipher(binary_to_text(ciphertext), seed_text))
print(f"Decrypted Text: {decrypted_text}")
