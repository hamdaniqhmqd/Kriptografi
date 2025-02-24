def enkripsi_caesar(plaintext, shift_value, source):
    m = len(source)
    # print(f"modulus : {m}")
    result = ""

    for i in range(len(plaintext)): 
        char = plaintext[i]
        if char in source:
            index = source.index(char)
            chiper = (index + shift_value) % m 
            result += source[chiper]
            print("=================================================")
            print(f"Indeks : {index}, key : {shift_value}")
            print(f"Penambahan : {index} + {shift_value}")
            print(f"Hasil : {index + shift_value}")
            print(f"Indeks : {chiper}, menghasilkan : {source[chiper]}")
            print("=================================================")
        else:
            result += "%"

    return result

def dekripsi_caesar(ciphertext, shift_value, source):
    m = len(source)
    result = ""

    for i in range(len(ciphertext)): 
        char = ciphertext[i]
        if char in source:
            index = source.index(char)
            chiper = (index - shift_value) % m 
            result += source[chiper]
            # print("=================================================")
            # print(f"Indeks : {index}, key : {shift_value}")
            # print(f"Pengurangan : {index} - {shift_value}")
            # print(f"Hasil : {index - shift_value}")
            # print(f"Indeks : {chiper}, menghasilkan : {source[chiper]}")
            # print("=================================================")
        else:
            result += " " 

    return result

source = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
# for i in source:
#   char = source.index(i)
#   print(f"Index: {char}, Huruf: {source[char]}")

shift_value = 233307092
plaintext = "Ahmad Hamdani"

value_enkripsi = enkripsi_caesar(plaintext, shift_value, source)
print(f"Hasil Enkripsi: {value_enkripsi}")

value_dekripsi = dekripsi_caesar(value_enkripsi, shift_value, source)
print(f"Hasil Dekripsi: {value_dekripsi}")
