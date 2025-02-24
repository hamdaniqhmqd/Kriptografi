def enkripsi_caesar(plaintext, shift_value, source):
    m = len(source)
  
    result = ""

    for i in range(len(plaintext)): 
        char = plaintext[i]
        if char in source:
            index = source.index(char)
            chiper = (index + shift_value) % m 
            result += source[chiper]
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
        else:
            result += " " 

    return result

source = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

shift_value = 233307092
plaintext = "Ahmad Hamdani"

value_enkripsi = enkripsi_caesar(plaintext, shift_value, source)
value_dekripsi = dekripsi_caesar(value_enkripsi, shift_value, source)

print(f"Plaintext : {plaintext}")
print(f"Hasil Enkripsi: {value_enkripsi}")
print(f"Hasil Dekripsi: {value_dekripsi}")
