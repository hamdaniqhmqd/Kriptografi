def enkripsi_caesar(plaintext, shift_value, source):
    m = len(source)
    shift_value %= m  
    result = ""

    for char in plaintext:
        if char in source:
            for _ in range(shift_value):  
                index = source.index(char)
                char = source[(index + 1) % m]  
            result += char
        else:
            result += "?"  

    return result

def dekripsi_caesar(ciphertext, shift_value, source):
    m = len(source)
    shift_value %= m  
    result = ""

    for char in ciphertext:
        if char in source:
            for _ in range(shift_value):  
                index = source.index(char)
                char = source[(index - 1) % m]  
            result += char
        else:
            result += " "  

    return result

source = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
shift_value = 233307092
plaintext = "Ahmad Hamdani"

value_enkripsi = enkripsi_caesar(plaintext, shift_value, source)
print(f"Hasil Enkripsi: {value_enkripsi}")

value_dekripsi = dekripsi_caesar(value_enkripsi, shift_value, source)
print(f"Hasil Dekripsi: {value_dekripsi}")
