class BinConvert:
    def __init__(self, text=""):
        self.text = text
        self.binary = ""
        self.decoded_text = ""

    def get_string_to_bin(self):
        self.binary = ''.join(f"{ord(c):08b}" for c in self.text)
        return self.binary

    def bin_to_text(self, binary_text):
        byte_array = bytearray(int(binary_text[i:i + 8], 2) for i in range(0, len(binary_text), 8))
        self.decoded_text = byte_array.decode('Windows-1252')

    def get_bin_to_text(self):
        return self.decoded_text

class LFSR:
    def __init__(self, bin_seed):
        self.seed = bin_seed
        self.seed_length = len(bin_seed)

    def generate_keystream(self, length):
        keystream = ""
        current_seed = self.seed

        for _ in range(length):
            feedback_bit = current_seed[-1]
            keystream += feedback_bit

            new_bit = int(current_seed[0])
            for i in range(1, self.seed_length):
                new_bit ^= int(current_seed[i])

            current_seed = str(new_bit) + current_seed[:-1]

        return keystream

class StreamCipher:
    def __init__(self):
        self.ciphertext = ""

    def encrypt_decrypt(self, text, key_stream):
        self.ciphertext = ''.join(str(int(text[i]) ^ int(key_stream[i])) for i in range(len(text)))

    def get_text(self):
        return self.ciphertext

def main():
    pt = "Ahmad Hamdani"
    seed = "kotapendekark"

    bin_pt = BinConvert(pt)
    pt_conv = bin_pt.get_string_to_bin()

    seed_conv = BinConvert(seed)
    bin_seed = seed_conv.get_string_to_bin()
    keystream_gen = LFSR(bin_seed)
    key_stream = keystream_gen.generate_keystream(len(pt_conv))

    sc = StreamCipher()
    sc.encrypt_decrypt(pt_conv, key_stream)
    ciphertext = sc.get_text()

    sc.encrypt_decrypt(ciphertext, key_stream)
    decrypted = sc.get_text()

    bin_pt.bin_to_text(ciphertext)
    hasil_enkripsi = bin_pt.get_bin_to_text()

    bin_pt.bin_to_text(decrypted)
    hasil_dekripsi = bin_pt.get_bin_to_text()

    # Output
    print(f"PT          = {pt}")
    print(f"Seed Key    = {seed}\n")
    print(f"Binary Seed = {bin_seed}")
    print(f"Binary PT   = {pt_conv}")
    print(f"Keystream   = {key_stream}")
    print(f"Ciphertext  = {ciphertext}")
    print(f"Decrypted   = {decrypted}\n")
    print(f"Hasil Enkripsi = {hasil_enkripsi}")
    print(f"Hasil Dekripsi = {hasil_dekripsi}")

if __name__ == "__main__":
    main()