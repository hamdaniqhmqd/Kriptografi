def vigenere_encrypt(plaintext, key, alphabet):
    key = key.upper()
    ciphertext = ""
    key_index = 0  # Untuk melacak posisi key yang digunakan
    alphabet_size = len(alphabet)

    print("\n=== ENKRIPSI ===")
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    print("-" * 50)

    for char in plaintext:
        if char not in alphabet:
            ciphertext += char  # Pertahankan karakter yang tidak ada di alphabet (termasuk spasi)
            print(f"'{char}' bukan huruf dalam alphabet, tetap '{char}'")
        else:
            row = alphabet.index(char)  # Baris dari huruf plaintext
            col = alphabet.index(key[key_index % len(key)])  # Kolom dari key
            encrypted_char = alphabet[(row + col) % alphabet_size]
            
            print(f"'{char}' (baris {row}) + '{key[key_index % len(key)]}' (kolom {col}) → '{encrypted_char}'")
            
            ciphertext += encrypted_char
            key_index += 1  # Hanya naik jika char ada dalam alphabet

    print("-" * 50)
    print(f"Ciphertext: {ciphertext}\n")
    return ciphertext


def vigenere_decrypt(ciphertext, key, alphabet):
    key = key.upper()
    plaintext = ""
    key_index = 0  # Untuk melacak posisi key yang digunakan
    alphabet_size = len(alphabet)

    print("\n=== DEKRIPSI ===")
    print(f"Ciphertext: {ciphertext}")
    print(f"Key: {key}")
    print("-" * 50)

    for char in ciphertext:
        if char not in alphabet:
            plaintext += char  # Pertahankan karakter yang tidak ada di alphabet (termasuk spasi)
            print(f"'{char}' bukan huruf dalam alphabet, tetap '{char}'")
        else:
            col = alphabet.index(key[key_index % len(key)])  # Kolom dari key
            row = alphabet.index(char)  # Baris dari ciphertext
            decrypted_char = alphabet[(row - col) % alphabet_size]
            
            print(f"'{char}' (baris {row}) - '{key[key_index % len(key)]}' (kolom {col}) → '{decrypted_char}'")
            
            plaintext += decrypted_char
            key_index += 1  # Hanya naik jika char ada dalam alphabet

    print("-" * 50)
    print(f"Decrypted Text: {plaintext}\n")
    return plaintext


# Variabel alphabet tanpa menggunakan string library
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Contoh penggunaan
plaintext = "AHMAD HAMDANI"
key = "AHMAD"

ciphertext = vigenere_encrypt(plaintext, key, alphabet)
decrypted_text = vigenere_decrypt(ciphertext, key, alphabet)