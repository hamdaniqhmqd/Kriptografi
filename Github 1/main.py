import numpy as np
from copy import deepcopy
from key_handling import *
from boxes import *

counter = 1


def file_actions_dec(path, key):  # manages and organizing the data and calling the decryption
    # action
    stri = ''
    deep_copy = deepcopy(key)
    deep_copy = create_the_key(deep_copy)
    global counter
    counter = 1
    for s in range(10):
        deep_copy = key_expansion(deep_copy)  # creating the final form of the key
    final_key = deep_copy
    da_key = create_the_key(key)
    size = len(path)
    inside = path
    data_to_dec = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]
    count = 0
    if len(inside) == 16:  # managing when data length is 16 bytes
        for i in range(4):
            for j in range(4):
                data_to_dec[j][i] = int(ord(path[count]))
                count = count + 1

        data = decryption(data_to_dec, final_key, da_key)

        stri = ""
        for i in range(4):
            for j in range(4):
                stri = stri + chr(data[j][i])

    elif (len(inside) % 16) == 0:  # managing when data length is divisible by 16 bytes
        stri = ""
        for m in range(int(size / 16)):
            for i in range(4):
                for j in range(4):
                    data_to_dec[j][i] = int(ord(inside[count]))
                    count = count + 1

            data = decryption(data_to_dec, final_key, da_key)

            for i in range(4):
                for j in range(4):
                    stri = stri + chr(data[j][i])
    return stri  # returning decrypted data


def file_actions(path, da_key):  # manages and organizing the data and calling the encryption
    # action
    final = ""
    size = len(path)
    if size % 16 != 0:
        distance = 16 - size % 16
        for i in range(distance):
            path.append(chr(0))
        size = size + distance
    data_to_enc = data_to_dec = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]
    count = 0
    if size == 16:
        for i in range(4):
            for j in range(4):
                data_to_enc[j][i] = ord(path[count])
                count = count + 1

        data, final_key = encryption(data_to_enc, da_key)

        for i in range(4):
            for j in range(4):
                hexa = (hex(data[j][i]))
                final = final + (chr(int(hexa, 16)))

    elif size % 16 == 0:
        final = ""
        for m in range(int(size / 16)):
            for i in range(4):
                for j in range(4):
                    data_to_enc[j][i] = ord(path[count])
                    count = count + 1

            data, final_key = encryption(data_to_enc, da_key)
            for i in range(4):
                for j in range(4):
                    hexa = (hex(data[j][i]))
                    final = final + (chr(int(hexa, 16)))
    return final


def in_shift_rows(file):  # inverting shift rows
    for i in range(len(file)):
        file[i] = list(np.roll(file[i], i))
    print("after shift rows ", end='')
    print(file)
    print("--------------------------------------------------------")
    return file


def sub_bytes(file, action):
    units = 0
    tens = 0
    if action == "enc":
        sbox = enc_box
    else:
        sbox = dec_box

    for i in range(len(file)):
        line = file[i]
        for j in range(len(line)):
            if len(str(file[i][j])) > 1:
                if len(hex(file[i][j])) != 3:
                    try:
                        tens = (hex(file[i][j])[2])
                        units = (hex(file[i][j])[3])
                    except:
                        print(str(file[i][j]))
                        print(len(str(file[i][j])))
                        print((hex(file[i][j])))
                else:
                    tens = "0"
                    units = (hex(file[i][j])[2])
            else:  # when number is Single-digit
                tens = "0"
                units = (hex(file[i][j])[2])
            if ord(tens) <= 57:
                tens = ord(tens) - 48
            else:
                tens = ord(tens) - 87

            if ord(units) <= 57:
                units = ord(units) - 48
            else:
                units = ord(units) - 87
            switch_num = sbox[tens][units]  # gets the data to replace from the table

            file[i][j] = switch_num
    print("after sub bytes ", end='')
    print(file)
    print("--------------------------------------------------------")
    return file


def even(num):  # balancing the length of numbers when needed
    if len(num) < 10:
        num = num[0:2] + ('0' * (10 - len(num))) + num[2::]
    return num


def key_expansion(init_key):  # expanding the key for the encryption&decryption
    s_box = enc_box
    global counter  # remembering how many times the action has been called, so we will get the
    # right value from Rcon table
    last = []
    addition = []
    extended = init_key
    new = []
    for i in range(3, 7):  # starting from i=3
        if i == 3:  # only the third column gets those actions
            for j in range(4):
                last.append(extended[j][i])
            last = list(np.roll(last, -1))
            for j in last:
                if len(hex(j)) == 4:
                    tens = (hex(j))[2]
                    units = (hex(j))[3]
                else:
                    tens = '0'
                    units = (hex(j))[2]
                if tens.isalpha():
                    tens = ord(tens) - 87
                else:
                    tens = int(tens)
                if units.isalpha():
                    units = ord(units) - 87
                else:
                    units = int(units)
                switch_num = s_box[tens][units]  # replacing with the S box
                new.append(switch_num)
            back = []
            array = []
            addition = [[], [], [], []]
            for j in range(4):
                back.append(extended[j][i - 3])
            for j in range(4):
                if j == 0:
                    num_xor = (new[j] ^ back[j] ^ r_con[counter])  # xor'ing with the Rcon table
                    counter += 1
                else:
                    num_xor = (new[j] ^ back[j])
                array.append(num_xor)
            counter1 = 0
            for j in array:
                addition[counter1].append(j)
                counter1 += 1
        else:
            last = []
            xor_with = []
            for j in range(4):
                last.append(addition[j][i - 4])
            for j in range(4):
                xor_with.append(extended[j][i - 3])
            for j in range(4):
                addition[j].append(last[j] ^ xor_with[j])
    return addition  # returning the key needed for the next round


def math_3(file):  # handles multiplication by 3 (x+1)
    zero_to_one = {'0': '1', '1': '0'}
    bin_format = bin(file)
    bin_add = bin(file)
    bin_final = bin(int(bin_format, 2) + int(bin_add, 2))  # like doubling action
    has_8 = False
    same = []
    if len(bin_final) == 11:  # checking that the length is good to go
        has_8 = True
        bin_final = bin_final[0:2] + bin_final[3::]
    bin_format = even(bin_format)
    bin_final = even(bin_final)
    for i in range(2, len(bin_final)):  # starting from two because the start of the bin string
        # is '0b'
        if bin_final[i] == bin_format[i]:
            same.append(i)
    bin_final_final = ""
    for i in range(len(bin_final)):
        if i in same:
            if bin_final[i] == '1':
                bin_final_final += zero_to_one[bin_final[i]]  # switching the bit
            else:
                bin_final_final += bin_final[i]
        elif i > 1:
            bin_final_final += '1'
        else:
            bin_final_final += bin_final[i]
    if has_8:
        bin_end = ''
        for i in range(len(bin_final_final)):
            if i == 5 or i == 6 or i == 8 or i == 9:
                bin_end += zero_to_one[bin_final_final[i]]
            else:
                bin_end += bin_final_final[i]
    else:
        bin_end = bin_final_final
    return bin_end  # returns the result of multiplying by 3


def math_2(file):  # handles multiplication by 2 (x)
    zero_to_one = {"0": '1', '1': '0'}
    bin_format = bin(file)
    bin_add = bin(file)
    bin_final = bin(int(bin_format, 2) + int(bin_add, 2))
    has_8 = False
    if len(bin_final) == 11:  # checking that the length is good to go
        has_8 = True
        bin_final = bin_final[0:2] + bin_final[3::]
    if has_8:
        bin_end = ''
        for i in range(len(bin_final)):
            if i == 5 or i == 6 or i == 8 or i == 9:
                bin_end += zero_to_one[bin_final[i]]  # switching the bit
            else:
                bin_end += bin_final[i]
    else:
        bin_end = bin_final
    return bin_end  # returns the result of multiplying by 2


def decryption(file, key, init):  # contains all the sequence of the decryption
    file = add_round_key(file, key)
    file = in_shift_rows(file)
    file = sub_bytes(file, "dec")
    global counter
    counter = 1
    key = init
    for i in range(9):
        for _ in range(9 - i):
            key = key_expansion(key)  # getting in "reverse" the key that needed
        counter = 1
        file = add_round_key(file, key)
        key = init
        file = inverse_mix_columns(file)
        file = in_shift_rows(file)
        file = sub_bytes(file, "dec")

    file = add_round_key(file, init)
    return file


def encryption(file, key):  # contains all the sequence of the encryption
    global counter
    counter = 1
    file = add_round_key(file, key)
    for _ in range(9):
        file = sub_bytes(file, "enc")
        file = shift_rows(file)
        file = mix_columns(file)
        key = key_expansion(key)
        file = add_round_key(file, key)
    file = sub_bytes(file, "enc")
    file = shift_rows(file)
    key = key_expansion(key)
    file = add_round_key(file, key)
    return file, key


def shift_rows(file):  # shifting rows
    for i in range(len(file)):
        file[i] = list(np.roll(file[i], -i))  # rotating using numpy library
    print("after shift rows ", end='')
    print(file)
    print("--------------------------------------------------------")
    return file


def mix_columns(file):
    matriz1 = [2, 3, 1, 1]
    matriz2 = [1, 2, 3, 1]
    matriz3 = [1, 1, 2, 3]
    matriz4 = [3, 1, 1, 2]

    copy = file
    binn = []
    binn1 = []

    for j in range(4):
        file1 = [file[0][j], file[1][j], file[2][j], file[3][j]]

        arr = []
        for i in range(len(file1)):
            if matriz1[i] == 2:
                binn = math_2(file1[i])
            elif matriz1[i] == 3:
                binn1 = math_3(file1[i])
            else:
                arr.append(file1[i])
        final_num = (int(binn, 2) ^ int(binn1, 2) ^ arr[0] ^ arr[1])  # xor of all the 4 results
        copy[0][j] = final_num
        arr = []
        for i in range(len(file1)):
            if matriz2[i] == 2:
                binn = math_2(file1[i])
            elif matriz2[i] == 3:
                binn1 = math_3(file1[i])
            else:
                arr.append(file1[i])
        final_num = (int(binn, 2) ^ int(binn1, 2) ^ arr[0] ^ arr[1])  # xor of all the 4 results
        copy[1][j] = final_num
        arr = []
        for i in range(len(file1)):
            if matriz3[i] == 2:
                binn = math_2(file1[i])
            elif matriz3[i] == 3:
                binn1 = math_3(file1[i])
            else:
                arr.append(file1[i])
        final_num = (int(binn, 2) ^ int(binn1, 2) ^ arr[0] ^ arr[1])  # xor of all the 4 results
        copy[2][j] = final_num
        arr = []
        for i in range(len(file1)):
            if matriz4[i] == 2:
                binn = math_2(file1[i])
            elif matriz4[i] == 3:
                binn1 = math_3(file1[i])
            else:
                arr.append(file1[i])
        final_num = (int(binn, 2) ^ int(binn1, 2) ^ arr[0] ^ arr[1])  # xor of all the 4 results
        copy[3][j] = final_num
    print("after mix columns: ", end='')
    print(copy)
    print("--------------------------------------------------------")
    return copy


def inverse_mix_columns(file):  # inverting mix columns using two tables
    matriz1 = [0xDF, 0x68, 0xEE, 0xC7]
    matriz2 = [0xC7, 0xDF, 0x68, 0xEE]
    matriz3 = [0xEE, 0xC7, 0xDF, 0x68]
    matriz4 = [0x68, 0xEE, 0xC7, 0xDF]

    copy = deepcopy(file)

    units = 0
    tens = 0

    for m in range(4):
        file1 = [file[0][m], file[1][m], file[2][m], file[3][m]]
        matriz = matriz1
        for j in range(4):
            if j == 1:
                matriz = matriz2
            elif j == 2:
                matriz = matriz3
            elif j == 3:
                matriz = matriz4
            arr = []
            final = []
            for i in range(len(file1)):
                file_to_organize = file1
                if len(str(file_to_organize[i])) > 1:
                    if len(hex(file_to_organize[i])) != 3:
                        try:
                            tens = (hex(file_to_organize[i])[2])
                            units = (hex(file_to_organize[i])[3])
                        except:
                            print(str(file_to_organize[i]))
                            print(len(str(file_to_organize[i])))
                            print((hex(file_to_organize[i])))
                    else:
                        tens = "0"
                        units = (hex(file_to_organize[i])[2])
                else:
                    tens = "0"
                    units = (hex(file_to_organize[i])[2])
                if ord(tens) <= 57:
                    tens = ord(tens) - 48
                else:
                    tens = ord(tens) - 87

                if ord(units) <= 57:
                    units = ord(units) - 48
                else:
                    units = ord(units) - 87
                arr.append(l_table[tens][units])

            for k in range(len(arr)):
                if arr[k] == 0xFFF:
                    final.append(0x0)
                else:
                    sum = arr[k] + matriz[k]
                    if sum > 0xFF:
                        sum = sum - 0xFF
                    if len(str(sum)) > 1:
                        if len(hex(sum)) != 3:
                            try:
                                tens = (hex(sum)[2])
                                units = (hex(sum)[3])
                            except:
                                print(str(sum))
                                print(len(str(sum)))
                                print((hex(sum)))
                        else:
                            tens = "0"
                            units = (hex(sum)[2])
                    else:
                        tens = "0"
                        units = (hex(sum)[2])
                    if ord(tens) <= 57:
                        tens = ord(tens) - 48
                    else:
                        tens = ord(tens) - 87

                    if ord(units) <= 57:
                        units = ord(units) - 48
                    else:
                        units = ord(units) - 87
                    final.append(e_table[tens][units])

            final_num = final[0] ^ final[1] ^ final[2] ^ final[3]  # xor of all the 4 results
            copy[j][m] = final_num
    return copy


def enc(key, path):  # called from the app when encrypting
    if len(path) % 16 != 0:  # adds nulls to the data if it not divisible by 16
        distance = 16 - len(path) % 16
        for i in range(distance):
            path = path + chr(0)
    key = str(key)
    the_key = create_the_key(key)  # creating key that can be used
    ret_key = deepcopy(the_key)
    ret_key_string = ""  # the original key (before key schedule)
    for i in range(4):
        for j in range(4):
            ret_key_string = ret_key_string + chr(ret_key[j][i])
    result = file_actions(path, the_key)
    return encrypt_string(ret_key_string) + result  # returns encrypted data+hash string of key


def dec(key, path):  # called from the app when decrypting
    key = str(key)
    path = str(path)
    if encrypt_string(create_the_key_for_check(key)) != path[0:64]:  # checks if key is right
        print(encrypt_string(key))  # printing for debugging
        print(path[0:64])
    else:
        result = file_actions_dec(path[64::], key)  # sending only the data to decrypt, without
        # key
        return result


if __name__ == '__main__':
    # key, data
    input_key = "x"
    input_data = "a"
    while len(input_key) != 8:
        input_key = input("Enter your 8 character long key: ")

    while len(input_data) != 16:
        input_data = input("Enter your 16 character long message: ")

    to = enc(input_key, input_data)  # if you run on pc

    print(dec(input_key, to))