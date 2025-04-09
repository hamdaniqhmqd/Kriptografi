class TextBinaryConverter:
    @staticmethod
    def text_to_binary(text: str) -> str:
        return ''.join(format(ord(char), '08b') for char in text)

    @staticmethod
    def binary_to_text(binary: str) -> str:
        return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))


class KeyStreamGenerator:
    def __init__(self, key: str):
        self.key = key
        self.binary_key = TextBinaryConverter.text_to_binary(key)

    def generate(self, length: int) -> str:
        return (self.binary_key * ((length // len(self.binary_key)) + 1))[:length]


class StreamCipher:
    def __init__(self, key: str):
        self.key_stream_generator = KeyStreamGenerator(key)

    def _xor_binary(self, bin1: str, bin2: str) -> str:
        return ''.join('0' if b1 == b2 else '1' for b1, b2 in zip(bin1, bin2))

    def encrypt(self, plaintext: str) -> str:
        binary_plaintext = TextBinaryConverter.text_to_binary(plaintext)
        key_stream = self.key_stream_generator.generate(len(binary_plaintext))
        return self._xor_binary(binary_plaintext, key_stream)

    def decrypt(self, encrypted_binary: str) -> str:
        key_stream = self.key_stream_generator.generate(len(encrypted_binary))
        decrypted_binary = self._xor_binary(encrypted_binary, key_stream)
        return TextBinaryConverter.binary_to_text(decrypted_binary)

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
