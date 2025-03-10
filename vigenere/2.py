def vigenere_encrypt(plaintext, key, alphabet):
    key = key.upper()
    ciphertext = ""
    key_index = 0  # Untuk melacak posisi key yang digunakan
    alphabet_size = len(alphabet)

    print("\n=== ENKRIPSI ===")
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    print("-" * 40)

    for char in plaintext:
        if char not in alphabet:
            ciphertext += char  # Pertahankan karakter yang tidak ada di alphabet (termasuk spasi)
            print(f"'{char}' bukan huruf dalam alphabet, tetap '{char}'")
        else:
            shift = alphabet.index(key[key_index % len(key)])  # Posisi huruf dari key
            encrypted_char = alphabet[(alphabet.index(char) + shift) % alphabet_size]

            print(f"'{char}' + shift({shift}, '{key[key_index % len(key)]}') → '{encrypted_char}'")

            ciphertext += encrypted_char
            key_index += 1  # Hanya naik jika char ada dalam alphabet

    print("-" * 40)
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
    print("-" * 40)

    for char in ciphertext:
        if char not in alphabet:
            plaintext += char  # Pertahankan karakter yang tidak ada di alphabet (termasuk spasi)
            print(f"'{char}' bukan huruf dalam alphabet, tetap '{char}'")
        else:
            shift = alphabet.index(key[key_index % len(key)])  # Posisi huruf dari key
            decrypted_char = alphabet[(alphabet.index(char) - shift) % alphabet_size]

            print(f"'{char}' - shift({shift}, '{key[key_index % len(key)]}') → '{decrypted_char}'")

            plaintext += decrypted_char
            key_index += 1  # Hanya naik jika char ada dalam alphabet

    print("-" * 40)
    print(f"Decrypted Text: {plaintext}\n")
    return plaintext


# Variabel alphabet tanpa menggunakan string library
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Contoh penggunaan
plaintext = "AHMAD HAMDANI"
key = "AHMAD"

ciphertext = vigenere_encrypt(plaintext, key, alphabet)
decrypted_text = vigenere_decrypt(ciphertext, key, alphabet)
