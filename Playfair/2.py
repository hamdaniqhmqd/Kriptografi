def prepare_key(key):
    """Membuat matriks 6x6 dari kunci yang diberikan"""
    key = key.upper().replace(" ", "")  # Hilangkan spasi pada kunci
    matrix = []
    used_chars = set()
    
    # Tambahkan karakter dari kunci
    for char in key:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    # Tambahkan sisa huruf A-Z dan angka 0-9
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    # Ubah ke format 6x6
    return [matrix[i:i+6] for i in range(0, 36, 6)]

def find_position(matrix, char):
    """Mencari posisi karakter dalam matriks"""
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def prepare_text(plaintext):
    """Mempersiapkan teks: menyimpan posisi spasi dan menghapus spasi"""
    positions = [i for i, char in enumerate(plaintext) if char == " "]  # Simpan posisi spasi
    text = plaintext.replace(" ", "").upper()  # Hapus spasi, ubah ke huruf besar

    # Pisahkan teks menjadi pasangan huruf
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:  # Jika dua huruf sama, tambahkan 'X' di antaranya
                pairs.append((a, 'X'))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        else:
            pairs.append((a, 'X'))  # Jika jumlah huruf ganjil, tambahkan 'X' di akhir
            i += 1

    return pairs, positions

def encrypt_pair(matrix, a, b):
    """Enkripsi satu pasang huruf"""
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:  # Jika dalam baris yang sama
        return matrix[row_a][(col_a + 1) % 6], matrix[row_b][(col_b + 1) % 6]
    elif col_a == col_b:  # Jika dalam kolom yang sama
        return matrix[(row_a + 1) % 6][col_a], matrix[(row_b + 1) % 6][col_b]
    else:  # Jika berbeda, tukar kolom
        return matrix[row_a][col_b], matrix[row_b][col_a]

def decrypt_pair(matrix, a, b):
    """Dekripsi satu pasang huruf"""
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:  # Jika dalam baris yang sama
        return matrix[row_a][(col_a - 1) % 6], matrix[row_b][(col_b - 1) % 6]
    elif col_a == col_b:  # Jika dalam kolom yang sama
        return matrix[(row_a - 1) % 6][col_a], matrix[(row_b - 1) % 6][col_b]
    else:  # Jika berbeda, tukar kolom
        return matrix[row_a][col_b], matrix[row_b][col_a]

def encrypt_text(text, matrix):
    """Proses enkripsi seluruh teks"""
    pairs, positions = prepare_text(text)
    encrypted_text = "".join("".join(encrypt_pair(matrix, a, b)) for a, b in pairs)
    return encrypted_text, positions

def decrypt_text(ciphertext, matrix, positions):
    """Proses dekripsi dan mengembalikan spasi"""
    pairs = [(ciphertext[i], ciphertext[i + 1]) for i in range(0, len(ciphertext), 2)]
    decrypted_text = "".join("".join(decrypt_pair(matrix, a, b)) for a, b in pairs)
    
    # Kembalikan spasi pada posisi semula
    decrypted_text = list(decrypted_text)
    for pos in positions:
        decrypted_text.insert(pos, " ")
    
    return "".join(decrypted_text)

# ========== CONTOH PENGGUNAAN ==========
key = "SECURITY CODE"
matrix = prepare_key(key)

plaintext = "HELLO WORLD"
encrypted, spaces = encrypt_text(plaintext, matrix)
decrypted = decrypt_text(encrypted, matrix, spaces)

print("Plaintext    :", plaintext)
print("Ciphertext   :", encrypted)
print("Decrypted    :", decrypted)
