class StreamCipher:
    def __init__(self, key: str):
        self.key = key
        self.binary_key = self._text_to_binary(key)

    def _text_to_binary(self, text: str) -> str:
        return ''.join(format(ord(char), '08b') for char in text)

    def _binary_to_text(self, binary: str) -> str:
        return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

    def _xor_binary(self, bin1: str, bin2: str) -> str:
        return ''.join('0' if b1 == b2 else '1' for b1, b2 in zip(bin1, bin2))

    def _generate_key_stream(self, length: int) -> str:
        # Ulangi key biner agar panjangnya sama dengan plaintext
        return (self.binary_key * ((length // len(self.binary_key)) + 1))[:length]

    def encrypt(self, plaintext: str) -> str:
        binary_plaintext = self._text_to_binary(plaintext)
        key_stream = self._generate_key_stream(len(binary_plaintext))
        encrypted_binary = self._xor_binary(binary_plaintext, key_stream)
        return encrypted_binary

    def decrypt(self, encrypted_binary: str) -> str:
        key_stream = self._generate_key_stream(len(encrypted_binary))
        decrypted_binary = self._xor_binary(encrypted_binary, key_stream)
        return self._binary_to_text(decrypted_binary)


# Contoh penggunaan
if __name__ == "__main__":
    key = "rahasia"
    plaintext = "Halo Dunia!"

    cipher = StreamCipher(key)
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print("Plaintext     :", plaintext)
    print("Key           :", key)
    print("Encrypted Bin :", encrypted)
    print("Decrypted     :", decrypted)
