import hashlib


def create_the_key_for_check(string):
    the_key = string
    hash_object = hashlib.md5(str(string).encode())
    hash_object = hash_object.hexdigest()
    the_key = the_key + hash_object[0:8]
    return the_key


def create_the_key(string):  # creating key with 16 bytes that can be used in encryption&decryption
    the_key = string
    hash_object = hashlib.md5(str(string).encode())  # creating md5 hash of the key
    hash_object = hash_object.hexdigest()
    the_key = the_key + hash_object[0:8]  # adding 8 characters of hash to the key
    the_cube = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]
    count = 0
    for i in range(4):
        for j in range(4):
            the_cube[j][i] = ord(the_key[count])
            count = count + 1
    return the_cube


def add_round_key(file, key):  # xor with key
    for i in range(len(file)):
        line = file[i]
        for j in range(len(line)):
            file[i][j] = (file[i][j] ^ key[i][j])
    # print("after xor  ", end='')
    # print(file)
    # print("--------------------------------------------------------")
    return file


def encrypt_string(hash_string):  # makes hash string from the key
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature