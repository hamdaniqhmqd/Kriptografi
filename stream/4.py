class BinConvert:
    def __init__(self, text=""):
        self.text = text
        self.binary = ""
        self.decoded_text = ""

    def get_string_to_bin(self):
        self.binary = ''.join(f"{ord(c):08b}" for c in self.text)
        return self.binary

    def bin_to_text(self, binary_text):
        chars = [chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8)]
        self.decoded_text = ''.join(chars)

    def get_bin_to_text(self):
        return self.decoded_text


class LFSR:
    def __init__(self, bin_seed):
        self.seed_length = len(bin_seed)
        self.feed_back = bin_seed[-1]
        self.new_seed = self.new_seed_process(bin_seed)

    def new_seed_process(self, bin_seed):
        new_bit = int(bin_seed[0])
        for i in range(1, self.seed_length):
            new_bit ^= int(bin_seed[i])
        new_seed = str(new_bit)
        for i in range(self.seed_length - 1):
            new_seed += bin_seed[i]
        return new_seed

    def get_new_seed(self):
        return self.new_seed

    def get_feed_back(self):
        return self.feed_back


class StreamCipher:
    def __init__(self):
        self.ciphertext = ""

    def encrypt_decrypt(self, text, key_stream):
        self.ciphertext = ''.join(str(int(text[i]) ^ int(key_stream[i])) for i in range(len(text)))

    def get_text(self):
        return self.ciphertext


def main():
    # 🔒 Hardcoded input
    pt = "Ahmad Hamdani"
    seed = "hi"

    print(f"Plaintext: {pt}")
    print(f"Seed Key : {seed}\n")

    # Konversi plaintext dan seed ke binary
    bin_pt = BinConvert(pt)
    pt_conv = bin_pt.get_string_to_bin()

    seed_conv = BinConvert(seed)
    bin_seed = seed_conv.get_string_to_bin()

    keystream_gen = LFSR(bin_seed)
    new_seed = keystream_gen.get_new_seed()
    feedback = keystream_gen.get_feed_back()

    print(f"Seed awal   = {bin_seed}")
    print(f"New Seed    = {new_seed}")
    print(f"Feedback    = {feedback}\n")

    key_stream = feedback
    for _ in range(1, len(pt_conv)):
        print(f"Seed        = {new_seed}")
        keystream_gen_next = LFSR(new_seed)
        new_seed = keystream_gen_next.get_new_seed()
        feedback = keystream_gen_next.get_feed_back()
        key_stream += feedback
        print(f"New Seed    = {new_seed}")
        print(f"Feedback    = {feedback}")
        print(f"Keystream   = {key_stream}\n")

    sc = StreamCipher()
    sc.encrypt_decrypt(pt_conv, key_stream)
    ciphertext = sc.get_text()

    sc.encrypt_decrypt(ciphertext, key_stream)
    decrypted = sc.get_text()

    print(f"Binary PT   = {pt_conv}")
    print(f"Keystream   = {key_stream}")
    print(f"Ciphertext  = {ciphertext}")
    print(f"Decrypted   = {decrypted}")

    bin_pt.bin_to_text(ciphertext)
    print(f"Hasil Enkripsi = {bin_pt.get_bin_to_text()}")

    bin_pt.bin_to_text(decrypted)
    print(f"Hasil Dekripsi = {bin_pt.get_bin_to_text()}")


if __name__ == "__main__":
    main()
