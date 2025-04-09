class StreamCipher:
    def __init__(self, key: str):
        # Inisialisasi dengan key (kunci) enkripsi
        self.key = key
        # Konversi key ke dalam bentuk biner (8 bit per karakter)
        self.binary_key = self._text_to_binary(key)

        # Tampilkan hasil inisialisasi
        print(f"[INIT] Key: {self.key}")
        print(f"[INIT] Binary Key: {self.binary_key}\n")

    def _text_to_binary(self, text: str) -> str:
        # Ubah setiap karakter menjadi representasi biner 8-bit
        return ''.join(format(ord(char), '08b') for char in text)

    def _binary_to_text(self, binary: str) -> str:
        # Ubah string biner kembali menjadi teks
        return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

    def _xor_binary(self, bin1: str, bin2: str) -> str:
        # XOR antara dua string biner: 0 jika sama, 1 jika berbeda
        return ''.join('0' if b1 == b2 else '1' for b1, b2 in zip(bin1, bin2))

    def _generate_key_stream(self, length: int) -> str:
        # Membuat key stream (aliran kunci) sepanjang plaintext
        # Dengan mengulang binary key sesuai panjang plaintext
        repeated_key = (self.binary_key * ((length // len(self.binary_key)) + 1))[:length]

        # Tampilkan key stream
        print(f"[KEY STREAM] Generated Key Stream: {repeated_key}")
        return repeated_key

    def encrypt(self, plaintext: str) -> str:
        # Proses enkripsi
        print(f"[ENCRYPT] Plaintext: {plaintext}")
        
        # Konversi plaintext ke biner
        binary_plaintext = self._text_to_binary(plaintext)
        print(f"[ENCRYPT] Binary Plaintext: {binary_plaintext}")

        # Generate key stream dengan panjang yang sama
        key_stream = self._generate_key_stream(len(binary_plaintext))

        # Lakukan XOR antara plaintext dan key stream
        encrypted_binary = self._xor_binary(binary_plaintext, key_stream)
        print(f"[ENCRYPT] Encrypted Binary: {encrypted_binary}\n")

        return encrypted_binary

    def decrypt(self, encrypted_binary: str) -> str:
        # Proses dekripsi (kebalikan dari enkripsi)
        print(f"[DECRYPT] Encrypted Binary: {encrypted_binary}")

        # Generate key stream sama seperti saat enkripsi
        key_stream = self._generate_key_stream(len(encrypted_binary))

        # XOR kembali antara cipher dan key stream untuk dapatkan plaintext
        decrypted_binary = self._xor_binary(encrypted_binary, key_stream)
        print(f"[DECRYPT] Decrypted Binary: {decrypted_binary}")

        # Konversi biner ke teks
        decrypted_text = self._binary_to_text(decrypted_binary)
        print(f"[DECRYPT] Decrypted Text: {decrypted_text}\n")

        return decrypted_text


# Contoh penggunaan
if __name__ == "__main__":
    key = "goatantony"           # Key enkripsi
    plaintext = "Ahmad Hamdani" # Teks asli yang ingin dienkripsi

    # Buat objek cipher dengan key tertentu
    cipher = StreamCipher(key)

    # key_binary = cipher.__init__(plaintext)
    
    # Enkripsi plaintext
    encrypted = cipher.encrypt(plaintext)

    # Dekripsi kembali untuk memastikan hasilnya sama dengan plaintext awal
    decrypted = cipher.decrypt(encrypted)

    # Tampilkan hasil akhir
    print("===== HASIL AKHIR =====")
    print("Plaintext       :", plaintext)
    print("Key             :", key)
    # print("Key Binary      :", key)
    print("Encrypted Binary:", encrypted)
    print("Decrypted Text  :", decrypted)
