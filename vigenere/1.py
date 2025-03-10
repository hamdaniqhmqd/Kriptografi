def vigenere_encrypt(plain_text, key):
    encrypted_text = []
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(plain_text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                encrypted_text.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                encrypted_text.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.isupper():
                decrypted_text.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                decrypted_text.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

# Contoh penggunaan
plain_text = "Ahmad Hamdani"
key = "AHMAD"

encrypted = vigenere_encrypt(plain_text, key)
decrypted = vigenere_decrypt(encrypted, key)

print(f"Teks Asli     : {plain_text}")
print(f"Teks Enkripsi : {encrypted}")
print(f"Teks Dekripsi : {decrypted}")
