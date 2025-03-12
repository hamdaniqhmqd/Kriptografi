def create_matrix(key):
    key = key.upper().replace(" ", "")  # Hilangkan spasi & kapitalisasi
    matrix = []
    used_chars = set()

    # Menambahkan karakter dari kunci ke dalam matriks
    for char in key:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    # Menambahkan sisa huruf A-Z dan angka 0-9
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    return [matrix[i:i+6] for i in range(0, 36, 6)]  # Ubah ke format 6x6

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def prepare_text(text):
    text = text.upper().replace(" ", "").replace("J", "I")  # Hilangkan spasi dan ganti J dengan I
    new_text = []
    
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            new_text.append(text[i] + 'X')  # Tambahkan X jika jumlah karakter ganjil
            break
        if text[i] == text[i+1]:  
            new_text.append(text[i] + 'X')  # Jika ada huruf ganda, selipkan X
            i += 1
        else:
            new_text.append(text[i] + text[i+1])
            i += 2
    return new_text

def encrypt_playfair(text, matrix):
    pairs = prepare_text(text)
    encrypted_text = ""

    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])

        if r1 == r2:  # Jika dalam baris yang sama, geser ke kanan
            encrypted_text += matrix[r1][(c1 + 1) % 6] + matrix[r2][(c2 + 1) % 6]
        elif c1 == c2:  # Jika dalam kolom yang sama, geser ke bawah
            encrypted_text += matrix[(r1 + 1) % 6][c1] + matrix[(r2 + 1) % 6][c2]
        else:  # Jika berbentuk persegi, tukar kolom
            encrypted_text += matrix[r1][c2] + matrix[r2][c1]

    return encrypted_text

def decrypt_playfair(text, matrix):
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    decrypted_text = ""

    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])

        if r1 == r2:  # Jika dalam baris yang sama, geser ke kiri
            decrypted_text += matrix[r1][(c1 - 1) % 6] + matrix[r2][(c2 - 1) % 6]
        elif c1 == c2:  # Jika dalam kolom yang sama, geser ke atas
            decrypted_text += matrix[(r1 - 1) % 6][c1] + matrix[(r2 - 1) % 6][c2]
        else:  # Jika berbentuk persegi, tukar kolom
            decrypted_text += matrix[r1][c2] + matrix[r2][c1]

    return decrypted_text.replace("X", "")  # Hilangkan padding 'X' dari enkripsi

# Contoh penggunaan
key = "RORONOAZORO"
plaintext = "AHMAD HAMDANI"

matrix = create_matrix(key)
ciphertext = encrypt_playfair(plaintext, matrix)
decrypted_text = decrypt_playfair(ciphertext, matrix)

print("Matriks Playfair 6x6:")
for row in matrix:
    print(" ".join(row))

print("\nPlaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted_text)
