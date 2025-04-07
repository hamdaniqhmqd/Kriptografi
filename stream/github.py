def generate_keystream(key: bytes, nonce: bytes, length: int) -> bytes:
    """
    Generate a keystream of the specified length using the given key and nonce.
    
    Parameters:
        key (bytes): The secret key (should be a byte string).
        nonce (bytes): The nonce (should be a byte string).
        length (int): The desired length of the keystream in bytes.

    Returns:
        bytes: The generated keystream.
    """
    
    # Make sure key and nonce are byte strings
    if not isinstance(key, bytes) or not isinstance(nonce, bytes):
        raise ValueError("Key and nonce must be bytes.")

    # Initialize the keystream
    keystream = bytearray()

    # Repeat XOR operation until the desired length is achieved
    while len(keystream) < length:
        # Calculate the length of the next block to be added
        block_size = min(len(key), len(nonce), length - len(keystream))
        
        # XOR key and nonce
        block = bytes(k ^ n for k, n in zip(key[:block_size], nonce[:block_size]))
        
        # Append the block to the keystream
        keystream.extend(block)

    # Return the keystream truncated to the desired length
    return keystream[:length]


def encrypt(plaintext: bytes, key: bytes, nonce: bytes) -> bytes:
    """
    Encrypt the plaintext using the XOR operation with the generated keystream.

    Parameters:
        plaintext (bytes): The plaintext to be encrypted (should be a byte string).
        key (bytes): The secret key (should be a byte string).
        nonce (bytes): The nonce (should be a byte string).

    Returns:
        bytes: The encrypted ciphertext.
    """
    # Generate the required length of the keystream
    keystream_length = len(plaintext)  # Keystream length should match plaintext length
    keystream = generate_keystream(key, nonce, keystream_length)

    # Encrypt by XORing the plaintext with the keystream
    ciphertext = bytes(p ^ k for p, k in zip(plaintext, keystream))

    return ciphertext


def decrypt(ciphertext: bytes, key: bytes, nonce: bytes) -> bytes:
    """
    Decrypt the ciphertext using the XOR operation with the generated keystream.

    Parameters:
        ciphertext (bytes): The ciphertext to be decrypted (should be a byte string).
        key (bytes): The secret key (should be a byte string).
        nonce (bytes): The nonce (should be a byte string).

    Returns:
        bytes: The decrypted plaintext.
    """
    # Generate the required length of the keystream
    keystream_length = len(ciphertext)  # Keystream length should match ciphertext length
    keystream = generate_keystream(key, nonce, keystream_length)

    # Decrypt by XORing the ciphertext with the keystream
    plaintext = bytes(c ^ k for c, k in zip(ciphertext, keystream))

    return plaintext


# Example usage
if __name__ == "__main__":
    key = b"mysecretkey1234"      # Example key
    nonce = b"unique_nonce"        # Example nonce
    plaintext = b"Hello, World!"   # Example plaintext

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key, nonce)
    print("Ciphertext:", ciphertext.hex())

    # Decrypt the ciphertext
    decrypted_plaintext = decrypt(ciphertext, key, nonce)
    print("Decrypted Plaintext:", decrypted_plaintext.decode())