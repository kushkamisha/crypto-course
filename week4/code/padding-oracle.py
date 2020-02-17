import requests
from binascii import unhexlify
from copy import deepcopy

TARGET = 'http://crypto-class.appspot.com/po?er='


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

def isTrue(c):
    print("".join(["".join(blk) for blk in c]))
    return request("".join(["".join(blk) for blk in c]))

# 128 bytes -> iv (16 bytes) + 3 ciphertext blocks
c = [
    ['f2', '0b', 'db', 'a6', 'ff', '29', 'ee', 'd7', 'b0', '46', 'd1', 'df', '9f', 'b7', '00', '00'],
    ['58', 'b1', 'ff', 'b4', '21', '0a', '58', '0f', '74', '8b', '4a', 'c7', '14', 'c0', '01', 'bd'],
    ['4a', '61', '04', '44', '26', 'fb', '51', '5d', 'ad', '3f', '21', 'f1', '8a', 'a5', '77', 'c0'],
    ['bd', 'f3', '02', '93', '62', '66', '92', '6f', 'f3', '7d', 'bf', '70', '35', 'd5', 'ee', 'b6']
]

r = [
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '7b', 'b7', '71'],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
]

m = [
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '78', 'b5', '70']
]

# print("".join(["".join(blk) for blk in blocks]))

changed = [
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', 'c2', 'b0'],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']  # ¶p
]

plaintext = [
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', 'b6', '70']  # ¶p
]

# n = 15
# i = 3
#
# for rr in range(110, 256, 1):
#     print(rr)
#     original = c[i-1][n]
#
#     a = xor(c[i-1][n], hex_of(rr))
#     b = xor(a, str(15 - n + 1))
#     c[i-1][n] = b
#
#     if isTrue(c):
#         r[i-1][n] = hex_of(rr)
#         m[i][n] = xor(r[i-1][n], str(15 - n + 1))
#         break
#
#     c[i-1][n] = original

# n = 14
# i = 3
#
# a = xor(c[i-1][n+1], r[i-1][n+1])
# b = str(15 - n + 1)
# c[i - 1][n + 1] = xor(a, b)
#
# print(c)
#
# for rr in range(256):
#     print(rr)
#     original = c[i - 1][n]
#
#     a = xor(c[i - 1][n], hex_of(rr))
#     b = xor(a, str(15 - n + 1))
#     c[i - 1][n] = b
#
#     if isTrue(c):
#         r[i - 1][n] = hex_of(rr)
#         m[i][n] = xor(r[i - 1][n], str(15 - n + 1))
#         break
#
#     c[i - 1][n] = original

# n = 13
# i = 3
#
# a = xor(c[i-1][n+1], r[i-1][n+1])
# b = str(15 - n + 1)
# c[i-1][n+1] = xor(a, b)
#
# a = xor(c[i-1][n+2], r[i-1][n+2])
# b = str(15 - n + 1)
# c[i-1][n+2] = xor(a, b)
#
# # print(c)
#
# for rr in range(256):
#     print(rr)
#     original = c[i - 1][n]
#
#     a = xor(c[i - 1][n], hex_of(rr))
#     b = xor(a, str(15 - n + 1))
#     c[i - 1][n] = b
#
#     if isTrue(c):
#         r[i - 1][n] = hex_of(rr)
#         m[i][n] = xor(r[i - 1][n], str(15 - n + 1))
#         break
#
#     c[i - 1][n] = original

n = 13
i = 3

a = xor(c[i-1][n+1], r[i-1][n+1])
b = str(15 - n + 1)
c[i-1][n+1] = xor(a, b)

a = xor(c[i-1][n+2], r[i-1][n+2])
b = str(15 - n + 1)
c[i-1][n+2] = xor(a, b)

# print(c)

for rr in range(256):
    print(rr)
    original = c[i - 1][n]

    a = xor(c[i - 1][n], hex_of(rr))
    b = xor(a, str(15 - n + 1))
    c[i - 1][n] = b

    if isTrue(c):
        r[i - 1][n] = hex_of(rr)
        m[i][n] = xor(r[i - 1][n], str(15 - n + 1))
        break

    c[i - 1][n] = original

print('\nr')
print(r)

print('\nm')
print(m)



































































# blk_number = 2
# n = -1
#
# for i in range(110, 256, 1):
#     print()
#     tmp = c.copy()
#     g = hex_of(i)
#     tmp[blk_number][n] = xor(tmp[blk_number][n], xor(g, '01'))
#     req = "".join(["".join(blk) for blk in c])
#     res = request(req)
#
#     print(req)
#     print("i = %s" % i)
#     print(res)
#     if res:
#         print(g)  # plaintext value in hex
#         break

# blk_number = 2
# n = -2
#
# for i in range(100, 256, 1):
#     print()
#     tmp = c.copy()
#     g = hex_of(i)
#
#     tmp[blk_number][n] = xor(tmp[blk_number][n], xor(g, '02'))
#     # 1) d ^ 0xb0 = 0x1
#     # 2) d ^ 0xb0 ^ 0x3 = 0x1 ^ 0x3 = 0x2
#     # 3) d ^ 0xb3 = 0x2
#     tmp[blk_number][n+1] = 'b3'  # xor(tmp[blk_number][n+1], xor(plaintext[blk_number + 1][n+1], '72'))
#
#     req = "".join(["".join(blk) for blk in c])
#     res = request(req)
#
#     print(req)
#     print("i = %s" % i)
#     print(res)
#     if res:
#         print(g)  # plaintext value in hex
#         break

# blk_number = 2
# n = -3
#
# for i in range(0, 256, 1):
#     print()
#     tmp = blocks.copy()
#     g = hex_of(i)
#
#     tmp[blk_number][n] = xor(tmp[blk_number][n], xor(g, '03'))
#     # 1) d ^ 0xb0 = 0x1
#     # 2) d ^ 0xb0 ^ 0x2 = 0x1 ^ 0x2 = 0x3
#     # 3) d ^ 0xb2 = 0x3
#     # ===================================
#     # 1) d ^ 0xb3 = 0x2
#     # 2) d ^ 0xb3 ^ 0x1 = 0x2 ^ 0x1 = 0x3
#     # 3) d ^ 0xb2 = 0x3
#     tmp[blk_number][n+1] = 'b2'  # xor(tmp[blk_number][n+1], xor(plaintext[blk_number + 1][n+1], '72'))
#     # 1) d ^ 0xc2 = 0x2
#     # 2) d ^ 0xc2 ^ 0x1 = 0x2 ^ 0x1 = 0x3
#     # 3) d ^ 0xc3 = 0x3
#     tmp[blk_number][n+2] = 'c3'
#
#     req = "".join(["".join(blk) for blk in blocks])
#     res = request(req)
#
#     print(req)
#     print("i = %s" % i)
#     print(res)
#     if res:
#         print(g)  # plaintext value in hex
#         break

# res = request("f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577b0bdf302936266926ff37dbf7035d5eeb4")

