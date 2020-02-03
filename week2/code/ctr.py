from Crypto.Cipher import AES
from binascii import unhexlify


def aes_ctr(key, c):
    key = unhexlify(key)
    iv = int(c[:32], 16)

    blocks = []
    tmp = ''
    for char in c[32:]:
        tmp += char
        if len(tmp) == 32:
            blocks.append(tmp)
            tmp = ''

    if tmp:
        blocks.append(tmp)

    msgs = ""
    obj = AES.new(key, AES.MODE_ECB)

    for i in range(0, len(blocks)):
        enc = obj.encrypt(unhexlify(hex(iv + i)[2:]))
        xorVal = "".join([chr(a ^ b) for (a, b) in zip(enc, unhexlify(blocks[i]))])

        msgs += xorVal

    return msgs
