def prepare_key(key):
    """Membuat matriks 5x5 dari kunci yang diberikan"""
    key = key.upper().replace("J", "I")  # Format key
    matrix = []
    used_chars = set()

    # Tambahkan karakter dari kunci
    for char in key:
        if char not in used_chars and char.isalpha():  # Hanya huruf
            matrix.append(char)
            used_chars.add(char)

    # Tambahkan sisa huruf A-Z tanpa J
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    # Ubah ke format 5x5
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    """Mencari posisi karakter dalam matriks"""
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def prepare_text(text):
    """Mempersiapkan teks sesuai aturan Playfair"""
    text = text.upper().replace("J", "I").replace(" ", "")  # Format teks
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:  # Jika ada huruf berulang, tambahkan 'X'
                pairs.append((a, 'X'))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        else:
            pairs.append((a, 'X'))  # Jika ganjil, tambahkan 'X' di akhir
            i += 1
    return pairs

def encrypt_pair(matrix, a, b):
    """Enkripsi satu pasang huruf"""
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:  # Jika dalam satu baris
        return matrix[row_a][(col_a + 1) % 5], matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:  # Jika dalam satu kolom
        return matrix[(row_a + 1) % 5][col_a], matrix[(row_b + 1) % 5][col_b]
    else:  # Jika membentuk persegi
        return matrix[row_a][col_b], matrix[row_b][col_a]

def decrypt_pair(matrix, a, b):
    """Dekripsi satu pasang huruf"""
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:  # Jika dalam satu baris
        return matrix[row_a][(col_a - 1) % 5], matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:  # Jika dalam satu kolom
        return matrix[(row_a - 1) % 5][col_a], matrix[(row_b - 1) % 5][col_b]
    else:  # Jika membentuk persegi
        return matrix[row_a][col_b], matrix[row_b][col_a]

def encrypt_text(text, matrix):
    """Enkripsi seluruh teks"""
    pairs = prepare_text(text)
    encrypted_text = "".join("".join(encrypt_pair(matrix, a, b)) for a, b in pairs)
    return encrypted_text

def decrypt_text(ciphertext, matrix):
    """Dekripsi seluruh teks"""
    pairs = [(ciphertext[i], ciphertext[i + 1]) for i in range(0, len(ciphertext), 2)]
    decrypted_text = "".join("".join(decrypt_pair(matrix, a, b)) for a, b in pairs)
    return decrypted_text

# ========== CONTOH PENGGUNAAN ==========
key = "RORONOAZORO"
plaintext = "AHMAD HAMDANI"

matrix = prepare_key(key)

encrypted_text = encrypt_text(plaintext, matrix)
decrypted_text = decrypt_text(encrypted_text, matrix)

print("Plaintext:", plaintext)
print("Ciphertext:", encrypted_text)  # Hasil enkripsi
print("Decrypted:", decrypted_text)  # Harus kembali ke plaintext
