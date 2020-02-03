from Crypto.Cipher import AES
from binascii import unhexlify


def aes_cbc(key, c):
    key = unhexlify(key)
    iv = unhexlify(c[:32])

    blocks = []
    tmp = ''
    for char in c:
        tmp += char
        if len(tmp) == 32:
            blocks.append(tmp)
            tmp = ''

    msgs = ""
    obj = AES.new(key, AES.MODE_ECB, iv)

    for i in range(1, len(blocks)):
        c = unhexlify(blocks[i])
        ciphertext = obj.decrypt(c)

        xorVal = "".join([chr(a ^ b) for (a, b) in zip(ciphertext, unhexlify(blocks[i - 1]))])
        msgs += xorVal

    return msgs
