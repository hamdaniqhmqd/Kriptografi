class StreamCipher:
    def __init__(self, key: str):
        self.key = key
        print(f"[INIT] Key: {self.key}")

        self.binary_key = self._text_to_binary(key)
        print(f"[INIT] Binary Key: {self.binary_key}\n")

    def _text_to_binary(self, text: str) -> str:
        result = ''
        print("[CONVERT] Text to Binary:")
        for char in text:
            binary_char = format(ord(char), '08b')
            result += binary_char
            print(f"  '{char}' -> {binary_char}")
        print()
        return result

    def _binary_to_text(self, binary: str) -> str:
        print("[CONVERT] Binary to Text:")
        chars = []
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            char = chr(int(byte, 2))
            chars.append(char)
            print(f"  {byte} -> '{char}'")
        print()
        return ''.join(chars)

    def _xor_binary(self, bin1: str, bin2: str) -> str:
        print("[XOR] Binary XOR Operation:")
        result = ''
        for i in range(0, len(bin1), 8):
            b1 = bin1[i:i+8]
            b2 = bin2[i:i+8]
            xor_byte = ''.join('0' if x == y else '1' for x, y in zip(b1, b2))
            print(f"  {b1} XOR {b2} = {xor_byte}")
            result += xor_byte
        print()
        return result

    def _generate_key_stream(self, length: int) -> str:
        repeated_key = (self.binary_key * ((length // len(self.binary_key)) + 1))[:length]
        print(f"[KEY STREAM] Generated Key Stream: {repeated_key}\n")
        return repeated_key

    def encrypt(self, plaintext: str) -> str:
        print(f"[ENCRYPT] Plaintext: {plaintext}")
        binary_plaintext = self._text_to_binary(plaintext)
        key_stream = self._generate_key_stream(len(binary_plaintext))
        encrypted_binary = self._xor_binary(binary_plaintext, key_stream)
        print(f"[ENCRYPT] Final Encrypted Binary: {encrypted_binary}\n")
        return encrypted_binary

    def decrypt(self, encrypted_binary: str) -> str:
        print(f"[DECRYPT] Encrypted Binary: {encrypted_binary}")
        key_stream = self._generate_key_stream(len(encrypted_binary))
        decrypted_binary = self._xor_binary(encrypted_binary, key_stream)
        decrypted_text = self._binary_to_text(decrypted_binary)
        print(f"[DECRYPT] Final Decrypted Text: {decrypted_text}\n")
        return decrypted_text


# Contoh penggunaan
if __name__ == "__main__":
    key = "goatantony"
    plaintext = "Ahmad Hamdani"

    cipher = StreamCipher(key)

    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print("===== HASIL AKHIR =====")
    print("Plaintext       :", plaintext)
    print("Key             :", key)
    print("Encrypted Binary:", encrypted)
    print("Decrypted Text  :", decrypted)
