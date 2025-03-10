def vigenere_encrypt(plaintext, key, alphabet):
    key = key.upper()
    ciphertext = ""
    key_index = 0
    alphabet_size = len(alphabet)

    for char in plaintext:
        if char not in alphabet:
            ciphertext += char
        else:
            row = alphabet.index(char)
            col = alphabet.index(key[key_index % len(key)])
            encrypted_char = alphabet[(row + col) % alphabet_size]
            ciphertext += encrypted_char
            key_index += 1

    return ciphertext


def vigenere_decrypt(ciphertext, key, alphabet):
    key = key.upper()
    plaintext = ""
    key_index = 0
    alphabet_size = len(alphabet)

    for char in ciphertext:
        if char not in alphabet:
            plaintext += char
        else:
            col = alphabet.index(key[key_index % len(key)])
            row = alphabet.index(char)
            decrypted_char = alphabet[(row - col) % alphabet_size]
            plaintext += decrypted_char
            key_index += 1

    return plaintext


# Variabel alphabet tanpa menggunakan string library
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Contoh penggunaan
plaintext = "AHMAD HAMDANI"
key = "AHMAD"

ciphertext = vigenere_encrypt(plaintext, key, alphabet)
decrypted_text = vigenere_decrypt(ciphertext, key, alphabet)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
