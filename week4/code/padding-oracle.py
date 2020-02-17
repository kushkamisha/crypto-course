import requests
from binascii import unhexlify
from copy import deepcopy

TARGET = 'https://crypto-class.appspot.com/po?er='


def request(msg):
    res = requests.get(TARGET + msg)
    print(res.status_code)
    return True if res.status_code == 404 else False


def hex_of(x):
    h = hex(x)[2:]
    return h if len(h) == 2 else "0" + h


def xor(str1, str2):
    if not len(str1) or not len(str2):
        return ""
    if len(str1) > len(str2):
        diff = len(str1) - len(str2)
        for i in range(diff):
            str2 = "0" + str2
    if len(str2) > len(str1):
        diff = len(str2) - len(str1)
        for i in range(diff):
            str1 = "0" + str1
    return "".join([hex_of(a ^ b) for (a, b) in zip(unhexlify(str1), unhexlify(str2))])


# numbering starts from 1
def getNthLastByte(str, n):
    return str[len(str) - n*2:len(str) - n*2 + 2]


def is_true(c):
    print("".join(["".join(blk) for blk in c]))
    return request("".join(["".join(blk) for blk in c]))


# 128 bytes -> iv (16 bytes) + 3 ciphertext blocks
c = [
    ['f2', '0b', 'db', 'a6', 'ff', '29', 'ee', 'd7', 'b0', '46', 'd1', 'df', '9f', 'b7', '00', '00'],
    ['58', 'b1', 'ff', 'b4', '21', '0a', '58', '0f', '74', '8b', '4a', 'c7', '14', 'c0', '01', 'bd'],
    # ['4a', '61', '04', '44', '26', 'fb', '51', '5d', 'ad', '3f', '21', 'f1', '8a', 'a5', '77', 'c0'],
    # ['bd', 'f3', '02', '93', '62', '66', '92', '6f', 'f3', '7d', 'bf', '70', '35', 'd5', 'ee', 'b4']
]

m = [
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['54', '68', '65', '20', '4d', '61', '67', '69', '63', '20', '57', '6f', '72', '64', '73', '20'],
    ['61', '72', '65', '20', '53', '71', '75', '65', '61', '6d', '69', '73', '68', '20', '4f', '73'],
    ['73', '69', '66', '72', '61', '67', '65', '09', '09', '09', '09', '09', '09', '09', '09', '09']  # '11', '7b', 'b7', '71'
]


i = 1
for n in range(6, -1, -1):
    found = False
    c_original = deepcopy(c)

    for k in range(n, 15):
        print(xor(xor(c[i-1][k+1], m[i][k+1]), hex(16 - n)[2:]))
        c[i - 1][k+1] = xor(xor(c[i-1][k+1], m[i][k+1]), hex(16 - n)[2:])
        print(c[i-1][k+1])

    print('\nc')
    print(c)

    for rr in range(0, 256):
        found = False
        print(rr)
        original = c[i-1][n]

        b = xor(xor(c[i-1][n], hex_of(rr)), hex(16 - n)[2:])
        c[i-1][n] = b

        if is_true(c):
            m[i][n] = hex_of(rr)
            print(m[i][n])
            found = True
            break

        c[i-1][n] = original

    if not found:
        print('\n\nElement with n = %s wasn\'t found in all 256 iterations:(' % n)
        break

    c = c_original

    print('\nm')
    print(m)

print("".join("".join([chr(int.from_bytes(unhexlify(xx), "little")) for xx in x]) for x in m))
